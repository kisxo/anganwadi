from fastapi import APIRouter, HTTPException, Response, Depends, Form
from typing import Annotated
from app.db.session import SessionDep
from app.core.security import authx_security, auth_scheme
from authx import TokenPayload
from app.db.schemas.student import StudentCreate, Student, StudentBase, StudentPublic, StudentsPublic
from app.db.models import student_model
from app.services import staff_service, admin_service, student_service, anganwadi_service
from uuid import uuid4
import datetime
from app.services.face_id import generate_face_id
from app.db.schemas.face_id import FaceID
import base64
from app.services.image import save_image

router = APIRouter()

@router.post("/",
    response_model=StudentPublic,
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)]
)
async def create_student(
    input_data: Annotated[StudentCreate, Form(media_type="multipart/form-data")],
    session: SessionDep,
    payload: TokenPayload = Depends(authx_security.access_token_required)
):

    if payload.user_type == "staff":
        current_user = staff_service.get_staff(payload.user_id, session)
        input_data.student_center_id = current_user.staff_center_id

    # check's if anganwadi center exists
    anganwadi_service.get_anganwadi(input_data.student_center_id, session)

    # saves image and returns unique image ID
    unique_image_id = save_image(input_data.student_image_file, "students", input_data.student_center_id)

    # generates a unique face signature from input image
    face_id: FaceID = generate_face_id(image_group="students", image_id=unique_image_id)
    try:

        validated_student = Student(
            **input_data.model_dump(),
            student_image=unique_image_id,
            student_face_id=face_id.model_dump_json(),
        )

        new_student = student_model.Student(**validated_student.model_dump())

        session.add(new_student)
        session.commit()
        session.refresh(new_student)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Something went wrong!")

    return new_student


@router.get("/",
    response_model=StudentsPublic,
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)]
)
async def list_students(
    session: SessionDep,
    payload: TokenPayload = Depends(authx_security.access_token_required)
):
    result = student_service.list_students(session=session)
    return {'data': result}



@router.get("/{student_id}",
    response_model=StudentPublic,
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)]
)
async def get_student(
    student_id: int,
    session: SessionDep
):
    # TODO Check user permission

    result = student_service.get_student(student_id=student_id, session=session)
    return result
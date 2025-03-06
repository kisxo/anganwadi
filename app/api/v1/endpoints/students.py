from fastapi import APIRouter, HTTPException, Response, Depends, Form
from typing import Annotated
from app.db.session import SessionDep
from app.core.security import authx_security, auth_scheme
from authx import TokenPayload
from app.db.schemas.student import StudentCreate, Student
from app.db.models import student_model
from app.services import staff_service, admin_service
from uuid import uuid4
import datetime
from app.services.face_id import generate_face_id
from app.db.schemas.face_id import FaceID

router = APIRouter()

@router.post("/",
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
    elif payload.user_type == "admin":
        current_user = admin_service.get_admin(payload.user_id, session)
    else:
        raise HTTPException(status_code=403, detail="Forbidden !")

    try:
        # Format: center_id + '-' + uuid
        unique_image_id = f"{input_data.student_center_id}-{uuid4()}"

        with open(f"media/images/students/{unique_image_id}", "bw") as image_file:
            contents = await input_data.student_image_file.read()
            image_file.write(contents)

        face_id : FaceID = generate_face_id(image_group="students", image_id=unique_image_id)
        face_id_status = False
        if face_id:
            face_id_status = True

        validated_student = Student(
            **input_data.model_dump(),
            student_image=unique_image_id,
            student_face_id= face_id.model_dump_json(),
            student_face_id_status= face_id_status
        )
        new_student = student_model.Student(**validated_student.model_dump())

        session.add(new_student)
        session.commit()
        session.refresh(new_student)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Something went wrong!")

    return new_student
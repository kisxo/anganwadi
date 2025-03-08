from fastapi import APIRouter, HTTPException, Response, Depends, Form
from typing import Annotated
from app.db.session import SessionDep
from app.core.security import authx_security, auth_scheme
from authx import TokenPayload
from app.services import staff_service
from app.db.schemas.staff import StaffPublic, StaffCreate

router = APIRouter()

@router.get("/self/",
    response_model=StaffPublic,
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)],
)
async def get_self(
    session: SessionDep,
    payload: TokenPayload = Depends(authx_security.access_token_required)
):
    if payload.user_type != "staff":
        raise HTTPException(status_code=400, detail="Not a staff!")
    result = staff_service.get_staff(staff_id=payload.user_id,session=session)
    return result

@router.get("/")
async def list_staffs(
    session: SessionDep,
):
    # TODO implement RBAC
    result = staff_service.list_staffs(session=session)
    return {'data': result}

@router.get("/{staff_id}")
async def get_staff(
    staff_id: int,
    session: SessionDep,
):
    # TODO implement RBAC
    result = staff_service.get_staff(staff_id=staff_id,session=session)
    return {'data': result}

@router.post("/",
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)]
)
async def create_staff(
    input_data: Annotated[StaffCreate, Form(media_type="multipart/form-data")],
    session: SessionDep,
    payload: TokenPayload = Depends(authx_security.access_token_required)
):
    if payload.user_type not in ["officer", "admin"]:
        raise HTTPException(status_code=400, detail="Does not have permission to create staff!")
    # result = staff_service.get_staff(staff_id=staff_id,session=session)
    return {'data': "result"}

 = APIRouter()

@router.post("/",

)
async def create_student(
    ,


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

@router.get("/",
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)]
)
async def list_students(
    session: SessionDep,
    payload: TokenPayload = Depends(authx_security.access_token_required)
):
    if payload.user_type == "staff":
        current_user = staff_service.get_staff(payload.user_id, session)
        center_id = current_user.staff_center_id
        result = student_service.list_students_by_center(center_id=center_id, session=session)
        return {'data': result}
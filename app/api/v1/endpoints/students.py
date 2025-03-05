from fastapi import APIRouter, HTTPException, Response, Depends
from sqlalchemy.testing.suite.test_reflection import users

from app.db.session import SessionDep
from sqlalchemy import select
from pathlib import Path
from app.core.security import authx_security, auth_scheme
from authx import TokenPayload
from app.db.schemas.student import StudentCreate
from app.db.models.student import Student
from app.services import staff_service, admin_service

router = APIRouter()

@router.post("/",
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)]
)
async def create_student(
    input_data: StudentCreate,
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

    new_student = Student(**input_data.model_dump())

    try:
        session.add(new_student)
        session.commit()
        session.refresh(new_student)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Something went wrong!")

    return new_student

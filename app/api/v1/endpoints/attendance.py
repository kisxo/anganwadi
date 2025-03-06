from fastapi import APIRouter, UploadFile, File, Depends
from typing import Annotated
from app.db.session import SessionDep
from app.services.face_id import verify_student_face_id
from app.services.student_service import get_student
from app.core.security import authx_security, auth_scheme

router = APIRouter()

@router.post("/students/{student_id}",
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)]
)
async def log_attendance(
    student_id: int,
    image_file: Annotated[UploadFile, File()],
    session: SessionDep
):
    student = get_student(student_id, session)
    result = verify_student_face_id(image_file, student)

    if result:
        return "Face matched!"
    else:
        return "Face does not match!"
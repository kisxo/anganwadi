from fastapi import APIRouter
from app.api.v1.endpoints import auth, students

router = APIRouter()

router.include_router(auth.router, prefix="/v1/auth", tags=["Authentication"])
router.include_router(students.router, prefix="/v1/students", tags=["Students"])
# router.include_router(members.router, prefix="/v1/members", tags=["member"])
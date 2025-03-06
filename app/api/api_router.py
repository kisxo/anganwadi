from fastapi import APIRouter
from app.api.v1.endpoints import auth, students, anganwadi, attendance, staff

router = APIRouter()

router.include_router(auth.router, prefix="/v1/auth", tags=["Authentication"])
router.include_router(staff.router, prefix="/v1/staffs", tags=["Staffs"])
router.include_router(students.router, prefix="/v1/students", tags=["Students"])
router.include_router(anganwadi.router, prefix="/v1/anganwadi", tags=["Anganwadi Centers"])
router.include_router(attendance.router, prefix="/v1/attendance", tags=["Attendance"])
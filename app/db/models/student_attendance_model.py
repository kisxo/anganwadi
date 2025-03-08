from app.db.database import Base
from sqlalchemy import TIMESTAMP, func, ForeignKey, Enum as SqlEnum, DATE
from sqlalchemy.orm import Mapped, mapped_column
from app.db.schemas.attendance import AttendanceModeChoice

class StudentAttendance(Base):
    __tablename__ = "student_attendance"

    attendance_id: Mapped[int] = mapped_column(primary_key=True)
    attendance_student_id: Mapped[int] = mapped_column(ForeignKey("students.student_id"))
    attendance_center_id: Mapped[int] = mapped_column(ForeignKey("anganwadi_centers.center_id"))
    attendance_mode: Mapped[SqlEnum] = mapped_column(SqlEnum(AttendanceModeChoice))
    attendance_date: Mapped[DATE] = mapped_column(DATE, server_default=func.now())
    attendance_create_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
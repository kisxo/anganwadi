from app.db.database import Base
from sqlalchemy import TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class StaffAttendance(Base):
    __tablename__ = "staff_attendance"

    attendance_id: Mapped[int] = mapped_column(primary_key=True)
    attendance_staff_id: Mapped[int] = mapped_column(ForeignKey("staffs.staff_id"))
    attendance_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
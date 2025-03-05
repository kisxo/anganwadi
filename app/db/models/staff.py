from app.db.database import Base
from sqlalchemy import String, Enum as SqlEnum, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db.schemas.staff import StaffRole

class Staff(Base):
    __tablename__ = "staffs"

    staff_id: Mapped[int] = mapped_column(primary_key=True)
    staff_full_name: Mapped[str] = mapped_column(String(30))
    staff_phone: Mapped[str] = mapped_column(String(10))
    staff_aadhar: Mapped[str] = mapped_column(String(12))
    staff_hashed_mpin: Mapped[str] = mapped_column(String(5))
    staff_role: Mapped[SqlEnum] = mapped_column(SqlEnum(StaffRole))
    staff_center_id: Mapped[int] = mapped_column(ForeignKey("anganwadi_centers.center_id"))
    staff_created_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
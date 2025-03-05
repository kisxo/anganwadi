from app.db.database import Base
from sqlalchemy import String, Enum as SqlEnum, JSON, DATE, TIMESTAMP, FLOAT, func, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from app.db.schemas.member import StatusChoice, GenderChoice, TrainingChoice, PlanChoice, BatchChoice

class Student(Base):
    __tablename__ = "students"

    student_id: Mapped[int] = mapped_column(primary_key=True)
    student_name: Mapped[str] = mapped_column(String(30))
    student_mother_name: Mapped[str] = mapped_column(String(30))
    student_father_name: Mapped[str] = mapped_column(String(30))
    student_dob: Mapped[Optional[DATE]] = mapped_column(DATE)
    student_phone: Mapped[str] = mapped_column(String(10))
    student_verified: Mapped[bool] = mapped_column(Boolean(), default=False)
    student_face_id: Mapped[Optional[JSON]] = mapped_column(JSON())
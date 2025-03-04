from app.db.database import Base
from sqlalchemy import String, Enum as SqlEnum, JSON, DATE, TIMESTAMP, FLOAT, func
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from app.db.schemas.member import StatusChoice, GenderChoice, TrainingChoice, PlanChoice, BatchChoice

class Members(Base):
    __tablename__ = "members"

    member_id: Mapped[int] = mapped_column(primary_key=True)
    member_name: Mapped[str] = mapped_column(String(30))
    member_image_url: Mapped[Optional[str]] = mapped_column(String(250))
    member_phone: Mapped[str] = mapped_column(String(10))
    member_status: Mapped[SqlEnum] = mapped_column(SqlEnum(StatusChoice))
    member_gender: Mapped[SqlEnum] = mapped_column(SqlEnum(GenderChoice))
    member_measurements: Mapped[Optional[JSON]] = mapped_column(JSON())
    member_dob: Mapped[Optional[DATE]] = mapped_column(DATE)
    member_address: Mapped[Optional[str]] = mapped_column(String(150))
    member_training: Mapped[SqlEnum] = mapped_column(SqlEnum(TrainingChoice))
    member_plan: Mapped[SqlEnum] = mapped_column(SqlEnum(PlanChoice))
    member_batch: Mapped[SqlEnum] = mapped_column(SqlEnum(BatchChoice))
    member_joined_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    member_starting_date: Mapped[Optional[DATE]] = mapped_column(DATE)
    member_ending_date: Mapped[Optional[DATE]] = mapped_column(DATE)
    member_info: Mapped[Optional[str]] = mapped_column(String(50))
    member_due_date: Mapped[DATE] = mapped_column(DATE)
    member_due_amount: Mapped[float] = mapped_column(FLOAT)
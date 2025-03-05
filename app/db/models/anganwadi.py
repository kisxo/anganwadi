from app.db.database import Base
from sqlalchemy import String, Enum as SqlEnum, JSON, DATE, TIMESTAMP, FLOAT, func
from sqlalchemy.orm import Mapped, mapped_column

class AnganwadiCenters(Base):
    __tablename__ = "anganwadi_centers"

    center_id: Mapped[int] = mapped_column(primary_key=True)
    center_name: Mapped[str] = mapped_column(String(30))
    center_uid: Mapped[str] = mapped_column(String(30))
    center_address: Mapped[str] = mapped_column(String(500))
    # center_supervisor_id Mapped[int] = mapped_column(ForeignKey("members.member_id"))
    # center_worker_id: Mapped[int] = mapped_column(ForeignKey("members.member_id"))
    # center_helper_id: Mapped[int] = mapped_column(ForeignKey("members.member_id"))

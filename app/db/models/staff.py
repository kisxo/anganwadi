from app.db.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Workers(Base):
    __tablename__ = "staffs"

    worker_id: Mapped[int] = mapped_column(primary_key=True)
    worker_name: Mapped[str] = mapped_column(String(30))
    worker_phone: Mapped[str] = mapped_column(String(10))
    # worker_face_id:

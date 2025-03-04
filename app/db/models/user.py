from app.db.database import Base
from sqlalchemy import String, TIMESTAMP, Enum as SqlEnum, func
from sqlalchemy.orm import Mapped, mapped_column
from app.db.schemas.user import UserRole

class Users(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_username: Mapped[str] = mapped_column(String(20), unique=True)
    user_hashed_password: Mapped[str] = mapped_column(String())
    user_role: Mapped[SqlEnum] = mapped_column(SqlEnum(UserRole))
    user_created_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
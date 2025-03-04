from app.db.database import Base
from sqlalchemy import String, TIMESTAMP, FLOAT, ForeignKey, Enum as SqlEnum, func
from sqlalchemy.orm import Mapped, mapped_column
from app.db.schemas.payment import PaymentMethodChoice
from typing import Optional

class Payments(Base):
    __tablename__ = "payments"

    payment_id: Mapped[int] = mapped_column(primary_key=True)
    payment_member_id: Mapped[int] = mapped_column(ForeignKey("members.member_id"))
    payment_amount: Mapped[float] = mapped_column(FLOAT)
    payment_method: Mapped[SqlEnum] = mapped_column(SqlEnum(PaymentMethodChoice))
    payment_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    payment_txn_no: Mapped[str] = mapped_column(String(20))
    payment_remark: Mapped[Optional[str]] = mapped_column(String(50))
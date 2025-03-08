from pydantic import BaseModel
from pydantic.types import date


class RationItem(BaseModel):
    item: str
    quantity: str

class RationDetail(BaseModel):
    last_restock_date: date
    last_restock_detail: list[RationItem]
from pydantic import BaseModel

class RationItem(BaseModel):
    item: str
    quantity: str

class RationDetail(BaseModel):
    detail: list[RationItem]
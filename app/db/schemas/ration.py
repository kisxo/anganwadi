from pydantic import BaseModel
from pydantic.types import datetime

class RationItem(BaseModel):
    item: str
    quantity: str

class RationData(BaseModel):
    note: str
    data: list[RationItem]

class RationCreate(RationData):
    pass

class RationPublic(BaseModel):
    ration_id: int
    ration_center_id: int
    ration_created_date: datetime
    ration_data: RationData
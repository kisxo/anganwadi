from pydantic import BaseModel, Field
from pydantic.types import date

class AnganwadiBase(BaseModel):
    center_code: str = Field(max_length=30)
    center_name: str = Field(max_length=30)
    center_address: str = Field(max_length=500)
    center_supervisor_id: int | None = Field(default=None)

class AnganwadiCreate(AnganwadiBase):
    pass
import enum
from symtable import Class

from pydantic import BaseModel, Field
from pydantic.types import datetime, Json
from typing import Optional

class StaffRole(enum.Enum):
    worker = "Worker"
    helper = "Helper"
    # member = "Member"
    def __str__(self) -> str:
        return self.value

class StaffBase(BaseModel):
    staff_full_name: str =  Field(min_length=5, max_length=30)
    staff_phone: str = Field(min_length=10, max_length=10)
    staff_aadhar: str = Field(min_length=12, max_length=12)
    staff_role: StaffRole
    staff_center_id: int

class StaffPublic(StaffBase):
    staff_id: int
    staff_created_date: datetime
    staff_image: str
    staff_face_id: object

class StaffsPublic(BaseModel):
    data: list[StaffPublic]

class Staff(StaffBase):
    staff_hashed_mpin: str
    staff_image: str
    staff_face_id: Json

class StaffCreate(StaffBase):
    staff_mpin: str = Field(min_length=5, max_length=5)
    staff_image_file: str
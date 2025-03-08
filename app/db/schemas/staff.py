import enum
from symtable import Class

from pydantic import BaseModel, Field
from pydantic.types import datetime
from typing import Optional

class StaffRole(enum.Enum):
    worker = "Worker"
    helper = "Helper"
    # member = "Member"
    def __str__(self) -> str:
        return self.value

class StaffBase(BaseModel):
    staff_full_name: str
    staff_phone: str
    staff_aadhar: str
    staff_role: StaffRole
    staff_center_id: int

class StaffPublic(StaffBase):
    staff_id: int
    staff_created_date: datetime

class Staff(StaffBase):
    staff_hashed_mpin: str
    staff_image: str
    staff_face_id: Json | None = Field(default=None)
    staff_face_id_status: bool = Field(default=False)

class StaffCreate(StaffBase):
    staff_mpin: str = Field(min_length=5, max_length=5)
    staff_image_file: str
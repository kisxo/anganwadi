import enum
from pydantic import BaseModel, Field

class StaffRole(enum.Enum):
    worker = "Worker"
    helper = "Helper"
    # member = "Member"
    def __str__(self) -> str:
        return self.value

class StaffBase(BaseModel):
    staff_id: int
    staff_full_name: str
    staff_phone: str
    staff_role: StaffRole
    staff_center_id: int
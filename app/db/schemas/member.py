import enum
from pydantic.types import date
from pydantic import BaseModel, Field

class GenderChoice(enum.Enum):
    male = "Male"
    female = "Female"
    def __str__(self) -> str:
        return self.value

class TrainingChoice(enum.Enum):
    trainer = "Trainer"
    personal = "Personal"
    def __str__(self) -> str:
        return self.value

class PlanChoice(enum.Enum):
    regular = "Regular"
    advance = "Advance"
    def __str__(self) -> str:
        return self.value

class BatchChoice(enum.Enum):
    morning = "Morning"
    evening = "Evening"
    def __str__(self) -> str:
        return self.value

class StatusChoice(enum.Enum):
    active = "Active"
    inactive = "Inactive"
    # expired = "Expired"
    # trial = "Trial"
    # overdue = "Overdue"
    # cancelled = "Cancelled"
    # pending = "Pending"
    # hold = "Hold"
    def __str__(self) -> str:
        return self.value

class MemberPublic(BaseModel):
    member_id: int
    member_name: str
    member_gender: GenderChoice
    member_phone: str

class MembersPublic(BaseModel):
    data: list[MemberPublic]

class MemberMeasurements(BaseModel):
    height: str = Field(max_length=10)
    weight: str = Field(max_length=10)
    chest: str = Field(max_length=10)
    waist: str = Field(max_length=10)

class MemberBase(BaseModel):
    member_name: str = Field(max_length=30)
    member_image_url: str | None = Field(default=None, max_length=250)
    member_phone: str = Field(max_length=10)
    member_status: StatusChoice = Field(default="Active")
    member_gender: GenderChoice
    member_measurements: MemberMeasurements | None = Field(default=None)
    member_dob: date | None = Field(default=None)
    member_address: str | None = Field(max_length=150, default=None)
    member_training: TrainingChoice
    member_plan: PlanChoice
    member_batch:BatchChoice
    member_starting_date: date | None = Field(default=None)
    member_ending_date: date | None = Field(default=None)
    member_info: str | None = Field(default=None, max_length=50)
    member_due_date: date
    member_due_amount: float

class MemberCreate(MemberBase):
    pass

class MemberDetail(MemberBase):
    pass
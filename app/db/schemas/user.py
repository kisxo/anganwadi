import enum
from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self

class UserRole(enum.Enum):
    admin = "Admin"
    staff = "Staff"
    # member = "Member"
    def __str__(self) -> str:
        return self.value

class UserBase(BaseModel):
    user_username: str = Field(min_length=4, max_length=20)

    @model_validator(mode='after')
    def check_username(self) -> Self:
        if self.user_username.isalpha():
            return self
        else:
            raise ValueError('Username should only contain alphabets and numbers!')

class UserCreate(UserBase):
    password: str = Field(min_length=6)
    user_role: UserRole = Field(default="Staff")

class UserPublic(UserBase):
    user_role: UserRole
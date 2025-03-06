import enum
from pydantic import BaseModel, Field
from pydantic.types import date
from typing import Annotated
from fastapi import UploadFile, File

class StudentGender(enum.Enum):
    male = "Male"
    female = "Female"
    other = "Other"
    def __str__(self) -> str:
        return self.value

class StudentBase(BaseModel):
    student_name: str = Field(max_length=30)
    student_dob: date
    student_gender: StudentGender
    student_mother_name: str = Field(max_length=30)
    student_father_name: str = Field(max_length=30)
    student_phone: str = Field(max_length=10)
    student_center_id: int | None = Field(default=None)

class Student(StudentBase):
    student_image: str
    student_center_id: int

class StudentCreate(StudentBase):
    student_image_file: Annotated[UploadFile, File()]
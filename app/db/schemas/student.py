import enum
from pydantic import BaseModel, Field
from pydantic.types import date, Base64Str
from typing import Annotated
from fastapi import UploadFile, File
from pydantic.types import Json

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
    student_center_id: int
    student_image: str
    student_face_id: Json | None = Field(default=None)
    student_face_id_status: bool = Field(default=False)

class StudentCreate(StudentBase):
    student_image_file: str
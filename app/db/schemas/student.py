import enum
from pydantic import BaseModel, Field
from pydantic.types import datetime, date
from typing import Optional
from pydantic.types import Json


class StudentGender(enum.Enum):
    male = "Male"
    female = "Female"
    other = "Other"
    def __str__(self) -> str:
        return self.value

class StudentBase(BaseModel):
    student_full_name: str = Field(min_length=5, max_length=30)
    student_dob: date
    student_gender: StudentGender
    student_mother_name: str =  Field(min_length=5, max_length=30)
    student_father_name: str =  Field(min_length=5, max_length=30)
    student_phone: str = Field(max_length=10)
    student_aadhar: Optional[str] = Field(min_length=12, max_length=12, default=None)
    student_center_id: int

class StudentPublic(StudentBase):
    student_image: str
    student_face_id: object
    student_center_id: int
    student_created_date: datetime

class StudentsPublic(BaseModel):
    data: list[StudentPublic]

class Student(StudentBase):
    student_image: str
    student_face_id: Json
    student_center_id: int

class StudentCreate(StudentBase):
    student_image_file: str
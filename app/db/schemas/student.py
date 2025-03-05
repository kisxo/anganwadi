import enum

class StudentGender(enum.Enum):
    male = "Male"
    female = "Female"
    other = "Other"
    def __str__(self) -> str:
        return self.value
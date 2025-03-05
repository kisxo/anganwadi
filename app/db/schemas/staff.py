import enum

class StaffRole(enum.Enum):
    worker = "Worker"
    helper = "Helper"
    # member = "Member"
    def __str__(self) -> str:
        return self.value
import enum

class OfficerRole(enum.Enum):
    supervisor = "Supervisor"
    cdpo = "CDPO"
    dpo = "DPO"
    def __str__(self) -> str:
        return self.value
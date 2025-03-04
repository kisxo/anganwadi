import enum

class PaymentMethodChoice(enum.Enum):
    cash = "Cash"
    online = "Online"
    def __str__(self) -> str:
        return self.value
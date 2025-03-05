from pydantic import BaseModel

# JSON payload containing access token
class Token(BaseModel):
    access_token: str = "JWT-token"
    token_type: str = "bearer"

class StaffLoginForm(BaseModel):
    phone: str = "phone"
    mpin: str = "mpin"
from fastapi import APIRouter, HTTPException
from app.core.security import authx_security
from app.db.session import SessionDep
from app.db.models.staff import Staff
from app.db.schemas.auth import Token, StaffLoginForm
from app.core.security import verify_password
from sqlalchemy import select
from pathlib import Path

router = APIRouter()

@router.post("/token",
    response_model=Token
)
async def get_jwt_token(
    input_data: StaffLoginForm,
    session: SessionDep
):
    statement = select(Staff).where(Staff.staff_phone== input_data.phone)
    result = session.execute(statement).first()

    if result is None:
        raise HTTPException(status_code=400, detail="Phone and MPIN does not match!")

    # Select the User object
    staff_in_db = result[0]

    if staff_in_db.staff_role.value != "Worker":
        raise HTTPException(status_code=403, detail="Forbidden !")

    if not verify_password(input_data.mpin, staff_in_db.staff_hashed_mpin):
        raise HTTPException(status_code=400, detail="Phone and MPIN does not match!")

    # Used 'user_in_db.user_role.value' to get the actual string value from the Enum
    token_data = {
        'user_type': 'staff',
        'user_id' : staff_in_db.staff_id,
        'user_role' : staff_in_db.staff_role.value
    }

    token = authx_security.create_access_token(uid=str(staff_in_db.staff_id), data=token_data)

    return {"access_token": token}
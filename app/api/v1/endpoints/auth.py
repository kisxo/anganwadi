from fastapi import APIRouter, HTTPException
from app.core.security import authx_security
from app.db.session import SessionDep
from app.db.models.user import Users
from app.db.schemas.auth import Token, LoginForm
from app.core.security import verify_password
from sqlalchemy import select
from pathlib import Path

router = APIRouter()

@router.post("/token",
    response_model=Token,
    description=Path('app/openapi_docs/api/v1/post_auth_token_LoginForm.md').read_text(),
)
async def get_jwt_token(
    input_data: LoginForm,
    session: SessionDep
):
    statement = select(Users).where(Users.user_username == input_data.username)
    result = session.execute(statement).first()

    if result is None:
        raise HTTPException(status_code=400, detail="Username and password does not match!")

    # Select the User object
    user_in_db = result[0]

    if not verify_password(input_data.password, user_in_db.user_hashed_password):
        raise HTTPException(status_code=400, detail="Username and password does not match!")

    # Used 'user_in_db.user_role.value' to get the actual string value from the Enum
    token_data = {'user_id' : user_in_db.user_id, 'username' : user_in_db.user_username, 'role' : user_in_db.user_role.value}

    token = authx_security.create_access_token(uid=str(user_in_db.user_id), data=token_data)

    return {"access_token": token}
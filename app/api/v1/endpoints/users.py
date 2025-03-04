from fastapi import APIRouter, Depends, HTTPException
from app.core.security import authx_security, hash_password, auth_scheme
from app.db.schemas.user import UserCreate
from app.db.session import SessionDep
from app.db.models.user import Users
from app.db.schemas.user import UserPublic
from sqlalchemy.exc import IntegrityError
from authx import TokenPayload
from pathlib import Path

router = APIRouter()

@router.post("/",
    response_model = UserPublic,
    description=Path('app/openapi_docs/api/v1/post_users_UserCreate.md').read_text(),
    dependencies=[Depends(auth_scheme)]
)
def create_user(
    input_data: UserCreate,
    session: SessionDep,
    payload: TokenPayload = Depends(authx_security.access_token_required)
):
    if payload.role != "Admin":
        raise HTTPException(status_code=403, detail="Only Admin can create accounts!")

    new_user = Users(
        user_username = input_data.user_username,
        user_hashed_password = hash_password(input_data.password),
        user_role = input_data.user_role
    )

    session.add(new_user)
    try:
        session.commit()
        session.refresh(new_user)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User already exists!")
    except:
        raise HTTPException(status_code=400, detail="Something went wrong!")

    return new_user
from fastapi import APIRouter, HTTPException, Response, Depends, Form
from typing import Annotated
from app.db.session import SessionDep
from app.core.security import authx_security, auth_scheme
from authx import TokenPayload
from app.services import staff_service
from app.db.schemas.staff import StaffPublic

router = APIRouter()

@router.get("/self/",
    response_model=StaffPublic,
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)],
)
async def get_self(
    session: SessionDep,
    payload: TokenPayload = Depends(authx_security.access_token_required)
):
    if payload.user_type != "staff":
        raise HTTPException(status_code=400, detail="Not a staff!")
    result = staff_service.get_staff(staff_id=payload.user_id,session=session)
    return result

@router.get("/")
async def list_staffs(
    session: SessionDep,
):
    # TODO implement RBAC
    result = staff_service.list_staffs(session=session)
    return {'data': result}

@router.get("/{staff_id}")
async def get_staff(
    staff_id: int,
    session: SessionDep,
):
    # TODO implement RBAC
    result = staff_service.get_staff(staff_id=staff_id,session=session)
    return {'data': result}
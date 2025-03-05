from fastapi import APIRouter, HTTPException, Response, Depends
from app.db.session import SessionDep
from app.core.security import authx_security, auth_scheme
from authx import TokenPayload
from app.db.schemas.anganwadi import AnganwadiCreate
from app.db.models.anganwadi import AnganwadiCenters
from app.services import admin_service, officer_service

router = APIRouter()

@router.post("/",
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)]
)
async def create_center(
    input_data: AnganwadiCreate,
    session: SessionDep,
    payload: TokenPayload = Depends(authx_security.access_token_required)
):
    if payload.user_type == "officer":
        current_user = officer_service.get_officer(payload.user_id, session)
        if current_user.officer_role.value == "Supervisor":
            input_data.center_supervisor_id = current_user.officer_id
        else:
            raise HTTPException(status_code=403, detail="Forbidden !")
    elif payload.user_type == "admin":
        if not input_data.center_supervisor_id:
            raise HTTPException(status_code=400, detail="Supervisor id required !")
        current_user = admin_service.get_admin(payload.user_id, session)
    else:
        raise HTTPException(status_code=403, detail="Forbidden !")

    new_anganwadi_center = AnganwadiCenters(**input_data.model_dump())

    try:
        session.add(new_anganwadi_center)
        session.commit()
        session.refresh(new_anganwadi_center)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Something went wrong!")

    return new_anganwadi_center

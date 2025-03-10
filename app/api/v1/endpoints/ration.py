from fastapi import APIRouter, HTTPException, Response, Depends, Form
from typing import Annotated
from app.db.session import SessionDep
from app.core.security import authx_security, auth_scheme
from authx import TokenPayload
from app.db.schemas import ration
from app.db.models import ration_model

router = APIRouter()


@router.post("/",
    response_model= ration.RationPublic,
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)],
)
async def get_self(
    input_data: ration.RationCreate,
    session: SessionDep,
    payload: TokenPayload = Depends(authx_security.access_token_required)
):
    if payload.user_role != "Worker":
        raise HTTPException(status_code=400, detail="Only Workers can enter ration details!")

    try:
        new_ration = ration_model.Rations(
            ration_center_id = payload.user_center_id,
            ration_data = input_data.model_dump()
        )

        session.add(new_ration)
        session.commit()
        session.refresh(new_ration)
        return new_ration
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Ration data saving failed!")
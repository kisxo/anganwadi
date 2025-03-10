from fastapi import APIRouter, Depends, UploadFile, HTTPException
from app.services.image import save_image
from app.core.security import authx_security, auth_scheme
from app.db.schemas import beneficiary
from app.db.session import SessionDep
from authx import TokenPayload
from app.db.models import beneficiary_model


router = APIRouter()


@router.post("/",
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)],
)
async def create_beneficiary(
    input_data: beneficiary.BeneficiaryCreate,
    session: SessionDep,
    payload: TokenPayload = Depends(authx_security.access_token_required)
):
    if payload.user_role != "Worker":
        raise HTTPException(status_code=400, detail="Only Anganwadi worker can add a beneficiary!")

    try:
        new_beneficiary = beneficiary_model.Beneficiaries(
            **input_data.model_dump(),
            beneficiary_center_id = payload.user_center_id
        )

        session.add(new_beneficiary)
        session.commit()
        session.refresh(new_beneficiary)
        return new_beneficiary

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Failed adding beneficiary!")

    return new_beneficiary
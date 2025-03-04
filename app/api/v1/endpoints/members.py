from fastapi import APIRouter, HTTPException, Response, Depends
from app.db.session import SessionDep
from app.db.models.member import Members
from app.db.schemas.member import MembersPublic, MemberCreate, MemberPublic, MemberDetail
from sqlalchemy import select
from pathlib import Path
from app.core.security import authx_security, auth_scheme
from authx import TokenPayload

router = APIRouter()

@router.get("/",
    response_model=MembersPublic,
    description=Path('app/openapi_docs/api/v1/get_members.md').read_text(),
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)],
)
async def list_members(session: SessionDep,payload: TokenPayload = Depends(authx_security.access_token_required)):
    statement = select(Members.member_id, Members.member_name, Members.member_gender, Members.member_phone)
    # used mapping to resolve type-error caused due to use of enums
    result = session.execute(statement).mappings().all()
    print(payload.expiry_datetime)
    return {'data': result}

@router.get("/{member_id}",
    response_model=MemberDetail,
    description=Path('app/openapi_docs/api/v1/post_members_member_id.md').read_text(),
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)],
)
async def get_member_detail(
    session: SessionDep,
    member_id: int
):
    statement = select(Members).where(Members.member_id == member_id)
    # used mapping to resolve type-error caused due to use of enums
    result = session.execute(statement).mappings().first()

    if result is None:
        raise HTTPException(status_code=404, detail="Member not found!")

    return result.Members

@router.post("/",
    response_model= MemberPublic,
    status_code=201,
    description=Path('app/openapi_docs/api/v1/post_members_MemberCreate.md').read_text(),
    dependencies=[Depends(authx_security.access_token_required), Depends(auth_scheme)]
)
async def create_member(
    session: SessionDep,
    input_data: MemberCreate,
    response: Response
):
    new_member = Members(**input_data.model_dump())
    try:
        session.add(new_member)
        session.commit()
        session.refresh(new_member)
    except:
        raise HTTPException(status_code=400, detail="Something went wrong!")

    return new_member
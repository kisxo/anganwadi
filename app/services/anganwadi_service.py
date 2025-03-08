from app.db.models.anganwadi_model import AnganwadiCenters
from app.db.session import SessionDep
from fastapi import HTTPException

def get_anganwadi(anganwadi_id: int, session: SessionDep):
    anganwadi_in_db = None
    try:
        anganwadi_in_db = session.get(AnganwadiCenters, anganwadi_id)
    except Exception as e:
        print(e)

    if not anganwadi_in_db:
        raise HTTPException(status_code=404, detail="Anganwadi Center not found!")

    return anganwadi_id
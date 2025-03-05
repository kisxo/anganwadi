from app.db.models.staff import Staff
from app.db.session import SessionDep
from fastapi import HTTPException

def get_staff(staff_id: int, session: SessionDep):
    staff_in_db = None
    try:
        staff_in_db = session.get(Staff, staff_id)
    except Exception as e:
        print(e)

    if not staff_in_db:
        raise HTTPException(status_code=404, detail="Staff not found!")

    return staff_in_db
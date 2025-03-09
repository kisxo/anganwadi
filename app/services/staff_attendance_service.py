from app.db.models.staff_attendance_model import StaffAttendance
from app.db.session import SessionDep
from fastapi import HTTPException
from sqlalchemy import select
from datetime import date

def list_attendance(session: SessionDep):
    try:
        statement = select(StaffAttendance)
        result =  session.execute(statement).mappings().all()
        attendances = []
        for row in result:
            attendances.append(row.StaffAttendance.__dict__)

        return attendances
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Failed to load staff attendance list!")

def list_attendance_by_staff_id_and_date(staff_id: int, input_date: date, session: SessionDep):
    try:
        statement = select(StaffAttendance).where(StaffAttendance.attendance_staff_id == staff_id, StaffAttendance.attendance_date == input_date)
        result =  session.execute(statement).mappings().all()
        print(result)
        attendances = []
        for row in result:
            attendances.append(row.StaffAttendance.__dict__)

        return attendances
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Failed to load staff attendance list!")
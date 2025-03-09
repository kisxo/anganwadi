from app.db.models.student_attendance_model import StudentAttendance
from app.db.session import SessionDep
from fastapi import HTTPException
from sqlalchemy import select

def list_attendance(session: SessionDep):
    try:
        statement = select(StudentAttendance)
        result =  session.execute(statement).mappings().all()
        attendances = []
        for row in result:
            attendances.append(row.StudentAttendance.__dict__)

        return attendances
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Failed to load student attendance list!")
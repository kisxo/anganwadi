from app.db.models.student_attendance_model import StudentAttendance
from app.db.session import SessionDep
from fastapi import HTTPException
from sqlalchemy import select
from datetime import date

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


def list_attendance_by_student_id_and_date(student_id: int, input_date: date, session: SessionDep):
    try:
        statement = select(StudentAttendance).where(StudentAttendance.attendance_student_id == student_id, StudentAttendance.attendance_date == input_date)
        result =  session.execute(statement).mappings().all()
        attendances = []
        for row in result:
            attendances.append(row.StudentAttendance.__dict__)

        return attendances
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Failed to load student attendance list!")
from app.db.models.student_model import Student
from app.db.session import SessionDep
from fastapi import HTTPException

def get_student(student_id: int, session: SessionDep):
    student_in_db = None
    try:
        student_in_db = session.get(Student, student_id)
    except Exception as e:
        print(e)

    if not student_in_db:
        raise HTTPException(status_code=404, detail="Student not found!")

    return student_in_db
import cv2 as cv
import face_recognition
import matplotlib.pyplot as plt
from app.db.schemas.face_id import FaceID
import numpy

from app.db.models import student_model

def generate_face_id(image_group: str, image_id: str) -> FaceID:
    """
    image_group = ``students`` or ``staffs``
    Specify whose image to load image file from correct file route
    """

    known_image = face_recognition.load_image_file(f"media/images/{image_group}/{image_id}")
    known_faces = face_recognition.face_encodings(face_image=known_image, num_jitters=50, model='large')[0]

    return FaceID(face_signature=known_faces)

def verify_student_face_id(image, student: student_model.Student) -> bool:
    input_image = face_recognition.load_image_file(image.file)
    input_faces = face_recognition.face_encodings(face_image=input_image, num_jitters=50, model='large')[0]

    known_face_id = numpy.array(student.student_face_id["face_signature"])

    result = face_recognition.compare_faces([known_face_id], input_faces)

    return bool(result[0])
from app.models import Lecture, Slide
from app.schemas import LectureSchema, SlideSchema


def get_all_lectures():
    lectures = Lecture.query.all()
    schema = LectureSchema()
    result = [schema.dump(lecture) for lecture in lectures]
    return result

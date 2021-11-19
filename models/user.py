from pydantic import BaseModel

class User(BaseModel):
    id: str
    email: str
    full_name: str
    name: str
    student_id: str
    is_student: bool
    grade: int
    classnum: int
    number: int


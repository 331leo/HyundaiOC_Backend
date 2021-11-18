from pydantic import BaseModel, Field
from pydantic.types import conint
from typing import List

from models.user import User

class Subject(BaseModel):
    url: str = Field(description="온라인 학습방 URL")
    name: str = Field(description="과목명")
    teacher: str = Field(description="교사명")
    teacher_tel: str = Field(description="교사 연락처")


class Classes(BaseModel):
    mon: List[Subject] = Field(description="월요일 수업 목록")
    tue: List[Subject] = Field(description="화요일 수업 목록")
    wen: List[Subject] = Field(description="수요일 수업 목록")
    thu: List[Subject] = Field(description="목요일 수업 목록")
    fri: List[Subject] = Field(description="금요일 수업 목록")

class Class(BaseModel):
    student: User = Field(description="학생 정보")
    teacher: str = Field(description="담임선생님 이름", example="김선생")
    teacher_tel: str = Field(description="담임선생님 연락처", example="01012345678")
    classes: Classes = Field(description="수업 목록")
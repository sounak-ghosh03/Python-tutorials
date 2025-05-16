# TODO: Create Course model
# Each Course has modules
# Each Module has lessons

from pydantic import BaseModel
from typing import List


class Lessons(BaseModel):
    lesson_id: int
    topic: str


class Module(BaseModel):
    module_id: int
    name: str
    lessons: List[Lessons]


class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]

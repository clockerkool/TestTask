from typing import List
from pydantic import BaseModel


class Department(BaseModel):
    departmentId: int
    displayName: str


class Departments(BaseModel):
    departments: List[Department] = []

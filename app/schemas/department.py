from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class Department(BaseModel):
    department_uuid: UUID
    department_name: str
    manager_uuid: Optional[UUID]
    location: str

class DepartmentCreate(BaseModel):
    department_name: str
    manager_uuid: Optional[UUID]
    location: str

class DepartmentUpdate(BaseModel):
    department_name: Optional[str]
    manager_uuid: Optional[UUID]
    location: Optional[str]
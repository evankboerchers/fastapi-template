from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


class Project(BaseModel):
    project_uuid: UUID
    project_name: str
    description: str
    start_date: str
    end_date: str
    assigned_employees: List[UUID]

class ProjectCreate(BaseModel):
    project_name: str
    description: str
    start_date: str
    end_date: str
    assigned_employees: List[UUID]

class ProjectUpdate(BaseModel):
    project_name: Optional[str]
    description: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    assigned_employees: Optional[List[UUID]]

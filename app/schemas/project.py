from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Project(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    uuid: UUID
    project_name: str
    description: str
    start_date: datetime
    end_date: datetime
    # employees: List[UUID]

class ProjectCreate(BaseModel):
    project_name: str
    description: str
    start_date: datetime
    end_date: datetime
    employees: List[UUID]

class ProjectUpdate(BaseModel):
    project_name: Optional[str]
    description: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    employees: Optional[List[UUID]]

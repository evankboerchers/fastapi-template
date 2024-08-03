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
    project_name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    employees: Optional[List[UUID]] = None

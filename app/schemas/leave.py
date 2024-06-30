from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Leave(BaseModel):
    leave_uuid: UUID
    employee_uuid: UUID
    leave_type: str
    start_date: str
    end_date: str
    status: str
    comments: Optional[str]

class LeaveCreate(BaseModel):
    employee_uuid: UUID
    leave_type: str
    start_date: str
    end_date: str
    status: str
    comments: Optional[str]

class LeaveUpdate(BaseModel):
    employee_uuid: Optional[UUID]
    leave_type: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    status: Optional[str]
    comments: Optional[str]

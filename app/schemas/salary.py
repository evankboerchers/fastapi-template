from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class Salary(BaseModel):
    salary_uuid: UUID
    employee_uuid: UUID
    salary_amount: float
    start_date: str
    end_date: Optional[str]

class SalaryCreate(BaseModel):
    employee_uuid: UUID
    salary_amount: float
    start_date: str
    end_date: Optional[str]

class SalaryUpdate(BaseModel):
    employee_uuid: Optional[UUID]
    salary_amount: Optional[float]
    start_date: Optional[str]
    end_date: Optional[str]
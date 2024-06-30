from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class Employee(BaseModel):
    employee_uuid: UUID
    first_name: str
    last_name: str
    date_of_birth: str
    email: str
    phone_number: str
    address: str
    department_uuid: Optional[UUID]
    position: str

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    email: str
    phone_number: str
    address: str
    department_uuid: Optional[UUID]
    position: str

class EmployeeUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    date_of_birth: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]
    department_uuid: Optional[UUID]
    position: Optional[str]
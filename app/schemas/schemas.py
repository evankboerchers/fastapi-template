from pydantic import BaseModel
from typing import List, Optional

class Employee(BaseModel):
    employee_id: int
    first_name: str
    last_name: str
    date_of_birth: str
    email: str
    phone_number: str
    address: str
    department_id: Optional[int]
    position: str

class Department(BaseModel):
    department_id: int
    department_name: str
    manager_id: Optional[int]
    location: str

class Salary(BaseModel):
    salary_id: int
    employee_id: int
    salary_amount: float
    start_date: str
    end_date: Optional[str]

class Leave(BaseModel):
    leave_id: int
    employee_id: int
    leave_type: str
    start_date: str
    end_date: str
    status: str
    comments: Optional[str]

class Department(BaseModel):
    project_id: int
    project_name: str
    description: str
    start_date: str
    end_date: str
    assigned_employees: List[int]

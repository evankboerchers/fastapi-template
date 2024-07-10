from app.models.salary import Salary
from app.services.crud.base import CRUDBase


class CRUDSalary(CRUDBase):
   pass 

salary = CRUDSalary(Salary)
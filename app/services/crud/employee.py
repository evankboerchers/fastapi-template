
from app.models.employee import Employee
from app.services.crud.base import CRUDBase


class CRUDEmployee(CRUDBase):
   pass

employee = CRUDEmployee(Employee)
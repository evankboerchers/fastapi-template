
from app.models.leave import Leave 
from app.services.crud.base import CRUDBase


class CRUDLeave(CRUDBase):
   pass

leave = CRUDLeave(Leave)
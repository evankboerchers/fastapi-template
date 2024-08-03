from app.models.project import Project
from app.services.crud.base import CRUDBase


class CRUDProject(CRUDBase):
   pass

project = CRUDProject(Project)
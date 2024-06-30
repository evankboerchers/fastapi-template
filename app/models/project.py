from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from app.models.mixins import UUIDPKMixin
from .base import Base
from .employee_project_association import  employee_project_association

class Project(Base, UUIDPKMixin):
    __tablename__ = 'projects'

    project_name = Column(String)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

    employees = relationship("Employee", secondary=employee_project_association, back_populates="projects")
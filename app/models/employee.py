from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.models.mixins import UUIDPKMixin
from .base import Base
from .employee_project_association import employee_project_association

class Employee(Base, UUIDPKMixin):
    __tablename__ = 'employees'

    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    address = Column(String)
    position = Column(String)

    salaries = relationship("Salary", back_populates="employee")
    leaves = relationship("Leave", back_populates="employee")
    projects = relationship("Project", secondary=employee_project_association, back_populates="employees")
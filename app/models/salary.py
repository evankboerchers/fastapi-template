from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.models.mixins import UUIDPKMixin
from .base import Base

class Salary(Base, UUIDPKMixin):
    __tablename__ = 'salaries'

    employee_uuid = Column(Integer, ForeignKey('employees.uuid'))
    salary_amount = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)

    employee = relationship("Employee", back_populates="salaries")
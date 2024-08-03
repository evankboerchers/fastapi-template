from sqlalchemy import Column, Float, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.mixins import UUIDPKMixin
from .base import Base

class Salary(Base, UUIDPKMixin):
    __tablename__ = 'salaries'

    employee_uuid = Column(UUID(as_uuid=True), ForeignKey('employees.uuid'))
    salary_amount = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)

    employee = relationship("Employee", back_populates="salaries")
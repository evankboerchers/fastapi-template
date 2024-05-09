from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Salary(Base):
    __tablename__ = 'salaries'

    salary_id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    salary_amount = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)

    employee = relationship("Employee", back_populates="salaries")
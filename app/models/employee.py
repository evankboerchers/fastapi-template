from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Employee(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    address = Column(String)
    department_id = Column(Integer, ForeignKey('departments.department_id'))
    position = Column(String)

    department = relationship("Department", back_populates="employees")
    salaries = relationship("Salary", back_populates="employee")
    attendances = relationship("Attendance", back_populates="employee")
    leaves = relationship("Leave", back_populates="employee")
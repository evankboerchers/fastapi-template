from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Leave(Base):
    __tablename__ = 'leaves'

    leave_id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    leave_type = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)
    comments = Column(String, nullable=True)

    employee = relationship("Employee", back_populates="leaves")
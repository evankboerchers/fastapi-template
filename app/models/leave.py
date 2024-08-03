from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.mixins import UUIDPKMixin
from .base import Base

class Leave(Base, UUIDPKMixin):
    __tablename__ = 'leaves'

    employee_uuid = Column(UUID(as_uuid=True), ForeignKey('employees.uuid'))
    leave_type = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)
    comments = Column(String, nullable=True)

    employee = relationship("Employee", back_populates="leaves")
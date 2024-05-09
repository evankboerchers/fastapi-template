from sqlalchemy import Column, Integer, String, Date
from .base import Base

class Project(Base):
    __tablename__ = 'projects'

    project_id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
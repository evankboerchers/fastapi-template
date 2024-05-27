from sqlalchemy import Table, Column, ForeignKey, Integer
from .base import Base

employee_project_association = Table(
    'employee_project', Base.metadata,
    Column('employee_id', Integer, ForeignKey('employees.employee_id')),
    Column('project_id', Integer, ForeignKey('projects.project_id'))
)
from sqlalchemy import Table, Column, ForeignKey, Integer
from .base import Base

employee_project_association = Table(
    'employee_project', Base.metadata,
    Column('employee_uuid', Integer, ForeignKey('employees.uuid')),
    Column('project_uuid', Integer, ForeignKey('projects.uuid'))
)
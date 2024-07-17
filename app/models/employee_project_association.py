from sqlalchemy import Table, Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from .base import Base

employee_project_association = Table(
    'employee_project', Base.metadata,
    Column('employee_uuid', UUID(as_uuid=True), ForeignKey('employees.uuid')),
    Column('project_uuid', UUID(as_uuid=True), ForeignKey('projects.uuid'))
)
import sys
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy_utils import database_exists, create_database

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from app.models import Base, Employee, Leave, Project, Salary, employee_project_association

DATABASE_URL = "postgresql://postgres:password@localhost/fastapp"
engine = create_engine(DATABASE_URL)

if not database_exists(engine.url):
    create_database(engine.url)

def create_database():
    metadata = MetaData()
    metadata.create_all(bind=engine, tables=[Employee.__table__, Leave.__table__, Project.__table__, Salary.__table__])
    metadata.create_all(bind=engine, tables=[employee_project_association])

if __name__ == "__main__":
    create_database()

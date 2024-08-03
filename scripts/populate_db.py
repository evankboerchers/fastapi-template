import sys
import os
import csv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from app.models import Employee, Leave, Project, Salary, employee_project_association

DATABASE_URL = "postgresql://postgres:password@localhost:5111/fastapp"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

if not database_exists(engine.url):
    create_database(engine.url)

def create_database():
    metadata = MetaData()
    metadata.create_all(bind=engine, tables=[Employee.__table__, Leave.__table__, Project.__table__, Salary.__table__])
    metadata.create_all(bind=engine, tables=[employee_project_association])

def import_employees(session, file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employee = Employee(
                uuid=row['uuid'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                date_of_birth=row['date_of_birth'],
                email=row['email'],
                phone_number=row['phone_number'],
                address=row['address'],
                position=row['position']
            )
            session.add(employee)

def import_projects(session, file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            project = Project(
                uuid=row['uuid'],
                project_name=row['project_name'],
                description=row['description'],
                start_date=row['start_date'],
                end_date=row['end_date']
            )
            session.add(project)

def import_leaves(session, file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            leave = Leave(
                uuid=row['uuid'],
                employee_uuid=row['employee_uuid'],
                leave_type=row['leave_type'],
                start_date=row['start_date'],
                end_date=row['end_date'],
                status=row['status'],
                comments=row['comments']
            )
            session.add(leave)

def import_salaries(session, file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            salary = Salary(
                uuid=row['uuid'],
                employee_uuid=row['employee_uuid'],
                salary_amount=row['salary_amount'],
                start_date=row['start_date'],
                end_date=row['end_date']
            )
            session.add(salary)

def import_employee_projects(session, file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employee_uuid = row['employee_uuid']
            project_uuid = row['project_uuid']
            stmt = employee_project_association.insert().values(employee_uuid=employee_uuid, project_uuid=project_uuid)
            session.execute(stmt)

def clear_all_tables(session):
    """Custom rollback function to clear all tables."""
    session.execute("TRUNCATE TABLE employees, projects, leaves, salaries, employee_project_association RESTART IDENTITY CASCADE")
    session.commit()

def main():
    session = SessionLocal()
    create_database()
    try:
        import_employees(session, 'data/db_init/employees.csv')
        import_projects(session, 'data/db_init/projects.csv')
        session.commit() 

        import_leaves(session, 'data/db_init/leaves.csv')
        import_salaries(session, 'data/db_init/salaries.csv')
        session.commit() 

        import_employee_projects(session, 'data/db_init/employee_project_association.csv')
        session.commit() 
        print("Sucessfully populated db")
    except Exception as e:
        clear_all_tables()
        session.rollback()
        raise e
    finally:
        session.close()

if __name__ == "__main__":
    main()

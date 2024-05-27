import sys
import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, drop_database

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

DATABASE_URL = "postgresql://postgres:password@localhost/fastapp"  # Update with your PostgreSQL credentials
engine = create_engine(DATABASE_URL)

def drop_db():
    if database_exists(engine.url):
        drop_database(engine.url)
        print("Database dropped successfully.")
    else:
        print("Database does not exist.")

if __name__ == "__main__":
    drop_db()

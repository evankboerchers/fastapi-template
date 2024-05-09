from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..app.models import Base

DATABASE_URL = "postgresql://username:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_database():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_database()

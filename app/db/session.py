from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

connection_str = "postgresql://postgres:password@localhost:5111/fastapp"

engine = create_engine(connection_str, 
                        echo=True, # TODO: change to env var
                        connect_args={"options": "-c timezone=utc"},
                        query_cache_size=0
                    )
sessionmaker = sessionmaker(
    autoflush=True,
    autocommit=False,
    bind=engine
)

def get_session():
    return sessionmaker()
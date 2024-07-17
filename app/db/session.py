from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import config

connection_str = f"{config.DB_CONN_METHOD}://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOSTNAME}/{config.DB_DATABASE}"
# connection_str = "postgresql://postgres:password@localhost:5111/fastapp"


engine = create_engine(connection_str, 
                        echo=config.DB_ECHO, # TODO: change to env var
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
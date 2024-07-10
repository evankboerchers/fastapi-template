"""Database dependency."""
from typing import AsyncIterable

from fastapi import Depends
from fastapi import Request
from sqlalchemy.orm import Session

from app.db.session import get_session

async def get_db(db=Depends(get_session)) -> AsyncIterable[Session]:
    """Yield a db session."""
    try:
        yield db
    finally:
        db.close()

def attach_db(request: Request, db: Session = Depends(get_db)):
    """Attach a db session to request."""
    request.state.db = db
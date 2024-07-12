from fastapi import APIRouter, Depends, Request
from app.api.dependencies.db import get_db
from sqlalchemy.orm import Session

from app.schemas.employee import Employee

router = APIRouter(
    prefix='/employees', tags=['employees']
)

@router.get("/{id}", response_model=Employee)
def get_project(request: Request, id: str, db: Session = Depends(get_db)) -> Employee:
    return 
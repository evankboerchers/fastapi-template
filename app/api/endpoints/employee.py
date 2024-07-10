from fastapi import APIRouter, Depends, Request
from app.schemas import Department
from app.api.dependencies.db import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/projects', tags=['projects']]
)

@router.get("/{id}", response_model=Department)
def get_project(request: Request, id: str, db: Session = Depends(get_db)) -> Department:

    return 
from uuid import UUID
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.api.dependencies.db import get_db
from app.schemas.project import Project
from app.services import crud

router = APIRouter(
    prefix='/projects', tags=['projects']
)

@router.get("/{uuid}", response_model=Project)
def get_project(request: Request, uuid: UUID, db: Session = Depends(get_db)) -> Project:
    return crud.project.get(db=db, pk=uuid)
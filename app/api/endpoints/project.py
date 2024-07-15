from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.api.dependencies.db import get_db
from app.schemas.project import Project, ProjectCreate, ProjectUpdate
from app.services import crud

router: APIRouter = APIRouter(
    prefix='/projects', tags=['projects']
)

@router.post("", response_model=Project)
def post_project(body: ProjectCreate , db: Session = Depends(get_db)) -> Project:
    return crud.project.create(db=db, obj=body)

@router.get("/{uuid}", response_model=Project)
def get_project(uuid: UUID, db: Session = Depends(get_db)) -> Project:
    return crud.project.get(db=db, pk=uuid)

@router.get("", response_model=List[Project])
def get_projects(db: Session = Depends(get_db)) -> Project:
    return crud.project.get_multi(db=db)

@router.patch("/{uuid}", response_model=Project)
def patch_project(body: ProjectUpdate, uuid: UUID, db: Session = Depends(get_db)) -> Project:
    return crud.project.update(db=db, pk=uuid, obj=body)



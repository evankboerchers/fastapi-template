from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies.db import get_db
from app.schemas.salary import Salary, SalaryCreate, SalaryUpdate
from app.services import crud

router = APIRouter(
    prefix='/salaries', tags=['salaries']
)

@router.post("", response_model=Salary)
def post_salary(body: SalaryCreate , db: Session = Depends(get_db)) -> Salary:
    return crud.project.create(db=db, obj=body)

@router.get("/{uuid}", response_model=Salary)
def get_salary(uuid: UUID, db: Session = Depends(get_db)) -> Salary:
    return crud.project.get(db=db, pk=uuid)

@router.get("", response_model=List[Salary])
def get_salaries(db: Session = Depends(get_db)) -> Salary:
    return crud.project.get_multi(db=db)

@router.patch("/{uuid}", response_model=Salary)
def patch_salary(body: SalaryUpdate, uuid: UUID, db: Session = Depends(get_db)) -> Salary:
    return crud.project.update(db=db, pk=uuid, obj=body)

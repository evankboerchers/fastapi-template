from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from app.api.dependencies.db import get_db
from sqlalchemy.orm import Session

from app.schemas.employee import Employee, EmployeeCreate, EmployeeUpdate
from app.services import crud

router = APIRouter(
    prefix='/employees', tags=['employees']
)

@router.post("", response_model=Employee)
def post_employee(body: EmployeeCreate , db: Session = Depends(get_db)) -> Employee:
    return crud.employee.create(db=db, obj=body)

@router.get("/{uuid}", response_model=Employee)
def get_employee(uuid: UUID, db: Session = Depends(get_db)) -> Employee:
    return crud.employee.get(db=db, pk=uuid)

@router.get("", response_model=List[Employee])
def get_employees(db: Session = Depends(get_db)) -> Employee:
    return crud.employee.get_multi(db=db)

@router.patch("/{uuid}", response_model=Employee)
def patch_employee(body: EmployeeUpdate, uuid: UUID, db: Session = Depends(get_db)) -> Employee:
    return crud.employee.update(db=db, pk=uuid, obj=body)

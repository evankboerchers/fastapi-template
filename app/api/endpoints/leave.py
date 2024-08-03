from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies.db import get_db
from app.schemas.leave import Leave, LeaveCreate, LeaveUpdate
from app.services import crud


router = APIRouter(
    prefix='/leaves', tags=['leaves']
)

@router.post("", response_model=Leave)
def post_leave(body: LeaveCreate , db: Session = Depends(get_db)) -> Leave:
    return crud.leave.create(db=db, obj=body)

@router.get("/{uuid}", response_model=Leave)
def get_leave(uuid: UUID, db: Session = Depends(get_db)) -> Leave:
    return crud.leave.get(db=db, pk=uuid)

@router.get("", response_model=List[Leave])
def get_leaves(db: Session = Depends(get_db)) -> Leave:
    return crud.leave.get_multi(db=db)

@router.patch("/{uuid}", response_model=Leave)
def patch_leave(body: LeaveUpdate, uuid: UUID, db: Session = Depends(get_db)) -> Leave:
    return crud.leave.update(db=db, pk=uuid, obj=body)

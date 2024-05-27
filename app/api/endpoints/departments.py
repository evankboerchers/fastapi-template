from fastapi import APIRouter, Request
from app.schemas import Department

router = APIRouter(
    prefix='/departments', tags=['projects']
)

@router.get("", response_model=List[Department])
def get_project(request: Request):
    return
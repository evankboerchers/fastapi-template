from fastapi import APIRouter, Request
from app.schemas import Department

router = APIRouter(
    prefix='/projects', tags=['projects']
)

@router.get("/{id}", response_model=Department)
def get_project(request: Request, id: str) -> Department:
    return crud.
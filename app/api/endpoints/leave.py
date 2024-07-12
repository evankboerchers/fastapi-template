from fastapi import APIRouter, Request
from app.schemas.leave import Leave 

router = APIRouter(
    prefix='/leaves', tags=['leaves']
)

@router.get("/{id}", response_model=Leave)
def get_project(request: Request, id: str) -> Leave:
    return 
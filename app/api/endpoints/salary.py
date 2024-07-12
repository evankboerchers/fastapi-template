from fastapi import APIRouter, Request

from app.schemas.salary import Salary

router = APIRouter(
    prefix='/salaries', tags=['salaries']
)

@router.get("/{id}", response_model=Salary)
def get_project(request: Request, id: str) -> Salary:
    return 
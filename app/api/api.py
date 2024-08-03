from .endpoints.employee import router as employees_router
from .endpoints.leave import router as leave_router
from .endpoints.project import router as projects_router
from .endpoints.salary import router as salary_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(employees_router)
router.include_router(leave_router)
router.include_router(projects_router)
router.include_router(salary_router)
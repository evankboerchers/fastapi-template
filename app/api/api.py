from .endpoints.departments import router as department_router
from .endpoints.employees import router as employees_router
from .endpoints.leave import router as leave_router
from .endpoints.project import router as projects_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(department_router)
router.include_router(employees_router)
router.include_router(leave_router)
router.include_router(projects_router)
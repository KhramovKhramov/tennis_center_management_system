from fastapi import APIRouter

from src.api.health.router import router as health_router
from src.api.user.router import router as user_router

router = APIRouter(prefix='/api')
router.include_router(health_router)
router.include_router(user_router)

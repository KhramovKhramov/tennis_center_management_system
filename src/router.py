from fastapi import APIRouter

from src.api.health.router import router as health_router

router = APIRouter(prefix='/api')
router.include_router(health_router)

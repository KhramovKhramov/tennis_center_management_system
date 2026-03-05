from fastapi import APIRouter

from src.entrypoints.api.health.router import router as health_check_router

api_router = APIRouter(prefix="/api")

api_router.include_router(health_check_router)

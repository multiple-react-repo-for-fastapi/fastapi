from fastapi import APIRouter

from .a_view import router as a_router


router = APIRouter()
router.include_router(a_router)

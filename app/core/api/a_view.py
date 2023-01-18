from fastapi import APIRouter

from app.core.models import User


router = APIRouter()


@router.get("/hello")
async def hello():
    await User.objects.acreate(name="random")
    return {"message": f"Hello World, count: {await User.objects.acount()}"}

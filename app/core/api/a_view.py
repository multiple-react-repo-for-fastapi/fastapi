from app.core.models import User
from app.fast import templates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse


template_router = APIRouter()
api_router = APIRouter(prefix="/api")


@template_router.post("/login")
async def login():
    response = RedirectResponse("/")
    response.set_cookie("session", "123")
    response.status_code = 302
    return response


@template_router.get("/{full_path:path}", response_class=HTMLResponse)
async def get(request: Request, full_path: str):
    await User.objects.acreate(name="random")
    if request.user.is_authenticated:
        return templates.TemplateResponse("login.html", {"request": request})
    return templates.TemplateResponse("splash.html", {"request": request})


@api_router.get("/user")
async def get_data():
    """
    This is a regular API request, but you only need to enable cookie in
    your fetch request since you should rely on session HttpOnly cookies.
    """
    return {"data": "data"}

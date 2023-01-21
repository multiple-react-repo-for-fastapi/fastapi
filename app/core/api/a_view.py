from app.fast import templates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse


template_router = APIRouter()
api_router = APIRouter(prefix="/api")


@template_router.post("/login")
def login():
    response = RedirectResponse("/")
    response.set_cookie("session", "123")
    response.status_code = 302
    return response


@template_router.get("/{full_path:path}", response_class=HTMLResponse)
def get(request: Request, full_path: str):
    if request.user.is_authenticated:
        return templates.TemplateResponse("dashboard.html", {"request": request})
    return templates.TemplateResponse("landing.html", {"request": request})


@api_router.get("/user")
def get_data():
    """
    This is a regular API request, but you only need to enable cookie in
    your fetch request since you should rely on session HttpOnly cookies.
    """
    return {"data": "data"}

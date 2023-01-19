from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app.fast import templates


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def default_page(request: Request):
    if "session" in request.cookies:
        return templates.TemplateResponse("login.html", {"request": request})
    return templates.TemplateResponse("splash.html", {"request": request})


@router.post("/login")
def login():
    response = RedirectResponse("/")
    response.set_cookie("session", "123")
    response.status_code = 302
    return response

from django import setup as django_setup
from django.core.handlers.asgi import ASGIHandler

from app.core.api.a_view import api_router, template_router
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


django_setup(set_prefix=False)
application = ASGIHandler()
fast = FastAPI(title="My app", openapi_url=f"/openapi.json")

fast.include_router(api_router)
fast.include_router(template_router)
fast.mount("/static", StaticFiles(directory="app/static"), name="static")
fast.mount("/d", application)  # noqa

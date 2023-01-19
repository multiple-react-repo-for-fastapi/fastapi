from django import setup as django_setup
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from django.core.handlers.asgi import ASGIHandler


def get_asgi_application():
    """
    The public interface to Django's ASGI support. Return an ASGI 3 callable.

    Avoids making django.core.handlers.ASGIHandler a public API, in case the
    internal implementation changes or moves in the future.
    """
    django_setup(set_prefix=False)
    return ASGIHandler()


application = get_asgi_application()
fast = FastAPI(title="My app", openapi_url=f"/openapi.json")

from app.core.api import router  # noqa

fast.include_router(router)
fast.mount("/static", StaticFiles(directory="app/static"), name="static")
fast.mount("/d", application)

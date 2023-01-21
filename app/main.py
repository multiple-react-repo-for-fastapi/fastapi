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


import base64
import binascii

from starlette.applications import Starlette
from starlette.authentication import (
    AuthCredentials,
    AuthenticationBackend,
    AuthenticationError,
    SimpleUser,
)
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import PlainTextResponse
from starlette.routing import Route


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        if "Authorization" not in conn.headers:
            return

        auth = conn.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != "basic":
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError("Invalid basic auth credentials")

        username, _, password = decoded.partition(":")
        # TODO: You'd want to verify the username and password here.
        return AuthCredentials(["authenticated"]), SimpleUser(username)


fast.add_middleware(AuthenticationMiddleware, backend=BasicAuthBackend())

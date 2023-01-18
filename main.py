#!/usr/bin/env python

import os

import click
import uvicorn


@click.group()
def run():
    ...


@click.command("run", help="Runs the FastAPI server")
@click.option(
    "--host",
    default="127.0.0.1",
    help="The host to bind to; set to 0.0.0.0 for external network usage",
)
@click.option("--port", default=5000, type=int)
@click.option(
    "--log-level",
    default="info",
    type=click.Choice(["debug", "info", "warning", "error"]),
)
@click.option("--reload", is_flag=True, default=False)
@click.option("--settings", default="production")
def run_fast(host, port, log_level, reload, settings: str):
    # Turn off bytecode generation
    import sys

    sys.dont_write_bytecode = True
    if settings not in {"production", "staging", "local"}:
        raise ValueError(
            f"Invalid settings value: {settings}."
            "Must be one of: production, staging, or local"
        )
    os.environ["DJANGO_SETTINGS_MODULE"] = f"config.settings.{settings}"

    uvicorn.run(
        "app.main:fast",
        host=host,
        port=port,
        log_level=log_level,
        reload=reload,
        reload_includes=["app", "config", "manage.py"],
    )


run.add_command(run_fast)


if __name__ == "__main__":
    run()

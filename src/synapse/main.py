"""Synapse gateway — FastAPI application entry point."""

from fastapi import FastAPI

from synapse.config import get_settings

__version__ = "0.1.0"


def create_app() -> FastAPI:
    """Build and configure the FastAPI application.

    Using a factory function (rather than a module-level `app = FastAPI()`)
    makes testing easier: each test can build a fresh app instance.
    """
    app = FastAPI(
        title="Synapse",
        description="Cost-aware LLM router.",
        version=__version__,
    )

    @app.get("/healthz")
    async def healthz() -> dict[str, str]:
        """Liveness probe. Returns 200 if the process is up.

        Kubernetes hits this to know whether to restart the pod.
        It must NOT check downstream dependencies — a slow database
        should not cause the gateway to be killed.
        """
        return {"status": "ok"}

    @app.get("/readyz")
    async def readyz() -> dict[str, str]:
        """Readiness probe. Returns 200 if ready to serve traffic.

        Kubernetes hits this to decide whether to route traffic here.
        In v0.1 it always returns ready. Later milestones will check
        that backends, Redis, and Postgres are reachable.
        """
        return {"status": "ready"}

    return app


# The ASGI server (uvicorn) imports this `app` object.
app = create_app()


def run() -> None:
    """CLI entry point: `synapse` runs this. Starts the uvicorn server."""
    import uvicorn

    settings = get_settings()
    uvicorn.run(
        "synapse.main:app",
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level.lower(),
    )

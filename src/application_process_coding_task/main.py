import typer
import uvicorn
from fastapi import FastAPI

from application_process_coding_task.config import settings

api = FastAPI(title=settings.name)
cli = typer.Typer()


@api.get("/")
def health_check() -> dict[str, str]:
    return {"status": "API is running"}


def run_server() -> None:
    """Start the FastAPI server via the CLI."""
    uvicorn.run(
        "application_process_coding_task.main:api",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
    )


@cli.command()
def start_server() -> None:
    run_server()


if __name__ == "__main__":
    run_server()

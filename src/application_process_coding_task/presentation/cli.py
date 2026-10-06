import typer
import uvicorn

from application_process_coding_task.config import settings

app = typer.Typer()


@app.callback()
def main() -> None:
    """Application management commands."""


@app.command("start-server")
def start_server() -> None:
    """Start the FastAPI server using environment-based configuration."""
    uvicorn.run(
        "application_process_coding_task.main:api",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
    )


if __name__ == "__main__":
    app()

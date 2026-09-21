import typer

app = typer.Typer()


@app.callback()
def main() -> None:
    """Application management commands."""


@app.command()
def deploy(env: str) -> None:
    typer.echo(f"Deploying to {env}")


if __name__ == "__main__":
    app()
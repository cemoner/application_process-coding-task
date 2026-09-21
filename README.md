# Application Process Coding Task

FastAPI application scaffold managed with Python 3.14 and `uv`.

## Requirements

- Python 3.14+
- `uv`
- Docker and Docker Compose (for containerized execution)

## Local setup

Create the virtual environment and install the locked dependencies:

```bash
uv sync
```

The application reads settings from an ignored `.env` file using the `APP_` prefix. A local
`.env` should contain values such as:

```dotenv
APP_NAME=Coding Task API
APP_HOST=0.0.0.0
APP_PORT=8000
APP_RELOAD=false
APP_SOURCE_PATH=source.parquet
APP_TARGET_EOD_PATH=target_eod.csv
APP_TARGET_ORDERBOOK_PATH=target_orderbook.csv
```

Start the API locally:

```bash
uv run python -m application_process_coding_task.main
```

The server listens on the configured host and port. Swagger UI is available at
`http://localhost:8000/docs`, and the ReDoc interface is available at
`http://localhost:8000/redoc`.

## Docker

Build and start the API with Compose:

```bash
docker compose up --build
```

`compose.yaml` injects the local `.env` file into the container at runtime through
Compose's `env_file` option. The `.env` file is intentionally not copied into the image
and is excluded from Git.

Stop the service with:

```bash
docker compose down
```

To run the image directly, build it and pass the environment file explicitly:

```bash
docker build -t application-process-coding-task .
docker run --env-file .env -p 8000:8000 application-process-coding-task
```

When `APP_PORT` is changed, use the same port on both sides of the direct Docker port
mapping, for example `-p 9000:9000`.

## Quality checks

Run the configured lint and type checks:

```bash
uv run ruff check .
uv run mypy src
```

Run tests:

```bash
uv run pytest
```

## Repository layout

```text
src/application_process_coding_task/
├── application/
├── domain/
├── infrastructure/
├── presentation/
├── config.py
└── main.py
```

The supplied Parquet and CSV files are kept at the repository root and are available to
the application through the configured paths.

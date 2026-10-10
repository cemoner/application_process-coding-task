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

The application has safe defaults for local execution. To customize them, copy the committed
template to the ignored `.env` file:

```bash
cp .env.example .env
```

The application reads settings from `.env` using the `APP_` prefix:

```dotenv
APP_NAME=Coding Task API
APP_HOST=0.0.0.0
APP_PORT=8000
APP_RELOAD=false
APP_SOURCE_PATH=source.parquet
```

Start the API locally:

```bash
uv run application-process-coding-task start-server
```

The server listens on the configured host and port. Swagger UI is available at
`http://localhost:8000/docs`, and the ReDoc interface is available at
`http://localhost:8000/redoc`.

The same server can also be started directly with:

```bash
uv run python -m application_process_coding_task.main
```

## API usage

Single-RIC lookups use `GET`; multiple-RIC lookups use `POST`. The `type` value can be
`csv` or `json`, and defaults to `csv`.

```bash
curl --no-buffer \
  "http://localhost:8000/eod?ric=SETH27&date=2026-09-04&type=json"
```

```bash
curl --no-buffer -X POST "http://localhost:8000/eod" \
  -H "Content-Type: application/json" \
  -d '{"date":"2026-09-04","rics":["SETH27","SETH28"],"type":"csv"}'
```

```bash
curl --no-buffer \
  "http://localhost:8000/orderbook?ric=SETU26&date=2026-09-04&type=json"
```

```bash
curl --no-buffer -X POST "http://localhost:8000/orderbook" \
  -H "Content-Type: application/json" \
  -d '{"date":"2026-09-04","rics":["SETU26","SETZ26"],"type":"csv"}'
```

JSON responses are streamed as newline-delimited JSON (`application/x-ndjson`). CSV
responses are streamed as semicolon-delimited data using the target-file column aliases.
Use `--no-buffer` with curl to observe records as they arrive.

## Docker

Build and start the API with Compose:

```bash
docker compose up --build
```

`compose.yaml` injects the local `.env` file into the container at runtime through
Compose's `env_file` option when it exists. The file is optional because the application
also provides defaults. The `.env` file is intentionally not copied into the image and is
excluded from Git.

Stop the service with:

```bash
docker compose down
```

To run the image directly, build it and pass the environment file explicitly:

```bash
docker build -t application-process-coding-task .
docker run --env-file .env -p 8000:8000 application-process-coding-task
```

If you do not create `.env`, run the image without `--env-file`:

```bash
docker run -p 8000:8000 application-process-coding-task
```

When `APP_PORT` is changed, use the same port on both sides of the direct Docker port
mapping, for example `-p 9000:9000`. Compose uses the same value for the host and
container port.

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

The supplied `source.parquet` file is used by the application through `APP_SOURCE_PATH`.
The target CSV files are reference fixtures for validation and are not runtime inputs.

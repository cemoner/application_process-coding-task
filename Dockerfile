FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./
COPY src ./src
COPY source.parquet ./
COPY target_eod.csv ./
COPY target_orderbook.csv ./

RUN uv sync --frozen --no-dev

CMD ["uv", "run", "python", "-m", "application_process_coding_task.presentation.router.main"]

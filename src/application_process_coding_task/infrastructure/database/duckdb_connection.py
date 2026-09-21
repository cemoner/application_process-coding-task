from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

import duckdb


@contextmanager
def get_duckdb_connection(
    source_path: Path,
) -> Iterator[duckdb.DuckDBPyConnection]:
    if not source_path.is_file():
        raise FileNotFoundError(f"Parquet source file not found: {source_path}")

    connection = duckdb.connect()
    try:
        yield connection
    finally:
        connection.close()

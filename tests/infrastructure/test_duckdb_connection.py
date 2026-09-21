from pathlib import Path

import duckdb
import pytest

from application_process_coding_task.infrastructure.database.duckdb_connection import (
    get_duckdb_connection,
)

SOURCE_PATH = Path(__file__).parents[2] / "source.parquet"


def test_reads_rows_from_source_parquet() -> None:
    with get_duckdb_connection(SOURCE_PATH) as connection:
        row_count = connection.execute(
            "SELECT COUNT(*) FROM read_parquet(?)",
            [str(SOURCE_PATH)],
        ).fetchone()

    assert row_count is not None
    assert row_count[0] == 12_079


def test_retrieves_settlement_record_from_source_parquet() -> None:
    with get_duckdb_connection(SOURCE_PATH) as connection:
        record = connection.execute(
            """
            SELECT "#RIC", "Date-Time", "Price"
            FROM read_parquet(?)
            WHERE "#RIC" = ? AND "Type" = ?
            ORDER BY "Date-Time"
            LIMIT 1
            """,
            [str(SOURCE_PATH), "SETH27", "Settlement Price"],
        ).fetchone()

    assert record == ("SETH27", "2026-09-03T23:03:19.356147683Z", "121.05")


def test_rejects_missing_source_file(tmp_path: Path) -> None:
    missing_path = tmp_path / "missing.parquet"

    with pytest.raises(FileNotFoundError), get_duckdb_connection(missing_path):
        pass


def test_connection_is_closed_after_context() -> None:
    connection: duckdb.DuckDBPyConnection

    with get_duckdb_connection(SOURCE_PATH) as connection:
        connection.execute("SELECT 1")

    with pytest.raises(duckdb.ConnectionException):
        connection.execute("SELECT 1")

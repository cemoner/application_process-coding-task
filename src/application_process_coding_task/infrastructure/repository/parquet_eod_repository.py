from collections.abc import Iterator
from pathlib import Path

from application_process_coding_task.application.dto.query.eod_query import (
    MultipleEodQuery,
    SingleEodQuery,
)
from application_process_coding_task.domain.entity.eod_record import EodRecord
from application_process_coding_task.infrastructure.database.duckdb_connection import (
    get_duckdb_connection,
)
from application_process_coding_task.infrastructure.mapper.eod_mapper import to_eod_record


class ParquetEodRepository:
    def __init__(self, source_path: Path) -> None:
        self.source_path = source_path
        # Shared base SQL to avoid duplication
        self.base_sql = """
                        SELECT "#RIC", \
                               CAST("Date-Time" AS DATE) AS trade_date, \
                               "Bid Price", \
                               "Ask Price", \
                               "Price"
                        FROM read_parquet(?)
                        WHERE "Type" = 'Settlement Price'
                          AND CAST("Date-Time" AS DATE) = ? \
                        """

        self.qualify_sql = """
                    QUALIFY ROW_NUMBER() OVER (
                        PARTITION BY "#RIC"
                        ORDER BY "Date-Time" DESC
                    ) = 1
                    ORDER BY "#RIC"
                """

    def find_single(self, query: SingleEodQuery) -> Iterator[EodRecord]:
        sql = self.base_sql + ' AND "#RIC" = ? ' + self.qualify_sql
        parameters = [str(self.source_path), query.trade_date, query.ric]

        return self._stream_results(sql, parameters)

    def find_multiple(self, query: MultipleEodQuery) -> Iterator[EodRecord]:
        placeholders = ", ".join("?" for _ in query.rics)
        sql = self.base_sql + f' AND "#RIC" IN ({placeholders}) ' + self.qualify_sql
        parameters = [str(self.source_path), query.trade_date, *query.rics]

        return self._stream_results(sql, parameters)

    def _stream_results(self, sql: str, parameters: list[object]) -> Iterator[EodRecord]:
        with get_duckdb_connection(self.source_path) as connection:
            cursor = connection.execute(sql, parameters)
            while True:
                rows = cursor.fetchmany(1000)
                if not rows:
                    break
                for row in rows:
                    yield to_eod_record(row)

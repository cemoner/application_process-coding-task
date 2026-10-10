from collections.abc import Iterator
from pathlib import Path

from application_process_coding_task.domain.entity.orderbook_record import OrderBookRecord
from application_process_coding_task.domain.query.lookup_query import (
    MultipleLookup,
    SingleLookup,
)
from application_process_coding_task.infrastructure.database.duckdb_connection import (
    get_duckdb_connection,
)
from application_process_coding_task.infrastructure.mapper.orderbook_mapper import (
    to_orderbook_record,
)


class ParquetOrderBookRepository:
    def __init__(self, source_path: Path) -> None:
        self.source_path = source_path

        # Shared base SQL for quotes
        self.base_sql = """
                        SELECT "#RIC", \
                               NULL AS "Alias Underlying RIC", \
                               "Domain", \
                               "Date-Time", \
                               "GMT Offset", \
                               "Type", \
                               "Bid Price", \
                               "Bid Size", \
                               "Ask Price", \
                               "Ask Size"
                        FROM read_parquet(?)
                        WHERE "Type" = 'Quote'
                          AND CAST("Date-Time" AS DATE) = ? \
                          AND ("Bid Price" IS NOT NULL OR "Ask Price" IS NOT NULL)
                        """

    def find_single(self, query: SingleLookup) -> Iterator[OrderBookRecord]:

        sql = self.base_sql + ' AND "#RIC" = ? ORDER BY "Date-Time"'
        parameters: list[object] = [str(self.source_path), query.trade_date, query.ric]

        return self._stream_results(sql, parameters)

    def find_multiple(self, query: MultipleLookup) -> Iterator[OrderBookRecord]:

        placeholders = ", ".join("?" for _ in query.rics)
        sql = self.base_sql + f' AND "#RIC" IN ({placeholders}) ORDER BY "Date-Time"'
        parameters: list[object] = [str(self.source_path), query.trade_date, *query.rics]

        return self._stream_results(sql, parameters)

    def _stream_results(self, sql: str, parameters: list[object]) -> Iterator[OrderBookRecord]:

        with get_duckdb_connection(self.source_path) as connection:
            cursor = connection.execute(sql, parameters)

            while True:
                rows = cursor.fetchmany(1000)
                if not rows:
                    break
                for row in rows:
                    yield to_orderbook_record(row)

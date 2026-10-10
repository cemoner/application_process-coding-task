from datetime import date
from pathlib import Path
from typing import Iterator

from application_process_coding_task.application.dto.query.orderbook_query import MultipleOrderBookQuery, \
    SingleOrderBookQuery
from application_process_coding_task.domain.entity.orderbook_record import (
    OrderBookRecord,
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

    def find_quotes_by_date(
        self,
        trade_date: date,
        query: SingleOrderBookQuery | MultipleOrderBookQuery
    ) -> Iterator[OrderBookRecord]:
        """Return quote events for a date, optionally filtered by RICs."""


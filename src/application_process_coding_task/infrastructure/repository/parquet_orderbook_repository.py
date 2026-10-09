from datetime import date
from pathlib import Path
from typing import Iterator

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
        ric: str
    ) -> Iterator[OrderBookRecord]:


    def find_quotes_by_date(
            self,
            trade_date:date,
            rics: list[str]

     ) -> Iterator[OrderBookRecord]:


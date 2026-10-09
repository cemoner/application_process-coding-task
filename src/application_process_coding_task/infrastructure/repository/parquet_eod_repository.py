from datetime import date
from pathlib import Path

from application_process_coding_task.domain.entity.eod_record import EodRecord
from typing import Iterator
from application_process_coding_task.infrastructure.database.duckdb_connection import (
    get_duckdb_connection,
)
from application_process_coding_task.infrastructure.mapper.eod_mapper import (
    to_eod_record,
)


class ParquetEodRepository:
    def __init__(self, source_path: Path) -> None:
        self.source_path = source_path

    def find_by_date(
        self,
        trade_date: date,
        ric: str
    ) -> Iterator[EodRecord]:


    def find_by_date(
            self,
            trade_date: date,
            rics: list[str]
    ) -> Iterator[EodRecord]:

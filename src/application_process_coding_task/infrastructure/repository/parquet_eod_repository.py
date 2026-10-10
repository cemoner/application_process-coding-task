from datetime import date
from pathlib import Path

from application_process_coding_task.domain.entity.eod_record import EodRecord
from typing import Iterator



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

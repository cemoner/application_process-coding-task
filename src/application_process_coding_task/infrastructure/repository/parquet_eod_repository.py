from datetime import date
from pathlib import Path

from application_process_coding_task.application.dto.query.eod_query import SingleEodQuery, MultipleEodQuery
from application_process_coding_task.domain.entity.eod_record import EodRecord
from typing import Iterator



class ParquetEodRepository:
    def __init__(self, source_path: Path) -> None:
        self.source_path = source_path

    def find_by_date(
        self,
        trade_date: date,
        query: SingleEodQuery | MultipleEodQuery
    ) -> Iterator[EodRecord]:
        """Return EOD records for a date, optionally filtered by RICs."""
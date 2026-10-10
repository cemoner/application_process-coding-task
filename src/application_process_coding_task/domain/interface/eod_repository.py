from datetime import date
from typing import Protocol, Iterator

from application_process_coding_task.application.dto.query.eod_query import SingleEodQuery, MultipleEodQuery
from application_process_coding_task.domain.entity.eod_record import (
    EodRecord,
)


class EodRepository(Protocol):
    def find_by_date(
        self,
        trade_date: date,
        query: SingleEodQuery | MultipleEodQuery

    ) -> Iterator[EodRecord]:
        """Return EOD records for a date, optionally filtered by RICs."""
from datetime import date
from typing import Protocol, Iterator

from application_process_coding_task.application.dto.query.eod_query import SingleEodQuery, MultipleEodQuery
from application_process_coding_task.domain.entity.eod_record import (
    EodRecord,
)


class EodRepository(Protocol):
    def find_single(self, query: SingleEodQuery) -> Iterator[EodRecord]:
        pass

    def find_multiple(self, query: MultipleEodQuery) -> Iterator[EodRecord]:
        pass
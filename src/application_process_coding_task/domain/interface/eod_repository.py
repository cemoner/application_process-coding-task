from collections.abc import Iterator
from typing import Protocol

from application_process_coding_task.application.dto.query.eod_query import (
    MultipleEodQuery,
    SingleEodQuery,
)
from application_process_coding_task.domain.entity.eod_record import (
    EodRecord,
)


class EodRepository(Protocol):
    def find_single(self, query: SingleEodQuery) -> Iterator[EodRecord]:
        pass

    def find_multiple(self, query: MultipleEodQuery) -> Iterator[EodRecord]:
        pass

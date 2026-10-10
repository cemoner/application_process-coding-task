from collections.abc import Iterator
from typing import Protocol

from application_process_coding_task.domain.entity.eod_record import (
    EodRecord,
)
from application_process_coding_task.domain.query.lookup_query import (
    MultipleLookup,
    SingleLookup,
)


class EodRepository(Protocol):
    def find_single(self, query: SingleLookup) -> Iterator[EodRecord]:
        pass

    def find_multiple(self, query: MultipleLookup) -> Iterator[EodRecord]:
        pass

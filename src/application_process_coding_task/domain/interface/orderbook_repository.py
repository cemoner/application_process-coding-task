from collections.abc import Iterator
from typing import Protocol

from application_process_coding_task.domain.entity.orderbook_record import (
    OrderBookRecord,
)
from application_process_coding_task.domain.query.lookup_query import (
    MultipleLookup,
    SingleLookup,
)


class OrderBookRepository(Protocol):
    def find_single(self, query: SingleLookup) -> Iterator[OrderBookRecord]:
        pass

    def find_multiple(self, query: MultipleLookup) -> Iterator[OrderBookRecord]:
        pass

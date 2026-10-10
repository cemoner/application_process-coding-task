from collections.abc import Iterator
from datetime import date
from typing import Protocol

from application_process_coding_task.application.dto.query.orderbook_query import (
    MultipleOrderBookQuery,
    SingleOrderBookQuery,
)
from application_process_coding_task.domain.entity.orderbook_record import (
    OrderBookRecord,
)


class OrderBookRepository(Protocol):
    def find_single_quotes(
        self, trade_date: date, query: SingleOrderBookQuery
    ) -> Iterator[OrderBookRecord]:
        pass

    def find_multiple_quotes(
        self, trade_date: date, query: MultipleOrderBookQuery
    ) -> Iterator[OrderBookRecord]:
        pass

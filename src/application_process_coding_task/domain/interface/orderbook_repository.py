from datetime import date
from typing import Protocol, Iterator

from application_process_coding_task.application.dto.query.orderbook_query import SingleOrderBookQuery, \
    MultipleOrderBookQuery
from application_process_coding_task.domain.entity.orderbook_record import (
    OrderBookRecord,
)


class OrderBookRepository(Protocol):
    def find_quotes_by_date(
        self,
        trade_date: date,
        query: SingleOrderBookQuery | MultipleOrderBookQuery

    ) -> Iterator[OrderBookRecord]:
        """Return quote events for a date, optionally filtered by RIC."""
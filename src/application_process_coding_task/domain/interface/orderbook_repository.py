from datetime import date
from typing import Protocol, Iterator

from application_process_coding_task.application.dto.query.orderbook_query import SingleOrderBookQuery, \
    MultipleOrderBookQuery
from application_process_coding_task.domain.entity.orderbook_record import (
    OrderBookRecord,
)


from datetime import date
from typing import Protocol, Iterator
from application_process_coding_task.domain.entity.orderbook_record import OrderBookRecord
from application_process_coding_task.application.dto.query.orderbook_query import (
    SingleOrderBookQuery,
    MultipleOrderBookQuery
)

class OrderBookRepository(Protocol):
    def find_single_quotes(
        self,
        trade_date: date,
        query: SingleOrderBookQuery
    ) -> Iterator[OrderBookRecord]:
        pass

    def find_multiple_quotes(
        self,
        trade_date: date,
        query: MultipleOrderBookQuery
    ) -> Iterator[OrderBookRecord]:
        pass
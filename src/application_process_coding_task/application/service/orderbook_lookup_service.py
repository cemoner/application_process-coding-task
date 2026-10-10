from collections.abc import Iterator

from application_process_coding_task.application.dto.query.orderbook_query import (
    MultipleOrderBookQuery,
    SingleOrderBookQuery,
)
from application_process_coding_task.application.dto.result.orderbook_result import OrderBookResult
from application_process_coding_task.application.mapper.orderbook_mapper import to_orderbook_result
from application_process_coding_task.domain.interface.orderbook_repository import (
    OrderBookRepository,
)
from application_process_coding_task.domain.query.lookup_query import (
    MultipleLookup,
    SingleLookup,
)


class OrderBookLookupService:
    def __init__(self, repository: OrderBookRepository) -> None:
        self.repository = repository

    def find_single(self, query: SingleOrderBookQuery) -> Iterator[OrderBookResult]:
        repository_query = SingleLookup(trade_date=query.trade_date, ric=query.ric)
        for record in self.repository.find_single(repository_query):
            yield to_orderbook_result(record)

    def find_multiple(self, query: MultipleOrderBookQuery) -> Iterator[OrderBookResult]:
        repository_query = MultipleLookup(
            trade_date=query.trade_date,
            rics=tuple(query.rics),
        )
        for record in self.repository.find_multiple(repository_query):
            yield to_orderbook_result(record)

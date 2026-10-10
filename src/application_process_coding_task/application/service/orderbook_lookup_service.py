from collections.abc import Iterator

from application_process_coding_task.application.dto.query.orderbook_query import (
    MultipleOrderBookQuery,
    SingleOrderBookQuery,
)
from application_process_coding_task.application.dto.result.orderbook_result import OrderBookResult
from application_process_coding_task.application.mapper.orderbook_mapper import (
    to_orderbook_result,
)
from application_process_coding_task.domain.interface.orderbook_repository import (
    OrderBookRepository,
)


class OrderBookLookupService:
    def __init__(self, repository: OrderBookRepository) -> None:
        self.repository = repository

    def find(
        self, query: SingleOrderBookQuery | MultipleOrderBookQuery
    ) -> Iterator[OrderBookResult]:
        for record in self.repository.find_quotes_by_date(query.trade_date, query):
            yield to_orderbook_result(record)

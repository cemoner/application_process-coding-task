from application_process_coding_task.application.dto.orderbook_query import OrderBookQuery
from application_process_coding_task.application.dto.orderbook_result import OrderBookResult
from application_process_coding_task.domain.interface.orderbook_repository import (
    OrderBookRepository,
)


class OrderBookLookupService:
    def __init__(self, repository: OrderBookRepository) -> None:
        self.repository = repository

    def find(self, query: OrderBookQuery) -> list[OrderBookResult]:
        records = self.repository.find_quotes_by_date(query.trade_date, query.ric, query.rics)
        return [
            OrderBookResult(
                ric=record.ric,
                alias_underlying_ric=record.alias_underlying_ric,
                domain=record.domain,
                date_time=record.date_time,
                gmt_offset=record.gmt_offset,
                event_type=record.event_type,
                bid_price=record.bid_price,
                bid_size=record.bid_size,
                ask_price=record.ask_price,
                ask_size=record.ask_size,
            )
            for record in records
        ]

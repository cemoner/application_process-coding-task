from application_process_coding_task.application.dto.result.orderbook_result import (
    OrderBookResult,
)
from application_process_coding_task.domain.entity.orderbook_record import OrderBookRecord


def to_orderbook_result(record: OrderBookRecord) -> OrderBookResult:
    return OrderBookResult(
        ric=record.ric,
        alias_underlying_ric=record.alias_underlying_ric,
        domain=record.domain,
        date_time=record.date_time,
        date_time_text=record.date_time_text,
        gmt_offset=record.gmt_offset,
        event_type=record.event_type,
        bid_price=record.bid_price,
        bid_size=record.bid_size,
        ask_price=record.ask_price,
        ask_size=record.ask_size,
    )

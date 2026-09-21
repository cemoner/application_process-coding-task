from collections.abc import Sequence
from datetime import datetime
from decimal import Decimal

from application_process_coding_task.domain.entity.orderbook_record import (
    OrderBookRecord,
)


def _decimal_or_none(value: object) -> Decimal | None:
    if value is None or value == "":
        return None
    if isinstance(value, (Decimal, int, float, str)):
        return Decimal(str(value))
    raise TypeError("Order-book numeric fields must be numeric or null")


def to_orderbook_record(row: Sequence[object]) -> OrderBookRecord:
    if len(row) != 10:
        raise ValueError("Order-book row must contain 10 target columns")

    (
        ric,
        alias_underlying_ric,
        domain,
        date_time,
        gmt_offset,
        event_type,
        bid_price,
        bid_size,
        ask_price,
        ask_size,
    ) = row

    if not isinstance(ric, str) or not isinstance(domain, str):
        raise TypeError("Order-book RIC and domain must be strings")
    if alias_underlying_ric is not None and not isinstance(alias_underlying_ric, str):
        raise TypeError("Order-book underlying RIC must be a string or null")
    if not isinstance(date_time, (datetime, str)):
        raise TypeError("Order-book date-time must be a datetime or ISO string")
    if not isinstance(gmt_offset, str) or not isinstance(event_type, str):
        raise TypeError("Order-book GMT offset and event type must be strings")

    parsed_date_time = (
        date_time if isinstance(date_time, datetime) else datetime.fromisoformat(date_time)
    )
    return OrderBookRecord(
        ric=ric,
        alias_underlying_ric=alias_underlying_ric,
        domain=domain,
        date_time=parsed_date_time,
        gmt_offset=gmt_offset,
        event_type=event_type,
        bid_price=_decimal_or_none(bid_price),
        bid_size=_decimal_or_none(bid_size),
        ask_price=_decimal_or_none(ask_price),
        ask_size=_decimal_or_none(ask_size),
    )

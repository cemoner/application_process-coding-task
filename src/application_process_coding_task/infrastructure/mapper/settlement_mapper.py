from collections.abc import Sequence
from datetime import date
from decimal import Decimal

from application_process_coding_task.domain.entity.settlement_record import (
    SettlementRecord,
)


def to_settlement_record(row: Sequence[object]) -> SettlementRecord:
    if len(row) != 3:
        raise ValueError("Settlement row must contain RIC, trade date, and settlement price")

    ric, trade_date, settlement_price = row

    if not isinstance(ric, str):
        raise TypeError("Settlement RIC must be a string")
    if not isinstance(trade_date, (date, str)):
        raise TypeError("Settlement trade date must be a date or ISO date string")
    if not isinstance(settlement_price, (Decimal, str, int, float)):
        raise TypeError("Settlement price must be numeric")

    parsed_trade_date = (
        trade_date if isinstance(trade_date, date) else date.fromisoformat(trade_date[:10])
    )

    return SettlementRecord(
        ric=ric,
        trade_date=parsed_trade_date,
        settlement_price=Decimal(str(settlement_price)),
    )

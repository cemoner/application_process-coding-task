from collections.abc import Sequence
from datetime import date
from decimal import Decimal

from application_process_coding_task.domain.entity.eod_record import (
    EodRecord,
)


def to_eod_record(row: Sequence[object]) -> EodRecord:
    if len(row) != 4:
        raise ValueError(
            "EOD row must contain asset subtype, RIC, trade date, and settlement price"
        )

    asset_subtype, ric, trade_date, settlement_price = row

    if not isinstance(asset_subtype, str):
        raise TypeError("Settlement asset subtype must be a string")
    if not isinstance(ric, str):
        raise TypeError("Settlement RIC must be a string")
    if not isinstance(trade_date, (date, str)):
        raise TypeError("Settlement trade date must be a date or ISO date string")
    if not isinstance(settlement_price, (Decimal, str, int, float)):
        raise TypeError("Settlement price must be numeric")

    parsed_trade_date = (
        trade_date if isinstance(trade_date, date) else date.fromisoformat(trade_date[:10])
    )

    return EodRecord(
        asset_subtype=asset_subtype,
        ric=ric,
        trade_date=parsed_trade_date,
        ask=None,
        bid=None,
        settlement_price=Decimal(str(settlement_price)),
    )

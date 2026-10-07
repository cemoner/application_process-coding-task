import re
from collections.abc import Sequence
from datetime import date
from decimal import Decimal

from application_process_coding_task.domain.entity.eod_record import (
    EodRecord,
)

_FUTURES_RIC_PATTERN = re.compile(r"^SET[A-Z]\d{2}$")


def infer_asset_subtype(ric: str) -> str:
    if _FUTURES_RIC_PATTERN.fullmatch(ric):
        return "FUT"
    raise ValueError(f"Cannot infer asset subtype from RIC: {ric}")


def to_eod_record(row: Sequence[object]) -> EodRecord:
    if len(row) != 5:
        raise ValueError("EOD row must contain RIC, trade date, bid, ask, and settlement price")

    ric, trade_date, bid, ask, settlement_price = row

    if not isinstance(ric, str):
        raise TypeError("Settlement RIC must be a string")
    if not isinstance(trade_date, (date, str)):
        raise TypeError("Settlement trade date must be a date or ISO date string")
    if not isinstance(settlement_price, (Decimal, str, int, float)):
        raise TypeError("Settlement price must be numeric")
    if bid is not None and not isinstance(bid, (Decimal, str, int, float)):
        raise TypeError("EOD bid must be numeric or null")
    if ask is not None and not isinstance(ask, (Decimal, str, int, float)):
        raise TypeError("EOD ask must be numeric or null")

    parsed_trade_date = (
        trade_date if isinstance(trade_date, date) else date.fromisoformat(trade_date[:10])
    )

    return EodRecord(
        asset_subtype=infer_asset_subtype(ric),
        ric=ric,
        trade_date=parsed_trade_date,
        ask=Decimal(str(ask)) if ask is not None else None,
        bid=Decimal(str(bid)) if bid is not None else None,
        settlement_price=Decimal(str(settlement_price)),
    )

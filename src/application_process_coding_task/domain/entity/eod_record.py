from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class EodRecord:
    asset_subtype: str
    ric: str
    trade_date: date
    ask: Decimal | None
    bid: Decimal | None
    settlement_price: Decimal

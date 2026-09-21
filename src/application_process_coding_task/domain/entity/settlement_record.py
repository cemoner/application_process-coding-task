from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class SettlementRecord:
    ric: str
    trade_date: date
    settlement_price: Decimal

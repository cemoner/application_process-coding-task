from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class EodResult(BaseModel):
    asset_subtype: str
    ric: str
    trade_date: date
    ask: Decimal | None = None
    bid: Decimal | None = None
    settlement_price: Decimal

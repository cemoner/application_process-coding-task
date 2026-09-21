from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class OrderBookResult(BaseModel):
    ric: str
    alias_underlying_ric: str | None
    domain: str
    date_time: datetime
    gmt_offset: str
    event_type: str
    bid_price: Decimal | None
    bid_size: Decimal | None
    ask_price: Decimal | None
    ask_size: Decimal | None

from datetime import date
from typing import Literal

from pydantic import BaseModel


class SettlementQuery(BaseModel):
    ric: str
    trade_date: date
    output_type: Literal["csv", "json"] = "json"

from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


class SettlementRequest(BaseModel):
    ric: str | None = Field(default=None, min_length=1)
    trade_date: date = Field(alias="date")
    output_type: Literal["csv", "json"] = Field(default="json", alias="type")

    model_config = {"populate_by_name": True}

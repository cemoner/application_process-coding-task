from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class OrderBookResponse(BaseModel):
    ric: str = Field(alias="#RIC")
    alias_underlying_ric: str | None = Field(alias="Alias Underlying RIC")
    domain: str = Field(alias="Domain")
    date_time: datetime = Field(alias="Date-Time")
    gmt_offset: str = Field(alias="GMT Offset")
    event_type: str = Field(alias="Type")
    bid_price: Decimal | None = Field(alias="Bid Price")
    bid_size: Decimal | None = Field(alias="Bid Size")
    ask_price: Decimal | None = Field(alias="Ask Price")
    ask_size: Decimal | None = Field(alias="Ask Size")

    model_config = {"populate_by_name": True}

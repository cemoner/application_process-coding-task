from datetime import date

from pydantic import BaseModel, Field


class EodResponse(BaseModel):
    asset_subtype: str = Field(alias="Asset SubType")
    ric: str = Field(alias="RIC")
    trade_date: date = Field(alias="Trade Date")
    ask: str | None = Field(default=None, alias="Ask")
    bid: str | None = Field(default=None, alias="Bid")
    settlement_price: str = Field(alias="Settlement Price")

    model_config = {"populate_by_name": True}

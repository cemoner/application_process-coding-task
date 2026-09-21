from datetime import date

from pydantic import BaseModel

from .output_format import OutputFormat


class OrderBookQuery(BaseModel):
    ric: str | None = None
    rics: list[str] | None = None
    trade_date: date
    output_type: OutputFormat = OutputFormat.JSON

from datetime import date

from pydantic import BaseModel

from .output_format import OutputFormat


class SettlementQuery(BaseModel):
    ric: str | None = None
    trade_date: date
    output_type: OutputFormat = OutputFormat.JSON

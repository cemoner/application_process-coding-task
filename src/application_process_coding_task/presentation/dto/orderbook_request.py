from datetime import date

from pydantic import BaseModel, Field

from application_process_coding_task.application.dto.output_format import OutputFormat


class OrderBookRequest(BaseModel):
    ric: str | None = Field(default=None, min_length=1)
    trade_date: date = Field(alias="date")
    output_type: OutputFormat = Field(default=OutputFormat.JSON, alias="type")

    model_config = {"populate_by_name": True}

from datetime import date
from typing import Annotated

from pydantic import BaseModel, Field

from application_process_coding_task.application.dto.helper.output_format import OutputFormat


class MultipleOrderbookRequest(BaseModel):
    rics: list[Annotated[str, Field(min_length=1)]] = Field(min_length=1)
    trade_date: date = Field(alias="date")
    output_type: OutputFormat = Field(default=OutputFormat.CSV, alias="type")
    model_config = {"populate_by_name": True}

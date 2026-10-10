from datetime import date

from pydantic import BaseModel, Field

from application_process_coding_task.application.dto.helper.output_format import OutputFormat


class MultipleEodRequest(BaseModel):
    rics: list[str] = Field(min_length=1)
    trade_date: date = Field(alias="date")
    output_type: OutputFormat = Field(default=OutputFormat.CSV, alias="type")
    model_config = {"populate_by_name": True}

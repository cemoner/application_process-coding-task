from datetime import date

from pydantic import BaseModel

from application_process_coding_task.application.dto.helper.output_format import OutputFormat


class EodQuery(BaseModel):
    ric: str | None = None
    rics: list[str] | None = None
    trade_date: date
    output_type: OutputFormat = OutputFormat.CSV

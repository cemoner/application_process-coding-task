from datetime import date

from pydantic import BaseModel

from application_process_coding_task.application.dto.helper.output_format import OutputFormat

class BaseEodQuery(BaseModel):
    trade_date: date
    output_type: OutputFormat = OutputFormat.CSV

class SingleEodQuery(BaseEodQuery):
    ric: str

class MultipleEodQuery(BaseEodQuery):
    rics: list[str]
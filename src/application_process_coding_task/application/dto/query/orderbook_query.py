from datetime import date

from pydantic import BaseModel

from application_process_coding_task.application.dto.helper.output_format import OutputFormat


class BaseQuery(BaseModel):
    trade_date: date
    output_type: OutputFormat = OutputFormat.CSV


class SingleOrderBookQuery(BaseQuery):
    ric: str


class MultipleOrderBookQuery(BaseQuery):
    rics: list[str]

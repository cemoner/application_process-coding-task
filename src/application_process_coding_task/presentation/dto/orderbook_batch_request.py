from pydantic import BaseModel, Field


class OrderBookBatchRequest(BaseModel):
    rics: list[str] = Field(min_length=1)

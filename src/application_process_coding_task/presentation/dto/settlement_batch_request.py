from pydantic import BaseModel, Field


class SettlementBatchRequest(BaseModel):
    rics: list[str] = Field(min_length=1)

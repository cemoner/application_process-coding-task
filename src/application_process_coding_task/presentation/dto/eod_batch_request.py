from pydantic import BaseModel, Field


class EodBatchRequest(BaseModel):
    rics: list[str] = Field(min_length=1)

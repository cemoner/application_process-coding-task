from pydantic import BaseModel, Field


class MultipleOrderbookRequest(BaseModel):
    rics: list[str] = Field(min_length=1)

from pydantic import BaseModel, Field


class MultipleEodRequest(BaseModel):
    rics: list[str] = Field(min_length=1)

from typing import Annotated

from fastapi import APIRouter, Depends

from ..dto.settlement_request import SettlementRequest
from ..dto.settlement_response import SettlementResponse

router = APIRouter(prefix="/settlements", tags=["settlements"])


@router.get("", response_model=SettlementResponse)
def get_settlement(
    request: Annotated[SettlementRequest, Depends()],
) -> SettlementResponse:
    raise NotImplementedError

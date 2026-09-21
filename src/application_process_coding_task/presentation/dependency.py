from application_process_coding_task.application.service.eod_lookup_service import (
    EodLookupService,
)
from application_process_coding_task.application.service.orderbook_lookup_service import (
    OrderBookLookupService,
)
from application_process_coding_task.config import settings

from ..infrastructure.repository.parquet_eod_repository import ParquetEodRepository
from ..infrastructure.repository.parquet_orderbook_repository import (
    ParquetOrderBookRepository,
)


def get_eod_repository() -> ParquetEodRepository:
    return ParquetEodRepository(settings.source_path)


def get_eod_service() -> EodLookupService:
    return EodLookupService(get_eod_repository())


def get_orderbook_repository() -> ParquetOrderBookRepository:
    return ParquetOrderBookRepository(settings.source_path)


def get_orderbook_service() -> OrderBookLookupService:
    return OrderBookLookupService(get_orderbook_repository())

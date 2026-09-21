from application_process_coding_task.application.service.settlement_lookup_service import (
    SettlementLookupService,
)
from application_process_coding_task.config import settings

from ..infrastructure.repository.parquet_settlement_repository import ParquetSettlementRepository


def get_settlement_repository() -> ParquetSettlementRepository:
    return ParquetSettlementRepository(settings.source_path)


def get_settlement_service() -> SettlementLookupService:
    return SettlementLookupService(get_settlement_repository())

from application_process_coding_task.application.service.settlement_lookup_service import (
    SettlementLookupService,
)

from ..infrastructure.repository.parquet_settlement_repository import ParquetSettlementRepository


def get_settlement_repository() -> ParquetSettlementRepository:
    return ParquetSettlementRepository()


def get_settlement_service() -> SettlementLookupService:
    return SettlementLookupService(get_settlement_repository())

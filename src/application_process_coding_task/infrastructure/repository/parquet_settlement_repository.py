from datetime import date
from pathlib import Path

from application_process_coding_task.domain.entity.settlement_record import SettlementRecord
from application_process_coding_task.infrastructure.database.duckdb_connection import (
    get_duckdb_connection,
)
from application_process_coding_task.infrastructure.mapper.settlement_mapper import (
    to_settlement_record,
)


class ParquetSettlementRepository:
    def __init__(self, source_path: Path) -> None:
        self.source_path = source_path

    def find_by_date(
        self,
        trade_date: date,
        ric: str | None = None,
        rics: list[str] | None = None,
    ) -> list[SettlementRecord]:
        query = """
            SELECT 'FUT', "#RIC", "Date-Time", "Price"
            FROM read_parquet(?)
            WHERE "Type" = 'Settlement Price'
              AND CAST("Date-Time" AS DATE) = ?
        """
        parameters: list[object] = [str(self.source_path), trade_date]
        if ric is not None:
            query += ' AND "#RIC" = ?'
            parameters.append(ric)
        elif rics:
            placeholders = ", ".join("?" for _ in rics)
            query += f' AND "#RIC" IN ({placeholders})'
            parameters.extend(rics)
        query += """
            QUALIFY ROW_NUMBER() OVER (
                PARTITION BY "#RIC"
                ORDER BY "Date-Time" DESC
            ) = 1
            ORDER BY "#RIC"
        """

        with get_duckdb_connection(self.source_path) as connection:
            rows = connection.execute(query, parameters).fetchall()

        return [to_settlement_record(row) for row in rows]

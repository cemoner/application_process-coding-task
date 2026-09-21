from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    name: str = "Coding Task API"
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = False
    source_path: Path = Path("source.parquet")
    target_eod_path: Path = Path("target_eod.csv")
    target_orderbook_path: Path = Path("target_orderbook.csv")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        extra="ignore",
    )


settings = Settings()

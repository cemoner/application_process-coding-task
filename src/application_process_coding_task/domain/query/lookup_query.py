from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class SingleLookup:
    trade_date: date
    ric: str


@dataclass(frozen=True, slots=True)
class MultipleLookup:
    trade_date: date
    rics: tuple[str, ...]

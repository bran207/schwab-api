from typing import Literal

from schwab.models.utils import SchwabDataModel


class Screener(SchwabDataModel):
    description: str
    volume: int
    last_price: float
    net_change: float
    market_share: float
    total_volume: int
    trades: int
    net_percent_change: float
    symbol: str

    # Included in Schwab Documentation but not in the API response
    change: float | None = None
    direction: Literal["up", "down"] | None = None
    last: float | None = None

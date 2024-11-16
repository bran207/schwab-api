from typing import Literal

from schwab.models.utils import SchwabDataModel


class Underlying(SchwabDataModel):
    ask: float
    ask_size: int
    bid: float
    bid_size: int
    change: float
    close: float
    delayed: bool
    description: str
    exchange_name: Literal["IND", "ASE", "NYS", "NAS", "NAP", "PAC", "OPR", "BATS"]
    fifty_two_week_high: float
    fifty_two_week_low: float
    high_price: float
    last: float
    low_price: float
    mark: float
    mark_change: float
    mark_percent_change: float
    open_price: float
    percent_change: float
    quote_time: int
    symbol: str
    total_volume: int
    trade_time: int

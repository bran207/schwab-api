from pydantic import Field

from schwab.models.utils import SchwabDataModel


class SchwabForexQuoteForex(SchwabDataModel):
    fifty_two_week_high: float = Field(alias="52WeekHigh")
    fifty_two_week_low: float = Field(alias="52WeekLow")
    ask_price: float
    ask_size: float
    bid_price: float
    bid_size: int
    close_price: float
    high_price: float
    last_price: float
    last_size: int
    low_price: float
    mark: float
    net_change: float
    net_percent_change: float
    open_price: float
    quote_time: int
    security_status: str
    tick: float
    tick_amount: float
    total_volume: int
    trade_time: int

from pydantic import Field
from schwab.models.utils import SchwabDataModel


class SchwabQuoteEquity(SchwabDataModel):
    fifty_two_week_high: float = Field(alias="52WeekHigh")
    fifty_two_week_low: float = Field(alias="52WeekLow")
    ask_MIC_id: str = Field(alias="askMICId")
    ask_price: float
    ask_size: int
    ask_time: int
    bid_MIC_id: str = Field(alias="bidMICId")
    bid_price: float
    bid_size: int
    bid_time: int
    close_price: float
    high_price: float
    last_MIC_id: str = Field(alias="lastMICId")
    last_price: float
    last_size: int
    low_price: float
    mark: float
    mark_change: float
    mark_percent_change: float
    net_change: float
    net_percent_change: float
    open_price: float
    quote_time: int
    security_status: str
    total_volume: int
    trade_time: int
    volatility: float | None = (
        None  # Included in Schwab documentation but not in the response
    )

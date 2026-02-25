from pydantic import Field
from schwab.models.utils import SchwabDataModel


class SchwabIndexQuote(SchwabDataModel):
    fifty_two_week_high: float = Field(alias="52WeekHigh")
    fifty_two_week_low: float = Field(alias="52WeekLow")
    close_price: float
    high_price: float
    last_price: float
    low_price: float
    net_change: float
    net_percent_change: float
    open_price: float
    security_status: str
    total_volume: int
    trade_time: int

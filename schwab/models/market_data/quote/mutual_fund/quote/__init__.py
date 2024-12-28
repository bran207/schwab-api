from pydantic import Field

from schwab.models.utils import SchwabDataModel


class SchwabQuoteMutualFundOption(SchwabDataModel):
    fifty_two_week_high: float = Field(alias="52WeekHigh")
    fifty_two_week_low: float = Field(alias="52WeekLow")
    close_price: float
    nav: float = Field(alias="nAV")
    net_change: float
    net_percent_change: float
    security_status: str
    total_volume: int | None = (
        None  # Included in Schwab documentation but not in the response
    )
    trade_time: int

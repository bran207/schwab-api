from pydantic import Field

from schwab.models.utils import SchwabDataModel


class SchwabQuoteFuture(SchwabDataModel):
    ask_MIC_id: str = Field(alias="askMICId")
    ask_price: float
    ask_size: int
    ask_time: int
    bid_MIC_id: str = Field(alias="bidMICId")
    bid_price: float
    bid_size: int
    bid_time: int
    close_price: float
    future_percent_change: float
    high_price: float
    last_MIC_id: str = Field(alias="lastMICId")
    last_price: float
    last_size: int
    low_price: float
    mark: float
    net_change: float
    open_interest: int
    open_price: float
    quote_time: int
    quoted_in_session: bool
    security_status: str
    settle_time: int
    tick: float
    tick_amount: float
    total_volume: int
    trade_time: int

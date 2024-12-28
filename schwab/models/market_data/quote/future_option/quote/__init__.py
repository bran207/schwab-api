from pydantic import Field

from schwab.models.utils import SchwabDataModel


class SchwabQuoteFutureOption(SchwabDataModel):
    ask_MIC_id: str = Field(alias="askMICId")
    ask_price: float
    ask_size: int
    ask_time: int
    bid_MIC_id: str = Field(alias="bidMICId")
    bid_price: float
    bid_size: int
    close_price: float
    high_price: float
    last_MIC_id: str = Field(alias="lastMICId")
    last_price: float
    last_size: int
    low_price: float
    mark: float
    mark_change: float
    net_change: float
    open_interest: int
    open_price: float
    quote_time: int
    security_status: str
    settlement_price: int
    tick: float
    tick_amount: float
    total_volume: int
    trade_time: int

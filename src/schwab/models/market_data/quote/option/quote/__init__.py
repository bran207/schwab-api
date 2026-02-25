from pydantic import Field

from schwab.models.utils import SchwabDataModel


class SchwabOptionQuoteOption(SchwabDataModel):
    fifty_two_week_high: float = Field(alias="52WeekHigh")
    fifty_two_week_low: float = Field(alias="52WeekLow")
    ask_price: float
    ask_size: float
    bid_price: float
    bid_size: int
    close_price: float
    delta: float
    gamma: float
    high_price: float
    ind_ask_price: float
    ind_bid_price: float
    ind_quote_time: int
    implied_yield: float
    last_price: float
    last_size: int
    low_price: float
    mark: float
    mark_change: float
    mark_percent_change: float
    money_intrinsic_value: float
    net_change: float
    net_percent_change: float
    open_interest: float
    open_price: float
    quote_time: int
    rho: float
    security_status: str
    theoretical_option_value: float
    theta: float
    time_value: float
    total_volume: int
    trade_time: int
    underlying_price: float
    vega: float
    volatility: float

from typing import Literal

from schwab.models.utils import SchwabDataModel
from schwab.models.market_data.utils import SETTLEMENT_TYPE


class OptionContract(SchwabDataModel):
    put_call: Literal["PUT", "CALL"]
    symbol: str
    description: str
    exchange_name: str
    bid_price: float
    ask_price: float
    last_price: float
    mark_price: float
    bid_size: int
    ask_size: int
    last_size: int
    high_price: float
    low_price: float
    open_price: float
    close_price: float
    total_volume: int
    trade_date: int
    quote_time_in_long: int
    trade_time_in_long: int
    net_change: float
    volatility: float
    delta: float
    gamma: float
    theta: float
    vega: float
    rho: float
    time_value: float
    open_interest: float
    is_in_the_money: bool
    theoretical_option_value: float
    theoretical_volatility: float
    is_mini: bool
    is_non_standard: bool
    option_deliverables_list: ...
    strike_price: float
    expiration_date: str
    days_to_expiration: int
    expiration_type: ...
    last_trading_day: float
    multiplier: float
    settlement_type: SETTLEMENT_TYPE
    deliverable_note: str
    is_index_option: bool
    percent_change: float
    mark_change: float
    mark_percent_change: float
    is_penny_pilot: bool
    instrinsic_value: float
    option_root: str

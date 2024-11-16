from typing import Literal

from schwab.models.utils import SchwabDataModel
from schwab.models.market_data.option_chain.underlying import Underlying


class OptionChain(SchwabDataModel):
    symbol: str
    status: str
    underlying: Underlying | None = None
    strategy: Literal[
        "SINGLE",
        "ANALYTICAL",
        "COVERED",
        "VERTICAL",
        "CALENDAR",
        "STRANGLE",
        "STRADDLE",
        "BUTTERFLY",
        "CONDOR",
        "DIAGONAL",
        "COLLAR",
        "ROLL",
    ]
    interval: float
    is_delayed: bool
    is_index: bool
    days_to_expiration: float
    interest_rate: float
    underlying_price: float
    volatility: float
    call_exp_date_map: dict
    put_exp_date_map: dict

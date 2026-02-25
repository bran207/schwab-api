from typing import Literal
from schwab.models.trading.currency import SchwabCurrency


class SchwabAccountPositionCashEquivalentPositionModel(SchwabCurrency):
    type: Literal["SWEEP_VEHICLE", "SAVINGS", "MONEY_MARKET_FUND", "UNKNOWN"]

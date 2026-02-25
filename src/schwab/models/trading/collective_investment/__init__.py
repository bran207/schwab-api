from typing import Literal
from schwab.models.trading.currency import SchwabCurrency


class SchwabCollectiveInstrument(SchwabCurrency):
    type: Literal[
        "UNIT_INVESTMENT_TRUST",
        "EXCHANGE_TRADED_FUND",
        "CLOSED_END_FUND",
        "INDEX",
        "UNITS",
    ]

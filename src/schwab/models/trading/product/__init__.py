from typing import Literal

from schwab.models.trading.currency import SchwabCurrency


class SchwabProduct(SchwabCurrency):
    type: Literal["TBD", "UNKNOWN"]

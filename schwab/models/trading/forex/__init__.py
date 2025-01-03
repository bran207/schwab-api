from typing import Literal

from schwab.models.trading.accounts.account.security.position.instrument.currency import (
    SchwabAccountPositionCurrencyModel,
)
from schwab.models.trading.currency import SchwabCurrency


class SchwabForex(SchwabCurrency):
    type: Literal["STANDARD", "NBBO", "UNKNOWN"]
    base_currency: SchwabAccountPositionCurrencyModel
    counter_currency: SchwabAccountPositionCurrencyModel

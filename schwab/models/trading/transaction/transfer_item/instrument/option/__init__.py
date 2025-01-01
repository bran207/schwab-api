from datetime import datetime
from typing import Literal, Any

from schwab.models.trading.currency import SchwabCurrency
from schwab.models.trading.transaction.transfer_item.instrument.option.deliverable import (
    SchwabTransactionOptionDeliverable,
)


class SchwabTransactionOption(SchwabCurrency):
    expiration_date: datetime
    option_deliverables: list[SchwabTransactionOptionDeliverable]
    option_premium_multiplier: int
    put_call: Literal["PUT", "CALL", "UNKNOWN"]
    strike_price: float
    type: Literal["VANILLA", "BINARY", "BARRIER", "UNKNOWN"]
    underlying_symbol: str
    underlying_cusip: str
    deliverable: Any

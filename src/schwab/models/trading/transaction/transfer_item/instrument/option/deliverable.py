from typing import Any

from schwab.models.trading.constants import ASSET_TYPES
from schwab.models.trading.currency import SchwabCurrency


class SchwabTransactionOptionDeliverable(SchwabCurrency):
    root_symbol: str
    strike_percent: int
    deliverable_number: int
    deliverable_units: float
    deliverable: Any
    asset_type: ASSET_TYPES

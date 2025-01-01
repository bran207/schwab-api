from typing import Literal

from schwab.models.utils import SchwabDataModel
from schwab.models.trading.constants import (
    ASSET_TYPES,
)


class OptionDeliverable(SchwabDataModel):
    symbol: str
    deliverable_units: float
    currency_type: Literal["USD", "CAD", "EUR", "JPY"]
    asset_type: ASSET_TYPES

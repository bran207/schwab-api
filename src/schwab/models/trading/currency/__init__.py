from schwab.models.utils import SchwabDataModel
from schwab.models.trading.constants import (
    ASSET_TYPES,
)


class SchwabCurrency(SchwabDataModel):
    asset_type: ASSET_TYPES
    cusip: str
    symbol: str
    description: str
    instrument_id: int
    net_change: float

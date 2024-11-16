from typing import TypeVar

from schwab.models.utils import SchwabDataModel
from schwab.models.trading.accounts.account.security.position.instrument.constants import (
    ASSET_TYPES,
)


class SchwabAccountPositionInstrumentModel(SchwabDataModel):
    asset_type: ASSET_TYPES
    cusip: str
    symbol: str
    description: str
    # instrument_id: int
    type: str
    # net_change: float


SchwabInstruments = TypeVar(
    "SchwabInstruments", bound=SchwabAccountPositionInstrumentModel
)

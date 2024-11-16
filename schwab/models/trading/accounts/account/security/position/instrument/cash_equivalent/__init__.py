from typing import Literal
from schwab.models.trading.accounts.account.security.position.instrument.utils import (
    SchwabAccountPositionInstrumentModel,
)


class SchwabAccountPositionCashEquivalentPositionModel(
    SchwabAccountPositionInstrumentModel
):
    type: Literal["SWEEP_VEHICLE", "SAVINGS", "MONEY_MARKET_FUND", "UNKNOWN"]

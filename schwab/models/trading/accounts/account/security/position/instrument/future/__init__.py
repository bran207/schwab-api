from datetime import date
from typing import Literal

from schwab.models.trading.accounts.account.security.position.instrument.utils import (
    SchwabAccountPositionInstrumentModel,
)


class SchwabAccountPositionFuturePositionModel(SchwabAccountPositionInstrumentModel):
    active_contract: bool
    type: Literal["STANDARD", "UNKNOWN"]
    expiration_date: date
    last_trading_date: date
    first_notice_date: date
    multiplier: float

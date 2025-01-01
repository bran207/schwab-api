from datetime import datetime
from typing import Literal

from schwab.models.utils import SchwabDataModel


class SchwabFuture(SchwabDataModel):
    active_contract: bool
    type: Literal["STANDARD", "UNKNOWN"]
    expiration_date: datetime
    last_trading_date: datetime
    first_notice_date: datetime
    multiplier: float

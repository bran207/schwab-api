from typing import Literal
from schwab.models.trading.accounts.account.security.position.instrument.utils import (
    SchwabAccountPositionInstrumentModel,
)
from schwab.models.trading.accounts.account.security.position.instrument.option.deliverable import (
    OptionDeliverable,
)


class SchwabAccountPositionOptionPositionModel(SchwabAccountPositionInstrumentModel):
    option_deliverables: list[OptionDeliverable]
    put_call: Literal["PUT", "CALL", "UNKNOWN"]
    option_multiplier: int
    type: Literal["VANILLA", "BINARY", "BARRIER", "UNKNOWN"]
    underlying_symbol: str

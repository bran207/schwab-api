from typing import Literal
from schwab.models.trading.accounts.account.security.position.instrument.utils import (
    SchwabAccountPositionInstrumentModel,
)


class SchwabAccountPositionCollectiveInvestmentModel(
    SchwabAccountPositionInstrumentModel
):
    type: Literal[
        "UNIT_INVESTMENT_TRUST",
        "EXCHANGE_TRADED_FUND",
        "CLOSED_END_FUND",
        "INDEX",
        "UNITS",
    ]

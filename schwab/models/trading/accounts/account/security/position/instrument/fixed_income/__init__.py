from datetime import date

from schwab.models.trading.accounts.account.security.position.instrument.utils import (
    SchwabAccountPositionInstrumentModel,
)


class SchwabAccountPositionFixedIncomePositionModel(
    SchwabAccountPositionInstrumentModel
):
    maturity_date: date
    factor: float
    variable_rate: float

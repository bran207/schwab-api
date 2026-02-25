from datetime import date

from schwab.models.trading.currency import SchwabCurrency


class SchwabAccountPositionFixedIncomePositionModel(SchwabCurrency):
    maturity_date: date
    factor: float
    variable_rate: float

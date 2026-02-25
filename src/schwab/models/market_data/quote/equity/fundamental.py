from datetime import datetime
from typing import Literal
from schwab.models.utils import SchwabDataModel


class SchwabEquityFundamentalQuote(SchwabDataModel):
    avg_10_days_volume: float
    avg_1_year_volume: float
    declaration_date: datetime | None = (
        None  # Not Included for Securities with no Dividends
    )
    div_amount: float
    div_ex_date: datetime | None = None  # Not Included for Securities with no Dividends
    div_freq: Literal[0, 1, 2, 3, 4, 6, 11, 12]
    div_pay_amount: float
    div_pay_date: datetime | None = (
        None  # Not Included for Securities with no Dividends
    )
    div_yield: float
    eps: float
    fund_leverage_factor: float
    fund_strategy: Literal["A", "L", "P", "Q", "S"] | None = (
        None  # Included in Schwab documentation but not in the response
    )
    next_div_ex_date: datetime | None = (
        None  # Not Included for Securities with no Dividends
    )
    next_div_pay_date: datetime | None = (
        None  # Not Included for Securities with no Dividends
    )
    pe_ratio: float

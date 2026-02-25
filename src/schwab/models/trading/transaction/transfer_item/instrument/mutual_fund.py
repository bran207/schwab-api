from datetime import datetime
from typing import Literal

from schwab.models.trading.currency import SchwabCurrency


class SchwabTransactionMutualFund(SchwabCurrency):
    fund_family_name: str
    fund_family_symbol: str
    fund_group: str
    type: Literal[
        "NOT_APPLICABLE",
        "OPEN_END_NON_TAXABLE",
        "OPEN_END_TAXABLE",
        "NO_LOAD_NON_TAXABLE",
        "NO_LOAD_TAXABLE",
    ]
    exchange_cutoff_time: datetime
    purchase_cutoff_time: datetime
    redemption_cutoff_time: datetime

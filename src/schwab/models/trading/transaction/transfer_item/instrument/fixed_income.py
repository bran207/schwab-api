from datetime import datetime
from typing import Literal

from schwab.models.trading.currency import SchwabCurrency


class SchwabTransactionInstrumentFixedIncome(SchwabCurrency):
    type: Literal[
        "BOND_UNIT",
        "CERTIFICATE_OF_DEPOSIT",
        "CONVERTIBLE_BOND",
        "COLLATERALIZED_MORTGAGE_OBLIGATION",
        "CORPORATE_BOND",
        "GOVERNMENT_MORTGAGE",
        "GNMA_BONDS",
        "MUNICIPAL_ASSESSMENT_DISTRICT",
        "MUNICIPAL_BOND",
        "OTHER_GOVERNMENT",
        "SHORT_TERM_PAPER",
        "US_TREASURY_BOND",
        "US_TREASURY_BILL",
        "US_TREASURY_NOTE",
        "US_TREASURY_ZERO_COUPON",
        "AGENCY_BOND",
        "WHEN_AS_AND_IF_ISSUED_BOND",
        "ASSET_BACKED_SECURITY",
        "UNKNOWN",
    ]
    maturity_date: datetime
    factor: float
    multiplier: float
    variable_rate: float

from typing import Literal

from schwab.models.trading.currency import SchwabCurrency


class SchwabTransactionInstrumentEquity(SchwabCurrency):
    type: Literal[
        "COMMON_STOCK",
        "PREFERRED_STOCK",
        "DEPOSITORY_RECEIPT",
        "PREFERRED_DEPOSITORY_RECEIPT",
        "RESTRICTED_STOCK",
        "COMPONENT_UNIT",
        "RIGHT",
        "WARRANT",
        "CONVERTIBLE_PREFERRED_STOCK",
        "CONVERTIBLE_STOCK",
        "LIMITED_PARTNERSHIP",
        "WHEN_ISSUED",
        "UNKNOWN",
    ]

from typing import Literal

from schwab.models.utils import SchwabDataModel


class SchwabTransferItem(SchwabDataModel):
    instrument: ...
    amount: float
    cost: float
    price: float
    fee_type: Literal[
        "COMMISSION",
        "SEC_FEE",
        "STR_FEE",
        "R_FEE",
        "CDSC_FEE",
        "OPT_REG_FEE",
        "ADDITIONAL_FEE",
        "MISCELLANEOUS_FEE",
        "FUTURES_EXCHANGE_FEE",
        "LOW_PROCEEDS_COMMISSION",
        "BASE_CHARGE",
        "GENERAL_CHARGE",
        "GST_FEE",
        "TAF_FEE",
        "INDEX_OPTION_FEE",
        "UNKNOWN",
    ]
    position_effect: Literal["OPENING", "CLOSING", "AUTOMATIC", "UNKNOWN"]

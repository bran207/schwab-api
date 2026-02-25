from schwab.models.utils import SchwabDataModel


class SchwabEquityQuoteReference(SchwabDataModel):
    cusip: str
    description: str
    exchange: str
    exchange_name: str
    fsi_desc: str | None = (
        None  # Included in Schwab documentation but not in the response
    )
    htb_quantity: int | None = (
        None  # Included in Schwab documentation but not in the response
    )
    htb_rate: float
    is_hard_to_borrow: bool
    is_shortable: bool
    otc_market_tier: str | None = (
        None  # Included in Schwab documentation but not in the response
    )

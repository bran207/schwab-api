from schwab.models.utils import SchwabDataModel
from schwab.models.market_data.utils import EXPIRATION_TYPE, SETTLEMENT_TYPE


class Expiration(SchwabDataModel):
    days_to_expiration: int
    expiration: str | None = None
    expiration_type: EXPIRATION_TYPE
    standard: bool
    settlement_type: SETTLEMENT_TYPE

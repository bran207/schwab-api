from schwab.models.utils import SchwabDataModel
from schwab.models.market_data.utils import (
    CONTRACT_TYPE,
    EXERCISE_TYPE,
    EXPIRATION_TYPE,
)


class SchwabOptionReference(SchwabDataModel):
    contract_type: CONTRACT_TYPE
    cusip: str
    days_to_expiration: int
    deliverables: str
    description: str
    exchange: str
    exchange_name: str
    exercise_type: EXERCISE_TYPE
    expiration_day: int
    expiration_month: int
    expiration_type: EXPIRATION_TYPE
    expiration_year: int
    is_penny_pilot: bool
    last_trading_day: int
    multiplier: int
    settlement_type: str
    strike_price: float
    underlying: str

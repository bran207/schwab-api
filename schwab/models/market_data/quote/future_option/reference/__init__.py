from typing import Literal
from schwab.models.utils import SchwabDataModel


class SchwabFutureOptionReference(SchwabDataModel):
    contract_type: Literal["P", "C"]
    description: str
    exchange: str
    exchange_name: str
    multiplier: float
    expiration_date: int
    expiration_style: str
    strike_price: float
    underlying: str

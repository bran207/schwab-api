from typing import Literal
from schwab.models.utils import SchwabDataModel


class SchwabMutualFundReference(SchwabDataModel):
    cusip: str
    description: str
    exchange: str
    exchange_name: str

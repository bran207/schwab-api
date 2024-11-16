from datetime import datetime
from typing import Literal
from pydantic import Field
from schwab.models.utils import SchwabDataModel

# from schwab.models.trading.preview_order.order_strategy import OrderStrategy
from schwab.models.trading.order import ComplexOrderStrategyTypes


class OrderStrategy(SchwabDataModel):
    account_number: str
    advanced_order_type: Literal[
        "NONE", "OTO", "OCO", "OTOCO", "OT2OCO", "OT3OCO", "BLAST_ALL", "OTA", "PAIR"
    ]
    close_time: datetime
    entered_time: datetime

from datetime import datetime
from typing import Literal
from pydantic import Field
from schwab.models.utils import SchwabDataModel
from schwab.models.trading.order import (
    OrderSessionTypes,
    OrderStrategyType,
    APIOrderStatus,
)
from schwab.models.trading.preview_order.order_balance import OrderBalance


class PreviewOrder(SchwabDataModel):
    order_id: int
    advanced_order_type: Literal[
        "NONE", "OTO", "OCO", "OTOCO", "OT2OCO", "OT3OCO", "BLAST_ALL", "OTA", "PAIR"
    ]
    close_time: datetime
    entered_time: datetime
    order_balance: OrderBalance
    order_strategy_type: OrderStrategyType
    order_version: float
    session: OrderSessionTypes
    status: APIOrderStatus

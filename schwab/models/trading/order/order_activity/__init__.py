from typing import Literal
from schwab.models.utils import SchwabDataModel
from schwab.models.trading.order.execution_leg import ExecutionLeg


class OrderActivity(SchwabDataModel):
    activity_type: Literal["EXECUTION", "ORDER_ACTION"]
    execution_type: Literal["FILL"]
    quantity: float
    order_reamining_quantity: float
    execution_legs: list[ExecutionLeg]

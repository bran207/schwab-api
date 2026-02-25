from datetime import datetime
from typing import Literal

from schwab.models.trading.transaction.transfer_item import SchwabTransferItem
from schwab.models.trading.transaction.user_details import SchwabTransactionUserDetails
from schwab.models.utils import SchwabDataModel
from schwab.trading.transactions import SchwabTransactionTypes


class SchwabTransaction(SchwabDataModel):
    activity_id: int
    time: datetime
    user: SchwabTransactionUserDetails
    description: str
    account_number: str
    type: SchwabTransactionTypes
    status: Literal["VALID", "INVALID", "PENDING", "UNKNOWN"]
    sub_account: Literal["CASH", "MARGIN", "SHORT", "DIV", "INCOME", "UNKNOWN"]
    trade_date: datetime
    settlement_date: datetime
    position_id: int
    order_id: int
    net_amount: float
    activity_type: Literal[
        "ACTIVITY_CORRECTION", "EXECUTION", "ORDER_ACTION", "TRANSFER", "UNKNOWN"
    ]
    transfer_items: list[SchwabTransferItem]

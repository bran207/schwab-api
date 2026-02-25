from datetime import datetime
from typing import Literal
from pydantic import Field
from schwab.models.utils import SchwabDataModel
from schwab.models.trading.order.order_activity import OrderActivity

OrderSessionTypes = Literal["NORMAL", "AM", "PM", "SEAMLESS"]
OrderDuration = Literal[
    "DAY",
    "GOOD_TILL_CANCEL",
    "FILL_OR_KILL",
    "IMMEDIATE_OR_CANCEL",
    "END_OF_WEEK",
    "END_OF_MONTH",
    "NEXT_END_OF_MONTH",
    "UNKNOWN",
]
OrderType = Literal[
    "MARKET",
    "LIMIT",
    "STOP",
    "STOP_LIMIT",
    "TRAILING_STOP",
    "CABINET",
    "NON_MARKETABLE",
    "MARKET_ON_CLOSE",
    "EXERCISE",
    "TRAILING_STOP_LIMIT",
    "NET_DEBIT",
    "NET_CREDIT",
    "NET_ZERO",
    "LIMIT_ON_CLOSE",
    "UNKNOWN",
]
ComplexOrderStrategyTypes = Literal[
    "NONE",
    "COVERED",
    "VERTICAL",
    "BACK_RATIO",
    "CALENDAR",
    "DIAGONAL",
    "STRADDLE",
    "STANGLE",
    "COLLAR_SYNTHETIC",
    "BUTTERFLY",
    "CONDOR",
    "IRON_CONDOR",
    "VERTICAL_ROLL",
    "COLLAR_WITH_STOCK",
    "DOUBLE_DIAGONAL",
    "UNBALANCED_BUTTERFLY",
    "UNBALANCED_CONDOR",
    "UNBALANCED_IRON_CONDOR",
    "UNBALANCED_VERTICAL_ROLL",
    "MUTUAL_FUND_SWAP",
    "CUSTOM",
]

RequestedDestination = Literal[
    "INET",
    "ECN_ARCA",
    "CBOE",
    "AMEX",
    "PHLX",
    "ISE",
    "BOX",
    "NYSE",
    "NASDAQ",
    "BATS",
    "C2",
    "AUTO",
]

PriceLinkBasis = Literal[
    "MANUAL", "BASE", "TRIGGER", "LAST", "BID", "ASK", "ASK_BID", "MARK", "AVERAGE"
]
PriceLinkType = Literal["VALUE", "PERCENT", "TICK"]

OrderStrategyType = Literal[
    "SINGLE",
    "CANCEL",
    "RECALL",
    "PAIR",
    "FLATTEN",
    "TWO_DAY_SWAP",
    "BLAST_ALL",
    "OCO",
    "TRIGGER",
]
APIOrderStatus = Literal[
    "AWAITING_PARENT_ORDER",
    "AWAITING_CONDITION",
    "AWAITING_STOP_CONDITION",
    "AWAITING_MANUAL_REVIEW",
    "ACCEPTED",
    "AWAITING_UR_OUT",
    "PENDING_ACTIVIATION",
    "QUEUED",
    "WORKING",
    "REJECTED",
    "PENDING_CANCEL",
    "CANCELED",
    "PENDING_REPLACE",
    "REPLACED",
    "FILLED",
    "EXPIRED",
    "NEW",
    "AWAITING_RELEASE_TIME",
    "PENDING_ACKNOWLEDGEMENT",
    "PENDING_RECALL",
    "UNKNOWN",
]


class SchwabOrder(SchwabDataModel):
    session: OrderSessionTypes
    duration: OrderDuration
    type: OrderType = Field(alias="orderType")
    cancel_time: datetime
    complex_order_strategy_type: ComplexOrderStrategyTypes
    quantity: float
    filled_quantity: float
    remaining_quantity: float
    requested_destination: RequestedDestination
    destination_link_name: str
    release_time: datetime
    stop_price: float
    stop_price_link_basis: PriceLinkBasis
    stop_price_link_type: PriceLinkType
    stop_price_offset: float
    stop_type: Literal["STANDARD", "BID", "ASK", "LAST", "MARK"]
    price_link_basis: PriceLinkBasis
    price_link_type: PriceLinkType
    price: float
    tax_lot_method: Literal[
        "FIFO",
        "LIFO",
        "HIGH_COST",
        "LOW_COST",
        "AVERAGE_COST",
        "SPECIFIC_LOT",
        "LOSS_HARVESTER",
    ]
    order_leg_collection: dict
    activation_price: float
    special_instruction: Literal[
        "ALL_OR_NONE", "DO_NOT_REDUCE", "ALL_OR_NONE_DO_NOT_REDUCE"
    ]
    order_strategy_type: OrderStrategyType
    id: int = Field(alias="orderId")
    cancelable: bool = False
    editable: bool = False
    status: APIOrderStatus
    entered_time: datetime
    close_time: datetime
    tag: str
    account_number: int
    order_activity_collection: list[OrderActivity]
    replacing_order_collection: list[dict]
    child_order_strategies: list[dict]
    status_description: str

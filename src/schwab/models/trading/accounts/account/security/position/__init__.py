from typing import Generic


from schwab.models.utils import SchwabDataModel
from schwab.models.trading.accounts.account.security.position.instrument import (
    SchwabInstruments,
)


class SchwabAccountPositionModel(SchwabDataModel, Generic[SchwabInstruments]):
    short_quantity: float
    average_price: float
    current_day_profit_loss: float
    current_day_profit_loss_percentage: float
    long_quantity: float
    settled_long_quantity: float
    settled_short_quantity: float
    # aged_quantity: float
    instrument: SchwabInstruments
    market_value: float
    maintenance_requirement: float
    average_long_price: float
    # average_short_price: float
    tax_lot_average_long_price: float
    # tax_lot_average_short_price: float
    long_open_profit_loss: float
    # short_open_profit_loss: float
    previous_session_long_quantity: float
    # previous_session_short_quantity: float
    current_day_cost: float

from schwab.models.utils import SchwabDataModel


class SchwabAccountProjectedBalances(SchwabDataModel):
    available_funds: float
    available_funds_non_marginable_trade: float
    buying_power: float
    day_trading_buying_power: float
    day_trading_buying_power_call: float
    maintenance_call: float
    reg_t_call: float
    is_in_call: bool
    stock_buying_power: float

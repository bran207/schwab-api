from schwab.models.utils import SchwabDataModel


class SchwabAccountCurrentBalances(SchwabDataModel):
    accrued_interest: float
    cash_balance: float
    cash_receipts: float
    long_option_market_value: float
    liquidation_value: float
    long_market_value: float
    money_market_fund: float
    savings: float
    short_market_value: float
    pending_deposits: float
    mutual_fund_value: float
    bond_value: float
    short_option_market_value: float
    available_funds: float
    available_funds_non_marginable_trade: float
    buying_power: float
    buying_power_non_marginable_trade: float
    day_trading_buying_power: float
    equity: float
    equity_percentage: float
    long_margin_value: float
    maintenance_call: float
    maintenance_requirement: float
    margin_balance: float
    reg_t_call: float
    short_balance: float
    short_margin_value: float
    sma: float

from schwab.models.utils import SchwabDataModel


class SchwabAccountInitialBalances(SchwabDataModel):
    accrued_interest: float
    available_funds_non_marginable_trade: float
    bond_value: float
    buying_power: float
    cash_balance: float
    cash_available_for_trading: float
    cash_receipts: float
    day_trading_buying_power: float
    day_trading_buying_power_call: float
    day_trading_equity_call: float
    equity: float
    equity_percentage: float
    liquidation_value: float
    long_margin_value: float
    long_option_market_value: float
    long_stock_value: float
    maintenance_call: float
    maintenance_requirement: float
    margin: float
    margin_equity: float
    money_market_fund: float
    mutual_fund_value: float
    reg_t_call: float
    short_margin_value: float
    short_option_market_value: float
    short_stock_value: float
    total_cash: float
    is_in_call: bool
    pending_deposits: float
    margin_balance: float
    short_balance: float
    account_value: float

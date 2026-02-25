from schwab.models.utils import SchwabDataModel


class SchwabFutureReference(SchwabDataModel):
    description: str
    exchange: str
    exchange_name: str
    future_active_symbol: str
    future_expiration_date: str
    future_is_active: bool
    future_multiplier: float
    future_price_format: str
    future_settlement_price: float
    future_trading_hours: str
    product: str

from schwab.models.utils import SchwabDataModel


class SchwabForexReference(SchwabDataModel):
    description: str
    exchange: str
    exchange_name: str
    is_tradeable: bool
    market_maker: str
    product: str
    trading_hours: str

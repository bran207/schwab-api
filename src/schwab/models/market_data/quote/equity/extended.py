from schwab.models.utils import SchwabDataModel


class SchwabEquityExtendedMarketQuote(SchwabDataModel):
    ask_price: float
    ask_size: int
    bid_price: float
    bid_size: int
    last_price: float
    last_size: int
    mark: float
    quote_time: int
    total_volume: int
    trade_time: int

from schwab.models.utils import SchwabDataModel


class SchwabEquityQuoteRegularMarket(SchwabDataModel):
    regular_market_last_price: float
    regular_market_last_size: int
    regular_market_net_change: float
    regular_market_percent_change: float
    regular_market_trade_time: int

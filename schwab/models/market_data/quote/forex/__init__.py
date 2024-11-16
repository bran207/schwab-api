from schwab.models.utils import SchwabDataModel
from schwab.models.market_data.quote.utils import ASSET_MAIN_TYPE
from schwab.models.market_data.quote.forex.quote import SchwabForexQuoteForex
from schwab.models.market_data.quote.forex.refrence import SchwabForexReference


class SchwabForexQuote(SchwabDataModel):
    asset_main_type: ASSET_MAIN_TYPE
    ssid: int
    symbol: str
    realtime: bool
    quote: SchwabForexQuoteForex
    refrence: SchwabForexReference

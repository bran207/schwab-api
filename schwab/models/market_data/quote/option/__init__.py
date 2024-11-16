from schwab.models.utils import SchwabDataModel
from schwab.models.market_data.quote.utils import ASSET_MAIN_TYPE
from schwab.models.market_data.quote.option.quote import SchwabOptionQuoteOption
from schwab.models.market_data.quote.option.reference import SchwabOptionReference


class SchwabOptionQuote(SchwabDataModel):
    asset_main_type: ASSET_MAIN_TYPE
    ssid: int
    symbol: str
    realtime: bool
    quote: SchwabOptionQuoteOption
    reference: SchwabOptionReference

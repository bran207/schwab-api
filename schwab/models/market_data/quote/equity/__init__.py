from typing import Literal

from schwab.models.utils import SchwabDataModel
from schwab.models.market_data.quote.utils import ASSET_MAIN_TYPE


class SchwabEquityQuote(SchwabDataModel):
    asset_main_type: ASSET_MAIN_TYPE
    asset_sub_type: Literal[
        "COE", "PRF", "ADR", "GDR", "CEF", "ETF", "ETN", "UIT", "WAR", "RGT"
    ]
    ssid: int
    symbol: str
    realtime: bool
    quote_type: Literal["NBBO", "NFL"]

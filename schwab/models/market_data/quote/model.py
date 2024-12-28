from typing import TypeVar, Generic

from schwab.models.utils import SchwabDataModel
from schwab.models.market_data.quote.utils import ASSET_MAIN_TYPE


CORE_QUOTE = TypeVar("CORE_QUOTE")
QUOTE_REFERENCE = TypeVar("QUOTE_REFERENCE")


class CoreSchwabQuote(SchwabDataModel, Generic[CORE_QUOTE, QUOTE_REFERENCE]):
    asset_main_type: ASSET_MAIN_TYPE
    ssid: int
    symbol: str
    realtime: bool
    quote: CORE_QUOTE
    reference: QUOTE_REFERENCE

from typing import Literal

from schwab.models.market_data.quote.equity.extended import (
    SchwabEquityExtendedMarketQuote,
)
from schwab.models.market_data.quote.equity.fundamental import (
    SchwabEquityFundamentalQuote,
)
from schwab.models.market_data.quote.equity.quote import SchwabQuoteEquity
from schwab.models.market_data.quote.equity.reference import SchwabEquityQuoteReference
from schwab.models.market_data.quote.equity.regular_market import (
    SchwabEquityQuoteRegularMarket,
)
from schwab.models.market_data.quote.model import CoreSchwabQuote


class SchwabEquityQuote(CoreSchwabQuote[SchwabQuoteEquity, SchwabEquityQuoteReference]):
    asset_sub_type: Literal[
        "COE", "PRF", "ADR", "GDR", "CEF", "ETF", "ETN", "UIT", "WAR", "RGT"
    ]
    quote_type: Literal["NBBO", "NFL"]
    extended: SchwabEquityExtendedMarketQuote
    fundamental: SchwabEquityFundamentalQuote
    regular: SchwabEquityQuoteRegularMarket

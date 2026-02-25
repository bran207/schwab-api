from schwab.models.market_data.quote.model import CoreSchwabQuote
from schwab.models.market_data.quote.forex.quote import SchwabForexQuoteForex
from schwab.models.market_data.quote.forex.reference import SchwabForexReference


class SchwabForexQuote(CoreSchwabQuote[SchwabForexQuoteForex, SchwabForexReference]):
    pass

from schwab.models.market_data.quote.model import CoreSchwabQuote
from schwab.models.market_data.quote.index.quote import (
    SchwabIndexQuote as CoreSchwabIndexQuote,
)
from schwab.models.market_data.quote.index.reference import SchwabIndexQuoteReference


class SchwabIndexQuote(
    CoreSchwabQuote[CoreSchwabIndexQuote, SchwabIndexQuoteReference]
):
    pass

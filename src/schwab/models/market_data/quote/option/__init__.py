from schwab.models.market_data.quote.model import CoreSchwabQuote
from schwab.models.market_data.quote.option.quote import SchwabOptionQuoteOption
from schwab.models.market_data.quote.option.reference import SchwabOptionReference


class SchwabOptionQuote(
    CoreSchwabQuote[SchwabOptionQuoteOption, SchwabOptionReference]
):
    pass

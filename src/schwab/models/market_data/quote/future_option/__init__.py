from schwab.models.market_data.quote.model import CoreSchwabQuote
from schwab.models.market_data.quote.future_option.quote import SchwabQuoteFutureOption
from schwab.models.market_data.quote.future_option.reference import (
    SchwabFutureOptionReference,
)


class SchwabFutureOptionQuote(
    CoreSchwabQuote[SchwabQuoteFutureOption, SchwabFutureOptionReference]
):
    pass

from schwab.models.market_data.quote.model import CoreSchwabQuote
from schwab.models.market_data.quote.future.quote import SchwabQuoteFuture
from schwab.models.market_data.quote.future.reference import SchwabFutureReference


class SchwabFutureQuote(CoreSchwabQuote[SchwabQuoteFuture, SchwabFutureReference]):
    pass

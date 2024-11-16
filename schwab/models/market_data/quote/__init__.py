from schwab.models.market_data.quote.equity import SchwabEquityQuote
from schwab.models.market_data.quote.option import SchwabOptionQuote
from schwab.models.market_data.quote.forex import SchwabForexQuote
from schwab.models.market_data.quote.error import QuoteError

Quote = SchwabEquityQuote | SchwabOptionQuote | SchwabForexQuote | QuoteError

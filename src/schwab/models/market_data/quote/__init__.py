from typing import Any

from schwab.models.market_data.quote.equity import SchwabEquityQuote
from schwab.models.market_data.quote.error import QuoteError
from schwab.models.market_data.quote.forex import SchwabForexQuote
from schwab.models.market_data.quote.future import SchwabFutureQuote
from schwab.models.market_data.quote.future_option import SchwabFutureOptionQuote
from schwab.models.market_data.quote.index import SchwabIndexQuote
from schwab.models.market_data.quote.mutual_fund import SchwabMutualFundQuote
from schwab.models.market_data.quote.option import SchwabOptionQuote

Quote = (
    SchwabEquityQuote
    | SchwabForexQuote
    | SchwabFutureQuote
    | SchwabFutureOptionQuote
    | SchwabIndexQuote
    | SchwabMutualFundQuote
    | SchwabOptionQuote
    | QuoteError
)


def get_quote_model(raw_quote_response: dict[str, Any]):
    match raw_quote_response.get("assetMainType"):
        case "BOND":
            raise NotImplementedError("Bonds are not mentioned in the documentation")
        case "EQUITY":
            return SchwabEquityQuote(**raw_quote_response)
        case "FOREX":
            return SchwabForexQuote(**raw_quote_response)
        case "FUTURE":
            return SchwabFutureQuote(**raw_quote_response)
        case "FUTURE_OPTION":
            return SchwabFutureOptionQuote(**raw_quote_response)
        case "INDEX":
            return SchwabIndexQuote(**raw_quote_response)
        case "MUTUAL_FUND":
            return SchwabMutualFundQuote(**raw_quote_response)
        case "OPTION":
            return SchwabOptionQuote(**raw_quote_response)
        case _:
            return QuoteError(**raw_quote_response)

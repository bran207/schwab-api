from schwab.models.market_data.quote.model import CoreSchwabQuote
from schwab.models.market_data.quote.mutual_fund.quote import (
    SchwabQuoteMutualFundOption,
)
from schwab.models.market_data.quote.mutual_fund.reference import (
    SchwabMutualFundReference,
)


class SchwabMutualFundQuote(
    CoreSchwabQuote[SchwabQuoteMutualFundOption, SchwabMutualFundReference]
):
    pass

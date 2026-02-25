from schwab.models.utils import SchwabDataModel


class QuoteError(SchwabDataModel):
    invalid_cusips: list[str]
    invalid_ssids: list[int]
    invalid_symbols: list[str]

from schwab.models.utils import SchwabDataModel


class SchwabIndexQuoteReference(SchwabDataModel):
    description: str
    exchange: str
    exchange_name: str

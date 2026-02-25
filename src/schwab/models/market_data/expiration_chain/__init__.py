from schwab.models.utils import SchwabDataModel
from schwab.models.market_data.expiration_chain.expiration import Expiration


class ExpirationChain(SchwabDataModel):
    status: str | None = None
    expiration_list: list[Expiration]

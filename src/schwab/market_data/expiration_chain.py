from schwab.utils import ClientSession
from schwab.models.market_data.expiration_chain import ExpirationChain


class SchwabMarketDataExpirationChainClient(ClientSession):

    @property
    def base_url(self):
        return super().base_url + "/marketdata/v1/expirationchain"

    def get(self, symbol: str):
        return ExpirationChain(
            **self.call_api(method="GET", endpoint="", params={"symbol": symbol}).json()
        )

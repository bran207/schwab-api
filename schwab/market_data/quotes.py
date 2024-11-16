from schwab.utils import ClientSession

# from schwab.models.market_data.quote import Quote
from schwab.market_data.utils import QuoteFields


class SchwabMarketDataQuoteClient(ClientSession):
    @property
    def base_url(self):
        return super().base_url + "/marketdata/v1"

    def get(
        self,
        symbol: str,
        fields: list[QuoteFields],
    ):
        return self.call_api(
            method="GET",
            endpoint=f"/{symbol}/quotes",
            params={"fields": fields},
        ).json()

    def list(
        self,
        symbols: list[str],
        fields: list[QuoteFields],
        indicative: bool,
    ):
        return self.call_api(
            method="GET",
            endpoint="/quotes",
            params={"symbols": symbols, "fields": fields, "indicative": indicative},
        ).json()

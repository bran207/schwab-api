from typing import Literal
from schwab.utils import ClientSession
from schwab.models.market_data.instruments import Instrument


class SchwabMarketDataInstrumentsClient(ClientSession):
    @property
    def base_url(self):
        return super().base_url + "/marketdata/v1/instruments"

    def list(
        self,
        symbol: str,
        projection: Literal[
            "symbol-search",
            "symbol-regex",
            "desc-search",
            "desc-regex",
            "search",
            "fundamental",
        ],
    ):
        return [
            Instrument(**instrument)
            for instrument in self.call_api(
                method="GET",
                endpoint="",
                params={"symbol": symbol, "projection": projection},
            ).json()["instruments"]
        ]

    def get(self, cusip_id: str):
        return [
            Instrument(**instrument)
            for instrument in self.call_api(
                method="GET",
                endpoint=f"/{cusip_id}",
            ).json()["instruments"]
        ]

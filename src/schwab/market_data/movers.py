from typing import Literal
from schwab.utils import ClientSession
from schwab.models.market_data.screener import Screener


class SchwabMarketDataMoversClient(ClientSession):
    @property
    def base_url(self):
        return super().base_url + "/marketdata/v1/movers"

    def get(
        self,
        symbol_id: Literal[
            "$DJI",
            "$COMPX",
            "$SPX",
            "NYSE",
            "NASDAQ",
            "OCTBB",
            "INDEX_ALL",
            "EQUITY_ALL",
            "OPTION_ALL",
            "OPTION_PUT",
            "OPTION_CALL",
        ] = "$DJI",
        sort: (
            Literal["VOLUME", "TRADES", "PERCENT_CHANGE_UP", "PERCENT_CHANGE_DOWN"]
            | None
        ) = None,
        frequency: int | None = None,
    ):

        return [
            Screener(**mover)
            for mover in self.call_api(
                method="GET",
                endpoint=f"/{symbol_id}",
                params={"sort": sort, "frequency": frequency},
            ).json()["screeners"]
        ]

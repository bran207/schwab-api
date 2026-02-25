from datetime import date

from schwab.market_data.utils import MARKET_IDS
from schwab.models.market_data.market.hours import MarketHours
from schwab.utils import ClientSession


class SchwabMarketDataMarketHoursClient(ClientSession):
    @property
    def base_url(self):
        return super().base_url + "/marketdata/v1/markets"

    @staticmethod
    def __convert_to_dict(raw_data: dict):
        return {
            market_key: {
                individual_market_key: MarketHours(**individual_market_hours)
                for individual_market_key, individual_market_hours in raw_market_data.items()
            }
            for market_key, raw_market_data in raw_data.items()
        }

    def list(
        self,
        markets: list[MARKET_IDS],
        date: date | None = None,  # Only Valid if range between today and 1 year ago
    ):
        return self.__convert_to_dict(
            self.call_api(
                method="GET", endpoint="", params={"markets": markets, "date": date}
            ).json()
        )

    def get(self, market_id: MARKET_IDS, date: date | None = None):

        return self.__convert_to_dict(
            self.call_api(
                method="GET", endpoint=f"/{market_id}", params={"date": date}
            ).json()
        )

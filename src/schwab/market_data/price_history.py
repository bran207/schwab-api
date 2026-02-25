from datetime import date
from typing import Literal
from schwab.utils import ClientSession

from schwab.models.market_data.price_history.candle_list import CandleList


class SchwabMarketDataPriceHistoryClient(ClientSession):
    @property
    def base_url(self):
        return super().base_url + "/marketdata/v1/pricehistory"

    def get(
        self,
        symbol: str,
        period_type: Literal["day", "month", "year", "ytd"] | None = None,
        period: int | None = None,
        frequency_type: str | None = None,
        frequency: int | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
        need_extended_hours_data: bool | None = None,
        need_previous_close: bool | None = None,
    ):
        return CandleList(
            **self.call_api(
                method="GET",
                endpoint="",
                params={
                    "symbol": symbol,
                    "periodType": period_type,
                    "period": period,
                    "frequencyType": frequency_type,
                    "frequency": frequency,
                    "startDate": start_date,
                    "endDate": end_date,
                    "needExtendedHoursData": need_extended_hours_data,
                    "needPreviousClose": need_previous_close,
                },
            ).json()
        )

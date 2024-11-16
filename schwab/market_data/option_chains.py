from datetime import date
from typing import Literal
from schwab.utils import ClientSession

from schwab.models.market_data.option_chain import OptionChain


class SchwabMarketDataOptionChainClient(ClientSession):

    @property
    def base_url(self):
        return super().base_url + "/marketdata/v1/chains"

    def get(
        self,
        symbol: str,
        contract_type: Literal["CALL", "PUT", "ALL"] | None = None,
        strike_count: int | None = None,
        include_underlying_quote: bool | None = None,
        strategy: Literal[
            "SINGLE",
            "ANALYTICAL",
            "COVERED",
            "VERTICAL",
            "CALENDAR",
            "STRANGLE",
            "STRADDLE",
            "BUTTERFLY",
            "CONDOR",
            "DIAGONAL",
            "COLLAR",
            "ROLL",
        ] = "SINGLE",
        interval: float | None = None,
        strike: float | None = None,
        range: str | None = None,
        from_date: date | None = None,
        to_date: date | None = None,
        volatility: float | None = None,
        underlying_price: float | None = None,
        interest_rate: float | None = None,
        days_to_expiration: int | None = None,
        exp_month: (
            Literal[
                "JAN",
                "FEB",
                "MAR",
                "APR",
                "MAY",
                "JUN",
                "JUL",
                "AUG",
                "SEP",
                "OCT",
                "NOV",
                "DEC",
                "ALL",
            ]
            | None
        ) = None,
        option_type: str | None = None,
        entitlement: Literal["PN", "NP", "PP"] | None = None,
    ):
        return OptionChain(
            **self.call_api(
                method="GET",
                endpoint="",
                params={
                    "symbol": symbol,
                    "contractType": contract_type,
                    "strikeCount": strike_count,
                    "includeUnderlyingQuote": include_underlying_quote,
                    "strategy": strategy,
                    "interval": interval,
                    "strike": strike,
                    "range": range,
                    "fromDate": from_date.strftime("%Y-m-%d") if from_date else None,
                    "toDate": to_date.strftime("%Y-m-%d") if to_date else None,
                    "volatility": volatility,
                    "underlyingPrice": underlying_price,
                    "interestRate": interest_rate,
                    "daysToExpiration": days_to_expiration,
                    "expMonth": exp_month,
                    "optionType": option_type,
                    "entitlement": entitlement,
                },
            ).json()
        )

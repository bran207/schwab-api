from datetime import datetime
from typing import Literal
from schwab.utils import ClientSession

# from schwab.models.trading.transactions #TO-DO: Create Transaction Model

SchwabTransactionTypes = Literal[
    "TRADE",
    "RECEIVE_AND_DELIVER",
    "DIVIDEND_OR_INTEREST",
    "ACH_RECEIPT",
    "ACH_DISBURSEMENT",
    "CASH_RECEIPT",
    "CASH_DISBURSEMENT",
    "ELECTRONIC_FUND",
    "WIRE_OUT",
    "WIRE_IN",
    "JOURNAL",
    "MEMORANDUM",
    "MARGIN_CALL",
    "MONEY_MARKET",
    "SMA_ADJUSTMENT",
]


class SchwabTransactions(ClientSession):

    @property
    def base_url(self):
        return super().base_url + "/trader/v1/accounts"

    def list(
        self,
        account_number: str,
        start_date: datetime,
        end_date: datetime,
        symbol: str | None = None,
        types: SchwabTransactionTypes | None = None,
    ):
        return self.call_api(
            method="GET",
            endpoint=f"/{account_number}/transactions",
            params={
                "startDate": start_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                "endDate": end_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                "symbol": symbol,
                "types": types,
            },
        ).json()

    def get(self, account_number: str, transaction_id: str):
        return self.call_api(
            method="GET",
            endpoint=f"/{account_number}/transactions/{transaction_id}",
        ).json()

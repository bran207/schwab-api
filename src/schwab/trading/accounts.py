from typing import Literal
from schwab.utils import ClientSession

from schwab.models.trading.accounts.hash import SchwabAccountNumberHash
from schwab.models.trading.accounts.account import SchwabAccount

SchwabAccountFields = Literal["position"]


class SchwabAccounts(ClientSession):
    @property
    def base_url(self):
        return super().base_url + "/trader/v1/accounts"

    def list_account_numbers(self) -> list[SchwabAccountNumberHash]:
        return [
            SchwabAccountNumberHash.model_validate(account_number_hash)
            for account_number_hash in self.call_api(
                method="GET",
                endpoint="/accountNumbers",
            ).json()
        ]

    def list(self, fields: SchwabAccountFields | None = None):
        return [
            SchwabAccount(**account)
            for account in self.call_api(
                method="GET", endpoint="", params={"fields": fields}
            ).json()
        ]

    def get(self, account_number: str, fields: SchwabAccountFields | None = None):
        return SchwabAccount(
            **self.call_api(
                method="GET",
                endpoint=f"/{account_number}",
                params={"fields": fields},
            ).json()
        )

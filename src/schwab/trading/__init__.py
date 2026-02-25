from functools import cached_property
from schwab.utils import ClientSession

from schwab.trading.accounts import SchwabAccounts
from schwab.trading.orders import SchwabOrders
from schwab.trading.transactions import SchwabTransactions
from schwab.trading.user_preferences import SchwabUserPreferencesClient


class SchwabTrading(ClientSession):
    @property
    def base_url(self):
        return super().base_url + "/trader/v1"

    @cached_property
    def accounts(self):
        return SchwabAccounts(client=self.client)

    @cached_property
    def orders(self):
        return SchwabOrders(client=self.client)

    @cached_property
    def transactions(self):
        return SchwabTransactions(client=self.client)

    @cached_property
    def user_preferences(self):
        return SchwabUserPreferencesClient(client=self.client)

from functools import cached_property
from schwab.utils import ClientSession

from schwab.market_data.expiration_chain import SchwabMarketDataExpirationChainClient
from schwab.market_data.instruments import SchwabMarketDataInstrumentsClient
from schwab.market_data.market_hours import SchwabMarketDataMarketHoursClient
from schwab.market_data.movers import SchwabMarketDataMoversClient
from schwab.market_data.option_chains import SchwabMarketDataOptionChainClient
from schwab.market_data.price_history import SchwabMarketDataPriceHistoryClient
from schwab.market_data.quotes import SchwabMarketDataQuoteClient


class SchwabMarketData(ClientSession):
    @property
    def base_url(self):
        return super().base_url + "/marketdata/v1"

    @cached_property
    def expiration_chain(self):
        return SchwabMarketDataExpirationChainClient(client=self.client)

    @cached_property
    def instruments(self):
        return SchwabMarketDataInstrumentsClient(client=self.client)

    @cached_property
    def market_hours(self):
        return SchwabMarketDataMarketHoursClient(client=self.client)

    @cached_property
    def movers(self):
        return SchwabMarketDataMoversClient(client=self.client)

    @cached_property
    def option_chains(self):
        return SchwabMarketDataOptionChainClient(client=self.client)

    @cached_property
    def price_history(self):
        return SchwabMarketDataPriceHistoryClient(client=self.client)

    @cached_property
    def quotes(self):
        return SchwabMarketDataQuoteClient(client=self.client)

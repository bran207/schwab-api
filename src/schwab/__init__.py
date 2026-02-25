from datetime import datetime
from schwab.session import SchwabAPISession
from schwab.trading import SchwabTrading
from schwab.market_data import SchwabMarketData


class Schwab:
    trading: SchwabTrading
    market_data: SchwabMarketData

    def __init__(self, session: SchwabAPISession):
        self.trading = SchwabTrading(client=session)
        self.market_data = SchwabMarketData(client=session)

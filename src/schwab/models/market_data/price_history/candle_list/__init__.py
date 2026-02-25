from schwab.models.utils import SchwabDataModel
from schwab.models.market_data.price_history.candle_list.candle import Candle


class CandleList(SchwabDataModel):
    candles: list[Candle]
    empty: bool
    previous_close: float | None = None
    previous_close_date: int | None = None
    symbol: str

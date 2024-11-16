from schwab.models.utils import SchwabDataModel
from schwab.models.market_data.instruments.const import AssetTypes
from schwab.models.market_data.market.hours.interval import Interval


class MarketHours(SchwabDataModel):
    date: str
    market_type: AssetTypes
    exchange: str | None = None
    category: str | None = None
    product: str
    product_name: str | None = None
    is_open: bool
    sessionHours: dict[str, list[Interval]] | None = None

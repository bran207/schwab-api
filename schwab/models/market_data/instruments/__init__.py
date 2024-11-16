from schwab.models.utils import SchwabDataModel
from schwab.models.market_data.instruments.const import AssetTypes
from schwab.models.market_data.instruments.fundamental import Fundamental


class CoreInstrument(SchwabDataModel):
    cusip: str
    symbol: str
    description: str
    exchange: str
    asset_type: AssetTypes


class Bond(CoreInstrument):
    bond_factor: str
    bond_multiplier: str
    bond_price: float


class Instrument(CoreInstrument):
    bond_factor: str | None = None
    bond_multiplier: str | None = None
    bond_price: float | None = None
    fundamental: Fundamental | None = None
    instrument_info: CoreInstrument | None = None
    bond_instrument_info: Bond | None = None

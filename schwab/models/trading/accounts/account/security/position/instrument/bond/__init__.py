from schwab.models.trading.accounts.account.security.position.instrument.utils import (
    SchwabAccountPositionInstrumentModel,
)


class SchwabAccountPositionBondPositionModel(SchwabAccountPositionInstrumentModel):
    bond_factor: str
    bond_multiplier: str
    bond_price: float

from schwab.models.trading.currency import SchwabCurrency


class SchwabAccountPositionBondPositionModel(SchwabCurrency):
    bond_factor: str
    bond_multiplier: str
    bond_price: float

from schwab.models.utils import SchwabDataModel


class OrderBalance(SchwabDataModel):
    order_value: float
    projected_available_fund: float
    projected_buying_power: float
    projected_commision: float

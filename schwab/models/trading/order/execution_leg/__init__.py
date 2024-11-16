from datetime import datetime
from schwab.models.utils import SchwabDataModel


class ExecutionLeg(SchwabDataModel):
    leg_id: int
    price: float
    quantity: float
    mismarked_quantity: float
    instrument_id: int
    time: datetime

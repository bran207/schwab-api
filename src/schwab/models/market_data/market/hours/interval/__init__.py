from datetime import datetime

from schwab.models.utils import SchwabDataModel


class Interval(SchwabDataModel):
    start: datetime
    end: datetime

from typing import Literal
from schwab.models.utils import SchwabDataModel


class SchwabIndex(SchwabDataModel):
    active_contract: bool
    type: Literal["BROAD_BASED", "NARROW_BASED", "UNKNOWN"]

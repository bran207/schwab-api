from typing import Literal

from schwab.models.utils import SchwabDataModel
from schwab.models.trading.accounts.account.security.position import (
    SchwabAccountPositionModel,
)
from schwab.models.trading.accounts.account.security.balances.current import (
    SchwabAccountCurrentBalances,
)
from schwab.models.trading.accounts.account.security.balances.initial import (
    SchwabAccountInitialBalances,
)
from schwab.models.trading.accounts.account.security.balances.projected import (
    SchwabAccountProjectedBalances,
)


class SchwabAccountSecurityModel(SchwabDataModel):
    type: Literal["CASH", "MARGIN"]
    account_number: str
    round_trips: int
    is_day_trader: bool
    is_closing_only_restricted: bool
    pfcb_flag: bool
    positions: list[SchwabAccountPositionModel] | None = None
    initial_balances: SchwabAccountInitialBalances
    current_balances: SchwabAccountCurrentBalances
    projected_balances: SchwabAccountProjectedBalances

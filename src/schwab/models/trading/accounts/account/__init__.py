from schwab.models.utils import SchwabDataModel

from schwab.models.trading.accounts.account.security import SchwabAccountSecurityModel


class SchwabAccount(SchwabDataModel):
    securities_account: SchwabAccountSecurityModel

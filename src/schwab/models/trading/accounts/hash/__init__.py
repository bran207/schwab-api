from schwab.models.utils import SchwabDataModel


class SchwabAccountNumberHash(SchwabDataModel):
    account_number: str
    hash_value: str

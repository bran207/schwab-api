from typing import Literal

from schwab.models.utils import SchwabDataModel


class SchwabTransactionUserDetails(SchwabDataModel):
    cd_domain_id: str
    login: str
    type: Literal[
        "ADVISOR_USER", "BROKER_USER", "CLIENT_USER", "SYSTEM_USER", "UNKNOWN"
    ]
    user_id: int
    system_user_name: str
    first_name: str
    last_name: str
    broker_rep_code: str

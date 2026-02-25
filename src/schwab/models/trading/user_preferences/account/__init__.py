from typing import Literal

from pydantic import Field

from schwab.models.utils import SchwabDataModel


class SchwabUserPreferenceAccount(SchwabDataModel):
    account_number: str
    primary_account: bool
    type: str
    nickname: str = Field(alias="nickName")
    account_color: Literal["Green", "Blue"]
    display_account_id: str = Field(alias="displayAcctId")
    auto_position_effect: bool

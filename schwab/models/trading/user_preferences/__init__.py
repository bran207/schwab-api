from schwab.models.utils import SchwabDataModel
from schwab.models.trading.user_preferences.account import SchwabUserPreferenceAccount
from schwab.models.trading.user_preferences.streamer_info import (
    SchwabUserPreferenceStreamerInfo,
)
from schwab.models.trading.user_preferences.offer import SchwabUserPreferenceOffer


class SchwabUserPreferenceModel(SchwabDataModel):
    accounts: list[SchwabUserPreferenceAccount]
    streamer_info: list[SchwabUserPreferenceStreamerInfo]
    offers: list[SchwabUserPreferenceOffer]

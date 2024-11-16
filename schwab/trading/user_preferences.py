from schwab.models.trading.user_preferences import SchwabUserPreferenceModel
from schwab.utils import ClientSession


class SchwabUserPreferencesClient(ClientSession):

    @property
    def base_url(self):
        return super().base_url + "/trader/v1"

    def get(self):
        return SchwabUserPreferenceModel.model_validate(
            self.call_api(method="GET", endpoint="/userPreference").json()
        )

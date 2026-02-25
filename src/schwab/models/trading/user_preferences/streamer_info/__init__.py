from pydantic import Field

from schwab.models.utils import SchwabDataModel


class SchwabUserPreferenceStreamerInfo(SchwabDataModel):
    streamer_socket_url: str
    schwab_client_customer_id: str
    schwab_client_correlation_id: str = Field(alias="schwabClientCorrelId")
    schwab_client_channel: str
    schwab_client_function_id: str

from pydantic import Field

from schwab.models.utils import SchwabDataModel


class SchwabUserPreferenceOffer(SchwabDataModel):
    level_2_permissions: bool = Field(alias="level2Permissions")

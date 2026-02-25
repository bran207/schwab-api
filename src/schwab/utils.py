from abc import abstractmethod
from pydantic.alias_generators import to_camel
from pydantic import BaseModel, ConfigDict
from typing import TypeVar

from schwab.session import SchwabAPISession


class SchwabDataModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


SchwabModel = TypeVar("SchwabModel", bound=SchwabDataModel)


class ClientSession(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    client: SchwabAPISession

    @property
    @abstractmethod
    def base_url(self):
        return "https://api.schwabapi.com"

    def call_api(self, method: str, endpoint: str, **kwargs):
        return self.client.call_api(
            method=method, url=self.base_url + endpoint, **kwargs
        )

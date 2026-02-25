from authlib.integrations.requests_client.oauth2_session import OAuth2Session
from authlib.oauth2.rfc6749 import OAuth2Token


class SchwabAPISession(OAuth2Session):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        refresh_token: str | None = None,
    ):
        self.token_endpoint = "https://api.schwabapi.com/v1/oauth/token"
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            token_endpoint=self.token_endpoint,
        )

        if refresh_token:
            self.token = OAuth2Token({"refresh_token": refresh_token, "expires_in": -1})

    def create_authorization_url(self, state=None, code_verifier=None, **kwargs):
        return super().create_authorization_url(
            "https://api.schwabapi.com/v1/oauth/authorize",
            state,
            code_verifier,
            scope="readonly",
            **kwargs
        )

    def call_api(self, method: str, url: str, **kwargs):
        return self.request(method=method, url=url, **kwargs)

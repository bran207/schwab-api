import pytest
from unittest.mock import patch, MagicMock, PropertyMock
from schwab.market_data.expiration_chain import (
    SchwabMarketDataExpirationChainClient,
    ExpirationChain,
)
from tests.utils import DummyResponse


@pytest.fixture
def mock_expiration_chain_client(mock_session):
    return SchwabMarketDataExpirationChainClient(client=mock_session)


def test_base_url_appends_marketdata(mock_expiration_chain_client):

    # We patch the parent property to ensure we test the concatenation logic
    with patch(
        "schwab.utils.ClientSession.base_url", new_callable=PropertyMock
    ) as mock_base:
        mock_base.return_value = "https://api.schwabapi.com"
        assert (
            mock_expiration_chain_client.base_url
            == "https://api.schwabapi.com/marketdata/v1/expirationchain"
        )


def test_get_calls_api_correctly(mock_expiration_chain_client):
    mock_payload = {"expirations": ["2026-03-20"]}

    with (
        patch(
            "schwab.utils.ClientSession.call_api",
        ) as mock_call,
        patch(
            "schwab.market_data.expiration_chain.ExpirationChain",
            return_value=None,
        ) as mock_model,
    ):
        mock_call.return_value = DummyResponse(mock_payload)

        mock_expiration_chain_client.get("AAPL")

        mock_call.assert_called_once_with(
            method="GET",
            endpoint="",
            params={"symbol": "AAPL"},
        )
        mock_model.assert_called_once_with(**mock_payload)

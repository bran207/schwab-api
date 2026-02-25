import pytest
from unittest.mock import patch, MagicMock, PropertyMock
from schwab.market_data.instruments import (
    SchwabMarketDataInstrumentsClient,
    Instrument,
)
from tests.utils import DummyResponse


@pytest.fixture
def mock_instruments_client(mock_session):
    return SchwabMarketDataInstrumentsClient(client=mock_session)


def test_base_url_appends_marketdata(
    mock_instruments_client: SchwabMarketDataInstrumentsClient,
):

    # We patch the parent property to ensure we test the concatenation logic
    with patch(
        "schwab.utils.ClientSession.base_url", new_callable=PropertyMock
    ) as mock_base:
        mock_base.return_value = "https://api.schwabapi.com"
        assert (
            mock_instruments_client.base_url
            == "https://api.schwabapi.com/marketdata/v1/instruments"
        )


def test_get_calls_api_correctly(
    mock_instruments_client: SchwabMarketDataInstrumentsClient,
):
    instruments = [{"test": "data"}]
    mock_payload = {"instruments": instruments}

    with (
        patch(
            "schwab.utils.ClientSession.call_api",
        ) as mock_call,
        patch(
            "schwab.market_data.instruments.Instrument",
            return_value=None,
        ) as mock_model,
    ):
        mock_call.return_value = DummyResponse(mock_payload)

        mock_instruments_client.get("AAPL")

        mock_call.assert_called_once_with(
            method="GET",
            endpoint="/AAPL",
        )
        for instrument in instruments:
            mock_model.assert_called_with(**instrument)


def test_list_calls_api_correctly(
    mock_instruments_client: SchwabMarketDataInstrumentsClient,
):
    instruments = [{"test": "data"}]
    mock_payload = {"instruments": instruments}

    with (
        patch(
            "schwab.utils.ClientSession.call_api",
        ) as mock_call,
        patch(
            "schwab.market_data.instruments.Instrument",
            return_value=None,
        ) as mock_model,
    ):
        mock_call.return_value = DummyResponse(mock_payload)

        mock_instruments_client.list("AAPL", "search")

        mock_call.assert_called_once_with(
            method="GET",
            endpoint="",
            params={"symbol": "AAPL", "projection": "search"},
        )
        for instrument in instruments:
            mock_model.assert_called_with(**instrument)

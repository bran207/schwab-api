from datetime import date
import pytest
from unittest.mock import patch, MagicMock, PropertyMock
from schwab.market_data.movers import (
    SchwabMarketDataMoversClient,
    Screener,
)
from schwab.models.market_data.market.hours.interval import Interval
from tests.utils import DummyResponse


@pytest.fixture
def mock_market_movers_client(mock_session):
    return SchwabMarketDataMoversClient(client=mock_session)


def test_base_url_appends_movers(
    mock_market_movers_client: SchwabMarketDataMoversClient,
):

    # We patch the parent property to ensure we test the concatenation logic
    with patch(
        "schwab.utils.ClientSession.base_url", new_callable=PropertyMock
    ) as mock_base:
        mock_base.return_value = "https://api.schwabapi.com"
        assert (
            mock_market_movers_client.base_url
            == "https://api.schwabapi.com/marketdata/v1/movers"
        )


def test_get_returns_screeners(
    mock_market_movers_client: SchwabMarketDataMoversClient,
):
    # Mock the API response
    mock_response_data = {
        "screeners": [
            {
                "description": "Apple Inc.",
                "volume": 1000000,
                "last_price": 150.0,
                "net_change": 2.5,
                "market_share": 0.05,
                "total_volume": 20000000,
                "trades": 5000,
                "net_percent_change": 1.69,
                "symbol": "AAPL",
                "change": 2.5,
            },
            {
                "description": "Microsoft Corporation",
                "volume": 800000,
                "last_price": 250.0,
                "net_change": -1.0,
                "market_share": 0.04,
                "total_volume": 15000000,
                "trades": 4000,
                "net_percent_change": -0.4,
                "symbol": "MSFT",
                "change": -1.0,
                "direction": "down",
                "last": 250.0,
            },
        ]
    }
    mock_response = DummyResponse(payload=mock_response_data)

    with (
        patch(
            "schwab.utils.ClientSession.call_api",
            return_value=mock_response,
        ) as mock_call,
    ):

        # Call the get method
        screeners = mock_market_movers_client.get(symbol_id="$DJI")

        # Assert that the call_api method was called with the correct parameters
        mock_market_movers_client.call_api.assert_called_once_with(
            method="GET",
            endpoint="/$DJI",
            params={"sort": None, "frequency": None},
        )

        # Assert that the returned screeners are correctly parsed
        assert len(screeners) == 2
        assert isinstance(screeners[0], Screener)
        assert screeners[0].symbol == "AAPL"
        assert screeners[1].symbol == "MSFT"

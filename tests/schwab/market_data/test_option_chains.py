from datetime import date
import pytest
from unittest.mock import patch, MagicMock, PropertyMock
from schwab.market_data.option_chains import (
    SchwabMarketDataOptionChainClient,
    OptionChain,
)
from schwab.models.market_data.market.hours.interval import Interval
from tests.utils import DummyResponse


@pytest.fixture
def mock_option_chains_client(mock_session):
    return SchwabMarketDataOptionChainClient(client=mock_session)


def test_base_url_appends_option_chains(
    mock_option_chains_client: SchwabMarketDataOptionChainClient,
):

    # We patch the parent property to ensure we test the concatenation logic
    with patch(
        "schwab.utils.ClientSession.base_url", new_callable=PropertyMock
    ) as mock_base:
        mock_base.return_value = "https://api.schwabapi.com"
        assert (
            mock_option_chains_client.base_url
            == "https://api.schwabapi.com/marketdata/v1/chains"
        )


def test_get_option_chains_calls_api_with_correct_params(
    mock_option_chains_client: SchwabMarketDataOptionChainClient,
):
    mock_response = DummyResponse(
        payload={
            "symbol": "AAPL",
            "status": "SUCCESS",
            "strategy": "BUTTERFLY",
            "interval": 0.5,
            "is_delayed": False,
            "is_index": False,
            "days_to_expiration": 30,
            "interest_rate": 0.01,
            "underlying_price": 150.0,
            "volatility": 0.2,
            "call_exp_date_map": {},
            "put_exp_date_map": {},
        }
    )

    with patch(
        "schwab.utils.ClientSession.call_api",
        return_value=mock_response,
    ) as mock_call:
        result = mock_option_chains_client.get(symbol="AAPL")
        assert isinstance(result, OptionChain)
        assert result.symbol == "AAPL"
        assert result.status == "SUCCESS"
        assert result.strategy == "BUTTERFLY"

        mock_call.assert_called_once_with(
            method="GET",
            endpoint="",
            params={
                "symbol": "AAPL",
                "contractType": None,
                "strikeCount": None,
                "includeUnderlyingQuote": None,
                "strategy": "SINGLE",
                "interval": None,
                "strike": None,
                "range": None,
                "fromDate": None,
                "toDate": None,
                "volatility": None,
                "underlyingPrice": None,
                "interestRate": None,
                "daysToExpiration": None,
                "expMonth": None,
                "optionType": None,
                "entitlement": None,
            },
        )

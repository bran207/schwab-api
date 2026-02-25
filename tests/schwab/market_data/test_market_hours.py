from datetime import date
import pytest
from unittest.mock import patch, MagicMock, PropertyMock
from schwab.market_data.market_hours import (
    SchwabMarketDataMarketHoursClient,
    MarketHours,
)
from schwab.models.market_data.market.hours.interval import Interval
from tests.utils import DummyResponse


@pytest.fixture
def mock_market_hours_client(mock_session):
    return SchwabMarketDataMarketHoursClient(client=mock_session)


def test_base_url_appends_markethours(
    mock_market_hours_client: SchwabMarketDataMarketHoursClient,
):

    # We patch the parent property to ensure we test the concatenation logic
    with patch(
        "schwab.utils.ClientSession.base_url", new_callable=PropertyMock
    ) as mock_base:
        mock_base.return_value = "https://api.schwabapi.com"
        assert (
            mock_market_hours_client.base_url
            == "https://api.schwabapi.com/marketdata/v1/markets"
        )


def test_convert_to_dict_transforms_data_correctly(
    mock_market_hours_client: SchwabMarketDataMarketHoursClient,
):
    raw_data = {
        "market1": {
            "sub_market1": {
                "open": "9:30",
                "close": "16:00",
                "isOpen": True,
                "date": "2024-06-01",
                "marketType": "EQUITY",
                "product": "stocks",
                "category": "TEST",
                "product_name": "TEST 2",
            },
            "sub_market2": {
                "open": "10:00",
                "close": "15:00",
                "isOpen": False,
                "date": "2024-06-01",
                "marketType": "BOND",
                "product": "stocks",
                "exchange": "TEST",
            },
        },
        "market2": {
            "sub_market3": {
                "open": "8:00",
                "close": "14:00",
                "isOpen": True,
                "date": "2024-06-01",
                "marketType": "FUTURE",
                "product": "stocks",
                "sessionHours": {
                    "regularMarket": [
                        {
                            "start": "2022-04-14T09:30:00-04:00",
                            "end": "2022-04-14T16:00:00-04:00",
                        }
                    ]
                },
            },
        },
    }

    expected_output = {
        "market1": {
            "sub_market1": MarketHours(
                open="9:30",
                close="16:00",
                is_open=True,
                date=date(2024, 6, 1),
                market_type="EQUITY",
                product="stocks",
                category="TEST",
                product_name="TEST 2",
            ),
            "sub_market2": MarketHours(
                open="10:00",
                close="15:00",
                is_open=False,
                date=date(2024, 6, 1),
                market_type="BOND",
                product="stocks",
                exchange="TEST",
            ),
        },
        "market2": {
            "sub_market3": MarketHours(
                open="8:00",
                close="14:00",
                date=date(2024, 6, 1),
                market_type="FUTURE",
                product="stocks",
                is_open=True,
                sessionHours={
                    "regularMarket": [
                        Interval(
                            start="2022-04-14T09:30:00-04:00",
                            end="2022-04-14T16:00:00-04:00",
                        )
                    ]
                },
            ),
        },
    }

    # Accessing the private method for testing purposes
    output = (
        mock_market_hours_client._SchwabMarketDataMarketHoursClient__convert_to_dict(
            raw_data
        )
    )

    assert output == expected_output


def test_list_calls_api_with_correct_params(
    mock_market_hours_client: SchwabMarketDataMarketHoursClient,
):
    mock_response = DummyResponse(
        payload={
            "market1": {
                "sub_market1": {
                    "open": "9:30",
                    "close": "16:00",
                    "isOpen": True,
                    "date": "2024-06-01",
                    "marketType": "EQUITY",
                    "product": "stocks",
                    "category": "TEST",
                    "product_name": "TEST 2",
                }
            }
        }
    )

    with (
        patch(
            "schwab.utils.ClientSession.call_api",
            return_value=mock_response,
        ) as mock_call,
    ):

        markets = ["market1", "market2"]
        date_param = date(2024, 6, 1)
        result = mock_market_hours_client.list(markets=markets, date=date_param)

        mock_market_hours_client.call_api.assert_called_once_with(
            method="GET", endpoint="", params={"markets": markets, "date": date_param}
        )


def test_get_calls_api_with_correct_params(
    mock_market_hours_client: SchwabMarketDataMarketHoursClient,
):
    mock_response = DummyResponse(
        payload={
            "market1": {
                "sub_market1": {
                    "open": "9:30",
                    "close": "16:00",
                    "isOpen": True,
                    "date": "2024-06-01",
                    "marketType": "EQUITY",
                    "product": "stocks",
                    "category": "TEST",
                    "product_name": "TEST 2",
                }
            }
        }
    )

    with (
        patch(
            "schwab.utils.ClientSession.call_api",
            return_value=mock_response,
        ) as mock_call,
    ):

        market_id = "market1"
        date_param = date(2024, 6, 1)
        result = mock_market_hours_client.get(market_id=market_id, date=date_param)

        mock_market_hours_client.call_api.assert_called_once_with(
            method="GET", endpoint=f"/{market_id}", params={"date": date_param}
        )

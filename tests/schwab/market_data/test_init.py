import pytest

from unittest.mock import patch, MagicMock, PropertyMock
from schwab.market_data import SchwabMarketData
from schwab.session import SchwabAPISession

from unittest.mock import create_autospec, PropertyMock


@pytest.fixture
def mock_market_data(mock_session: SchwabAPISession) -> SchwabMarketData:
    return SchwabMarketData(client=mock_session)


def test_base_url(
    mock_market_data: SchwabMarketData,
):

    # We patch the parent property to ensure we test the concatenation logic
    with patch(
        "schwab.utils.ClientSession.base_url", new_callable=PropertyMock
    ) as mock_base:
        mock_base.return_value = "https://api.schwabapi.com"
        assert mock_market_data.base_url == "https://api.schwabapi.com/marketdata/v1"

import pytest

from schwab.market_data import SchwabMarketData
from schwab.session import SchwabAPISession

from unittest.mock import create_autospec, PropertyMock


@pytest.fixture
def mock_session() -> SchwabAPISession:
    mock_session: SchwabAPISession = create_autospec(
        spec=SchwabAPISession, instance=True
    )
    return mock_session

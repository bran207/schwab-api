from typing import TypeVar

from schwab.models.trading.currency import SchwabCurrency


SchwabInstruments = TypeVar("SchwabInstruments", bound=SchwabCurrency)

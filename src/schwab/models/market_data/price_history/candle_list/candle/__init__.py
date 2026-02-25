from schwab.models.utils import SchwabDataModel


class Candle(SchwabDataModel):
    close: float
    datetime: int
    high: float
    low: float
    open: float
    volume: int


if __name__ == "__main__":
    Candle.model_validate(
        {
            "open": 175.01,
            "high": 175.15,
            "low": 175.01,
            "close": 175.04,
            "volume": 10719,
            "datetime": 1639137600000,
        }
    )

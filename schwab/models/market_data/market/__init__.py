from schwab.models.market_data.market.hours import MarketHours

IndividualMarketHours = dict[str, MarketHours]
TotalMarketHours = dict[str, IndividualMarketHours]

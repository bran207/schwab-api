from datetime import date
from pydantic import Field
from schwab.models.utils import SchwabDataModel


class Fundamental(SchwabDataModel):
    symbol: str
    high_52: float = Field(alias="high52")
    low_52: float = Field(alias="low52")
    dividend_amount: float
    dividend_yield: float
    dividend_date: str
    pe_ratio: float
    peg_ration: float
    pb_ratio: float
    pr_ratio: float
    pcf_ratio: float
    gross_margin_ttm: float = Field(alias="grossMarginTTM")
    gross_margin_mrq: float = Field(alias="grossMarginMRQ")
    net_profit_margin_ttm: float = Field(alias="netProfitMarginTTM")
    net_profit_margin_mrq: float = Field(alias="netProfitMarginMRQ")
    operating_margin_ttm: float = Field(alias="operatingMarginTTM")
    operating_margin_mrq: float = Field(alias="operatingMarginMRQ")
    return_on_equity: float
    return_on_assets: float
    return_on_investments: float
    quick_ratio: float
    current_ratio: float
    interest_coverage: float
    total_debt_to_capital: float
    lt_debt_to_equity: float
    total_debt_to_equity: float
    esp_ttm: float = Field(alias="espTTM")
    esp_change_percent_ttm: float = Field(alias="epsChangePercentTTM")
    eps_change_year: float
    esp_change: float
    rev_change_year: float
    rev_change_ttm: float = Field(alias="revChangeTTM")
    rev_change_in: float
    shares_outstanding: float
    market_cap_float: float
    market_cap: float
    book_value_per_share: float
    short_int_to_float: float
    short_int_day_to_cover: float
    div_growth_rate_3_year: float = Field("divGrowthRate3Year")
    dividend_pay_amount: float
    dividend_pay_date: date
    beta: float
    vol_1_day_avg: float
    vol_10_day_avg: float
    vol_3_month_avg: float
    avg_10_days_volume: int
    avg_1_day_volume: int
    avg_3_month_volumne: int
    declaration_date: date
    dividend_freq: int
    esp: float
    corpaction_date: date
    dtn_volume: int
    next_dividend_pay_date: str
    next_dividend_date: date
    fund_leverage_factor: float
    fund_strategy: str

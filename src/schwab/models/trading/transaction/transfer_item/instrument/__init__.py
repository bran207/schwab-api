from schwab.models.trading.index import SchwabIndex
from schwab.models.trading.product import SchwabProduct
from schwab.models.trading.future import SchwabFuture
from schwab.models.trading.forex import SchwabForex
from schwab.models.trading.currency import SchwabCurrency
from schwab.models.trading.collective_investment import SchwabCollectiveInstrument
from schwab.models.trading.transaction.transfer_item.instrument.option import (
    SchwabTransactionOption,
)
from schwab.models.trading.transaction.transfer_item.instrument.cash_equivalent import (
    SchwabTransactionInstrumentCashEquivalent,
)
from schwab.models.trading.transaction.transfer_item.instrument.equity import (
    SchwabTransactionInstrumentEquity,
)
from schwab.models.trading.transaction.transfer_item.instrument.fixed_income import (
    SchwabTransactionInstrumentFixedIncome,
)
from schwab.models.trading.transaction.transfer_item.instrument.mutual_fund import (
    SchwabTransactionMutualFund,
)

TransactionInstrument = (
    SchwabTransactionInstrumentCashEquivalent
    | SchwabCollectiveInstrument
    | SchwabCurrency
    | SchwabTransactionInstrumentEquity
    | SchwabTransactionInstrumentFixedIncome
    | SchwabForex
    | SchwabFuture
    | SchwabIndex
    | SchwabTransactionMutualFund
    | SchwabTransactionOption
    | SchwabProduct
)

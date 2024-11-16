from typing import Literal

# OPTIONS Literals - Start

CONTRACT_TYPE = Literal["P", "C"]  # Put  # Call

SETTLEMENT_TYPE = Literal["A", "P"]  # AM  # PM

EXERCISE_TYPE = Literal["A", "E"]  # American  # European

EXPIRATION_TYPE = Literal[
    "M",  # End of Month
    "Q",  # End of Quarter
    "S",  # Regular (3rd Friday of the Month)
    "W",  # End of Week
]

# OPTIONS Literals - End

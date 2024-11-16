from datetime import datetime, timedelta
from typing import Literal
from typing_extensions import Annotated
from pydantic.functional_validators import AfterValidator
from schwab.utils import ClientSession
from schwab.models.trading.order import SchwabOrder

SchwabOrderStatus = Literal[
    "AWAITING_PARENT_ORDER",
    "AWAITING_CONDITION",
    "AWAITING_STOP_CONDITION",
    "AWAITING_MANUAL_REVIEW",
    "ACCEPTED",
    "AWAITING_UR_OUT",
    "PENDING_ACTIVATION",
    "QUEUED",
    "WORKING",
    "REJECTED",
    "PENDING_CANCEL",
    "CANCELED",
    "PENDING_REPLACE",
    "REPLACED",
    "FILLED",
    "EXPIRED",
    "NEW",
    "AWAITING_RELEASE_TIME",
    "PENDING_ACKNOWLEDGEMENT",
    "PENDING_RECALL",
    "UNKNOWN",
]


def is_more_than_60_days_ago(dte: datetime):
    assert dte < (
        datetime.today() - timedelta(days=60)
    ), "Date must be within 60 days of today's date"
    return dte


FROM_ENTERED_TIME = Annotated[datetime, AfterValidator(is_more_than_60_days_ago)]


class SchwabOrders(ClientSession):

    @property
    def base_url(self):
        return super().base_url + "/trader/v1"

    def list(
        self,
        from_entered_time: datetime,
        to_entered_time: FROM_ENTERED_TIME,
        account_number: str | None = None,
        max_results: int | None = None,
        status: SchwabOrderStatus | None = None,
    ):
        return [
            SchwabOrder(**order)
            for order in self.call_api(
                method="GET",
                endpoint=(
                    f"/accounts/{account_number}/orders"
                    if account_number
                    else "/orders"
                ),
                params={
                    "fromEnteredTime": from_entered_time.strftime(
                        "%Y-%m-%dT%H:%M:%S.%fZ"
                    ),
                    "toEnteredTime": to_entered_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    "maxResults": max_results,
                    "status": status,
                },
            ).json()
        ]

    def get(self, account_number: str, order_id: str):
        return SchwabOrder(
            **self.call_api(
                method="GET", endpoint=f"/accounts/{account_number}/orders/{order_id}"
            ).json()
        )

    def delete(self, account_number: str, order_id: str):
        return self.call_api(
            method="DELETE", endpoint=f"/accounts/{account_number}/orders/{order_id}"
        )

    def create(self, account_number: str, order: SchwabOrder):
        return self.call_api(
            method="POST",
            endpoint=f"/accounts/{account_number}/orders",
            json=order.model_dump(),
        )

    def replace(self, account_number: str, order_id: str, updated_order: SchwabOrder):
        return self.call_api(
            method="PUT",
            endpoint=f"/accounts/{account_number}/orders/{order_id}",
            json=updated_order.model_dump(),
        )

    def preview(self, account_number: str, order: SchwabOrder):
        return self.call_api(
            method="POST",
            endpoint=f"/accounts/{account_number}/previewOrder",
            json=order.model_dump(),
        )

### Breaking change in Order API

In December 2023 a change affecting order management API will be released. The exact date will be announced once
integrations with service providers are validated.


## Changes

- OrderItem API is removed. 
- Order is not a container of OrderItems any more, and has received new states, which now look like this:
    - PENDING_CONSUMER
    - PENDING_PROVIDER
    - EXECUTING
    - DONE
    - ERRED
    - CANCELED
    - REJECTED

## Migration

- If you are using python-waldur-client, make sure you upgrade to 0.2.9+.
    - New functions introduced: `marketplace_order_approve_by_provider`, `marketplace_order_reject_by_provider` 
    - Removed deprecated functions: `list_order_items`
- If you integrate directly with APIs and use Order API:
    - Order approval from consumer side has been made explicit:
        - `/marketplace-orders/order_uuid/approve_by_consumer/`
        - `/marketplace-orders/order_uuid/reject_by_provider/`


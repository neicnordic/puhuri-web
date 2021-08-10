# Initial setup

## Installation

Puhuri Core is based on Waldur, which exposes REST API. Puhuri Core SDK is a [python wrapper](https://github.com/waldur/ansible-waldur-module/blob/develop/waldur_client.py) for typical REST operations.

It is packaged as a Python module and published in PyPI, so you can install it with standard tools like:

```sh
pip install ansible-waldur-module
```

In order to perform operations, a user needs to create an instance of `WaldurClient` class:

```python
from waldur_client import WaldurClient

client = WaldurClient('<api-url>', '<api-token>')
```

This instance provides interface for further interaction with Puhuri Core and will be used across examples in related documentation.

## Error handling

If the client fails to perform an operation, it raises `WaldurClientException`. This can be handles using `try...except` block.
Example:
```python
from waldur_client import WaldurClient, WaldurClientException
import pprint

client = WaldurClient('https://abc.example.com/api', 'some-token')

try:
    client.list_marketplace_resources()
except WaldurClientException as e:
    pprint.pprint(e)

# WaldurClientException("HTTPSConnectionPool(host='abc.example.com', port=443):
# Max retries exceeded with url: /api/marketplace-resources/?page_size=200
# (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x110636430>:
# Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))")
```

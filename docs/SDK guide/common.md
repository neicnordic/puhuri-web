# Common

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

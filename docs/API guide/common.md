# Pagination 

All responses from Puhuri Core / Portal APIs are paginated. By default, 10 responses are returned.
You can request more by passing ``page_size=XXX`` as query attribute. XXX can go up to 200.


Pagination information is provided in Link headers.

Check [example](https://github.com/waldur/ansible-waldur-module/blob/a2299850fb1bb122b458aa5ab712f0d9a263d8e5/waldur_client.py#L147) of getting the full listing.

# Field selection

In order to get a specific field from the response, you can use `field=field_name` selector in the query parameters.
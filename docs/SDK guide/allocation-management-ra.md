# Allocation Lifecycle Management by Resource Allocator

## Listing associations between users and resources

To list the created associations between users and resources, the service provider should use `list_remote_offering_users` method. It receives an optional `filters` argument, a dictionary containing filters for the associations. The possible items are:

- `user_uuid` - UUID of a user associated with resources belonging to SP
- `offering` - SP resource URL
- `offering_uuid` - UUID of a resource
- `created` - date after what the association was created; the format is `YYYY-MM-DD`, e.g. `2022-01-30`
- `modified` - date after what the association was modified; the format is the same as for the `created` field

In case if SDK usage is not possible, HTTP request can be sent:

```http
GET <API-URL>/marketplace-offering-users/?user_uuid=<USER_UUID>&offering_uuid=<OFFERING_UUID>&created=2022-01-10&modified=2022-01-30

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

{
    "created": "2022-01-19T19:40:10.328758Z", # When the association has been created
    "modified": "2022-01-31T18:02:10.328758Z", #
    "offering": "<API-URL>/marketplace-offerings/<OFFERING_UUID>/", # URL of the offering
    "offering_name": "Remote offering", # Name of the offering
    "offering_uuid": "<OFFERING_UUID>", # UUID of the offering
    "user": "http://localhost:8000/api/users/<USER_UUID>/", # URL of the user
    "user_username": "<USER_USERNAME>", # Username of the user
    "user_uuid": "<USER_UUID>", # UUID of the user
    "username": "<USERNAME>" # Username used in the association
}
```

Example:

```bash
> http -v --pretty all GET http://puhuri.example.com/api/marketplace-offering-users/ user_uuid==<USER_UUID> offering_uuid==<OFFERING_UUID> created==2021-08-17 Authorization:"Token <TOKEN>"

GET /api/marketplace-offering-users/?user_uuid=<USER_UUID>&offering_uuid=<OFFERING_UUID>&created=2021-08-17 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token abc
Connection: keep-alive
Host: api.etais.ee
User-Agent: HTTPie/2.4.0



HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, POST, HEAD, OPTIONS
Content-Language: en
Content-Length: 436
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Wed, 16 Feb 2022 12:03:49 GMT
Link: <http://puhuri.example.com/api/marketplace-offering-users/?created=2021-08-17&offering_uuid=<OFFERING_UUID>&user_uuid=<USER_UUID>>; rel="first", <http://puhuri.example.com/api/marketplace-offering-users/?created=2021-08-17&offering_uuid=<OFFERING_UUID>&user_uuid=<USER_UUID>>; rel="last"
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-Result-Count: 1
X-XSS-Protection: 1; mode=block

[
    {
        "created": "2021-08-18T10:33:21.433472Z",
        "modified": "2022-02-04T19:35:19.382943Z",
        "offering": "http://puhuri.example.com/api/marketplace-offerings/<OFFERING_UUID>/",
        "offering_name": "<OFFERING_NAME>",
        "offering_uuid": "<OFFERING_UUID>",
        "user": "http://puhuri.example.com/api/users/<USER_UUID>/",
        "user_username": "<USER_USERNAME>",
        "user_uuid": "<USER_UUID>",
        "username": "<USERNAME>"
    }
]
```

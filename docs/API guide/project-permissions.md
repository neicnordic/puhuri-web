# Project permissions

## Getting a mapping of AAI user to Core user

To get Puhuri Core User UUID mapping from Puhuri AAI CUID, service providers should pass CUID as a parameter to the endpoint below.

```bash
http POST https://puhuri-core-beta.neic.no/api/remote-eduteams/ Authorization:"Token 32e7682378fa394b0f8b2538c444b60129ebfb47" cuid="01cfb7d6b76d400d12b8c8e0e33e36c5ef4562c1@acc.researcher-access.org"
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: POST, OPTIONS
Content-Language: en
Content-Length: 43
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Wed, 14 Apr 2021 09:32:37 GMT
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "uuid": "bc9db26ff9984f8fa972fc071bfd008e"
}

```

Example of error message if user information could not have been retrieved.

```bash
http POST https://puhuri-core-beta.neic.no/api/remote-eduteams/ Authorization:"Token 32e7682378fa394b0f8b2538c444b60129ebfb47" cuid="asdasd"
HTTP/1.1 401 Unauthorized
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: POST, OPTIONS
Content-Language: en
Content-Length: 53
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Wed, 14 Apr 2021 09:31:40 GMT
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "detail": "Eduteams error: Unable to get user info."
}


```

The calls to the mapping endpoint are only allowed to users with identity manager role!

```bash
$ http POST https://puhuri-core-beta.neic.no/api/remote-eduteams/ Authorization:"Token 32e7682378fa394b0f8b2538c444b60129ebfb47"
HTTP/1.1 403 Forbidden
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: POST, OPTIONS
Content-Language: en
Content-Length: 56
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Wed, 14 Apr 2021 09:28:05 GMT
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

"Only identity manager is allowed to sync remote users."

```

## Project members permissions allocation
User creates a role for a user in a project.

```bash
$ http --pretty=format -v POST https://puhuri-core-beta.neic.no/api/projects/2477fb6fad594922ac2f5ba195807502/add_user/ Authorization:"Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246" role=PROJECT.ADMIN user=d213b473874c44d0bb5e2588b091160d
POST /api/projects/2477fb6fad594922ac2f5ba195807502/add_user/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246
Connection: keep-alive
Content-Length: 69
Content-Type: application/json
Host: puhuri-core-beta.neic.no
User-Agent: HTTPie/3.2.2

{
    "role": "PROJECT.ADMIN",
    "user": "d213b473874c44d0bb5e2588b091160d"
}

HTTP/1.1 201 Created
access-control-allow-credentials: true
access-control-allow-headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With, sentry-trace, baggage
access-control-allow-methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
access-control-allow-origin: *
access-control-expose-headers: Link, X-Result-Count
allow: POST, OPTIONS
content-language: en
content-length: 24
content-security-policy: report-uri https://csp.hpc.ut.ee/log; form-action 'self'; frame-ancestors 'self';
content-type: application/json
date: Sun, 08 Oct 2023 17:28:49 GMT
referrer-policy: strict-origin-when-cross-origin
strict-transport-security: max-age=31536000; preload
vary: Accept-Language, Cookie
x-content-type-options: nosniff
x-frame-options: DENY
x-xss-protection: 1; mode=block

{
    "expiration_time": null
}
```

## List project permissions

```bash
$ http --pretty=format -v https://puhuri-core-beta.neic.no/api/projects/2477fb6fad594922ac2f5ba195807502/list_users/ Authorization:"Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246" 
GET /api/projects/2477fb6fad594922ac2f5ba195807502/list_users/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246
Connection: keep-alive
Host: puhuri-core-beta.neic.no
User-Agent: HTTPie/3.2.2



HTTP/1.1 200 OK
access-control-allow-credentials: true
access-control-allow-headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With, sentry-trace, baggage
access-control-allow-methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
access-control-allow-origin: *
access-control-expose-headers: Link, X-Result-Count
allow: GET, HEAD, OPTIONS
content-language: en
content-length: 484
content-security-policy: report-uri https://csp.hpc.ut.ee/log; form-action 'self'; frame-ancestors 'self';
content-type: application/json
date: Sun, 08 Oct 2023 17:29:53 GMT
link: <https://puhuri-core-beta.neic.no/api/projects/2477fb6fad594922ac2f5ba195807502/list_users/>; rel="first", <https://puhuri-core-beta.neic.no/api/projects/2477fb6fad594922ac2f5ba195807502/list_users/>; rel="last"
referrer-policy: strict-origin-when-cross-origin
strict-transport-security: max-age=31536000; preload
vary: Accept-Language, Cookie
x-content-type-options: nosniff
x-frame-options: DENY
x-result-count: 1
x-xss-protection: 1; mode=block

[
    {
        "created": "2023-10-08T17:28:49.565755Z",
        "created_by_full_name": "Demo User",
        "created_by_uuid": "d213b473874c44d0bb5e2588b091160d",
        "expiration_time": null,
        "role_name": "PROJECT.ADMIN",
        "role_uuid": "f734dc56c95e4f8880293defef00079e",
        "user_email": "demo.user@example.com",
        "user_full_name": "Demo User",
        "user_image": null,
        "user_username": "1af2bdea-73db-4790-baa5-5b487b6625f5@myaccessid.org",
        "user_uuid": "d213b473874c44d0bb5e2588b091160d",
        "uuid": "afdda66296c9490ebed72fce4a00d27a"
    }
]
```

## Removal of members from a project
User can remove the permissions calling DELETE verb on permission's URL.

```bash
$ http --pretty=format -v POST https://puhuri-core-beta.neic.no/api/projects/2477fb6fad594922ac2f5ba195807502/delete_user/ Authorization:"Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246" role=PROJECT.ADMIN user=d213b473874c44d0bb5e2588b091160d
POST /api/projects/2477fb6fad594922ac2f5ba195807502/delete_user/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token b0dd9a5eb32a158b2739d57d2b359aeb30aef246
Connection: keep-alive
Content-Length: 69
Content-Type: application/json
Host: puhuri-core-beta.neic.no
User-Agent: HTTPie/3.2.2

{
    "role": "PROJECT.ADMIN",
    "user": "d213b473874c44d0bb5e2588b091160d"
}

HTTP/1.1 200 OK
access-control-allow-credentials: true
access-control-allow-headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With, sentry-trace, baggage
access-control-allow-methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
access-control-allow-origin: *
access-control-expose-headers: Link, X-Result-Count
allow: POST, OPTIONS
content-language: en
content-length: 0
content-security-policy: report-uri https://csp.hpc.ut.ee/log; form-action 'self'; frame-ancestors 'self';
date: Sun, 08 Oct 2023 17:31:32 GMT
referrer-policy: strict-origin-when-cross-origin
strict-transport-security: max-age=31536000; preload
vary: Accept-Language, Cookie
x-content-type-options: nosniff
x-frame-options: DENY
x-xss-protection: 1; mode=block
```

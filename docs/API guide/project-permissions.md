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
User create a role for a user in a project.

```bash
$ http --pretty=format -v POST https://puhuri-core-beta.neic.no/api/project-permissions/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" role=member project=https://puhuri-core-beta.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/ user=https://puhuri-core-beta.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/
POST /api/project-permissions/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Content-Length: 200
Content-Type: application/json
Host: puhuri-core-beta.neic.no
User-Agent: HTTPie/2.4.0

{
    "project": "https://puhuri-core-beta.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "role": "member",
    "user": "https://puhuri-core-beta.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/"
}

HTTP/1.1 201 Created
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, POST, HEAD, OPTIONS
Content-Language: en
Content-Length: 721
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 10:37:47 GMT
Location: https://puhuri-core-beta.neic.no/api/project-permissions/10/
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "created": "2021-04-09T10:37:47.246607Z",
    "created_by": "https://puhuri-core-beta.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
    "customer_name": "Danish e-Infrastructure Cooperation",
    "expiration_time": null,
    "pk": 10,
    "project": "https://puhuri-core-beta.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "project_name": "New project name",
    "project_uuid": "4475ac77fa3a491aacb3fb3a6dfadadf",
    "role": "member",
    "url": "https://puhuri-core-beta.neic.no/api/project-permissions/10/",
    "user": "https://puhuri-core-beta.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
    "user_email": "admin@example.com",
    "user_full_name": "Demo Staff",
    "user_native_name": "",
    "user_username": "admin",
    "user_uuid": "3f2cadfbb2b145fd8cf18d549dcd7329"
}
```

## List project permissions

```bash
$ http --pretty=format -v https://puhuri-core-beta.neic.no/api/project-permissions/ project==4475ac77fa3a491aacb3fb3a6dfadadf Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811"
GET /api/project-permissions/?project=4475ac77fa3a491aacb3fb3a6dfadadf HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Host: puhuri-core-beta.neic.no
User-Agent: HTTPie/2.4.0



HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, POST, HEAD, OPTIONS
Content-Language: en
Content-Length: 723
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 10:37:47 GMT
Link: <https://puhuri-core-beta.neic.no/api/project-permissions/?project=4475ac77fa3a491aacb3fb3a6dfadadf>; rel="first", <https://puhuri-core-beta.neic.no/api/project-permissions/?project=4475ac77fa3a491aacb3fb3a6dfadadf>; rel="last"
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Result-Count: 1
X-XSS-Protection: 1; mode=block

[
    {
        "created": "2021-04-09T10:37:47.246607Z",
        "created_by": "https://puhuri-core-beta.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
        "customer_name": "Danish e-Infrastructure Cooperation",
        "expiration_time": null,
        "pk": 10,
        "project": "https://puhuri-core-beta.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
        "project_name": "New project name",
        "project_uuid": "4475ac77fa3a491aacb3fb3a6dfadadf",
        "role": "member",
        "url": "https://puhuri-core-beta.neic.no/api/project-permissions/10/",
        "user": "https://puhuri-core-beta.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
        "user_email": "admin@example.com",
        "user_full_name": "Demo Staff",
        "user_native_name": "",
        "user_username": "admin",
        "user_uuid": "3f2cadfbb2b145fd8cf18d549dcd7329"
    }
]
```

## Removal of members from a project
User can remove the permissions calling DELETE verb on permission's URL.

```bash
$ http --pretty=format -v DELETE https://puhuri-core-beta.neic.no/api/project-permissions/10/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811"
DELETE /api/project-permissions/10/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Content-Length: 0
Host: puhuri-core-beta.neic.no
User-Agent: HTTPie/2.4.0



HTTP/1.1 204 No Content
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Language: en
Content-Length: 0
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Date: Fri, 09 Apr 2021 10:38:37 GMT
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
```

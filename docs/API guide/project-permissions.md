# Project permissions

## Getting a mapping of AAI user to Core user
<!-- {generate_mapping_aai_to_core_getting} -->
### TODO

## Project members permissions allocation
User create a role for a user in a project.

```bash
$ http --pretty=format -v POST https://puhuri-core-demo.neic.no/api/project-permissions/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" role=member project=https://puhuri-core-demo.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/ user=https://puhuri-core-demo.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/
POST /api/project-permissions/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Content-Length: 200
Content-Type: application/json
Host: puhuri-core-demo.neic.no
User-Agent: HTTPie/2.4.0

{
    "project": "https://puhuri-core-demo.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "role": "member",
    "user": "https://puhuri-core-demo.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/"
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
Location: https://puhuri-core-demo.neic.no/api/project-permissions/10/
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "created": "2021-04-09T10:37:47.246607Z",
    "created_by": "https://puhuri-core-demo.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
    "customer_name": "Danish e-Infrastructure Cooperation",
    "expiration_time": null,
    "pk": 10,
    "project": "https://puhuri-core-demo.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "project_name": "New project name",
    "project_uuid": "4475ac77fa3a491aacb3fb3a6dfadadf",
    "role": "member",
    "url": "https://puhuri-core-demo.neic.no/api/project-permissions/10/",
    "user": "https://puhuri-core-demo.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
    "user_email": "admin@example.com",
    "user_full_name": "Demo Staff",
    "user_native_name": "",
    "user_username": "admin",
    "user_uuid": "3f2cadfbb2b145fd8cf18d549dcd7329"
}
```

## List project permissions

```bash
$ http --pretty=format -v https://puhuri-core-demo.neic.no/api/project-permissions/ project==4475ac77fa3a491aacb3fb3a6dfadadf Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811"
GET /api/project-permissions/?project=4475ac77fa3a491aacb3fb3a6dfadadf HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Host: puhuri-core-demo.neic.no
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
Link: <https://puhuri-core-demo.neic.no/api/project-permissions/?project=4475ac77fa3a491aacb3fb3a6dfadadf>; rel="first", <https://puhuri-core-demo.neic.no/api/project-permissions/?project=4475ac77fa3a491aacb3fb3a6dfadadf>; rel="last"
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
        "created_by": "https://puhuri-core-demo.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
        "customer_name": "Danish e-Infrastructure Cooperation",
        "expiration_time": null,
        "pk": 10,
        "project": "https://puhuri-core-demo.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
        "project_name": "New project name",
        "project_uuid": "4475ac77fa3a491aacb3fb3a6dfadadf",
        "role": "member",
        "url": "https://puhuri-core-demo.neic.no/api/project-permissions/10/",
        "user": "https://puhuri-core-demo.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
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
$ http --pretty=format -v DELETE https://puhuri-core-demo.neic.no/api/project-permissions/10/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811"
DELETE /api/project-permissions/10/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Content-Length: 0
Host: puhuri-core-demo.neic.no
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

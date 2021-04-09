# Project permissions

## Getting a mapping of AAI user to Core user
<!-- {generate_mapping_aai_to_core_getting} -->
### TODO

## Project members permissions allocation
User can set a permission for `user` in a `project` with `role`, and `expiration_time` (optional) fields. The list of possible roles:
- administrator
- manager
- member

The list of required fields:
- `user` - a user's URL
- `user` - a projects's URL
- `role` - a selected role from the list above

<!-- {generate_members_permissions_creation} -->

```bash
$ http --pretty=format -v POST https://puhuri-core-demo.neic.no/api/project-permissions/ Authorization:"Token 123" role=member project=https://puhuri-core-demo.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/ user=https://puhuri-core-demo.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/
POST /api/project-permissions/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 123
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
Content-Length: 719
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 10:08:42 GMT
Location: https://puhuri-core-demo.neic.no/api/project-permissions/8/
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "created": "2021-04-09T10:08:42.671883Z",
    "created_by": "https://puhuri-core-demo.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
    "customer_name": "Danish e-Infrastructure Cooperation",
    "expiration_time": null,
    "pk": 8,
    "project": "https://puhuri-core-demo.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "project_name": "New project name",
    "project_uuid": "4475ac77fa3a491aacb3fb3a6dfadadf",
    "role": "member",
    "url": "https://puhuri-core-demo.neic.no/api/project-permissions/8/",
    "user": "https://puhuri-core-demo.neic.no/api/users/3f2cadfbb2b145fd8cf18d549dcd7329/",
    "user_email": "admin@example.com",
    "user_full_name": "Demo Staff",
    "user_native_name": "",
    "user_username": "admin",
    "user_uuid": "3f2cadfbb2b145fd8cf18d549dcd7329"
}
```

## Removal of members from a project
User can remove the permissions by its `id` specified as a path variable.

<!-- {generate_project_members_removal} -->

```bash
$ http --pretty=format -v DELETE https://puhuri-core-demo.neic.no/api/project-permissions/8/ Authorization:"Token 123"
DELETE /api/project-permissions/8/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization: Token 123
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
Date: Fri, 09 Apr 2021 10:10:12 GMT
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
```

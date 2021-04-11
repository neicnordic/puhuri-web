# Project

## Lookup allocator customers available to a user

In most cases integration user can see only one allocating organization (or Puhuri Core "customer"), however it is
possible that the same account is used for allocating different shares, e.g. national share and community specific.
Projects are always created in the context of a specific customer, so as a first thing you need to lookup a specific
customer you want to use. Customer is a stable entity, so it's URL / UUID can be cached.

```bash
$ http --pretty=format -v https://puhuri-core-demo.neic.no/api/customers/ field==url field==name Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811"
GET /api/customers/?field=url&field=name HTTP/1.1
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
Content-Length: 1188
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 09:28:42 GMT
Link: <https://puhuri-core-demo.neic.no/api/customers/?field=url&field=name>; rel="first", <https://puhuri-core-demo.neic.no/api/customers/?field=url&field=name>; rel="last"
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Result-Count: 9
X-XSS-Protection: 1; mode=block

[
    {
        "name": "Danish e-Infrastructure Cooperation",
        "url": "https://puhuri-core-demo.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/"
    },
    {
        "name": "Estonian Scientific Computing Infrastructure",
        "url": "https://puhuri-core-demo.neic.no/api/customers/33541d82c56c4eca8dbb1dabee54b3b9/"
    },
    {
        "name": "IT CENTER FOR SCIENCE LTD",
        "url": "https://puhuri-core-demo.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/"
    },
    {
        "name": "Swedish National Infrastructure for Computing",
        "url": "https://puhuri-core-demo.neic.no/api/customers/479843b7d15543bba6c0596bf408df63/"
    },
    {
        "name": "Swiss National Supercomputing Centre",
        "url": "https://puhuri-core-demo.neic.no/api/customers/f7b91251f991485999f423529fcdc1ad/"
    },
    {
        "name": "The IT4Innovations",
        "url": "https://puhuri-core-demo.neic.no/api/customers/9a8891e0327b460dbce61f9dda74d679/"
    },
    {
        "name": "The Polish Grid Infrastructure",
        "url": "https://puhuri-core-demo.neic.no/api/customers/c11b0d4e95144bd5964a09a294d30196/"
    },
    {
        "name": "UNINETT Sigma2 AS",
        "url": "https://puhuri-core-demo.neic.no/api/customers/918594bae69449bb8d011a4c5987515d/"
    },
    {
        "name": "VLAAMS SUPERCOMPUTER CENTRUM",
        "url": "https://puhuri-core-demo.neic.no/api/customers/b5fd863c7159484b8b9009aac1833cd3/"
    }
]
```

## Create a new project

```bash
$ http --pretty=format -v POST https://puhuri-core-demo.neic.no/api/projects/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" customer=https://puhuri-core-demo.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/ name="Project name" description="Project description" backend_id="My unique string"
POST /api/projects/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Content-Length: 192
Content-Type: application/json
Host: puhuri-core-demo.neic.no
User-Agent: HTTPie/2.4.0

{
    "backend_id": "My unique string",
    "customer": "https://puhuri-core-demo.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
    "description": "Project description",
    "name": "Project name"
}

HTTP/1.1 201 Created
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, POST, HEAD, OPTIONS
Content-Language: en
Content-Length: 604
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 09:40:52 GMT
Location: https://puhuri-core-demo.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "backend_id": "My unique string",
    "billing_price_estimate": {
        "current": 0,
        "tax": 0,
        "tax_current": 0,
        "total": 0.0
    },
    "created": "2021-04-09T09:40:51.832870Z",
    "customer": "https://puhuri-core-demo.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
    "customer_abbreviation": "DeiC",
    "customer_name": "Danish e-Infrastructure Cooperation",
    "customer_native_name": "",
    "customer_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
    "description": "Project description",
    "name": "Project name",
    "type": null,
    "url": "https://puhuri-core-demo.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "uuid": "4475ac77fa3a491aacb3fb3a6dfadadf"
}
```

## Update an existing project

```bash
$ http --pretty=format -v PUT https://puhuri-core-demo.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" name="New project name" customer=https://puhuri-core-demo.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/
PUT /api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811
Connection: keep-alive
Content-Length: 124
Content-Type: application/json
Host: puhuri-core-demo.neic.no
User-Agent: HTTPie/2.4.0

{
    "customer": "https://puhuri-core-demo.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
    "name": "New project name"
}

HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Language: en
Content-Length: 608
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 09:45:16 GMT
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "backend_id": "My unique string",
    "billing_price_estimate": {
        "current": 0,
        "tax": 0,
        "tax_current": 0,
        "total": 0.0
    },
    "created": "2021-04-09T09:40:51.832870Z",
    "customer": "https://puhuri-core-demo.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
    "customer_abbreviation": "DeiC",
    "customer_name": "Danish e-Infrastructure Cooperation",
    "customer_native_name": "",
    "customer_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
    "description": "Project description",
    "name": "New project name",
    "type": null,
    "url": "https://puhuri-core-demo.neic.no/api/projects/4475ac77fa3a491aacb3fb3a6dfadadf/",
    "uuid": "4475ac77fa3a491aacb3fb3a6dfadadf"
}
```


## List projects
```bash
$ http --pretty=format -v https://puhuri-core-demo.neic.no/api/projects/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811"
GET /api/projects/ HTTP/1.1
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
Content-Length: 7129
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 09:46:41 GMT
Link: <https://puhuri-core-demo.neic.no/api/projects/>; rel="first", <https://puhuri-core-demo.neic.no/api/projects/?page=2>; rel="next", <https://puhuri-core-demo.neic.no/api/projects/?page=2>; rel="last"
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Result-Count: 20
X-XSS-Protection: 1; mode=block

[
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-26T10:57:02.640605Z",
        "customer": "https://puhuri-core-demo.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project description",
        "name": "CSC test project",
        "type": "https://puhuri-core-demo.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-demo.neic.no/api/projects/8cb53568cbed40c584029cb43cc540f6/",
        "uuid": "8cb53568cbed40c584029cb43cc540f6"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T06:06:30.911124Z",
        "customer": "https://puhuri-core-demo.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 10 description",
        "name": "CSC test project 10",
        "type": "https://puhuri-core-demo.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-demo.neic.no/api/projects/a6241bd8342c4fb4b8ea9507ea03d658/",
        "uuid": "a6241bd8342c4fb4b8ea9507ea03d658"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T06:06:43.645113Z",
        "customer": "https://puhuri-core-demo.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 11 description",
        "name": "CSC test project 11",
        "type": "https://puhuri-core-demo.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-demo.neic.no/api/projects/d21ccbb0033f49fa928dc6bcc739cd8e/",
        "uuid": "d21ccbb0033f49fa928dc6bcc739cd8e"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T06:07:03.472114Z",
        "customer": "https://puhuri-core-demo.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 12 description",
        "name": "CSC test project 12",
        "type": "https://puhuri-core-demo.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-demo.neic.no/api/projects/09119652d1f24a068ec8a6d29da1016a/",
        "uuid": "09119652d1f24a068ec8a6d29da1016a"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T06:07:22.023662Z",
        "customer": "https://puhuri-core-demo.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 13 description",
        "name": "CSC test project 13",
        "type": "https://puhuri-core-demo.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-demo.neic.no/api/projects/adf45385e57749c4b636d09b127039ea/",
        "uuid": "adf45385e57749c4b636d09b127039ea"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T06:07:37.658803Z",
        "customer": "https://puhuri-core-demo.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 14 description",
        "name": "CSC test project 14",
        "type": "https://puhuri-core-demo.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-demo.neic.no/api/projects/4b3ff8e4dfe84c8ab83834715c757e47/",
        "uuid": "4b3ff8e4dfe84c8ab83834715c757e47"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T06:07:52.235226Z",
        "customer": "https://puhuri-core-demo.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 15 description",
        "name": "CSC test project 15",
        "type": "https://puhuri-core-demo.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-demo.neic.no/api/projects/19cb4c0825ec4333adcdf3fce9382fac/",
        "uuid": "19cb4c0825ec4333adcdf3fce9382fac"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T05:44:25.730256Z",
        "customer": "https://puhuri-core-demo.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 2 description",
        "name": "CSC test project 2",
        "type": "https://puhuri-core-demo.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-demo.neic.no/api/projects/62808e67ca734d6c9710f7d1dd35a299/",
        "uuid": "62808e67ca734d6c9710f7d1dd35a299"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T05:44:50.921959Z",
        "customer": "https://puhuri-core-demo.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 3 description",
        "name": "CSC test project 3",
        "type": "https://puhuri-core-demo.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-demo.neic.no/api/projects/03a57d26bc5c448f96ccaf6e1ce2a91d/",
        "uuid": "03a57d26bc5c448f96ccaf6e1ce2a91d"
    },
    {
        "backend_id": "",
        "billing_price_estimate": {
            "current": 0,
            "tax": 0,
            "tax_current": 0,
            "total": 0.0
        },
        "created": "2021-03-30T05:45:07.739197Z",
        "customer": "https://puhuri-core-demo.neic.no/api/customers/29f29e6b65004bff9e831dec7c953177/",
        "customer_abbreviation": "CSC",
        "customer_name": "IT CENTER FOR SCIENCE LTD",
        "customer_native_name": "",
        "customer_uuid": "29f29e6b65004bff9e831dec7c953177",
        "description": "CSC test project 4 description",
        "name": "CSC test project 4",
        "type": "https://puhuri-core-demo.neic.no/api/project-types/c588e4bc82fa4cf0b97e545e117c4c21/",
        "type_name": "Name of project type",
        "url": "https://puhuri-core-demo.neic.no/api/projects/ed75f213306740588854ea3e973c7fb5/",
        "uuid": "ed75f213306740588854ea3e973c7fb5"
    }
]
```

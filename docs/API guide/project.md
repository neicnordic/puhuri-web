
## Lookup allocator customers available to a user

In most cases integration user can see only one allocating organization (or Puhuri Core "customer"), however it is
possible that the same account is used for allocating different shares, e.g. national share and community specific.
Projects are always created in the context of a specific customer, so as a first thing you need to lookup a specific
customer you want to use. Customer is a stable entity, so it's URL / UUID can be cached. 

{generate_customer_list}

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
Date: Wed, 07 Apr 2021 06:27:59 GMT
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

{generate_project_creation}

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
Content-Length: 4580
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Wed, 07 Apr 2021 06:28:00 GMT
Location: https://puhuri-core-demo.neic.no/api/projects/3c867e0b9c7f41cbb3fc666c5406b7ff/
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
    "created": "2021-04-07T06:28:00.565610Z",
    "customer": "https://puhuri-core-demo.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
    "customer_abbreviation": "DeiC",
    "customer_name": "Danish e-Infrastructure Cooperation",
    "customer_native_name": "",
    "customer_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
    "description": "Project description",
    "name": "Project name",
    "type": null,
    "url": "https://puhuri-core-demo.neic.no/api/projects/3c867e0b9c7f41cbb3fc666c5406b7ff/",
    "uuid": "3c867e0b9c7f41cbb3fc666c5406b7ff"
}
```
    

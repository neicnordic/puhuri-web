# Resource allocation management

## Getting a list of offerings
User can fetch offerings and filter them by the following fields:

- `name` - offering's name
- `name_exact` - offering's exact name
- `customer` - organization's URL
- `customer_uuid` - organization's UUID
- `allowed_customer_uuid` - allowed organization's UUID
- `service_manager_uuid` - service manager's UUID
- `attributes` - a set of attributes (key-value pairs)
- `state` - offering's state (`Active`, `Draft`, `Paused`, `Archived`), should be `Active`
- `category_uuid` - category's UUID
- `billable` - signalizing if an offering is billable or not, should be `true`
- `shared` - signalizing if an offering is public or not, should be `true`
- `type` - offering's type

```bash
$ http --pretty=format -v https://puhuri-core-demo.neic.no/api/marketplace-offerings/ Authorization:"Token 787de6b7c581ab6d9d42fe9ec12ac9f1811c5811" state==Active shared==true
GET /api/marketplace-offerings/?state=Active&shared=true HTTP/1.1
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
Content-Length: 4779
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Fri, 09 Apr 2021 12:49:06 GMT
Link: <https://puhuri-core-demo.neic.no/api/marketplace-offerings/?shared=true&state=Active>; rel="first", <https://puhuri-core-demo.neic.no/api/marketplace-offerings/?shared=true&state=Active>; rel="last"
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-Result-Count: 1
X-XSS-Protection: 1; mode=block

[
    {
        "attributes": {},
        "backend_id": "",
        "billable": true,
        "category": "https://puhuri-core-demo.neic.no/api/marketplace-categories/5b61d0811cfe4ed6a004119795a4c532/",
        "category_title": "HPC",
        "category_uuid": "5b61d0811cfe4ed6a004119795a4c532",
        "citation_count": -1,
        "components": [
            {
                "article_code": "",
                "billing_type": "usage",
                "default_limit": null,
                "description": "",
                "disable_quotas": false,
                "factor": null,
                "is_boolean": false,
                "limit_amount": null,
                "limit_period": null,
                "max_value": null,
                "measured_unit": "CPU kH",
                "min_value": null,
                "name": "CPU allocation",
                "type": "cpu_k_hours",
                "use_limit_for_billing": false
            },
            {
                "article_code": "",
                "billing_type": "usage",
                "default_limit": null,
                "description": "",
                "disable_quotas": false,
                "factor": null,
                "is_boolean": false,
                "limit_amount": null,
                "limit_period": null,
                "max_value": null,
                "measured_unit": "CPU kH",
                "min_value": null,
                "name": "GPU allocation",
                "type": "gpu_k_hours",
                "use_limit_for_billing": false
            },
            {
                "article_code": "",
                "billing_type": "usage",
                "default_limit": null,
                "description": "",
                "disable_quotas": false,
                "factor": null,
                "is_boolean": false,
                "limit_amount": null,
                "limit_period": null,
                "max_value": null,
                "measured_unit": "GB kH",
                "min_value": null,
                "name": "Storage allocation",
                "type": "gb_k_hours",
                "use_limit_for_billing": false
            }
        ],
        "created": "2021-03-09T10:27:47.170024Z",
        "customer": "https://puhuri-core-demo.neic.no/api/customers/d42a18b6b8ba4c2bb0591b3ff8fb181d/",
        "customer_name": "Danish e-Infrastructure Cooperation",
        "customer_uuid": "d42a18b6b8ba4c2bb0591b3ff8fb181d",
        "datacite_doi": "",
        "description": "LUMI share of Denmark",
        "files": [],
        "full_description": "<h2>Overview</h2>One of the most powerful supercomputers in the world, LUMI, will start its operations in CSC’s data center in Kajaani, Finland, next year. The peak performance of LUMI is an astonishing 552 petaflop/s. To date, the world’s fastest computer, Fugaku in Japan, reaches peak performance of 513 petaflop/s. When LUMI’s operations start next year, it will be one of the world’s fastest supercomputers",
        "google_calendar_is_public": null,
        "latitude": 64.2310486,
        "longitude": 27.7040942,
        "name": "LUMI Denmark",
        "native_description": "",
        "native_name": "",
        "options": {
            "options": {
                "nationality": {
                    "help_text": "Due to potential limitations of access to HPC systems and software, please provide nationalities of expected users",
                    "label": "Nationalities of users",
                    "required": true,
                    "type": "string"
                },
                "oecd_science_domain_configuration": {
                    "choices": [
                        "1.1 Mathematics",
                        "1.2 Computer and information sciences",
                        "1.3 Physical sciences",
                        "1.4 Chemical sciences",
                        "1.5 Earth and related environmental sciences",
                        "1.6 Biological sciences",
                        "1.7 Other natural sciences",
                        "2.1 Civil engineering",
                        "2.2 Electrical engineering, electronic engineering, information engineering",
                        "2.3 Mechanical engineering",
                        "2.4 Chemical engineering",
                        "2.5 Materials engineering",
                        "2.6 Medical engineering",
                        "2.7 Environmental engineering",
                        "2.8 Environmental biotechnology",
                        "2.9 Industrial Biotechnology",
                        "2.10 Nano-technology",
                        "2.11 Other engineering and technologies",
                        "3.1 Basic medicine",
                        "3.2 Clinical medicine",
                        "3.3 Health sciences",
                        "3.4 Health biotechnology",
                        "3.5 Other medical sciences",
                        "4.1 Agriculture, forestry, and fisheries",
                        "4.2 Animal and dairy science",
                        "4.3 Veterinary science",
                        "4.4 Agricultural biotechnology",
                        "4.5 Other agricultural sciences",
                        "5.1 Psychology",
                        "5.2 Economics and business",
                        "5.3 Educational sciences",
                        "5.3 Sociology",
                        "5.5 Law",
                        "5.6 Political Science",
                        "5.7 Social and economic geography",
                        "5.8 Media and communications",
                        "5.7 Other social sciences",
                        "6.1 History and archaeology",
                        "6.2 Languages and literature",
                        "6.3 Philosophy, ethics and religion",
                        "6.4 Art (arts, history of arts, performing arts, music)",
                        "6.5 Other humanities"
                    ],
                    "help_text": "Please select your intended science domain in (OECD 2007 classification)",
                    "label": "Science Domain",
                    "required": true,
                    "type": "select_string"
                }
            },
            "order": [
                "oecd_science_domain_configuration",
                "nationality"
            ]
        },
        "order_item_count": 1.0,
        "paused_reason": "",
        "plans": [
            {
                "archived": false,
                "article_code": "",
                "description": "Default plan for all LUMI",
                "init_price": 0,
                "is_active": true,
                "max_amount": null,
                "name": "LUMI Common",
                "prices": {
                    "cpu_k_hours": 0.1,
                    "gb_k_hours": 0.001,
                    "gpu_k_hours": 0.5
                },
                "quotas": {
                    "cpu_k_hours": 0,
                    "gb_k_hours": 0,
                    "gpu_k_hours": 0
                },
                "switch_price": 0,
                "unit": "month",
                "unit_price": "0.0000000",
                "url": "https://puhuri-core-demo.neic.no/api/marketplace-plans/c0fb33c79e9b48f69fcb6da26db5a28b/",
                "uuid": "c0fb33c79e9b48f69fcb6da26db5a28b"
            }
        ],
        "plugin_options": {
            "auto_approve_in_service_provider_projects": true
        },
        "quotas": null,
        "rating": 5,
        "scope": null,
        "screenshots": [],
        "secret_options": {},
        "shared": true,
        "state": "Active",
        "terms_of_service": "",
        "thumbnail": null,
        "type": "Marketplace.Basic",
        "url": "https://puhuri-core-demo.neic.no/api/marketplace-offerings/073a0ddd6eba4ff4a90b943ae3e1b7c9/",
        "uuid": "073a0ddd6eba4ff4a90b943ae3e1b7c9",
        "vendor_details": ""
    }
]
```

## Creation of a resource allocation
<!-- {generate_resource_creation} -->

## Modification of a resource allocation
<!-- {generate_resource_modification} -->

## Termination of a resource allocation
<!-- {generate_resource_termination} -->

# Authentication

Puhuri Core exposes REST API for all of its operations. Below are examples of typical operations performed against APIs.
To run the examples, we are using a [HTTPie](https://httpie.org/).

Almost all of the operations with API require an authentication token. Below we list two methods on how to get it.

## Authentication with username/password
If your account is allowed to use username/password and the method is enabled (e.g. in dev environment), you can get a new token by submitting a username/password as JSON to a specific endpoint.


```bash
$ http -v POST https://puhuri-core.neic.no/api-auth/password/ username=user password=password

POST /api-auth/password/ HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 52
Content-Type: application/json
Host: puhuri-core.neic.no
User-Agent: HTTPie/2.3.0

{
    "password": "user",
    "username": "password"
}

HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Accept, Accept-Encoding, Authorization, Content-Type, Origin, User-Agent, X-CSRFToken, X-Requested-With
Access-Control-Allow-Methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
Access-Control-Allow-Origin: *
Access-Control-Expose-Headers: Link, X-Result-Count
Allow: POST, OPTIONS
Content-Language: en
Content-Length: 52
Content-Security-Policy: report-uri csp.hpc.ut.ee; form-action 'self';
Content-Type: application/json
Date: Mon, 05 Apr 2021 14:37:55 GMT
Referrer-Policy: no-referrer-when-downgrade
Strict-Transport-Security: max-age=31536000; preload
Vary: Accept-Language, Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block

{
    "token": "65b4c4f5e25f0cadb3e11c181be4ffa3881741f8"
}
```

## Authentication Token management

You are also able to get token from the Puhuri Core web interface. Go to user workspace by selecting 'Manage' in the
user drop-down.

![side-bar](../assets/side-bar.png){: style="height:288px;width:220px"}

Scroll down to the Current API token field and click on the 'eye' icon to display the token.

![api-token](../assets/api-token.png)

# Authentication

Puhuri Core exposes REST API for all of its operations. Below are examples of typical operations performed against APIs.
To run the examples, we are using a [HTTPie](https://httpie.org/).

Almost all of the operations with API require an authentication token. Below we list two methods on how to get it.

## Authentication with username/password
If your account is allowed to use username/password and the method is enabled (e.g. in dev environment), you can get a new token by submitting a username/password as JSON to a specific endpoint.

{generate_username_password_authentication}

## Authentication Token management

You are also able to get token from the Puhuri Core web interface. Go to user workspace by selecting 'Manage' in the
user drop-down.

![side-bar](../assets/side-bar.png){: style="height:288px;width:220px"}

Scroll down to the Current API token field and click on the 'eye' icon to display the token.

![api-token](../assets/api-token.png)

# Integration with KeyCloak

## Background

[KeyCloak](https://www.keycloak.org/) is a popular open-source identity and access management 
server. It supports integration with external identity federations over SAML and OIDC protocols.

KeyCloak can be used as a local identity proxy enriching MyAccessID identities with local
information or applying local policies.

## Overview

1. [Register](https://webapp.prod.puhuri.eduteams.org/sp_request) your KeyCloak instance with Puhuri AAI proxy as an OIDC client.

2. Setup KeyCloak identity provider corresponding to MyAccessID.

## Configuration of Keycloak

1. Open KeyCloak realm where you want to add MyAccessID and go to Identity providers.

2. Click add new provider and select OpenID Connect v1.0

## Configure provider

- Alias: myaccessid (or pick a better name)
- Discovery endpoint: *https://proxy.prod.puhuri.eduteams.org/.well-known/openid-configuration*
- Client authentication: Client secret sent as post
- Client ID: OIDC client ID you got from registration in Puhuri AAI.
- Client Secret: OIDC client secret you got from registration in Puhuri AAI

## Save and edit additional properties:

- Validate signatures: On
- Use JWKS URL: On
- Trust email: On
- Sync mode: Force
- Under advanced settings, add Scopes: `openid profile email voperson_external_affiliation voperson_id given_name`

## Got to Mappers tab and click on Add mapper:

- Name: free name, e.g. cuid
- Sync mode override: Import
- Mapper type: Username Template Importer
- Template: ${CLAIM.sub}
- Target: Local

Save. **Profit!**


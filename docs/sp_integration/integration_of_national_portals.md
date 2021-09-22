# Integration of National Portals

## Introduction

National Portals are handling allocation of computing resources via national processes. Po maintains a local database of users, their roles in the approved projects and the resource allocations of the projects. 

When the project and resource allocation of LUMI resources is approved, the project with one or more users and their roles within the project needs to be shared with Puhuri Core database. Puhuri Core and National Portal must share the same user identifier, and this is MyAccessID User Identifier.
 
 ## Overview
 
To integrate your National Portal with Puhuri, several steps ARE needed: 
- Record MyAccessID User Identifier within the user profile in the National Portal. This entails: 
  -  **Registration of National Portal with Puhuri AAI proxy** as an OIDC client
  - **Implementation of user flow where National Portal UI asks user to link MyAccessID Identity** (and gets the MyAccessID User Identifier to store in your National Portal)
  - **Implement OIDC flow that enables sharing of MyAccessID User Identifier between MyAccessID and your National Portal**
  - Record the MyAccessID User Identifier within the user profile of user at your National Portal 
- **Push the allocation and project membership information to Puhuri Core**

Some of these are described in the following. 

## Registration of National Portal with Puhuri AAI proxy 

The process is described at .... add link to the other doc. National Portal needs to be connected as an OIDC Client, so please use that option when you are registering National Portal at Puhuri AAI proxy. 

The client library that you use should be able to detect all the setting just by passing the issuer URL (https://webapp.prod.puhuri.eduteams.org or https://webapp.acc.puhuri.eduteams.org) and getting the information from the discovery endpoint. If this is not the case, then you can find the information directly from the discovery endpoint of the OIDC Provider:

- https://proxy.prod.puhuri.eduteams.org/.well-known/openid-configuration (for production)
- https://proxy.prod.puhuri.eduteams.org/.well-known/openid-configuration (for acceptance environment)

## Implementation of user flow and UI that asks user to link MyAccessID Identity

In order to support the account linking at your National Portal, you will need to add a few changes to the UI. When a user becomes part of the project that uses allocations on LUMI, you will need to prompt your user to perform the MyAccessID account linking. That can be done at once if the user themselves are taking the action. In other situations, like when a Principal Investigator (PI) adds a project member on their initiative, an email may have to be sent to the user about MyAccessID linking.

For example implementation of the UI, you can refer to the implementation at Swedish National Portal SUPR. 

... Marina to add ScreenShoots

## Implement OIDC flow that enables sharing of MyAccessID User Identifier between MyAccessID and your National Portal

This is the OIDC technical implementation that supports the user flow discussed above.

You will need to install and use an OIDC client/library at the National Portal. 

The `mod_auth_openidc`Apache module can be used. Otherwise, other suitable software that implements the RP part of OIDC can be used. 

We can provide an **example** mod_auth_openidc configuration:

```
OIDCProviderMetadataURL https://proxy.acc.puhuri.eduteams.org/.well-known/openid-configuration
OIDCClientID NOT-SHOWN-HERE
OIDCClientSecret SECRET-NOT-SHOWN-HERE
OIDCRedirectURI https://portal.example.org/puhuri/register-redirect/
OIDCCryptoPassphrase SECRET-NOT-SHOWN-HERE
OIDCScope "openid email profile eduperson_entitlement"

<LocationMatch "^/(person/register_myaccessid|puhuri/.*)/$">
   AuthType openid-connect
   Require valid-user
</LocationMatch>
```

In the example above, the portal page implementing account linking (having `mod_auth_oidc` send the user to MyAccessID and getting the claims back in environment variables if successful) is at `/person/registermyaccessid`, while URLs under `/puhuri` are for use by `mod_auth_openidc` itself.



## Push of the allocation and project membership information to Puhuri Core

The API used between the National Portal and Puhuri Core is documented at https://puhuri.neic.no/resource-allocators/

When the National Portal pushes the information about project membership (also who is PI) to Puhuri Core, it will first do an API call (`/api/remote-eduteams/`) to map the user’s MyAccessID identifier to a Puhuri Core internal UUID, and then use that UUID in subsequent API calls. You may want to store that UUID for the user in the National Portal too, in order to not have to do the mapping every time.







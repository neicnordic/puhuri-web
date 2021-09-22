# Integration of National Portals

## Background

National portals are handling allocation of computing resources via national processes. It maintains a local database
of users, their roles in the approved projects and the resource allocations of the projects. This article describes
actions that a National portal operator needs to do to integrate allocation of LUMI resources via Puhuri Core.

When the project and resource allocation of LUMI resources is approved inside the National portal, the project with
one or more users and their roles within the project needs to be pushed to Puhuri Core service. When users references are
shared from National portal to Puhuri Core, a common identity must be used and that identity is MyAccessID User.
 
## Overview
 
The following steps are needed to integrate your National Portal with Puhuri:

1. Connect MyAccessID User Identifier with the user profile in the National Portal. This entails:
   1. **Registration of National Portal with Puhuri AAI proxy** as an OIDC client
   2. **Implementation of user flow where National Portal UI asks user to link MyAccessID Identity** (and gets the MyAccessID
      User Identifier to store in your National Portal)
   3. **Implement OIDC flow that enables sharing of MyAccessID User Identifier between MyAccessID and your National Portal**
2. Record the MyAccessID User Identifier within the user profile of user at your National Portal.
3. **Push the allocation and project membership information to Puhuri Core**.

Some of these are described in the following.

## Registration of National Portal with Puhuri AAI proxy

The process is described at ...TODO: add link to the other doc... National Portal needs to be connected as an
OIDC Client, so please use that option when you are registering National Portal at Puhuri AAI proxy. 

The client library that you use should be able to detect all the setting just by passing the issuer URL
(https://webapp.prod.puhuri.eduteams.org or https://webapp.acc.puhuri.eduteams.org) and getting the information from
the discovery endpoint. If this is not the case, then you can find the information directly from the discovery
endpoint of the OIDC Provider:

- [https://proxy.prod.puhuri.eduteams.org/.well-known/openid-configuration](https://proxy.prod.puhuri.eduteams.org/.well-known/openid-configuration) (for production)
- [https://proxy.acc.puhuri.eduteams.org/.well-known/openid-configuration](https://proxy.acc.puhuri.eduteams.org/.well-known/openid-configuration) (for acceptance environment)

## Implementation of user flow and UI that asks user to link MyAccessID Identity

In order to support the account linking at your National Portal, you will need to add a few changes to the UI. When
a user becomes part of the project that uses allocations on LUMI, you will need to prompt your user to perform the
MyAccessID account linking. That can be done at once if the user themselves are taking the action. In other situations,
like when a Principal Investigator (PI) adds a project member on their initiative, an email may have to be sent to the
user about MyAccessID linking.

For example implementation of the UI, you can refer to the implementation at Swedish National Portal SUPR. 

...TODO: add ScreenShoots .. 

## Implement OIDC flow that enables sharing of MyAccessID User Identifier between MyAccessID and your National Portal

This is the OIDC technical implementation that supports the user flow discussed above.

You will need to install and use an OIDC client/library at the National Portal. 

The `mod_auth_openidc` Apache module can be used. Otherwise, other suitable software that implements the RP part of OIDC can be used. 

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

In the example above, the portal page implementing account linking (having `mod_auth_oidc` send the user to MyAccessID
and getting the claims back in environment variables if successful) is at `/person/registermyaccessid`, while URLs
under `/puhuri` are for use by `mod_auth_openidc` itself.

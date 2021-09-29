## Overview



## Puhuri Components
![Components](assets/puhuri-components.png)
In the image is high level architecture of Puhuri. User either uses a National portal or an instance of a Puhuri Portal for the Project Application and the Project membership management. The User is using MyAccessID to register Puhuri User Account and to login (authenticate) to the Resources. The Registration creates a unique identifier (Community Unique Identifier, CUID) for the User, which is used for referencing and linking user identity across the different components. 

The identity provider releases the attributes about User’s identity and affiliation, which is important for the resource providers to know. F  User can also provide additional information such as SSH public keys and to define other email address than what was returned from the Idp. That email will be verified. 

Puhuri Core is the database storing Projects and their Members as well as Allocation, Accounting and related Resource information. A Resource provider (in Figure 1 LUMI) uses APIs to import the active allocation and project membership information from the Puhuri Core. 

The Resources receive User related information via Puhuri AAI from User’s Identity provider (IdP), when a User authenticates using home organisation’s credentials. 

## Puhuri roles
![Roles](assets/puhuri-roles.png)
User applies for a Resource Allocation and then manage the Members of the Project using a Puhuri Portal, hosted by University of Tartu, or via a National Portal, depending which solution is available for User.

The Resource application review process happens outside of Puhuri. The national portals are expected to push approved projects and resources  to Puhuri Core. The Principal Investigator (PI) creates project in the Puhuri Portal or National Portal. The submission is then accepted by the Resource Allocator, which is responsible for the particular application’s resource granting. Then the project information is propagated to Puhuri Core and from there synchronised to the Resource Provider. In addition to Project description and members, also the Resource-specific resource allocation attributes are included. 

A national portal may implement identity linking of local accounts with Puhuri AAI account. The recommended way for that is to use OIDC registration flow, which can be triggered from the national portal  and lead to  redirection back with a created Puhuri User CUID

## Puhuri model
![Model](assets/puhuri-model.png)
Information model of Puhuri. Please note that the terminology used in this documentation differs occasionally of this planned information model. 

# Requirements for IdPs integrated directly

*If the IdP is connected to one of the R&E Federations but is not published in eduGAIN, then please advise the IdP operator to request their IdP to be published to the eduGAIN metadata.*

IdPs that are not connected to an R&E federation, need to be in one of the eligible categories in order to be integrated on MyAccessID:

- Recognised community platforms that require access to resources using MyAccessID;
- High Performance Computing facilities which operate their Identity Management Systems.

If the IdP you wish to integrate is not connected to an R&E Federation and does not fit in any of the above categories, please contact us.

## Supported Protocols

The IdP MUST support one of the following protocols:

- OIDC
- SAML2

## Attribute release requirements

IdPs must release the following attributes for users to successfully complete registration and use MyAccessID and consequently PUHURI:

- **Email** 
- **Name**, that can be sent as :
  - **Common Name** or 
  - **Display Name** or
  - **Given Name** and **Family Name**
- **Identifier**, that can be sent as: 
  - **subject-id** or
  - **pairwise-id** or
  - **persistent name-id** or

IdPs are required to release also the following attributes for users to successfully use services connected to PUHURI:

- **Affiliation**
- **Home Organization**
- **Assurance**  - attribute will become mandatory in 2022 (date TBD)
- **Community Identifier**

Please refer to [Attribute formats](https://puhuri.neic.no/idp_integration/attributes) for specification of accepted attribute formats.

## Level of Assurance requirements

Access to services connected to PUHURI is allowed only with use of identities that fulfil certain identity assurance criteria. To express the required assurance levels, the REFEDS Assurance suite https://wiki.refeds.org/display/ASS is used. 

Requirements are defined for two aspects of identity assurance: 

- Identifier uniqueness to ensure unambiguous identification of users
- Identity proofing and credential issuance, renewal, and replacement to ensure that identity trustworthy represents right natural person 

Level of assurance for an identity issued to a user is expressed at the time of user authentication by the IdP sending eduPersonAssurance attribute with following values:

- https://refeds.org/assurance/ID/UNIQUE; or https://refeds.org/assurance/ID/eppn-unique-no-reassign, and
- https://refeds.org/assurance/IAP/medium or https://refeds.org/assurance/IAP/high

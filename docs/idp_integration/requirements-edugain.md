# Requirements for IdPs integrated through eduGAIN

In order for IdPs available in eduGAIN to be successfully integrated with MyAccessID and PUHURI, they must fulfil requirements described in this page.

## Supported Protocols

IdPs from eduGAIN MUST use the SAML2 protocol. 

## Attribute release requirements

IdPs MUST release the following attributes for user to successfully complete registration and use MyAccessID:

- **Email** 
- **Name**, that can be sent as :
  - **Common Name**,or 
  - **Display Name**, or
  - **Given Name** and **Family Name**
- **Identifier**, that can be sent as: 
  - **subject-id**, or
  - **pairwise-id**, or
  - **persistent name-id**, or
  - **eduPersonPrincipalName***, or
  - **eduPersonTargetedID**
  
IdPs are required to release also the following attributes for users to successfully use services connected to PUHURI: 

- **Affiliation** 
- **Home Organization**
- **Assurance** - attribute will become mandatory in 2023 (date TBD) 

Please refer to [Attribute formats](https://puhuri.neic.no/idp_integration/attributes)  for specification of accepted attribute formats. 

*_Note: In the case the IdP release only eduPersonPrincipalName as the user's identifier, then the IdP MUST either publish the R&S Entity Category in its metadata or release the eduPersonAssurance attribute with value of https://refeds.org/assurance/ID/eppn-unique-no-reassign or the federation in which the IdP has registered has a policy that prohibits the reassignment of the value of the eduPersonPrincipalName attribute._

## Level of Assurance requirements

Access to services connected to PUHURI is allowed only with use of identities that fulfil certain identity assurance criteria. To express the required assurance levels, the [REFEDS Assurance suite](https://wiki.refeds.org/display/ASS) is used. 

Requirements are defined for two aspects of identity assurance: 

- Identifier uniqueness to ensure unambiguous identification of users;
- Identity proofing and credential issuance, renewal, and replacement to ensure that identity trustworthy represents
  right natural person.

Level of assurance for an identity issued to a user is expressed at the time of user authentication by the IdP sending eduPersonAssurance attribute with following values: 

- **https://refeds.org/assurance/ID/UNIQUE** or **https://refeds.org/assurance/ID/eppn-unique-no-reassign** and
- **https://refeds.org/assurance/IAP/medium** or **https://refeds.org/assurance/IAP/high**

## Entity categories

IdPs are expected to support the following entity categories:

- [REFEDS R&S](https://refeds.org/category/research-and-scholarship) and
- [GEANT CoCo](https://wiki.refeds.org/display/CODE/Data+Protection+Code+of+Conduct+Home) 


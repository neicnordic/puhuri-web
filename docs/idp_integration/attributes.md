# Attributes

Depending on which protocol the IdP is using, SAML or OIDC, attributes need to be released in the following format, respectively. 

## SAML Attribute Names 

SAML Attributes MUST be sent using *urn:oasis:names:tc:SAML:2.0:attrname-format:uri* NameFormat. Below is the list of the canonical names of the SAML attributes:

- Subject ID
    - SAML attribute: *urn:oasis:names:tc:SAML:attribute:subject-id*
- Pairwise ID
    - SAML attribute: *urn:oasis:names:tc:SAML:attribute:pairwise-id*
- Community Identifier
    - SAML attribute: *urn:oid:1.3.6.1.4.1.25178.4.1.6 (voPersonID)*
- Email
    - SAML attribute: *urn:oid:0.9.2342.19200300.100.1.3 (email)*
- Common Name
    - SAML attribute: *urn:oid:2.5.4.3*
- Display Name
    - SAML attribute:  *urn:oid:2.16.840.1.113730.3.1.241 (displayName)*
- Given Name
    - SAML attribute: *urn:oid:2.5.4.42 (givenName)*
- Family Name
    - SAML attribute: *urn:oid:2.5.4.4 (surname)*
- Affiliation
    - SAML attribute: *urn:oid:1.3.6.1.4.1.5923.1.1.1.9 (eduPersonScopedAffiliation)*
    - SAML attribute: *urn:oid:1.3.6.1.4.1.25178.4.1.11 (voPersonExternalAffiliation)*
- Home Organization
    - SAML attribute: *urn:oid:1.3.6.1.4.1.25178.1.2.9 (schacHomeOrganization)*
- Assurance
    - SAML attribute: *urn:oid:1.3.6.1.4.1.5923.1.1.1.11 (eduPersonAssurance)*
    - Assurance attribute will become mandatory (date TBD).
    - The following letter was sent to the federations:
  [Assurance letter](../assets/Letter%20for%20Identity%20providers.pdf)


## OIDC Claim Names

- Subject ID
    - OIDC claim: *subject-id*
- Community Identifier
    - OIDC claim: *voperson_id*
- Email
    - OIDC claim: *email*
- Display Name
    - OIDC claim: *name*
- Given Name
    - OIDC claim: *given_name*
- Family Name
    - OIDC claim: *family_name*
- Affiliation
    - OIDC claim: *eduperson_scoped_affiliation*
    - OIDC claim: *voperson_external_affiliation*
- Home Organization
    - OIDC claim: *schac_home_organization*
- Assurance
    - OIDC claim: *eduperson_assurance*
    - Assurance attribute will become mandatory (date TBD).
    - The following letter was sent to the federations:
  [Assurance letter](../assets/Letter%20for%20Identity%20providers.pdf)


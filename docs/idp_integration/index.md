# Integrating Identity Providers with Puhuri AAI

## Overview

Puhuri AAI uses MyAccessID platform as an integration point for all IdPs. MyAccessID is published in eduGAIN as a Service Provider and will consume IdPs available in eduGAIN through the metadata exchange mechanism. MyAccessID can on request integrate IdPs in the case they are not available in eduGAIN.

![Puhuri AAI](../assets/puhuri_aai.png )

## Integration of IdPs

Depending on whether IdP is available in eduGAIN, following possibilities exist:

- **IdPs that are available in eduGAIN** will be automatically integrated. Please refer to
  [Requirements for IdPs integrated through eduGAIN](requirements-edugain.md) for further
  specification on requirements. You can check if your IdP is registered at
  [https://release-check.edugain.org/](https://release-check.edugain.org/).

- **IdPs that are not available in eduGAIN** will be integrated on a request basis. National
  LUMI integration contacts should get in touch with Puhuri to request integration and exchange
  the integration end points. Please refer to [Requirements for directly integrated IdPs](requirements-direct.md)
  for further specification on requirements.


## Questions?

Contact email for additional information: support@puhuri.io

## Technical details

- [Puhuri AAI - Production Environment](https://proxy.prod.puhuri.eduteams.org/.well-known/openid-configuration)
- [Puhuri AAI - Acceptance Environment](https://proxy.acc.puhuri.eduteams.org/.well-known/openid-configuration)
- [MyAccessID AAI - Production Environment](https://proxy.myaccessid.org/.well-known/openid-configuration)
- [MyAccessID AAI - Acceptance Environment](https://proxy.acc.myaccessid.org/.well-known/openid-configuration)
- [GEANT Support](mailto:support+puhuri@eduteams.org)
- [Profile management at MyAccessID - Production Environment](https://mms.myaccessid.org/profile/)
- [Profile management at MyAccessID - Acceptance Environment](https://mms.acc.myaccessid.org/profile/)
- [Demo SP for attribute release check](https://myaccessid.devtest.eduteams.org/)
- [Registration of a new client in Production](https://webapp.prod.puhuri.eduteams.org/sp_request)
- [Registration of a new client in Acceptance](https://webapp.acc.puhuri.eduteams.org/sp_request)


## Puhuri CORE specifics

- [A miniscript for getting refresh token](../assets/get_tokens.sh). Replace client_id / client_secret with actual values.

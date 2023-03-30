# Overview

As a Resource Allocator using Puhuri, you can choose between different ways to handle allocations and users:

- [Custom Portal Integration](resource-allocators.md) for National Portals and similar
- [Dedicated Puhuri Portal](dedicated-puhuri-portal.md)
- [Shared Puhuri Portal](shared-puhuri-portal.md)


## Puhuri portal hosting

- self-host Puhuri Portal (docker-compose or Helm-based);
- request a managed version of Puhuri Portal from University of Tartu.

Please reach out to [support@puhuri.io](mailto:support@puhuri.io) if you are interested in either option and we shall
assist you with setup.

## Customizing managed Puhuri Portal

### Custom languages

In addition to English, Puhuri Portal can be used in additional languages. Currently available options are:

- Czech
- Danish
- Dutch
- Dutch
- Estonian
- French
- Italian
- Lithuanian
- Norwegian
- Spanish

We try to maintain translations, but feedback from domain specialists and native speakers is very welcome.

### Custom DNS
If you want to use a custom domain for your Puhuri Portal, e.g. lumi.myorganization.eu, you need to set the DNS
records to point to the deployment in University of Tartu.

- option a) Add A records to point to ``193.40.36.55`` and ``193.40.36.57``.
- option b) Add CNAME record: ``IN CNAME web.cs.ut.ee``.

### Allowing sending out email under custom domain

Puhuri Portal needs to send out email on different occasions. In order to reduce chance of email being marked as spam,
you need to make sure that the following record is added in the DNS:

`` TXT "v=spf1 mx a:mailhost.ut.ee -all"``

### HTTP(S) certificates

Puhuri Portal exposes services on encrypted endpoints, for HTTPS to validate without issues, its certificate must match
the domain name.

Currently two options are supported:

- Getting certificates using Letsencrypt and http01 validation schema;
- Using custom certificates provided by the organization. Please reach out to support@puhuri.io for details on secure
  transfer of credentials.

## Puhuri AAI

TBA

## Puhuri Core

Puhuri provides several environments for the resource allocators:

- Development https://puhuri-core-dev.neic.no/api/
- Demo: https://puhuri-core-demo.neic.no/api/
- Production: https://puhuri-core.neic.no/api/

### Accounts

Resource allocators are eligible to one or more user accounts.
For production environments, we expect service provider's representative to pass the following data:

- Names, abbreviations, contact email and optionally web sites of each Allocator.
- For each of the allocators, access subnets from where the requests can be made should be provided.
- For each of the allocators, amount and purposes of allocator user accounts -- will be used for generating integration user accounts.
  We suggest to minimize number of such accounts per allocator to avoid potential overlap. All such accounts will have
  equal power. A single account is a valid number.

Please reach out to support@hpc.ut.ee to get one for Demo environment.

## Puhuri Portal

Puhuri provides several environments for the reference client portal aka Puhuri Portal.

You can:

- self-host Puhuri Portal (docker-compose or Helm-based) - please reach out to support@hpc.ut.ee if you are
  interested in instructions;
- request a managed version of Puhuri Portal from University of Tartu. Please reach out to support@hpc.ut.ee in this
  case too.

TODO: Add link to the ToS documents.

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
- Using custom certificates provided by the organization. Please reach out to support@hpc.ut.ee for details on secure
  transfer of credentials.

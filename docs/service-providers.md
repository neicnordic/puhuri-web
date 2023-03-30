# Integration Guide

A Service Provider (SP) can operate over resources as well as manage resource allocations requested by other organizations.

A typical flow of operations is as follows:

1. Organization representing allocation body creates allocation in a certain project. Allocations are created in 'Creating' state.
2. Service provider polls for new allocations and users with access to them, processes them and marks allocations as approved or rejected. Service provider also reports to Puhuri Core local username created for the user accounts as well as local references to allocations.
3. Service provider regularly reports back accounting data as well as can provide status report for allocation (a semi-structured report visible to end-users).

[SDK Guide](SDK guide/allocation-management-sp.md) provides description for resource allocation management methods performed via Python 3 SDK for Puhuri Core.

## Management of Resource Allocators

Service Provider is in charge of managing Resource Allocators for its resources.
Representative of the Service Provider should submit the initial list as well as updates to the support channel
of Puhuri Core operator: [support@puhuri.io](mailto:support@puhuri.io).

The following information must be provided for each Resource Allocator:

1. Name
2. Abbreviation
3. Subnet in CIDR format from where access to Puhuri Core will be done
4. Contact email
5. Contact phone
5. URL of organization

Contact email will be used for establishing a communication channel from operator to allocator for providing
and managing integration accounts. Contact phone will be used for emergencies only. URL of organization is
optional and will be used for better understanding of the background of the allocator.


## LUMI Use-case

TODO: Add interactions between components.

![Positioning](assets/lumi-vs-puhuri.png){ align=right }

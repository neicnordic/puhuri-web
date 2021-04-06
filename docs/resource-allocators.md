# Resource allocators
Allocators are external parties that are entitled to manage projects and resource allocations in Puhuri Core. 
In the scope of Puhuri, resource allocators are typically organizations operating national portals or research communities.

Resource allocator is expected to:

1. Be eligible to share specific resources, e.g. LUMI share.
2. Be aware of the Researcher Access identifiers of the users, aka CUIDs.

## Environments

Puhuri provides several environments for the resource allocators:

- Development https://puhuri-core-dev.neic.no/
- Demo: https://puhuri-core-demo.neic.no/
- Production: https://puhuri-core.neic.no/

## Accounts

Resource allocators are eligible to one or more user accounts. Please reach out to support@hpc.ut.ee to get one for Demo environment.

## Common operations

- [Authentication](API guide/authentication.md)

## Project management

- Creation of a project
    - Name + description. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L13).

## Group management

- Getting a mapping of Puhuri AAI user CUID to Puhuri Core user.
- Allocation of members to a project
    - Puhuri AAI reference + project + project role => permission link
- Removal of members from a project
    - Deletion of a permission link

## Allocation management
- Import of an offering. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/views.py#L84).

- Getting a list of offerings available for allocation
    - List of offerings accessible for a specific allocator. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/views.py#L45).
- Creation of a resource allocation
    - Project + offering (Resource Component) + requested parameters => Resource allocation. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L37).
- Modification of a resource allocation
    - Changing of allocated limits. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L53).
- Termination of a resource allocation
    - Deletion of a resource allocation. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L64).

## Reporting
- Usage collection for each allocation.

# Resource allocators
Allocators are external parties that are entitled to manage projects and resource allocations in Puhuri Core.
In the scope of Puhuri, resource allocators are typically organizations operating national portals or research communities.

Resource allocator is expected to:

1. Be eligible to share specific resources, e.g. LUMI share.
2. Be aware of the Researcher Access identifiers of the users, aka CUIDs.

## Terminology

Puhuri Core is based on [Waldur](https://github.com/waldur/waldur-mastermind/) orchestrator and as such some of the APIs
use a different naming than agreed in Puhuri. Below is a mapping to reduce confusion.


| Puhuri      | API / Waldur    |
| ----------- | --------------- |
| Resource    |  Offering       |
| Resource component | Offering component |
| Allocation  | Resource        |


## Common operations

- [Authentication](API guide/authentication.md)

## Project management

- [Customer lookup](API guide/project.md#lookup-allocator-customers-available-to-a-user)

- [Creation of a project](API guide/project.md#create-a-new-project)
    - selection of the allocator's organization aka Puhuri Core customer
    - uniqueness expectations
        - active projects per allocator
    - Name + description + backend_id. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L13).

- [Update of a project](API guide/project.md#update-an-existing-project)
    - Name + description. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L13).

- [Listing and filtering of projects](API guide/project.md#list-projects-with-pissible-fintering)
    - by name
    - by backend_id

## Project membership management
**NB**: Project permissions can be viewed and modified only by customer owners and staff users.

- [Getting a mapping of Puhuri AAI user CUID to Puhuri Core user](API guide/project-permissions.md#getting-a-mapping-of-AAI-user-to-Core-user)
    - explain why is needed
    - explain what exceptions can happen
- [Allocation of members to a project](API guide/project-permissions.md#project-members-permissions-allocation)
    - Puhuri AAI reference + project + project role => permission link
- [Removal of members from a project](API guide/project-permissions.md#removal-of-members-from-a-project)
    - Deletion of a permission link

## Resource allocation management

- [Getting a list of offerings available for allocation](API guide/resource-allocation-management.md#getting-a-list-of-offerings)
    - List of offerings accessible for a specific allocator. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/views.py#L45).
- [Creation of a resource allocation](API guide/resource-allocation-management.md#creation-of-a-resource-allocation)
    - Project + offering (Resource Component) + requested parameters => Resource allocation. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L37).
- [Modification of a resource allocation](API guide/resource-allocation-management.md#modification-of-a-resource-allocation)
    - Changing of allocated limits. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L53).
- [Termination of a resource allocation](API guide/resource-allocation-management.md#termination-of-a-resource-allocation)
    - Deletion of a resource allocation. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L64).

### Advanced
Information about Puhuri resources in Puhuri Core can change over time, for example, new components could be added.
Puhuri Portal implements a method for dynamic import and upkeep of that information from Puhuri Core.

As this is a more advanced topic, please check [implementation](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/views.py#L84).
If you have questions, we will be happy to help out! Please reach out to support@hpc.ut.ee.


## Reporting
- Usage collection for each allocation.

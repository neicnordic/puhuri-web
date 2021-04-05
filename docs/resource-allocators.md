# Resource allocators
Allocator is, for example, a national portal-related actor who is entitled to manage projects with Puhuri Core. Puhuri Core stores each Allocator-related data under an Organisation.

## Common operations
- Authentication
    - Getting authentication token

## Allocator operations
- Creation of a project
    - Name + description. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L13).
- Allocation of members to a project
    - Puhuri AAI reference + project + project role => permission link
- Removal of members from a project
    - Deletion of a permission link
- Getting a list of offerings available for allocation
    - List of offerings accessible for a specific allocator. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/views.py#L45).
- Creation of a resource allocation
    - Project + offering (Resource Component) + requested parameters => Resource allocation. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L37).
- Modification of a resource allocation
    - Changing of allocated limits. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L53).
- Termination of a resource allocation
    - Deletion of a resource allocation. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L64).
- Usage collection for each allocation.
- Import of an offering. Implementation: [link](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/views.py#L84).

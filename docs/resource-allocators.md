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

Almost all operations require authentication. Authentication process is a two-step:
1. Generation of authentication token using [Authentication API](API guide/authentication.md).
2. Passing that token in Authorization header along with all other REST API calls.

Please note that all of the responses to the listing are paginated, by default up to 10 elements are returned.
You can request more by passing `page_size=<number>` argument, number up to 200 will be respected. Information
about the whole set is contained in the response headers. Check [example of a "get_all" function](https://github.com/waldur/ansible-waldur-module/blob/6679b6b8f9ca21099eb3a6cb97e846d3e8dd1249/waldur_client.py#L140)
to see how a full traversal can be done.

## Project management

### Customer lookup
Puhuri Core implementes a multi-tenant model to allow different organizations to allocate shared resources simultaneously
and independently from each other. Each such organizaton is a customer of Puhuri Core and is able to create its own
projects. Project allows to create new allocations as well as connect users with the project.

Hence, to create a project, one needs first to have a reference to the customer. The reference is a stable one and
can be cached by REST API client.

Customers are created by Puhuri Core support team. Please reach out to [support@hpc.ut.ee](mailto:support@hpc.ut.ee)
if you think you should have one.

Examples:

- [API call for customer lookup](API guide/project.md#lookup-allocator-customers-available-to-a-user)


### Project creation
In order to create a new project in an organization, user needs to provide the following fields:

- **`customer`** - URL of the project's organization
- **`name`** - project's name
- `description` - description of a project description
- `backend_id` - optional identifier, which is intended to be unique in the resource allocator's project list. Can be 
  used for connecting Puhuri Core projects with client's project registry. 

Examples:

- [API call for project creation](API guide/project.md#create-a-new-project)
- [Project creation in Puhuri Portal](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L13).

### Project update

It is possible to update an existing project using its URL link. Name, description and backend_id can be updated.

Examples:

- [API call for project update](API guide/project.md#update-an-existing-project)

### Project lookup
User can list projects and filter them using the following query parameters:

- `name` - project's name (uses 'contains' logic for lookup)
- `name_exact` - project's exact name
- `description` - project's description
- `backend_id` - project's backend id

In case API user has access to more than one customer, extra filter by customer properties can be added:

- `customer` - exact filter by customer UUID 
- `customer_name` - filter by partial match of the full name of a customer
- `abbreviation` - filter by partial match of the abbreviation of a customer

Examples:

- [API call for listing  of projects](API guide/project.md#list-projects)

## Project membership management

### Puhuri AAI user mapping lookup

Puhuri Core maintains its own set of user records. Project membership is essentially a link between a project and user,
carrying also information about the role name.

A mapping from the Puhuri AAI CUID is implemented as a separate call. Resource allocator is able to send the CUID,
which would return a link to Puhuri Core user identity or error message, if this was not possible (e.g. CUID is
incorrect or connection with Puhuri AAI user registry has failed).

Examples:

- [API call for getting a mapping of Puhuri AAI user CUID to Puhuri Core user](API guide/project-permissions.md#getting-a-mapping-of-AAI-user-to-Core-user)

### Membership management 

Creating a membership for a user means creating a permission link. 

The list of fields for creation are:

- `user` - a user's URL, looked up from a previous step
- `project` - a URL of a project where the permission needs to be created.
- `role` - a role of the user. 'member', 'admin' and 'manager' are supported. TODO: add reference to Puhuri terminology.

Each permission has a unique URL. To remove the permission, REST API client needs to send a DELETE HTTP request
to that URL.

It is also possible to list available project permissions along with a various filters. User can list permissions for
all project in her visibility range. To limit the permission set to a specific project
or user, the following filters are supported:

Possible query params for filtering:

- `project` - a projects's UUID
- `project_url` - a projects's URL
- `user` - a user's UUID
- `user_url` - a user's URL
- `username` - a user's username (aka CUID)
- `full_name` - a user's full name
- `customer` - an organization's UUID
- `role` - a role's name

Examples:
- [Allocation of members to a project](API guide/project-permissions.md#project-members-permissions-allocation)
- [Removal of members from a project](API guide/project-permissions.md#removal-of-members-from-a-project)
- [Listing project permissions](API guide/project-permissions.md#project-members-permissions-allocation)


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

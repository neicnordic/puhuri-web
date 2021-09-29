# Integration guide

## Resource allocators

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


## Puhuri Core SDK

If you are integrating a python-based application, you might find useful a [python wrapper](SDK Guide) for typical operations.

## Common operations

Almost all operations require authentication. Authentication process is a two-step:
1. Generation of authentication token using [Authentication API](API guide/authentication.md).
2. Passing that token in the Authorization header along with all other REST API calls.

Please note that all of the responses to the listing are paginated, by default up to 10 elements are returned.
You can request more by passing `page_size=<number>` argument, number up to 200 will be respected. Information
about the whole set is contained in the response headers. Check [example of a "get_all" function](https://github.com/waldur/ansible-waldur-module/blob/6679b6b8f9ca21099eb3a6cb97e846d3e8dd1249/waldur_client.py#L140)
to see how a full traversal can be done.

## Project management

### Customer lookup
Puhuri Core implements a multi-tenant model to allow different organizations to allocate shared resources simultaneously
and independently from each other. Each such organizaton is a customer of Puhuri Core and is able to create its own
projects. Project allows us to create new allocations as well as connect users with the project.

Hence, to create a project, one needs first to have a reference to the customer. The reference is a stable one and
can be cached by a REST API client.

Customers are created by Puhuri Core support team. Please reach out to [support@hpc.ut.ee](mailto:support@hpc.ut.ee)
if you think you should have one.

Examples:

- [API call for customer lookup](API guide/project.md#lookup-allocator-customers-available-to-a-user)


### Project creation
In order to create a new project in an organization, user needs to provide the following fields:

- **`customer`** - URL of the project's organization
- **`name`** - project's name
- `description` - description of a project description
- `end_date` - optional date when the project and all allocations it contains will be scheduled for termination.
- `backend_id` - optional identifier, which is intended to be unique in the resource allocator's project list. Can be
  used for connecting Puhuri Core projects with the client's project registry.
- `oecd_fos_2007_code` - optional OECD Field of Science code. A code is represented by a string with two numbers separated by dot for a corresponding field of science. For example `"1.1"` is code for Mathematics. More information can be found [here](https://joinup.ec.europa.eu/collection/eu-semantic-interoperability-catalogue/solution/field-science-and-technology-classification/about).

Please note that the project becomes active at the moment of creation!

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
- `description` - project's description (uses 'contains' logic for lookup)
- `backend_id` - project's exact backend ID

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
incorrect or connection with Puhuri AAI user registry has failed). Note that endpoint returns UUID, full URL of the user
is constructed as Puhuri Core URL + ``/api/users/USER_UUID/``.

Examples:

- [API call for getting a mapping of Puhuri AAI user CUID to Puhuri Core user](API guide/project-permissions.md#getting-a-mapping-of-AAI-user-to-Core-user)

### Membership management

Creating a membership for a user means creating a permission link. While multiple roles of a user per project are allowed,
we recommed for clarity to have one active project role per user in a project.

The list of fields for creation are:

- `user` - a user's URL, looked up from a previous step
- `project` - a URL of a project where the permission needs to be created.
- `role` - a role of the user. 'member', 'admin' and 'manager' are supported. TODO: add reference to Puhuri terminology.

Each permission has a unique URL. To remove the permission, REST API client needs to send a DELETE HTTP request
to that URL.

It is also possible to list available project permissions along with a various filters. Users can list permissions for
all projects in their visibility range. To limit the permission set to a specific project
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

- [API call for allocating members to a project](API guide/project-permissions.md#project-members-permissions-allocation)
- [API call for removing members from a project](API guide/project-permissions.md#removal-of-members-from-a-project)
- [API call to listing project permissions](API guide/project-permissions.md#project-members-permissions-allocation)


## Resource allocation management

Creating and managing resource allocations in Puhuri Core follows ordering logic.

All operations on resources, which lead to changes in allocations - e.g. creation, modification of allocated limits
or termination - are wrapped in an order. It is possible to have multiple actions of the same type in one order.
Such actions are called Order items.

### Listing offerings

To create a new Allocation, one must first choose a specific Offering from available. Offering corresponds to a specific
part of a shared resource that Resource Allocator can allocate. For example, it can be a national share of LUMI resources.
Offerings can be visible to multiple allocators, however in the first iteration we plan to limit allocators with
access to only their owned shares.

User can fetch offerings and filter them by the following fields:

- `name` - offering's name
- `name_exact` - offering's exact name
- `customer` - organization's URL
- `customer_uuid` - organization's UUID

Generally Offering has a stable UUID, which can be used in Puhuri Core client configuration. Offering defines inputs
that are required to provision an instance of the offering, available accounting plans (at least one should be present)
as well as attributes that can or should be provided with each request.

Each Offering contains one or more plans, you will need to provide a reference (URL) to the plan when creating an
allocation.

API examples:

- [Getting a list of offerings available for allocation](API guide/resource-allocation-management.md#getting-a-list-of-offerings)


### Selecting an offering (LUMI specific)

In case of LUMI allocation, there are several offerings available for each allocator corresponding to the
access types defined by EuroHPC JU.

Offerings types are:

- Extreme Scale Access
- Regular Access
- Benchmark Access
- Development Access
- Fast Track Access for Academia
- Fast Track Access for Industry Access

During the integration period for convenience we use the following convention for offering names:
``LUMI <Country name> / <access type>``, e.g. ``LUMI Sweden / Extreme Scale Access`` or ``LUMI Finland / Regular Access``.
Each of the offering will include a single plan.

Full details of the Offering contain expected attributes that should be passed when creating an allocation.

### Orders, order items and resources.
To create a new allocation, an order must be created contain order item with requested attributes: project
as well as details about the allocations.

Order might require additional approval - in this case upon creation its status will be `REQUESTED FOR APPROVAL`, which
can transition to `REJECTED` if order is rejected.
Otherwise it will be switched to `EXECUTING`, ending either in `DONE` if all is good or `ERRED`, if error happens during the processing.

Within an order, an order item is expected correspondingly to a single allocation to be created.
You can provide multiple order items within a single order, but all of them have to be of the same type,
i.e. `CREATE`, `UPDATE` or `TERMINATE`.

As a result of successful processing of order item by Puhuri Core, it will create a new Resource. Its UUID will
be available as a `marketplace_resource_uuid` field of the creation order item.

In additipon, ``accepting_terms_of_service`` flag must be provided as a lightweight confirmation that allocator is
aware and agreeing with Terms of services of a specific Offering.

Example of the order payload sent with `POST` to ``https://puhuri-core-beta.neic.no/api/marketplace-orders/``:

```json

{
   "project": "https://puhuri-core-beta.neic.no/api/projects/72fff2b5f09643bdb1fa30684427336b/",
   "items": [
      {
         "offering": "https://puhuri-core-beta.neic.no/api/marketplace-offerings/0980e9426d5247a0836ccfd64769d900/",
         "attributes": {
            "name": "test20",
            "oecd_science_domain_configuration": "1.1 Mathematics"
         },
         "limits":{
            "gb_k_hours": 30,
            "cpu_k_hours": 1,
            "gpu_k_hours": 20
         },
         "plan": "https://puhuri-core-beta.neic.no/api/marketplace-plans/14b28e3a1cbe44b395bad48de9f934d8/",
         "accepting_terms_of_service": true
      }
   ]
}
```


### Change resource limits
Send ``POST`` request to ``https://puhuri-core-beta.neic.no/api/marketplace-resources/<UUID_OF_A_RESOURCE>/update_limits/`` providing
the new values of limits, for example:

```json
{
   "limits": {
      "gb_k_hours": 35,
      "cpu_k_hours": 6,
      "gpu_k_hours": 200
   }
}
```

### Resource termination

Send ``POST`` request to ``https://puhuri-core-beta.neic.no/api/marketplace-resources/<UUID_OF_A_RESOURCE>/terminate/``.

API examples:

- [Creation of a resource allocation](API guide/resource-allocation-management.md#creation-of-a-resource-allocation)
- [Modification of a resource allocation](API guide/resource-allocation-management.md#modification-of-a-resource-allocation)
- [Termination of a resource allocation](API guide/resource-allocation-management.md#termination-of-a-resource-allocation)

Example integrations:

- [Lookup of available offerings in Puhuri Portal](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/views.py#L45).
- [Creation of a resource in Puhuri Portal](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L37).
- [Changing allocated limits in Puhuri Portal](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L53).
- [Deletion of a resource allocation in Puhuri Portal](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/processors.py#L64).


### Advanced
Information about Puhuri resources in Puhuri Core can change over time, for example, new components could be added.
Puhuri Portal implements a method for dynamic import and upkeep of that information from Puhuri Core.

As this is a more advanced topic, please check [implementation](https://github.com/waldur/waldur-mastermind/blob/7b2eba62e1e0dab945845f05030c7935e57f0d9c/src/waldur_mastermind/marketplace_remote/views.py#L84).
If you have questions, we will be happy to help out! Please reach out to support@hpc.ut.ee.


## Reporting
- Usage collection for each allocation - provided as Resource attributes
- Aggregate reporting data

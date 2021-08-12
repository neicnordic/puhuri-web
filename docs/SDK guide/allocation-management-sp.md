# Allocation Lifecycle Management by Service Provider

This page describes operations to be performed by service provider.

## Prerequisites

Please, read [initial setup for Puhuri Core SDK](initial-setup.md) and
please reach out to [support email](mailto:support@hpc.ut.ee) to get credentials for Puhuri Core.

## Getting a list of resource allocations

`list_marketplace_resources` method is used to fetch resources related to offerings, which belong to user's service provider.

Possible filter options for allocations (each one is optional):

- `provider_uuid` - UUID of a service provider organization;
- `state` - current state of a resource allocation; valid values: `Creating`, `OK`, `Erred`, `Updating`, `Terminating`, `Terminated`;
- `offering_uuid` - UUID of a related resource;
- `fields` - list of fields to return.

```python
result = client.list_marketplace_resources(
    provider_uuid='f1353afe1dae4bcf94a5256c5612a189',
    state='Creating',
    offering_uuid='cf4eb9c29fc74af4ade667fcb53633d5',
    fields=['name', 'offering', 'state', 'limits', 'plan', 'project', 'url']
)

# result => {
#   'limits': {'cpu_k_hours': 1000, 'gb_k_hours': 3000, 'gpu_k_hours': 1000},
#   'name': 'Sample resource',
#   'offering': 'https://puhuri-core-demo.neic.no/api/marketplace-offerings/cf4eb9c29fc74af4ade667fcb53633d5/',
#   'plan': 'https://puhuri-core-demo.neic.no/api/marketplace-plans/1537de6e94f9427cafb74cb63fa21c72/',
#   'project': 'https://puhuri-core-demo.neic.no/api/projects/8a158ebf1abf4c74a431b9c65a0d7829/',
#   'state': 'Creating',
#   'url': 'https://puhuri-core-demo.neic.no/api/marketplace-resources/a1916bd53fd04b1ab1a4e700c926607b/'
# }
```

## Approving/rejecting allocations in status "CREATING"

The default state value after allocation creation is `CREATING`. A service provider can change it to `OK` (created successfully), `Erred` (not created due to some error) and `Terminated` (creation rejected). Only users with service provider owner and manager roles can perform this action.

The method for triggering this transition is `marketplace_resource_set_state`, which requires the following arguments:

- **`resource_uuid`** - UUID of a resource allocation;
- **`state`** - target resource state; valid values: `ok`, `erred`, `terminated`.

```python
result = client.marketplace_resource_set_state(
    '6ccfa59429964d8884a59c97165ed647',
    'ok',
)

# result => {
#   'status': 'Resource state has been changed.'
#}
```

## Updating resource allocation with local reference (setting `backend_id` field)

Each allocation can have a link to a service provider's internal reference using `backend_id` field. Only users with service provider owner and manager roles can set this value using `marketplace_resource_set_backend_id` method of the client. It requires the following arguments:

- **`resource_uuid`** - UUID of a resource allocation;
- **`backend_id`** - id of an external entity.

```python
result = client.marketplace_resource_set_backend_id(
    '6ccfa59429964d8884a59c97165ed647',
    'some-backend-id'
)

# result => {
#   'status': 'Resource backend_id has been changed.'
# }
```

## Providing additional access detail for resource allocation

For additional details related to allocation access, `report` field is used.
In order to provide this information, owners and managers can use `marketplace_resource_submit_report` method. It requires the following arguments:

- **`resource_uuid`** - UUID of a resource allocation;
- **`report`** - list with the structure:

    ```python
    [{
        'header': '<Section-header>',
        'body': '<Section-body>',
    }]
    ```

```python
result = client.marketplace_resource_submit_report(
    '6ccfa59429964d8884a59c97165ed647',
    [
        {'header': 'Header1', 'body': 'Body1'},
        {'header': 'Header2', 'body': 'Body2'}
    ]
)

# result => {
#   'status': 'Report is submitted'
# }
```

## Getting a list of members in a project with active resource allocations

Service provider owners and managers can list project members using a resource allocation with `marketplace_resource_get_team` method.
It requires the following arguments:

- **`resource_uuid`** - UUID of a resource allocation.

```python
result = client.marketplace_resource_get_team(
    '6ccfa59429964d8884a59c97165ed647'
)

# result => {
# [
#  {'email': 'CSC_api_user@example.com',
#   'expiration_time': None,
#   'full_name': 'Integration user (CSC)',
#   'permission': 'https://puhuri-core-demo.neic.no/api/project-permissions/10/',
#   'role': 'admin',
#   'url': 'https://puhuri-core-demo.neic.no/api/users/bb235c67dcb44470a45d4e0f94e0ed00/',
#   'username': 'CSC_api_user',
#   'uuid': 'bb235c67dcb44470a45d4e0f94e0ed00'},
#  {'email': 'ETAIS_api_user@example.com',
#   'expiration_time': None,
#   'full_name': 'Integration user (ETAIS)',
#   'permission': 'https://puhuri-core-demo.neic.no/api/project-permissions/3/',
#   'role': 'member',
#   'url': 'https://puhuri-core-demo.neic.no/api/users/0cc72de4ebb840d98fef133e4433ec9a/',
#   'username': 'ETAIS_api_user',
#   'uuid': '0cc72de4ebb840d98fef133e4433ec9a'}]
# }
```

## Reporting usage for a resource allocation

A usage of a resource allocation can be submitted by a corresponding service provider.
For this, the following methods are used:

- `get_marketplace_offering` - getting offering with components info.
  Arguments:

    - **`offering_uuid`** - UUID of an offering

- `marketplace_resource_get_plan_periods` - getting current plan periods for resource allocation. Arguments:

    - **`resource_uuid`** - UUID of a resource

- `create_component_usages` - creating or updating components usage for the current plan

    - **`plan_period_uuid`** - UUID of a plan period
    - **`usages`** - list of ComponentUsage instances

```python
from waldur_client import WaldurClient, ComponentUsage

offering = client.get_marketplace_offering('<offering-uuid>')
component_types = [component['type'] for component in offering['components']]
plan_periods = client.marketplace_resource_get_plan_periods('<resource-uuid>')

if len(plan_periods) > 0:
    plan_period = plan_periods[0]

    client.create_component_usages(
        plan_period['uuid'],
        [ComponentUsage(component_type=comp_type, amount=10, description='Usage') for comp_type in component_types]
    )

result = client.marketplace_resource_get_plan_periods('<resource-uuid>')

# result => {
# [{'components': [{'created': '2021-08-11T15:36:45.562440Z',
#                   'date': '2021-08-11T15:37:30.556830Z',
#                   'description': 'Usage',
#                   'measured_unit': 'units',
#                   'name': 'CPU',
#                   'type': 'cpu',
#                   'usage': 10,
#                   'uuid': '080066bebf9547d5ad3279f7c353b023'},
#                  {'created': '2021-08-11T15:36:45.842385Z',
#                   'date': '2021-08-11T15:37:30.556830Z',
#                   'description': 'Usage',
#                   'measured_unit': 'units',
#                   'name': 'GPU',
#                   'type': 'gpu',
#                   'usage': 10,
#                   'uuid': 'e8d745049bff4410b60f517e56daf421'}],
#   'end': None,
#   'plan_name': 'sample-plan',
#   'plan_uuid': '9f7b1d113f464214bb195db38c217cf9',
#   'start': '2021-08-11T15:20:25.762775Z',
#   'uuid': 'fb36ce56e53b43e59b3d963354d0467c'}]
# }

```
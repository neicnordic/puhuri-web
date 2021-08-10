# Resource Allocation Management (for Service Providers)

This page includes description and examples of several operations for resource allocation management.

## Prerequisites

Please, read [common notes for Puhuri Core SDK](common.md).

## Getting a list of resource allocations

`list_marketplace_resources` method is used to fetch resources related to offerings, which belong to user's service provider.

Possible filter options for allocations (each one is optional):

- `provider_uuid` - UUID of a service provider organization;
- `state` - current state of a resource; valid values: `Creating`, `OK`, `Erred`, `Updating`, `Terminating`, `Terminated`;
- `offering_uuid` - UUID of a related offering;
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

Each allocation has some state depending on actions made to it. The default value after allocation creation is `CREATING`. A service provider can manually change it to `OK` (created successfully), `Erred` (not created due to some error) and `Terminated` (creation is rejected). Only service provider owners and managers can perform this action.

The responsible method for this transitions is `marketplace_resource_set_state`, which requires the following arguments:

- **`resource_uuid`** - UUID of a resource;
- **`state`** - final resource state; valid values: `ok`, `erred`, `terminated`.

```python
result = client.marketplace_resource_set_state(
    '6ccfa59429964d8884a59c97165ed647',
    'ok',
)

# result => {
# {'status': 'Resource state has been changed.'}
#}
```

## Updating resource allocation with local reference (setting `backend_id` field).

## Providing additional access detail for resource allocation ("report")

## Getting a list of members in a project with active resource allocations.

## TODO: consider exposing `/team` endpoint for each resource.

## Reporting usage for a resource allocation.

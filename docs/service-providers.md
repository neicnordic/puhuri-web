# API Guide

## Operations
 <!-- TODO: Add guide for WaldurClient setup -->

###  Getting a list of resource allocations
```python
result = client.list_marketplace_resources(provider_uuid='<provider-uuid>')
```

### Approving/rejecting allocations in status "CREATING"

### Updating resource allocation with local reference (setting `backend_id` field).

### Providing additional access detail for resource allocation ("report")

### Getting a list of members in a project with active resource allocations.

### TODO: consider exposing `/team` endpoint for each resource.

### Reporting usage for a resource allocation.


## LUMI Use-case

![Positioning](assets/lumi-vs-puhuri.png){ align=right }

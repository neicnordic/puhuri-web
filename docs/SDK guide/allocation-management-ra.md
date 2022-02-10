# Allocation Lifecycle Management by Resource Allocator

## Listing associations between users and resources

To list the created associations between users and resources, the service provider should use `list_remote_offering_users` method. It receives an optional `filters` argument, a dictionary containing filters for the associations. The possible items are:

- `user_uuid` - UUID of a user associated with resources belonging to SP
- `offering` - SP resource URL
- `offering_uuid` - UUID of a resource
- `created` - date after what the association was created; the format is `YYYY-MM-DD`, e.g. `2022-01-30`
- `modified` - date after what the association was created; the format is the same as for the `created` field

In case if SDK usage is not possible, HTTP request can be sent:

```http
POST <API-URL>/marketplace-offering-users/?user_uuid=<USER_UUID>&offering_uuid=<OFFERING_UUID>&created=2022-01-10&modified=2022-01-30

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

{
    "created": "2022-01-19T19:40:10.328758Z",
    "offering": "<API-URL>/marketplace-offerings/<OFFERING_UUID>/",
    "offering_name": "Remote offering",
    "offering_uuid": "<OFFERING_UUID>",
    "user": "http://localhost:8000/api/users/<USER_UUID>/",
    "user_uuid": "<USER_UUID>",
    "username": "abc",
    "modified": "2022-01-31T18:02:10.328758Z",
}
```

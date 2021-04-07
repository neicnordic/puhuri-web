# Project

## Lookup allocator customers available to a user

In most cases integration user can see only one allocating organization (or Puhuri Core "customer"), however it is
possible that the same account is used for allocating different shares, e.g. national share and community specific.
Projects are always created in the context of a specific customer, so as a first thing you need to lookup a specific
customer you want to use. Customer is a stable entity, so it's URL / UUID can be cached.

<!-- {generate_customer_list} -->

## Create a new project

In order to create a new project in an organization, user need to provide project `name`, `description`, and possible `backend_id`

<!-- {generate_project_creation} -->

## Update an existing project
User can update `name`, `customer` (uuid), `description`, and `type` fields of selected project.

<!-- {generate_project_update} -->

## List projects with pissible fintering
User can list projects and filter them by `name`, `customer` (uuid, name, native name, abbreviation), `description`, `name_exact` and `backend_id`.

<!-- {generate_project_listing} -->

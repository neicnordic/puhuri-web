## Puhuri Terminology

**Puhuri Term** | **Puhuri Core API Term** |**Puhuri AAI Term** |**Definiton** |
--- | --- | --- | --- | 
AAI| - | - |Authentication and Authorisation Infrastructure (AAI) (also used alternative term IAM). A set of various services to register a user to get a Puhuri ID, authenticate (i.e. to get the user identity) to use the integrated Resources (services), and provide means for the resources provider to grant access to the eligible users. | 
Accepted Terms of Service | - | - | A boolean value indicating if the Person has accepted the terms of service for a given resource |  |
Access| - | - | A boolean value indicating if a User Account or Service Account has the right to use a resource. This includes that the user has accepted the Terms of Use. |  
Accounting| - | - | A set consisting of the aggregation of the allocation of resource components to a project, and the actual consumption of consumable units of allocated resource components within a project |  
AccountRequest| - | - | The process or action of requesting an account |
Allocating Body| - | - | The entity that decides on the allocation of the resources to projects. There are multiple allocating bodys but at least one per participating country. |  
Allocating Body Member| - | - | A person or persons able to create projects and allocate resources according to the respective allocating bodys decisions. |  
Allocation| Resource | - | The right to access a resource and use of a resource component from a start date to an end date and to an extent of a number of consumable units as defined in a project |  
API| - | - | Application Programming Interface. An interface for machine-to-machine data transfer. |  
Authentication| - | - | Process to get information regarding who the user is. |
Call| - | - | A Call represents a possibility to apply for a project on a certain resource(s). Different sets of resources with total available consumable units, min/max for requested allocation are available in different calls. Call-objects only live in the portal parts of Puhuri, or outside of Puhuri if the national stakeholders have their process set up in that way. |  
Consumable Unit| - | - | Consumable units that can be allocated to projects. These units are resource specific. Different resources and resource components may consume these at different rates. Consumable units and their rate of consumption are defined for all resources that have accountable resources. |  
Default quota| - | - | The default allotment of a limited asset. Default quotas are the same for everybody, and can be enforced per user or per user project. They should be documented to end users if relevant. If the requested amount of resources in a Project proposal exceeds the default quota, or if an active project needs an increased allotment, it is up to the resource owner to set a policy for how this is handled. See also Extended quota |  
DiskQuota| - | - | Disk is a consumable unit, the DiskQuota is the upper limit(s) to use of the amount(s) of disk available |  
GDPR| - | - | The General Data Protection Regulation is a regulation in EU law on data protection and privacy in the European Union and the European Economic Area. |  
Lifespan| - | - | The time period over which a project has an allocation on one or more resources. The Lifespan has a start date and an end date |  
Member| - | User | A member is a person who has the right to consume the consumable units allocated to a project. The person is then a member of that project |  
National Portal| - | Client | A National Portal is an existing portal that can communicate with Puhuri Core through an API and by which researchers can apply for the use of, and be given access to, a resource. If present it is to be used instead of the Puhuri portal |  
National Project| - | - | An object with one or more allocations on one or more resources. The project has a number of consumable units assigned for each of the allocations. It is assigned to a PI, has one or more optional proxy-PI and one or more members. The project is time limited by the lifespan. The Project has the PI, resource(s), the allocation(s), and the member(s) assigned. Here information of National character which is not necessarily represented in Project |  
Principal Investigator| - | - | A principal investigator (PI) is a person responsible for, and manager of, a Project |  
Project| - | - | A project is an object with one or more allocations of on one or more resources. The project has a number of consumable units assigned for each of the allocations. It is assigned to a PI, has one or more optional proxy-PI and one or more members. The project is time limited by the lifespan. |  
Project Proposal| - | - | Project proposal linked to a Call is subject to evaluation (review). It is created by a Project’s PI. |  
Puhuri AAI| - | - | A system for user registration and issuing Puhuri Account and AAI proxy for connecting IdPs and services |  
Puhuri Account| - | - | A representation of a unique real person with a unique identifier within Puhuri Core. Containing the contact information and institutional details for the person. A person can have multiple Resource Accounts |  
Puhuri Core| - | Client of Researcher Access | The central database that keeps track of the components of the Puhuri Services, with information on for example: resources, projects, Puhuri accounts, usage etc |  
Puhuri Portal| - | Client of Puhuri AAI | The portal to be used in absence of a National Portal with at least the same functionality as a National Portal |  
Puhuri Services| - | - | the aggregation of Puhuri Core, Puhuri AAI, Puhuri Portal, and corresponding APIs |  
Quota| - | - | A quota is an allotment of a limited set of assets. Comment: The term "Quota" is only to be used in an abstract sense, whereas the more specific terms for different quotas are to be used in the architecture work |  
Reporting| - | - | The process by which the utilisation of allocated resource components in terms of consumable units within a project by members of the project is presented to stakeholders. |  
Resource| Offering | - | A Resource object represents a compute cluster, storage system, or cloud resource. |  
Resource Account| - | - | A Resource Account object represent the possibility for a Puhuri Account to access a Resource with a unique identifier (username or similar) |  
Resource Component| Offering Component | - | An allocatable part of a resource with a type and a unit |  
Role| - | - |Role information to be used for example when making decisions in Puhuri Core or Resources |  
Service Account| - | - |syn. Robot Account - A User Account which is not representing a real person, but a machine. However, it must have associated contact information to responsible persons. |  
User ID| - | - | A user is the entity (a real person or a machine) that uses the Resource. A User can belong to zero, one, or more Projects. |  


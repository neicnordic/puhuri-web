# User guide

!!! warning
    User guide is in development. Early feedback is welcome, send email to ilja.livenson@ut.ee.
    
    
## Roles

- Operator - common view across all Puhuri services and users
- Service manager - responsible for specific services (e.g. LUMI)
- Users - end users of the Puhuri portal
- Owners of organizations (PI Users) - users with a role of organization owners, aka PIs

## Guide for the operator

### Organization on-boarding

1. Offline validation of organization
2. Creation of organization in Puhuri Portal

### Approval of organizational requests

Upcoming functionality

### Organization owner management

Owner == PI

Meaning == assignment of users that are eligible to create a project and allocate resources.

### Reporting

- cross services
- cross organizations
- etc

## Guide for service manager

### Management of service offerings

- Remote offering management (source - Puhuri Core)
- LUMI specific examples

### Approval of user requests for Puhuri resources

### Reporting

## Organization owner guide

### Creation of projects

Project creation is only allowed for project Principal Investigators (PIs).

Prerequisites for creating projects:
* User must have a Puhuri account (logged in to Puhuri Portal using MyAccessID)
* Allocator must set PI role to the user in certain organization


For creating project:
1. Login to Puhuri Portal using MyAccessID.
2. Select your home organization.
3. Click on "Add project".
4. Fill the necessary fields (fields marked with * are mandatory).
    1. Project name - The original title of the project.
    2. Project description - A brief description about the project.
    3. End date - this is the end date for using the computational resources.
    
5. Select "Service catalog" from the left menu and then correct LUMI project type:
    1. Extreme Scale Access
    2. Regular Access
    3. Benchmark Access
    4. Development Access
    5. Fast Track Access for Academia
    6. Fast Track Access for Industry
    
6. Write the name for the resource allocation (NOTE: This name will be visible in accounting data.).
7. Select correct plan (LUMI common) and write needed allocation quota (CPU, GPU and Storage).
8. Write short description (optional) and choose correct science field (mandatory).
9. Click on the "Add to cart".
10. Check once more and click on "Request an approval"

Now national allocator will receive notification about new project request and it can be approved or rejected.
    
### Management of project team

Project team contains users with different roles:
* Principal Investigator (PI) - The lead researcher and primary contact for the project.
* Co-Principal Investigator (Co-PI): An individual recognized by the prime institution and the principal investigator (PI) as someone who shares scientific and administrative leadership responsibilities for a project with the PI.
* Member - Users who work on one or more phases of the project and involved in doing assigned tasks.
* Guest - Users who are only able to see project related data, not able to modify it.


#### Adding project members
If user already has Puhuri account connected with the organization, then:
1. Open project in Puhuri portal
2. Click on "Add member"
3. Select user
4. Set role and expiration date if necessary.
5. Finally, click on "Add"

If user does not have Puhuri account, then:
1. Select correct organization
2. Click on "Invite team member"
3. Insert user's email and set the role and project for the new user.
4. Click "Invite user"


- delegation
- addition of PIs
- Mapping rules to Puhuri Core

### Requesting specific Puhuri resources

- selection, logic, input parameters
- accounting

### Requesting for help



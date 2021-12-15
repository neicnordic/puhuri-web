# User guide for creating new projects and allocations

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

- User must have a Puhuri account (logged in to Puhuri Portal using MyAccessID)
- Allocator must set PI role to the user in certain organization


For creating project:

1.Login to Puhuri Portal using MyAccessID.
   
![Login](../../assets/Login.PNG)

2.Select your home organization.
   
![Select organization](../../assets/Select%20workspace.PNG)
![Select organization](../../assets/Select%20workspace_1.PNG)

3.Click on "Add project".
   
![Add project](../../assets/Add%20project.PNG)

4.Fill the necessary fields (fields marked with * are mandatory).

- Project name - The original title of the project.
- Project description - A brief description about the project.
- End date - this is the end date for using the computational resources.
    
![Project details](../../assets/Project%20details.PNG)

5.Select "Service catalog" from the left menu and then correct LUMI project type:

- Extreme Scale Access
- Regular Access
- Benchmark Access
- Development Access
- Fast Track Access for Academia
- Fast Track Access for Industry
    
![Project details](../../assets/Service%20catalog.PNG)
![Project details](../../assets/LUMI%20resource.PNG)
![Project details](../../assets/Available%20resources.PNG)

6.Write the name for the resource allocation (NOTE: This name will be visible in accounting data.).

![Project details](../../assets/Resource%20config.PNG)

7.Select correct plan (LUMI common) and write needed allocation quota (CPU, GPU and Storage).

8.Write short description (optional) and choose correct science field (mandatory).

9.Click on the "Add to cart".

10.Check once more and click on "Request an approval"

![Project details](../../assets/Approval%20request.PNG)

Now national allocator will receive notification about new project request and it can be approved or rejected.
    
### Management of project team

Project team contains users with different roles:

- Principal Investigator (PI) - The lead researcher and primary contact for the project.
- Co-Principal Investigator (Co-PI) - An individual recognized by the prime institution and the principal investigator (PI) as someone who shares scientific and administrative leadership responsibilities for a project with the PI.
- Member - Users who work on one or more phases of the project and involved in doing assigned tasks.
- Guest - Users who are only able to see project related data, not able to modify it.


#### Adding project members
##### If user already has Puhuri account connected with the organization, then:

1.Login to Puhuri Portal with MyAccessID.
   
![Login](../../assets/Login.PNG)

2.Open project in Puhuri Portal.

3.Select "Team" from left menu and click on "Add member".
   
![Select organization](../../assets/Team.PNG)
![Select organization](../../assets/Add%20member.PNG)

4.Select correct user, set the role and expiration date if necessary.
   
![Add user](../../assets/Add%20user.PNG)

6.Finally, click on "Add".

7.User now will get invitation email with the acceptance link.

##### If user does not have Puhuri account, then:

1.Login to Puhuri Portal with MyAccessID.
   
![Login](../../assets/Login.PNG)

2.Select your organization.
   
![Select organization](../../assets/Select%20workspace.PNG)
![Select organization](../../assets/Select%20workspace_1.PNG)

3.Click on "Invite team member".
   
![Invite team member](../../assets/Organization%20overview.PNG)

4.Insert user's email (civil code is optional field for additional validation, can be used, if IdP will release this attribute) and set the role and project for the new user.
   
![Invite user](../../assets/Invite%20user.PNG)

5.Click "Invite user".

6.User now will get invitation email with the acceptance link.


- delegation
- addition of PIs
- Mapping rules to Puhuri Core

### Requesting specific Puhuri resources

- selection, logic, input parameters
- accounting

### Requesting for help



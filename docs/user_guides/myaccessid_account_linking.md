# MyAccessID account linking

MyAccessID allows to merge multiple identities into one MyAccessID identity. By doing this, no matter which IdP is used for authentication, connected services will get always one single identity.

To link identities, please follow these steps:

1. Login to [MyAccessID profile management page](https://mms.myaccessid.org/fed-apps/profile/) 
2. Click on "My Linked Accounts"
   ![Profile page](../assets/Profile1.png)

3. Now you can see the table with your linked accounts. 
   ![Linked accounts page](../assets/Linked_accounts1.png)

The first column shows the email connected to specific identity, second column shows the IdP name, third one shows the unique identifier connected to that IdP and the fourth one shows the timestamp of last usage of this IdP. X-mark after that allows to delete the linked identity.

The first row in that table (excl headings) shows that your identity belongs to MyAccessID and next to that you can find the unique identifier connected to your MyAccessID account and this will be shared with the connected service provider if you're using MyAccessID AAI service.
The row after that contains your current home organization (IdP) information.

To add more linked identities, please log into your **primary account** and click on "Link a New Account”. Please follow the steps as prompted to log into your secondary MyAccessID account, but this time, choose the identity provider that you used for **secondary account authentication** (options are your organization, eIDAS, or eduID Sweden).

!!! note
      Always log in with this primary account first before linking any additional identities. Consistently using your primary account for initial logins ensures a unified identity across services. Remember the authentication methods for all linked accounts to avoid login errors.
         

   ![Linked accounts page with marker](../assets/Linked_accounts.png)
   ![MyAccessID login](../assets/MyAccessID%20login.PNG)

When everything is correct, then you will see a message on a green background that your identities are successfully linked.

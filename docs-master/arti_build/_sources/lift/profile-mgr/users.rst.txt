.. include:: /common/global.rst

Creating and managing users
===========================

To view and potentially modify settings in |acquia-product:lpm|, you
must sign in as an authenticated user. To sign in, visit the
appropriate |acquia-product:lpm| `website </lift/profile-mgr>`__ for
your geographic location. If you don't have a user account, you can
create one if you are an administrator and have permission to create
accounts, or you can have an administrator create an account for you.

For more information about available |acquia-product:lpm| websites, see
the Signing into |acquia-product:lpm| section on the
|acquia-product:lpm| `introductory page </lift/profile-mgr#signing>`__.

By default, every new |acquia-product:lpm| customer account is set up
with three user groups:

-  *User* – Can review people details for visitors, and can manage
   segments
-  *Administrator* – Can access all available |acquia-product:lpm|
   features, including managing users and group security
-  *API user* – Able to authenticate to the Acquia Lift API, and can
   access API functions


Creating a new user account
---------------------------

To create a new |acquia-product:lpm| user account, you must be an
administrator or a member of a `security
group </lift/profile-mgr/admin/permissions>`__ that has permission to
manage users. To create a user account, complete the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface, and then click the
   **Admin** tab.
#. Click the **Manage users** link.
#. Click the **Add new users** link.
#. In the **Email** field, enter the user's email address.
#. In the **Full name** field, enter the user's full name.
#. In the **User group** list, click the name of the user group to which
   you want this new user to belong (typically one of the groups above,
   although an administrator can create additional groups).
#. In the **Password** field, enter a password for the user that meets
   the |acquia-product:lpm| `password strength
   requirements </acquia-cloud/access/password-strength>`__, and then
   re-enter the same password in the in the **Confirm password** field.
#. Depending on your requirements, modify the following additional
   settings:

   -  **Show password** check box – Displays or hides the password that
      you create
   -  **Enabled** check box – Enables or deactivates the user account
   -  **Change password next login** check box – Prompts the user to
      change the account's password during the next successful sign in
      attempt
   -  **Email user a link to set their password** check box – Emails a
      link to users that they can click to change their password and
      access |acquia-product:lpm|

#. Click **Save** to create the new user.


Finding user accounts
---------------------

To find a user account in |acquia-product:lpm|, complete the following
steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface, and then click the
   **Admin** tab.
#. Click the **Manage users** link. |acquia-product:lpm| displays a list
   of users.
#. To search for a specific user, enter your search criteria in one of
   the following fields:

   -  **Email** – Limits your search to users with a specific email
      address. You can enter part or all of an email address.
   -  **Full name** – Limits your search to users with a specific name.
      You can enter part or all of a user's name.

#. Click **Find** to display the available results.


Managing user accounts
----------------------

Depending on your needs, after you find a user account, you can edit its
associated user information or completely remove the account from
|acquia-product:lpm|.


Editing user accounts
~~~~~~~~~~~~~~~~~~~~~

To edit an existing user's information, after you find the account,
click the account's name, and then modify other values as required.

Be sure to click **Save** to save your changes.


Deleting user accounts
~~~~~~~~~~~~~~~~~~~~~~

To delete a user, find the user account that you want to remove, and
then click the account's **Delete** link.

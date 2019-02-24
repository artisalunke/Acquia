.. include:: /common/global.rst

Assigning hosted site roles during sign-in
==========================================

If you use OpenID to manage user accounts, |acquia-product:edg| users
have a single account that they use to access both the
|acquia-product:sfi| and hosted websites. Users have role and permission
assignments based on where they sign in. By default, all
|acquia-product:sfi| users, whatever their |acquia-product:edg| role,
have only the authenticated user role on hosted websites. For example, a
user may be assigned the *Site builder* role in the
|acquia-product:sfi|, but when they sign in to a hosted website, they
could have access only to the authenticated user role.

Because your users with the |platform admin|_ or |site builder|_ role in the
|acquia-product:sfi| may need additional access to hosted websites to
complete their primary purpose — to build and administer websites — you
can configure |acquia-product:edg| to assign a specific role on a hosted
website during the sign-in process to your *Platform admin* or *Site
builder* users.

.. |platform admin| replace:: *Platform admin*
.. _platform admin: /site-factory/users/admin/platform-admin

.. |site builder| replace:: *Site builder*
.. _site builder: /site-factory/users/admin/site-builder

.. note::  

   -  This process assigns hosted website roles only to users with the
      *Platform admin* or *Site builder* role in the |acquia-product:sfi|.
   -  Users cannot be assigned to roles that do not exist on hosted
      websites. For example, if a specified role exists on some, but not
      all, of your hosted websites, the role assignment process will add
      the role to your users only for websites with the role — the role
      assignment process will not create roles on websites. To see what
      roles exist on a hosted website, go to
      ``http://[site_URL]/admin/people/permissions/roles``.
   -  The role assignment process does not occur for users that are
      currently signed in to a hosted website. To obtain an assigned role,
      signed-in users must sign out of hosted websites, and then sign in
      again using OpenID.
   -  The role assignment process does not override the user registration
      setting for a hosted website. When an unknown user attempts to sign
      in, the website will not create an account unless the user had been
      previously invited by the website's administrator.


Assigning a role on hosted sites to *Platform admin* or *Site builder* users
----------------------------------------------------------------------------

To assign a role on your hosted websites to users with the *Platform
admin* or *Site builder* role, complete the following steps:

#. Sign in to the |acquia-product:sfi| using an account with the
   |platform admin|_ role.
#. In the admin menu, click **Administration**, and then click the
   **Centralized role management** link.
#. To assign a role to *Platform admins*, select the **Enable role
   assignment for Platform Admins** check box, and then enter the name
   of a role that exists on one or more of your hosted websites.
#. To assign a role to *Site builders*, select the **Enable role
   assignment for Site Builders** check box, and then enter the name of
   a role that exists on one or more of your hosted websites.
#. Click **Save**.

From this point onward, when users with the *Platform admin* or *Site
builder* role sign in to a hosted website, they are assigned the
specified role for the hosted website. If the hosted website does not
have a role with the name that you specified, the sign-in process does
not modify the user's role assignments on the hosted website.


Managing assigned site roles
----------------------------

Using the **Centralized role management** admin page, you can stop
assigning hosted website roles to users with the *Platform admin* or
*Site builder* roles, or change the assignment to another specified
role.


Changing the assigned hosted site role
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To assign *Platform admin* or *Site builder* users a different role on
hosted websites, complete the following steps:

#. Sign in to the |acquia-product:sfi| using an account with the
   |platform admin|_ role.
#. In the admin menu, click **Administration**, and then click the
   **Centralized role management** link.
#. In the **Site's role name** field, enter a different role that exists
   on one or more of your hosted websites.
#. Click **Save**.

|acquia-product:edg| now assigns the hosted website role that you
specified to users with the *Site builder* role. Changing the assigned
role does not affect any other hosted website role assignments,
including roles previously assigned by this feature.


Stopping hosted site role assignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To stop assigning hosted website roles to users with the *Platform
admin* or *Site builder* role, complete the following steps:

#. Sign in to the |acquia-product:sfi| using an account with the
   |platform admin|_ role.
#. In the admin menu, click **Administration**, and then click the
   **Centralized role management** link.
#. Clear the **Enable role assignment** check box for *Platform admins*,
   for *Site builders*, or both.
#. Click **Save**.

.. note::  

   Stopping the hosted website role assignment process during sign-in does
   not remove hosted website roles that were previously assigned to users
   with the *Platform admin* or *Site builder* role, regardless of how
   those roles were assigned.

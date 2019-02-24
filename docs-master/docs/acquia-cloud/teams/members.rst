.. include:: /common/global.rst

Managing team members
=====================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/teams/members/*

From the **Members** section of the **Organizations > Team management**
page, you can invite users to be members of a team. You can also invite
members on the main **Organizations** page. To do so, you must have the
*administer teams* permission, which by default is granted to *Team
leads*. *Owners* and *Administrators* can always invite members to any
team within the organization.

.. _invite:

Inviting a member to a team
---------------------------

To invite a member to a team, complete the following steps:

#. Sign in to the |uilink|_,
   and then click **Manage** in the top menu.
#. In your organization's information card, click **Manage**.
#. On the **Organizations > Team management** page, under **Members**,
   click **Add member**.

.. |uilink| replace:: \ |acquia-product:ui|\ 
.. _uilink: https://cloud.acquia.com

   |Invite members to a team|

#. If you are an *Owner* or *Administrator*, you may choose whether to
   invite a member as either an **Administrator** or a **Team Member**.
   Select one, and then click **Continue**.
#. Enter the email address of the user you want to add. To add more than
   one user at a time, enter the email address of each of them,
   separated by commas. Then, click **Continue**.
#. Select the team to which you want to add the user as a member, and
   then click **Continue**.
#. Select one or more roles to assign to the user on this team, and then
   click **Continue**.
#. Click **Invite**. The users you selected will each receive an email,
   letting them know that they've been invited to join a team in the
   organization.

As an alternative, you can invite a member to a team from the main
**Organizations** page. On the **Organizations** page, in the
information card for the organization, click **Invite member**, then
follow the same procedure starting with `step 4 <#step4>`__.

|Invite a member from the Organizations page|

The **Members** section of the **Organizations > Team management** page
also displays the following:

-  *Pending invitations* - You can resend or cancel any pending
   invitations that have not yet been accepted by the invited user.
-  *Last login date* - The **Last login** date, and time elapsed since
   that login, are displayed under the user's email address.

.. important:: 

   Team member accounts should not have any type of enabled autoresponder
   functionality. For more information, see the `Issues with
   autoresponders </support/tickets#autoresponders>`__ section of our
   Support ticket information documentation page.

.. _respond:

Responding to invitations
~~~~~~~~~~~~~~~~~~~~~~~~~

When a user is invited to join a team, they will receive an email from
``cloud.acquia.com``. The email contains a link to click to accept the
invitation. Clicking the link opens the account sign-in page at
``cloud.acquia.com``. If the invited user does not already have an
Acquia account, they need to set one up before they can sign in.

In addition to having an Acquia account, an invited user may also need
to:

-  Create a password that complies with your organization's `password
   strength requirements </acquia-cloud/access/password-strength>`__.
-  Set up `two-step authentication </acquia-cloud/access/signin>`__ for
   their Acquia account, if your organization is configured to require
   it.

After signing in to the |acquia-product:ui|, the invited user can accept
the invitation and thereby become part of the team they are assigned to,
with the roles and permissions they have been given in the invitation.

.. _remove:

Removing a member from a team
-----------------------------

To remove a member from a team, complete the following steps:

#. Sign in to the |acquia-product:ui|.
#. Select your organization and then click **Manage** in the top menu.
#. On the **Organizations > Team management** page, under **Members**,
   on the line that lists the member you want to remove, click
   **Remove**.
#. In the confirmation dialog, click **Remove**.

The team member is removed from that team.

As an alternative, you can remove a member from one or more teams from
the main **Organizations** page:

#. On the **Organizations** page, in the card for the organization,
   click **Remove member**.
#. Select the teams you want to remove the member from and click
   **Continue**.
#. In the confirmation dialog, click **Remove**.

.. note::  

   Instead of removing a member from a team, you may be able to change
   their role to one with lesser permissions. Click the **Edit role** to
   change a member's role.

For additional information about account security, see `Best practices
for team member departures </acquia-cloud/teams/members/remove>`__.

.. _roles:

Modifying a team member's roles
-------------------------------

You assign one or more roles to a user when you `invite <#invite>`__
them to a team in the organization. You can also modify the roles
assigned to a team member. To do so, complete the following steps:

#. Sign in to the |acquia-product:ui|, and then click **Manage** in the
   top menu.
#. In your organization's information card, click **Manage**.
#. On the **Organizations > Team management** page, under **Members**,
   on the line that lists the member whose roles you want to change,
   click **Edit roles**.
#. In the **Edit roles** dialog, select the roles you want the team
   member to have, and then click **Continue**.
#. In the confirmation dialog, click **Edit roles**.

.. |Invite members to a team| image:: https://cdn3.webdamdb.com/1280_Q23qfbA937w6.png?1526475918

.. |Invite a member from the Organizations page| image:: https://cdn2.webdamdb.com/md_U1P56zVVpt71.png?1526476110
   :width: 307px
   :height: 518px

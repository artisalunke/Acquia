.. include:: /common/global.rst

Working with teams
==================

You can organize the users who work to develop and manage your
applications into teams and then assign each team to one or more
applications in your organization. When you invite a user to be a member
of a team, you assign a role to the member. When you assign a team to an
application, all of the users on the team can exercise the permissions
of their roles with respect to that application. A user can belong to
more than one team; a team can govern access to more than one
application, and an application can have more than one team assigned to
it. Teams exist within an organization and cannot be assigned to
applications within a different organization. Learn more about
`organizations </acquia-cloud/teams/organizations>`__ and
`roles </acquia-cloud/teams/roles>`__.

To work with your organization's teams, sign in to the
|acquia-product:ui| and go to the
`Manage <https://cloud.acquia.com/app/manage/>`__ page. Note that the
functions of the **Manage** page itself are controlled by the Acquia
roles and permissions system, and to take any of these actions, you need
to be a user with the appropriate role. By default, an *Administrator*
can create and modify teams; a *Team lead* or an *Administrator* can add
users to a team or remove users from a team.

On the **Teams** page, you can:

-  `View teams <#view>`__
-  `Create a team <#create>`__
-  `Assign an application to a team <#addapp>`__

.. _view:

Viewing teams
-------------

#. Sign in to the |acquia-product:ui|, and then click **Manage** in the
   top menu.
#. In your organization's information card, click **Manage**.
#. On the **Organizations** page, click **Team management** in the left
   menu.

The **Organizations > Team management** page has three information cards
in the upper region:

|Information cards on the Team management page|

-  **My information** - Lists your user ID and, under **Details**, the
   role you have in the organization and, under **Membership**, the role
   you have on your teams in the organization
-  **Organization administrators** - Lists the organization's *Owner*
   and *Administrators*. You can contact these people if you need a team
   to be created or other actions to be taken that require the *Owner*
   or *Administrator* role.
-  **Team administrators** - Lists the people who have the ability to
   modify permissions for your teams. You can contact these people if
   you need a user to be invited to a team or if you need different
   roles or permissions for a team you are on.

Under these three information cards is a central menu with three links:

|The central menu on the Team management page|

-  **Members** - View all users who are active members of teams in this
   organization, together with the team name and role. You can invite
   new members, remove members, and modify roles. You can also view
   pending team invitations that have not yet been accepted. For
   details, see `Managing team members </acquia-cloud/teams/members>`__.
-  **Teams** - View all the teams in this organization, together with
   the applications assigned to each team, and its members. You can
   `create a team <#create>`__, `rename <#rename>`__ or
   `remove <#remove>`__ a team, or `assign applications <#addapp>`__ to
   a team.
-  **Applications** - Lists all of the applications in the organization,
   together with the teams assigned to each application. This is
   basically an alternate view of the **Teams** page, organized by
   application rather than by team. You can `assign a
   team <#applications>`__ to an application.

.. _crud:

Creating, renaming, or removing a team
--------------------------------------

The *Owner* or *Administrator* for an organization can create a new
team, or rename or remove an existing team.

.. _create:

Creating a team
~~~~~~~~~~~~~~~

To create a new team, complete the following steps:

#. Sign in to the |acquia-product:ui|, and then click **Manage** in the
   top menu.
#. In your organization's information card, click **Manage**.
#. On the **Organizations** page, click **Team management** in the left
   menu, and then click **Teams** in the central menu.

   |Create a team|

#. Click **Create team**.
#. In the **Team name** field, enter a descriptive name for the team,
   and then click **Add**.

After you create a team, `assign applications to the team <#addapp>`__
and `invite members </acquia-cloud/teams/members>`__ to the team, giving
each member the role that is appropriate for the applications that the
team will be working on.

.. _rename:

Renaming a team
~~~~~~~~~~~~~~~

To rename a team, complete the following steps:

#. On the **Teams** page, click the team's **Rename** link.
#. Enter the new name for the team, and then click **Rename**.

.. _remove:

Removing a team
~~~~~~~~~~~~~~~

To remove (delete) a team from an organization, complete the following
steps:

#. On the **Teams** page, click the team's **Remove** link.
#. In the confirmation dialog box, click **Remove**.

The team is deleted. The team members lose access to any applications to
which they had access by virtue of being members of this team, but their
Acquia accounts are otherwise unaffected. They could still have access
to some or all of the same applications by being members of other teams.

.. _addapp:

Adding an application to a team
-------------------------------

Before members of a team are able to use their roles to work on an
application, you must assign the application to the team. You can do
this either on the **Team management > Teams** page, or on the `**Teams
> Applications** page <#applications>`__. To assign applications to a
team on the **Teams > Teams** page:

#. Sign in to the |acquia-product:ui|, and then click **Manage** in the
   top menu.
#. In your organization's information card, click **Manage**.
#. On the **Organizations** page, click **Team management** in the left
   menu, and then click **Teams** in the central menu.
#. On the **Teams** page, click the team's **Assign apps** link.

   |Click the team's Assign apps link|

#. The **Assign applications** dialog displays all of the applications
   in the organization. You can enter text in the **Filter
   Applications** field to filter applications by name. Select any
   applications you want to assign to the team, and clear the checkbox
   for any applications you want to remove from the team. Then, click
   **Continue**.

   |Assign applications to a team|

#. In the confirmation dialog, review the applications that will be
   assigned to the team, and then click **Assign applications**.

Each member of the team can now access the applications assigned to the
team, with their already assigned team roles.

.. _applications:

Reviewing team and application assignments
------------------------------------------

On the **Team management > Applications** page, you can view all of the
applications in the organization, together with the teams assigned to
each application. If you have many applications, you can use the
**Filter by application** field to limit which applications are
displayed. You can also assign teams to an application.

To assign a team to an application from the **Team management >
Applications** page:

#. Click the application's **Assign teams** link.
#. Select the teams you want to assign to this application, and then
   click **Continue**.
#. In the confirmation dialog box, click **Assign teams**.

.. |Information cards on the Team management page| image:: https://cdn2.webdamdb.com/1280_YlHpW4v1pOO0.png?1526475901
   ;alt: Information cards on the Team Management page
.. |The central menu on the Team management page| image:: https://cdn4.webdamdb.com/1280_AvvN2CtIgHM2.png?1526475609
   :alt: central menu for team management page
.. |Create a team| image:: https://cdn3.webdamdb.com/1280_g8YEfcGc81.png?1526475987
   :alt: Create a team
.. |Click the team's Assign apps link| image:: https://cdn4.webdamdb.com/1280_oP3SCGq9JbT7.png?1526475690
   :alt: Assign apps link
.. |Assign applications to a team| image:: https://cdn2.webdamdb.com/md_Iq0e7S09zgG5.png?1526475473
   :alt: Assign applications to a team
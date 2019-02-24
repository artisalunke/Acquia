.. include:: /common/global.rst

Working with roles and permissions
==================================

A *role* is a collection of permissions to perform specific operations.
Grouping permissions into roles makes it easier to give and revoke
permission to users, based on their job functions. When you assign a
user to a team in the |acquia-product:ui|, you assign to them a role
that defines what they can and cannot do on the team's applications and
environments.

On the **Manage > Roles** page of the
|cloud-manage|, you can:

-  `View roles <#view>`__
-  `Compare roles <#compare>`__
-  `Create a new role <#create>`__
-  `Edit a role <#edit>`__

.. _roles:

Viewing an organization's roles
-------------------------------

To view the roles that exist in an organization, complete the following
steps:

#. Sign in to the |cloud-ui|,
   and then click **Manage** in the top menu.
#. In your organization's information card, click **Manage**.
#. On the **Organizations** page, click **Roles** in the left menu.

|Select the Roles tab from the left menu|

.. _filter:

Filtering roles
~~~~~~~~~~~~~~~

If you have many custom roles, you can filter the roles displayed on the
**Roles** page. To filter roles, enter text in the **Filter Roles**
field. As you type, the **Roles** page displays only the roles whose
name matches your filter string.

.. _view:

Viewing a role's permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can view the permissions granted to a role by clicking **View** next
to the role's name. You can also view the permissions by
`comparing <#compare>`__ two or more roles.

.. _default:

Default roles
-------------

By default, all organizations have four roles:

-  *Administrator*
-  *Team lead*
-  *Senior developer*
-  *Developer*

If the allocation of permissions to these roles matches your workflow
and business needs, you can use them as-is. You can also create new
custom roles or edit the default roles so that their permissions work
best with the way your organization runs.

The *Administrator* role cannot be edited; it always includes all
possible permissions. An *Administrator* has that role for the entire
organization; it is not limited by membership on a team. An
organization's *Owner* or *Administrator* can `edit the other default
roles <#edit>`__ (including changing the name of a default role) and can
`create <#create>`__, edit, and remove custom roles.

.. _compare:

Comparing roles
---------------

You can select two or three existing roles and compare their
permissions. To compare roles:

#. Sign in to the |acquia-product:ui| as an organization owner or
   administrator.
#. Select your organization and then click **Teams** in the top menu.
#. On the **Organizations** page, click **Roles** in the left menu.
#. Select the roles that you want to compare.
#. Click **Compare roles**.

The **Compare roles** page displays the permissions for the roles you
selected. Permissions granted to a role show a green checkbox, while
permissions not granted to a role show a black lock icon.

|Comparing roles|

.. _create:

Creating a custom role
----------------------

An *Owner* or *Administrator* can create custom roles within an
organization, in addition to the default roles (*Administrator*, *Team
lead*, *Senior developer*, and *Developer*). A custom role can be
created only if the organization includes at least one team. Once a
custom role is created, it can be assigned to team members in the
organization instead of or in addition to a default role. To create a
custom role, complete the following steps:

#. Sign in to the |acquia-product:ui| as an *Owner* or *Administrator*,
   and then click **Manage** in the top menu.
#. In your organization's information card, click **Manage**.
#. On the **Organizations** page, click **Roles** in the left menu.
#. Click **Create role**.
#. Enter a name and description for the role.
#. Optionally, select an existing role whose permissions you want to
   copy as a starting point. See `Copying a role <#copy>`__.
#. Select the permissions that you want to give to the new custom role.
#. Click **Create role**.

.. _edit:

Editing a role
--------------

You can edit an existing role, including the default *Team lead*,
*Senior developer*, and *Developer* roles, as well as custom roles
created for your organization. You cannot edit the *Administrator* or
*Owner* roles; those users always have all possible permissions.

To edit a role:

#. Sign in to the |acquia-product:ui| as an *Owner* or *Administrator*,
   and then click **Manage** in the top menu.
#. In your organization's information card, click **Manage**.
#. On the **Organizations** page, click **Roles** in the left menu.
#. Click **Edit** for the role that you want to edit.

   |Editing a role|

#. Add a permission to the role by selecting the checkbox for that
   permission; remove a permission by clearing the checkbox for that
   permission. You can also `copy an existing role <#copy>`__, then
   modify it, or select all or none of the permissions.
#. Click **Update role**.

After a role has been modified, its description lists the user who last
edited it.

.. _copy:

Copying a role
~~~~~~~~~~~~~~

You may want to create or edit a role so that it has most of the
permissions of an existing role, but differs by just a few permissions.
While creating or editing a role, you can copy the permission set of a
different existing role. To do this, select the role you want to copy
from in the menu under **Copy permissions from existing role**. This
sets the current role's permissions to be identical to those of the
other role. You can then make the permission modifications you want,
then click **Update role**.

.. _assign:

Assigning roles to users
------------------------

You assign one or more roles to a user when you add or invite them to a
team in the organization. A user can have different roles on different
teams. You can also modify the roles assigned to a user on the
**Members** section of the **Organizations > Team management** page. For
more information, see `Managing team
members </acquia-cloud/teams/members>`__.

.. |Select the Roles tab from the left menu| image:: https://cdn2.webdamdb.com/md_UA5NaTFq6QY3.png?1526475656
   :alt: Select the Roles tab from the left menu
.. |Comparing roles| image:: https://cdn2.webdamdb.com/md_E8yYyr8sncj5.png?1526476017
   :alt: Comparing roles
.. |Editing a role| image:: https://cdn3.webdamdb.com/md_of8Cz2dQrlw5.png?1526476065
   :alt: Editing a role

.. |cloud-manage| replace:: \ |acquia-product:ui|\ 
.. _cloud-manage: https://cloud.acquia.com/app/manage

.. |cloud-ui| replace:: \ |acquia-product:ui|\ 
.. _cloud-ui: https://cloud.acquia.com/

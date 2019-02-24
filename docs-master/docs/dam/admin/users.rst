.. include:: /common/global.rst

Managing users and groups
=========================

.. container:: message-status

  The information on this page applies only to users that have
  `Admin <#role>`__ role type permissions.

Because different users of |acquia-product:dam| require different levels
of access to your stored assets, you can control access through the use
of `roles <#role>`__, which can be assigned to individual
`users <#user>`__, or to a `group <#group>`__ of users with similar
needs.

.. _role:

Role types
----------

Role types are used to control access in |acquia-product:dam|, making
different features and asset items available to those users who require
access to them. There are four types of roles with varying access and
permissions:

-  End users

   -  *Brand Portal* - Can view and download assets in
      |acquia-product:bc|
   -  *Regular User* - Can view and download assets in both
      |acquia-product:dam| and |acquia-product:bc|

-  Power users

   -  *Contributor* - Can view, download, upload, edit, move, and delete
      assets in both |acquia-product:dam| and |acquia-product:bc|
   -  *Admin* - Full asset and folder permissions in both
      |acquia-product:dam| and |acquia-product:bc|
      These users can also configure the system preferences, metadata
      schema, |acquia-product:bc|, user permissions, and group
      permissions.

.. list-table::
  :header-rows: 1

  * - Feature
    - *Brand Portal*
    - *Regular User*
    - *Contributor*
    - *Admin*
  * - Access to Acquia DAM
    - |no|
    - |yes|
    - |yes|
    - |yes|
  * - Access to Brand Connect
    - |yes|
    - |yes|
    - |yes|
    - |yes|
  * - View and download assets
    - |yes|
    - |yes|
    - |yes|
    - |yes|
  * - Collaborate
    - |yes|
    - |yes|
    - |yes|
    - |yes|
  * - Asset/Folder management
    - |no|
    - |no|
    - |yes|
    - |yes|
  * - Edit permissions and configure metadata
    - |no|
    - |no|
    - |no|
    - |yes|

.. _group:

Groups
------

To help you manage the distribution of role types to your users,
|acquia-product:dam| includes the ability to group collections of users,
which can then be assigned a role type.

Group types
~~~~~~~~~~~

|acquia-product:dam| includes two `default groups <#group-default>`__
for your use, but you can also create `custom groups <group-custom>`__
for your specific needs.

.. _group-default:

Default groups
^^^^^^^^^^^^^^

There are two groups included with |acquia-product:dam| that all users
belong to, by default:

-  *Guest* - Use the Guest group to control access for a user that is
   not currently signed in or lacks sign-in credentials. Any folders
   that can be viewed or downloaded by the general public can be
   configured using the Guest group.
-  *Logged In* - Use the Logged In group to control access for a user
   with login credentials. Any folders that can be viewed and downloaded
   by any signed-in user can be configured using the Logged In group.

.. note::
  User membership assignment for these groups is handled by
  |acquia-product:dam| — you do not need to manually add users to these
  groups.

.. _group-custom:

Custom groups
^^^^^^^^^^^^^

|acquia-product:dam| supports the creation of custom groups that you can
use to organize your users for role assignments. To create a custom
group, complete the following steps:

#. Sign in to |acquia-product:dam|, click **Teams** in the top
   navigation, and then click **Groups**.
#. Click the plus icon ( **+** ) on the actions toolbar.
#. In the **Role (Type)**, click the role that you want to use for the
   group, from the following list:

   -  **Brand Portal**
   -  **Regular User**
   -  **Contributor**

#. Enter the option group name. The name is visible only to users with
   the *Admin* role.
#. Specify which image and video download
   `presets </dam/admin/system>`__ the group will have access to.
#. Click **Save**.
   |acquia-product:dam| will display the permissions grid dialog box.
#. `Edit the permissions of the group <group-perms>`__.
#. Click **Save**.

.. _group-perms:

Editing a group's folder permissions
------------------------------------

#. Sign in to |acquia-product:dam|, click **Teams** in the top
   navigation, and then click **Groups**.
#. Click the wrench icon |Wrench icon| in the **Actions** column for the
   group that you want to update, and then click **Permissions**.

   |Selecting Permissions for a group|

#. Specify which folders and nested folders the group should have
   permission to access. For a group to have access to a nested folder,
   they need view permission to the parent folder.

   .. note::
      The Default row can be used to set permissions for new parent-level
      folders. By default, new nested folders obtain the permissions of the
      parent folder.

   -  **View** column - Select the box to allow the group to view a
      folder.
   -  **Download** column - Click the list, and then click the
      appropriate download option from the following list:

      -  **Allow** - The group can download the original asset as well
         as predefined image and video download presets.
      -  **Download presets** - The group can download a
         `preset </dam/admin/system>`__ file version, but not the
         original version.
      -  **Do not allow** - Disables the group from downloading.
         When this option is selected, the *Admin* can allow users in
         the group to request a download by enabling download requests
         globally in system preferences or at a folder level in the
         folder’s advanced options.

   -  Contributor groups will have additional options to upload, edit,
      move and delete assets and folders. Select the check box in each
      appropriate column.

   You can update the permissions for multiple folders at once by
   selecting the check boxes in the orange column, and then specifying
   the permission access in the top orange row.

   |Editing a folder's permissions|

#. To apply permissions to nested folders, in the **Apply to Nested**
   column, set the value for the parent folder to **Yes**.

   .. note::
      The option will always default to **No**. The option can be updated
      when changing the permissions for a specific folder.

#. Click **Save**.

.. _group-edit:

Editing a group
---------------

Depending on a group's type, you can modify an existing group's
configuration:

-  Custom groups - The role type, name, description, image download
   presets, and video download presets can be edited.
-  Default groups - The image and download presets can be edited for the
   Logged In group, but the Guest group cannot be edited.

To modify a group's configuration, complete the following steps:

#. Sign in to |acquia-product:dam|, click **Teams** in the top
   navigation, and then click **Groups**.
#. Click the group name. You can also click the wrench icon |Wrench
   icon| in the row of the group you want to edit, and then click **Edit
   group**.
#. Edit the group's settings, based on the following fields:

   -  **Role (Type)**
   -  **Name**
   -  **Description**
   -  **Image Download Presets**

      -  **Allow users to**

   -  **Video Download Presets**

      -  **Allow users to**

#. Click **Save**.

.. _group-delete:

Deleting a group
----------------

You can delete any custom group that you no longer require. Default
groups cannot be deleted. To delete a custom group, complete the
following steps:

#. Sign in to |acquia-product:dam|, click **Teams** in the top
   navigation, and then click **Groups**.
#. Click the plus icon ( **+** ), and then click **Delete group**.
#. Click **Yes** to confirm.

.. _group-message:

Sending messages to groups
--------------------------

Click the email icon |Email icon| to send a message to specific groups
or all the groups. Users will receive an email and an in-system
notification.

.. _group-folder-perm:

Editing the group permissions of a folder
-----------------------------------------

You can also configure which groups have permission to specific folders
at the folder level. To do this, complete the following steps:

#. Sign in to |acquia-product:dam|.
#. Select the folder that you want to change, click the pencil icon
   |Pencil icon|, and then click **Permissions**.
#. `Edit the permissions of the folder <#group-perms>`__.
#. To apply permissions to nested folders, select the **Apply changes to
   all nested folders** check box.
#. Click **Save**.

.. _user:

Users
-----

To access |acquia-product:dam| users must have associated user accounts,
which can then be assigned to role types and associated with groups.

.. _user-create:

Creating a user
~~~~~~~~~~~~~~~

#. Sign in to |acquia-product:dam|, click **Teams** in the top
   navigation, and then click **Users**.
#. Click the plus icon ( **+** ) on the actions toolbar.
#. Enter the account information for the new user account. The
   **Username**, **Email**, **First Name**, and **Last Name** fields are
   required.
   If you do not select the ****\ Send user an email with account
   details check box, you will need to alert the user that an account
   has been created for them.
#. Click **Save**.

.. admonition:: Notes

  -  New users are assigned the *Brand Portal* role type and Guest and
     Logged In group memberships.
  -  Users can belong to several groups, and will receive the combined
     permissions of all groups they belong to.
  -  Users can be added to groups under either the Users or Groups
     section.
  -  Users must have an active status to sign in to |acquia-product:dam|.
  -  You may need to update a user’s role to add him or her to a group.

.. _user-group-affil:

Adding or removing a group affiliation from a user
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Sign in to |acquia-product:dam|, click **Teams** in the top
   navigation, and then click **Users**.
#. In the **Groups** column, select the item that you want to edit.
   Either add groups or click **X** for the groups that you want to
   remove. |br|
   You may have to change a user’s role to add the user to a group.

   |Selecting a group|

#. To batch add users to groups, check the check boxes for the users
   that you want to update. Click the wrench icon |Wrench icon| on the
   actions toolbar, and then click **Add to group**.
#. Click **Save**. Changes will be saved for you while editing in the
   main interface.

.. _user-group:

Adding or removing users from groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add or remove users from a group, complete the following steps:

#. Sign in to |acquia-product:dam|, click **Teams** in the top
   navigation, and then click **Groups**.
#. Click the number in the **Members** column of the group.
#. Update the users, depending on your needs for the group:

   -  *Adding users* - Click the field under **Add Users to this
      Group**, and then search for one or more users. Click the ones you
      want to add.
      You may need to update a user’s role to add the user to a group.
      To change roles, click **Teams**, and then click **Users**.
   -  *Removing users* - Click the minus icon ( **-** ) next to the
      users that you want to remove from the group.

#. Click **Save**.

.. _user-edit:

Editing users
~~~~~~~~~~~~~

To edit a user's account information, complete the following steps:

#. Sign in to |acquia-product:dam|, click **Teams** in the top
   navigation, and then click **Users**.
#. Click the username whose details you want to edit. You can also click
   the wrench icon |Wrench icon| in the row of the user that you want to
   edit, and then click **Edit user**.
#. Edit the user's information.
#. Click **Save**.

.. _user-delete:

Deleting users
~~~~~~~~~~~~~~

To delete a user account from |acquia-product:dam|, complete the
following steps:

#. Sign in to |acquia-product:dam|, click **Teams** in the top
   navigation, and then click **Users**.
#. Click the wrench icon |Wrench icon| in the row of the user that you
   want to delete, and then click **Delete user**.
   To batch delete users, click the check boxes for the users that you
   want to delete, click the wrench icon |Wrench icon| on the actions
   toolbar, and then click **Delete**.
#. Click **Yes** to confirm.

.. _user-status:

Updating a user's status
~~~~~~~~~~~~~~~~~~~~~~~~

To be able to sign in to |acquia-product:dam|, a user's account must be
active. If you deactivate a user's account, their account information
will continue to be tracked by |acquia-product:dam|, but the user will
not be allowed to sign in. To modify a user's status, complete the
following steps:

#. Sign in to |acquia-product:dam|, click **Teams** in the top
   navigation, and then click **Users**.
#. Find the user you want to modify, and in the **Status** column, click
   the icon to activate or deactivate the user's account, based on the
   following:

   -  |Active user icon| - User account is active
   -  |Inactive user icon| - User account is inactive

   To batch change user statuses, click the check boxes for the users
   that you want to change, click the wrench icon |Wrench icon| on the
   actions toolbar, and then click **Activate** or **Deactivate**.

.. _user-adv:

Additional user management options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To export all of your |acquia-product:dam| users' account information to
a ``.CSV`` file, click the export icon |Export icon| on the actions
toolbar.

To customize the columns displayed on the Users page, click the columns
icon |Columns icon|\ next to the search box. The columns on the Users
page will revert back to their default organization when you navigate
away from the page.

.. |Wrench icon| image:: https://cdn4.webdamdb.com/100th_sm_Y2YSPX4rcZ41.png?1526476131
   :width: 23px
   :height: 23px
.. |Selecting Permissions for a group| image:: https://cdn2.webdamdb.com/1280_wWf5d1akNT30.png?1526475626
   :width: 549px
   :height: 324px
.. |Editing a folder's permissions| image:: https://cdn2.webdamdb.com/1280_A0T3JFebUUp6.png?1526475453
   :width: 800px
   :height: 400px
.. |Email icon| image:: https://cdn2.webdamdb.com/100th_sm_2Tm1BmMkig11.png?1526475488
   :width: 23px
   :height: 23px
.. |Pencil icon| image:: https://cdn4.webdamdb.com/100th_sm_wdYPNKduP052.png?1526475946
   :width: 23px
   :height: 23px
.. |Selecting a group| image:: https://cdn4.webdamdb.com/1280_levQKivuC57.jpg?1526476016
   :width: 224px
   :height: 122px
.. |Active user icon| image:: https://cdn2.webdamdb.com/100th_sm_QgXnPsrWAyL9.png?1526476104
   :height: 23px
.. |Inactive user icon| image:: https://cdn3.webdamdb.com/100th_sm_Qt47hGLm7Sw3.png?1526476103
   :height: 23px
.. |Export icon| image:: https://cdn4.webdamdb.com/100th_sm_MHCHCylaqRS8.png?1526475724
   :width: 23px
   :height: 23px
.. |Columns icon| image:: https://cdn3.webdamdb.com/100th_sm_UjGTvNySto31.png?1526475746
   :width: 23px
   :height: 23px

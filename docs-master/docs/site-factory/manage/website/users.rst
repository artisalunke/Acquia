.. include:: /common/global.rst

Managing site group users
=========================

`Site groups </site-factory/manage/website/manage#group>`__ allow you to
organize your websites into logical groups (such as by product line or
geographic area). You can also use your site groups to control which
users have access to the websites in the |acquia-product:sfi|.

When users who don't have the |platform admin|_ role sign in to the
|acquia-product:sfi|, they can view only websites in groups to which
they have access, as well as all websites that don't belong to any
group.

.. |platform admin| replace:: *Platform admin*
.. _platform admin: /site-factory/users/admin/platform-admin

Groups can contain the following member types:

-  **Group member** - Can view and access websites and site collections
   contained by the group
-  **Group administrator** - Same permissions as a group member, but can
   also add or remove other group members (except for the group owner)
-  **Group owner** - This is the user account that created the group.
   The group owner has the same permissions as a group administrator,
   but can delete the group

.. note::  

   -  Users with the platform admin role can access all groups and
      websites, can add or remove members from any group, and can delete
      any group displayed in the |acquia-product:sfi|.
   -  You cannot make another user account the group owner for a group.

Adding group members
--------------------

To allow a user to access a group (and the websites that it contains):

#. Go to the group's detail page.
#. In the **Members** section, click **Manage** to open the **Manage
   users** page.

   |Manage users|

#. Enter an existing |acquia-product:sfi| user name in the **Username**
   field. The **Manage users** page displays user accounts that match
   your entry as you type.
#. Click **Add user**.
#. Click **Save**.

The user account is now a member of the current group and all of its
subgroups.

Removing group members
----------------------

To remove users from a group:

#. Go to the group's detail page.
#. In the **Members** section, find the user accounts that you want to
   remove from the group.
#. Click the minus icon for each user that you want to remove.

   |Remove user|

#. Click **Remove** on the confirmation page.

The users are no longer members of the group or its subgroups, and if
they don't have the platform admin role, they can no longer view the
websites contained by the group or subgroups in the
|acquia-product:sfi|.

.. note::  

   You cannot remove the group owner account from a group.

Changing a member's type
------------------------

To increase or decrease a user account's permissions for a group that
they already have access to:

#. Go to the group's detail page.
#. In the **Members** section, click **Manage**.
#. In the **People in this group** section, find the user account for
   which you want to modify its permissions.
#. Select from the following options to increase or decrease group
   permissions:

   |Group membership permission options|

   -  To make a group member a group administrator, click **Make group
      admin**.
   -  To make a group administrator a group member, click **Remove group
      admin**.

#. Click **Confirm** to confirm the permission change.

.. |Manage users| image:: https://cdn4.webdamdb.com/1280_IVIFdw8onN02.png?1527085465
   :width: 750px
   :height: 409px
.. |Remove user| image:: https://cdn2.webdamdb.com/1280_w7SlcCyOLA01.png?1527085482
   :width: 750px
   :height: 353px
.. |Group membership permission options| image:: https://cdn4.webdamdb.com/1280_gKWJqkv82JY4.png?1527085487
   :width: 750px
   :height: 283px

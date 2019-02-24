.. include:: /common/global.rst

Creating sites and site groups
==============================

Whether you have an existing set of |acquia-product:edg| websites or
you're creating your first website, use the procedures on this page to
`create new websites <#website>`__ and the `groups <#group>`__ that you
can use to organize your websites.

.. |platform admin| replace:: *Platform admin*
.. _platform admin: /site-factory/users/admin/platform-admin

.. |site builder| replace:: *Site builder*
.. _site builder: /site-factory/users/admin/site-builder

Creating new websites
---------------------

To create a new |acquia-product:edg| website, complete the following
steps:

#. `Sign in </site-factory/manage/login>`__ to the |acquia-product:sfi| 
   using a user account with either the |platform admin|_ or |site builder|_ role.
#. In the top menu, click **Sites**.
#. In the left sidebar, click the group in which you want to create your
   new website.
#. Click **Create a new site**.

   |Create a new site button|

#. In the **Site URL** field, enter a name for the website, which will
   become part of its internal URL. Because of this, the **Site URL**
   has the following naming requirements:

   -  Can contain only alphanumeric characters—no special characters
   -  Can be up 30 characters, with a minimum size of one character
   -  Cannot share a name with any other website or site collection in
      the |acquia-product:sfi|

#. If you have more than one `stack </site-factory/tiers/stacks>`__, in
   the **Available stacks** table, select the stack in which you want to
   create your new website.
#. If you have more than one `installation
   profile </site-factory/workflow/profiles>`__ in your codebase, in the
   **Select an installation profile** table, select the installation
   profile that you want to use for your new website.

   .. note::  

      You cannot change a website's installation profile after the website
      is created.

#. Click **Create site**.

|acquia-product:edg| creates your new website in a location that depends
on the |acquia-product:sfi| page that you're currently viewing:

-  *Group detail page* – Creates a website that belongs to the group you
   were viewing when you clicked **Create a new site**.
-  *Site collection page* – Creates a website that is a secondary site
   in the site collection that you were viewing. For information about
   site collections, see `Site
   collections </site-factory/manage/website/site-coll>`__.

.. note::  

   -  If |acquia-product:edg| does not display any available groups on the
      page, you must be added to a group by either a user with the
      *platform admin* role or a group administrator.
   -  If you don't see **Create a new site** for the group or site
      collection, be sure that your user account has either the *platform
      admin* or *site builder* role.

Creating groups and sub-groups
------------------------------

To create a new group or sub-group:

#. On the **All my sites** or **All my groups** page's action button,
   click **New group** (or **New sub-group** if you're creating a
   sub-group in an existing group or sub-group).

   |Create a new group|

   .. note::  

      Only users with the *platform admin* role can create top-level groups
      on the **All my sites** or **All my groups** pages.

#. Enter a **Title** for the new group.
#. Select the **Parent** group for the group or sub-group that you're
   creating.

   The Parent list displays all of the groups and sub-groups to which
   you have access. If you have the *platform admin* role, you can also
   create the group at the top level, with no parent group.

#. Click **Create group** (or **Create sub-group** if you're creating a
   sub-group in a group).

After |acquia-product:edg| creates your new group or sub-group, it
displays the new group's detail page.

|New group detail page|

Use this page to view the sites, site collections, and sub-groups
contained by the group, as well as its group members. For more
information about configuring user access to groups (including the sites
and site collections they contain), see `Managing site group
users </site-factory/manage/website/users>`__.

.. note::  

   Sub-groups inherit the group membership lists of their parent groups or
   sub-groups. If you add or remove members to a parent group, the group's
   sub-groups reflect the membership change.


Editing and deleting groups
---------------------------

For information about managing your existing groups, including editing
their information or deleting them from the management interface, see
`Managing site groups </site-factory/manage/website#group>`__.

.. |Create a new site button| image:: https://cdn4.webdamdb.com/1280_sOeeMmRkB51.png?1526475870
   :width: 750px
   :height: 357px
.. |Create a new group| image:: https://cdn3.webdamdb.com/1280_Q00azOnrUZJ0.png?1526476060
   :width: 750px
   :height: 370px
.. |New group detail page| image:: https://cdn4.webdamdb.com/1280_EpMt5iugDjR1.png?1526475768
   :width: 750px
   :height: 385px

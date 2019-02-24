.. include:: /common/global.rst

Managing site groups
====================

|acquia-product:edg| `groups </site-factory/manage/website#group>`__
allow you to separate your websites and `site
collections </site-factory/manage/website/site-coll>`__ into
organizational units that that mirror your organization's structure. For
example, you can create groups that contain |acquia-product:edg|-hosted
websites from different organizational units (such as Finance,
Marketing, or Support) or geographic regions (including North America,
Europe, or Asia/Pacific).

For information about naming your |acquia-product:edg| elements, see
`Organizing your websites, collections, and
groups </site-factory/manage/website/organize>`__.

You can manage site groups (including editing and deleting groups, and
adding or removing websites and site collections) from the site group
detail page.

.. note::  

   Although groups and subgroups are slightly different in the
   |acquia-product:sfi| (groups exist only at the top level and have no
   parent group, and subgroups have a group or subgroup parent), this page
   uses the general term of groups unless there's a need to be specific.

To view a group's detail page:

#. `Sign in to the |acquia-product:sfi| </site-factory/manage/login>`__.
#. Click the **All my groups** link to view a detailed list of the
   groups you're a member of and their contents.

   |All my groups page|

#. Find the group for which you want to view its detail page, and then
   click its name from either the menu on the left, or from the detailed
   listing.

   |Group name links|


Group detail page interface
---------------------------

|Group detail page overview|

#. Site group name
#. Number of websites and site collections and number of group members
   in the group
#. Methods to change the group name or location
#. Website sorting and group management options
#. Subgroups of the group
#. Websites and site collections in the group
#. User accounts that can access and view the group

Changing the group name
-----------------------

To change the name of a group that you previously created:

#. Go to the group's detail page.
#. Click **Edit group**.
#. Enter the new name for the group in the **Title** field.
#. Click **Save**.

The group detail page displays the new group name.

Moving the group
----------------

To change a group's parent group to another group, or to change a
subgroup to a top-level group:

#. Go to the group's detail page.
#. Click **Edit group**.
#. In the **Parent** list, click the new parent group or level of the
   current group.

   Users with the |platform admin|_ role can click
   **No parent group** to move the group to the top level.

#. Click **Save**.

.. |platform admin| replace:: *Platform admin*
.. _platform admin: /site-factory/users/admin/platform-admin

The group (along with its websites, site collections, and any subgroups
it contains) is moved to its new location with a new parent. The group
that you moved does not inherit group members from its new parent group.

Promoting a subgroup to a group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also make a subgroup a top-level group from the parent group's
detail page. To do so:

#. Go to the parent group's detail page.
#. In the **Sub-groups** section, find the subgroup that you want to set
   as a top-level group.
#. Click the minus icon to the right of the subgroup name.
#. Click **Remove**.

The subgroup (along with its websites, site collections, and subgroups)
is moved out of its existing parent group and is now a top-level group.

Adding sites and site collections
---------------------------------

To add a previously created website or site collection to a group:

#. Go to the page in the |acquia-product:sfi| that contains the websites
   or site collections that you want to add to a group (such as the All
   my sites page or the All my groups page).
#. Select the websites or site collections that you want to add to the
   group.

   |Selecting sites|

   |acquia-product:edg| enables the **Move** and **Remove** buttons.

#. Click **Move**.
#. In the To these groups list, select the group or groups to which you
   want to add the selected websites and site collections.
#. Click **Next**.

|acquia-product:edg| moves the selected websites and site collections to
the group or groups you selected and returns you to the All my sites
page.

Removing sites and site collections
-----------------------------------

To remove a website or site collection from a group:

#. Go to the group's detail page.
#. Select the websites or site collections that you want to remove from
   the group.

   |Selecting sites|

   |acquia-product:edg| enables the **Move** and **Remove** buttons.

#. Click **Remove**.
#. To confirm the removal of the selected websites and site collections
   from the group, click **Confirm**.

The websites and site collections that you selected are no longer in the
group. This process does not remove the selected websites and site
collections from other groups that they belong to. If this was the only
group that contained the removed website or site collection, you can now
find only the removed website or site collection on the All my sites
page.

Deleting a group
----------------

To delete a group from |acquia-product:edg|:

#. Sign in to |acquia-product:edg| as either the Group owner member of
   the group you want to delete or a user with the *`platform
   admin </site-factory/users/admin/platform-admin>`__* role.
#. Go to the group's detail page.
#. Click **Edit group**.
#. Click **Delete**.
#. To determine what |acquia-product:edg| does with the group's
   websites, site collections, and group member accounts, select from
   the following options:

   -  **Nothing, just remove the group** - Websites and site collections
      not contained by any other group are now displayed only on the All
      my sites page.
   -  **Merge all the group's sites with the group below** - Select a
      **Destination group** to which you want to move the websites and
      site collections contained by the group that you're deleting.
   -  **Merge all the group’s sites and members with the group below** -
      Select a **Destination group** to which you want to move the
      websites, site collections, and group member accounts contained by
      the group that you're deleting.

      .. note::  

         When you move user account permissions, the user accounts do not
         gain group administrator privileges for the group, even if they
         were group administrators of the deleted group.

#. Click **Delete group**.

.. |All my groups page| image:: https://cdn4.webdamdb.com/1280_2CT219akCw81.png?1526475892
   :width: 540px
   :height: 353px
.. |Group name links| image:: https://cdn4.webdamdb.com/1280_IXcS9TXiO641.png?1526475508
   :width: 540px
   :height: 113px
.. |Group detail page overview| image:: https://cdn4.webdamdb.com/1280_QJsZHNVnAX14.png?1526475673
   :width: 540px
   :height: 340px
.. |Selecting sites| image:: https://cdn3.webdamdb.com/1280_QhJqv8H1Ojj5.png?1526475803
   :width: 540px
   :height: 340px

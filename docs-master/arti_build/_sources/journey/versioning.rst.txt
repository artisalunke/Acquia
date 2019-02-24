.. include:: /common/global.rst

Creating and managing versions
==============================

.. container:: message-status

  This feature requires that you have the `Admin
  role </journey/admin/users/roles>`__ for your project.

|acquia-product:aj| includes project version control that allows
snapshots to be created at any time. The snapshot includes journeys,
graphs, metrics and connections.

Accessing a project's versions
------------------------------

To review or modify your project's versions, complete the following
actions:

#. Go to the **Admin** page, and then click **Projects** in the left
   menu.
#. Find your project in the project list, and then click its project
   name.
#. In the project's detail view, click **Versions**.

|Version list|

Creating a new version
----------------------

To create a new version, complete the following actions:

#.  From the project's versions detail view, click **Publish New Version**.
#.  In the **Name** field, enter a description for the version.

    .. note:: |acquia-product:aj| prepends a tag to your saved version name, of the
              form ``vX`` (where ``X`` is an integer starting at 1).

#.  Click **Save**.

A locked snapshot of the project is created and displayed in the
versions detail view.

.. note:: You cannot delete previously-created versions.

Selecting the current version
-----------------------------

The current version that is viewed in the editor windows and is also
used for deployed graphs can be any of the published versions in the
list or it can be the current unlocked version.

To change the current version, select the version that you want to
switch to from the list, and then click its checkmark icon ( |Checkmark
icon| ).

When you select a version, the **Active Version** will update to display
the version number, and the version's name will display a locked padlock
( |Padlock icon| ).

|Selecting a version|

Deployed graphs and graphs displayed in the editor will now include this
locked version. The page will be disabled, preventing the ability to
edit the graph. The locked padlock will appear at the top of the page,
along with the version description.

You can view a different version by clicking on the list and selecting
the version from the list. To resume editing, select the version that
you want to switch to from the list, and then click its checkmark icon.
The **Active Version** will change to **Current** and will display an
unlocked padlock ( |Unlocked icon| ).

Restore and archive
-------------------

It is possible to revert to a previous version and make that version the
current version. If you want to save any changes that you have before
restoring an old version, you should first publish a new version before
restoring a previous one.

When you restore a version, it will archive any future versions ahead of
the version that you are restoring. This allows you to return to the
original version stream at a later date, if this is just a temporary
change. For example, if you have three versions, restoring ``v2``
archives ``v3`` under ``v2``. To return to the latest version, click
**Restore Archive** for the ``v3`` version.

Archives that are restored will reapply all versions in that archive. In
the case of nested archives, |acquia-product:aj| will restore only the
top level of archives, but will open the next level to be restored, if
needed.

.. |Version list| image:: https://cdn2.webdamdb.com/1280_IvOl4x0ElLB5.png?-62169955200
   :width: 758px
   :height: 551px
.. |Checkmark icon| image:: https://cdn4.webdamdb.com/1280_At2JULYleMY8.png?-62169955200
   :width: 16px
   :height: 16px
.. |Padlock icon| image:: https://cdn2.webdamdb.com/1280_cSi1rzUfPq35.png?-62169955200
   :width: 21px
   :height: 21px
.. |Selecting a version| image:: https://cdn3.webdamdb.com/1280_gDC0puvUTU02.png?1526475718
   :width: 758px
   :height: 551px
.. |Unlocked icon| image:: https://cdn3.webdamdb.com/1280_kO6IwqGvU4a0.png?1526475761
   :width: 23px
   :height: 23px

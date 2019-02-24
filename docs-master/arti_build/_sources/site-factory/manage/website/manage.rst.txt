.. include:: /common/global.rst

Managing sites on a cluster
===========================

Although keeping track of a single website can be easy, the process can
become more difficult when you have more websites to keep track of. If
you have to manage many websites (30 or more), the process can become
seemingly impossible.

To help you manage your websites, |acquia-product:edg| includes a
website management interface, the |acquia-product:sfi|, that enables you
to `organize your websites into related groups <#group>`__ and more
effectively manage your organization's websites.

|The Site Factory Management Console|

Signing in to |acquia-product:edg|
----------------------------------

To view all of your websites, you must first `sign in to the
|acquia-product:sfi| </site-factory/manage/login>`__, which contains the
websites that you can access and view.


Site actions
------------

|Expanded site actions menu|

Depending on your `user role </site-factory/users/admin>`__, you can
complete several actions on the sites to which you have access.

To select an action for a website, open
the website's actions menu and then click an option:

-  Log in - Signs in to the website with the OpenID administrative
   account that you used to log in to |acquia-product:edg|.
-  `Clear caches </site-factory/manage/website/cache>`__ - Clears
   your website's site- and Varnish-cached content.
-  `Configure Terms of
   Service </site-factory/manage/website/tos#persite>`__ - Opens a
   site management page to allow you to set the terms of service notice
   for this website. A site-based terms of service notice overrides any
   global terms of service notice.
-  `Delete site </site-factory/manage/website/delete>`__ - Opens a
   site management page that allows you to permanently delete this site
   and its content.
-  `Duplicate site </site-factory/manage/website/duplicate>`__ -
   Opens a site management page that allows you to create a copy of this
   website to create a new website.
-  `Manage domains </site-factory/manage/website/domains>`__ - Opens
   a site management page that allows you to add domain names to this
   website.
-  `Transfer site
   ownership </site-factory/users/site-owner#transfer>`__ - Opens a
   site management page that allows you to transfer ownership of this
   website to another user account.

Groups and sub-groups
---------------------

The |acquia-product:sfi| enables you to organize your
|acquia-product:edg| websites into **groups** of websites. You can use
these groups to:

-  Manually sort your websites using logical connections, such as
   regions or business functions.
-  Control sign-in or maintenance access to your websites, by
   controlling which users have access to sites in the group.

.. note::  

   Users with the *platform admin* role can view all sites and groups,
   regardless of their group memberships.

In the |acquia-product:sfi|, the term *groups* describes organizational
groups at the top level, and *sub-groups* describe organizational units
that can contain sites, site collections, and other sub-groups, but have
a single parent group.

The **All my groups** page (displayed when you click the **All my groups
link** on any top-level management interface page) displays an overview
of the groups available to you on the left, and a detailed view of group
contents on the right. The detailed view on the right does not display
top-level groups that do not contain any sites, site collections, or
sub-groups.

For information about how to create groups and organize your
|acquia-product:edg| websites, see `Creating sites and site
groups </site-factory/manage/website/groups-create>`__.

.. |The Site Factory Management Console| image:: https://cdn2.webdamdb.com/1280_Y9Id0XuU6Q06.png?1526475957
   :width: 750px
   :height: 349px
.. |Expanded site actions menu| image:: https://cdn3.webdamdb.com/1280_scnLO4aOJc61.png?-62169955200
   :class: float-right
   :width: 200px
   :height: 399px

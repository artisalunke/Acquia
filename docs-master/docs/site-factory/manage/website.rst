.. include:: /common/global.rst

Site actions and organization
=============================

.. toctree::
   :hidden:
   :glob:

   /site-factory/manage/website/*

After you `sign in </site-factory/manage/login>`__ to the
|acquia-product:sfi|, you can complete management tasks relating to your
websites, including deleting unneeded websites, making duplicate copies
of websites, or organizing websites into related groups of websites.

Website actions
---------------

|Expanded site actions menu| 

To select an action for a website, open the
website's actions menu, and then click an option:

Depending on your |acquia-product:edg| `user
role </site-factory/users/admin>`__, you can complete the several
actions on the sites to which you have access.

-  Log in - Signs in to the website with the OpenID administrative
   account that you used to log in to |acquia-product:edg|.
-  `Clear caches </site-factory/manage/website/cache>`__ - Clears
   your website's site-cached and Varnish-cached content.
-  `Configure Terms of
   Service </site-factory/manage/website/tos#persite>`__ - Opens a
   site management page to allow you to set the terms of service notice
   for this website. Note that site-based terms of service override any
   global terms of service notice.
-  `Delete site </site-factory/manage/website/delete>`__ - Opens a
   site management page that allows you to permanently delete this site
   and its content.
-  `Duplicate site </site-factory/manage/website/duplicate>`__ -
   Opens a site management page that allows you to create a copy of this
   website to create a new website.
-  `Back up site </site-factory/manage/website/backup>`__ - Opens a
   site management page that allows you to create and download backups
   for this website.
-  `Manage domains </site-factory/manage/website/domains>`__ - Opens
   a site management page that allows you to add domain names to this
   website.
-  `Manage theme repository </site-factory/theme/external>`__ -
   Opens a site management page that allows you to connect an external
   theme repository to this website.

Groups and subgroups
--------------------

The |acquia-product:sfi| allows you to organize your
|acquia-product:edg| websites into *groups* of websites. You can use
these groups to do the following:

-  Manually sort your websites using logical connections, such as
   regions or business functions.
-  Control sign-in or maintenance access to your websites by controlling
   which users have access to sites in the group.

.. note::  

   Users with the *platform admin* role can view all sites and groups,
   regardless of their group memberships.

In the |acquia-product:sfi|, the term *groups* describes organizational
groups at the top level, and *subgroups* are organizational units that
can contain sites, site collections, and other subgroups, but have a
single parent group.

The **All my groups** page (displayed when you click the **All my groups
link** on any top-level |acquia-product:sfi| page) displays an overview
of the groups available to you on the left and a detailed view of group
contents on the right. Note that the detailed view on the right does not
display top-level groups that do not contain any websites, site
collections, or subgroups.

For information about how to create groups and organize your
|acquia-product:edg| websites, see `Creating sites and site
groups </site-factory/manage/website/groups-create>`__.

.. |Expanded site actions menu| image:: https://cdn3.webdamdb.com/1280_k9VF5RH9oQg6.png?1526475758
   :class: float-right
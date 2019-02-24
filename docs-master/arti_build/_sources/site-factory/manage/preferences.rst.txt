.. include:: /common/global.rst

Managing global settings for your Factory
=========================================

.. toctree::
   :hidden:
   :glob:

   /site-factory/manage/preferences/sf-perm/
   /site-factory/manage/preferences/tasks/
   /site-factory/manage/preferences/centralized/
   /site-factory/manage/preferences/profiles/
   /site-factory/manage/preferences/site-owner/
   /site-factory/manage/preferences/usage/
   /site-factory/manage/preferences/security/
   /site-factory/manage/preferences/shield/
   /site-factory/manage/preferences/tos/

The **Administration** area of the |acquia-product:sfi| enables users
with the |platform admin|_ role to
configure global settings that affect all of your
|acquia-product:edg|-hosted websites.


.. |platform admin| replace:: *platform admin*
.. _platform admin: /site-factory/users/admin

Managing your settings
----------------------

Users with the *`platform admin </site-factory/users/admin>`__* role can
manage global settings by performing the following steps:

#. `Sign in </site-factory/manage/login>`__ to the |acquia-product:sfi|.
#. In the top menu, click **Administration**.
#. Scroll to the **Site Factory management** section, and then click the
   preference that you want to view or modify.


Available administration settings
---------------------------------

The Administration page allows you to configure the following attributes
of your platform:

-  `Centralized role management </site-factory/users/centralized>`__ –
   Assign `roles </site-factory/users/admin>`__ to users on hosted
   websites based on their |acquia-product:sfi| roles.
-  `Cron jobs </site-factory/manage/tasks>`__ – View, edit, and add cron
   jobs to manage automated tasks on your websites.
-  `Factory information </site-factory/workflow/version>`__ – General
   information about your Factory, including its currently released
   version.
-  `Installation profile
   management </site-factory/manage/preferences/profiles>`__ – Select
   which `installation profiles </site-factory/workflow/profiles>`__
   website creators can select for use when creating a website.
-  `Manage permissions </site-factory/manage/sf-perm>`__ – Configure
   which `roles </site-factory/users/admin>`__ can set the primary
   website of a site collection or manage domains.
-  `Require HTTP authentication </site-factory/users/shield>`__ –
   Protect websites and `site
   collections </site-factory/manage/website/site-coll>`__ during
   development with HTTP authentication.
-  `Security settings </site-factory/users/security>`__ – Manage
   |acquia-product:edg| security settings, such as password strength.
-  `Site ownership settings </site-factory/users/site-owner>`__ –
   Configure website ownership for websites not created by a |platform admin|_.
-  `Subscription Usage </site-factory/manage/usage>`__ – View the number
   of websites used and dynamic requests served by your subscription.
-  `Terms of Service </site-factory/manage/website/tos>`__ – Specify the
   default Terms of Service notice used with each website.

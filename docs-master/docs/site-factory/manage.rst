.. include:: /common/global.rst

Managing your |acquia-product:edg| sites
========================================

.. toctree::
   :hidden:
   :glob:

   /site-factory/manage/website/
   /site-factory/manage/domains/
   /site-factory/manage/ra/
   /site-factory/manage/search/
   /site-factory/manage/cdn/
   /site-factory/manage/ssl/
   /site-factory/manage/preferences/
   /site-factory/manage/files/
   /site-factory/manage/login/
   /site-factory/manage/login-mode/
   /site-factory/manage/browsers/
   /site-factory/manage/sso/
   /site-factory/manage/users/
   /site-factory/manage/*

.. container:: internal-navigation

   **Configuring and using Site Factory**

   * :doc:`Setup </site-factory/setup>`
   * :doc:`Migrate </site-factory/migrate>`
   * Manage
   * :doc:`Workflow </site-factory/workflow>`
   * :doc:`Extend </site-factory/extend>`
   * :doc:`Monitor </site-factory/monitor>`

To help you manage your |acquia-product:edg| websites and their user
accounts, |acquia-product:edg| includes the |acquia-product:sfi|, a
browser-based website management interface that allows you to
effectively organize and work with many websites and users.

Using the |acquia-product:sfi|, you can `administer user
accounts <#user>`__, perform `website management tasks <#website>`__,
and |administer overall settings|_.

.. |administer overall settings| replace:: administer overall \ |acquia-product:edg|\  settings
.. _administer overall settings: #platform

For instructions for signing in to the |acquia-product:sfi|, see |acsfsignin|_.

.. |acsfsignin| replace:: Signing in to \ |acquia-product:edg|\ 
.. _acsfsignin: /site-factory/manage/login

|Site Factory Management Console|

.. |Site Factory Management Console| image:: https://cdn3.webdamdb.com/1280_Y9Id0XuU6Q06.png?-62169955200
   :width: 750px
   :height: 349px

.. container:: message-status

   |Learning Services logo|\ Visit |aalink|_ (sign-in required) for the |tutorial|_ video tutorial. Sign-in required.

.. |Learning Services logo| image:: https://cdn3.webdamdb.com/1280_w1WjsvuWixS1.png?-62169955200
   :class: no-sb float-left logo-sm-lift
   :width: 36px

.. |aalink| replace:: \ |acquia-product:aa|\ 
.. _aalink: https://customers.acquiacademy.com

.. |tutorial| replace:: Setting Up  \ |acquia-product:edg|\ 
.. _tutorial: https://customers.acquiacademy.com


User administration
-------------------

User management on |acquia-product:edg| involves both the roles, access,
and permissions for your |acquia-product:sfi|, and the roles, access,
and permissions for the individual |acquia-product:edg|-hosted websites.
The following user management tasks are available for your use:

-  `Manage users with access </site-factory/users>`__ to your |acquia-product:sfi|
-  `Assign roles to users </site-factory/users/centralized>`__ when they sign in
-  `Configure two-factor authentication </site-factory/users/tfa>`__ in the |acquia-product:sfi|
-  `Select an owner for a specific website </site-factory/users/site-owner>`__
-  `Manage policies for password strength </site-factory/users/security>`__

For information about the permissions matrix for roles on your |acquia-product:sfi|, see |acsfroles|_.

.. |acsfroles| replace:: \ |acquia-product:sfi|\  roles
.. _acsfroles: /site-factory/users/admin

Website management tasks
------------------------

Creating, maintaining, and configuring the individual websites hosted by |acquia-product:edg| is a straightforward process in the |acquia-product:sfi|, allowing you to complete the following common tasks:

-  `Stack configuration and management </site-factory/tiers/stacks>`__
-  `Create new websites or groups of websites </site-factory/manage/website/groups-create>`__
-  `Duplicate existing websites </site-factory/manage/website/duplicate>`__
-  `Backup management </site-factory/manage/website/backup>`__
-  `Theme repository management </site-factory/theme/external>`__
-  `Domain management </site-factory/manage/website/domains>`__

For a full list of tasks, see `Site actions and organization </site-factory/manage/website>`__.

Platform administration tasks
-----------------------------

As part of maintaining your platform, you need to evaluate how |acquia-product:edg| is handling your websites, both for normal use and during code deployments and updates. Also, periodically you may need to make configuration changes that can affect all of your |acquia-product:edg|-hosted websites. The following list includes links to several resources that describe how the |acquia-product:sfi| helps you meet these needs:

-  `Initiate and monitor code deployments </site-factory/workflow/deployments>`__
-  |logmonitor|_
-  |globalmanage|_

.. |logmonitor| replace:: Monitor \ |acquia-product:edg|\  logs
.. _logmonitor: /site-factory/monitor

.. |globalmanage| replace:: Manage global \ |acquia-product:edg|\  settings
.. _globalmanage: /site-factory/manage/preferences
.. include:: /common/global.rst

Working with environments
=========================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/manage/environments/*

The **Environments** page for an application displays each of the
application's `environments </acquia-cloud/glossary#environment>`__.
For each environment, it displays controls and information about the
environment's code, databases, and files.

.. _what:

About environments
------------------

|acquia-product:ac| uses separate environments in order to help you
maintain a clear and orderly workflow as you develop, test, and publish
your applications. An application is deployed on each of its
environments, but each environment may be in a different state, with its
own database and possibly a different code branch or tag deployed. Each
environment has a URL at which its application can be viewed, but only
the Production environment's URL is designed to be visible to the
application's users (website visitors).

How many environments your application has depends on the level of your
Acquia subscription.

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1 

   * - Environment
     - |acquia-product:ace|
     - |acquia-product:acs|
     - |acquia-product:acfs|
   * - Development (Dev)
     - |yes|
     - |yes|
     - |yes|
   * - Staging (Stage)
     - |yes|
     - |yes|
     - |yes|
   * - Production (Prod)
     - |yes|
     - |yes|
     - |no|
   * - `Additional environments </acquia-cloud/manage/more-envs>`__
     - |yes|
     - |no|
     - |no|


Environments are listed in this order:

-  Dev, Stage, and Prod
-  Custom environments
-  `Remote Administration environments </ra/environment>`__
-  |ccd|_


.. |ccd| replace:: \ |acquia-product:ccd|\  environments
.. _ccd: /acquia-cloud/cd/env

.. _manage:

Managing environments
---------------------

On an application's **Environments** page, click the name of an
environment to display its **Overview** page. From the **Overview** page
for an environment, you can:

-  `Manage your code </acquia-cloud/develop/code>`__, including
   switching the tag or branch deployed on the environment, or deploying
   a tag or branch from a different environment.
-  `Manage your databases </acquia-cloud/manage/database>`__, including
   backing up and restoring databases, and copying databases from a
   different environment.
-  `Manage your files </acquia-cloud/manage/files>`__, including copying
   files from a different environment.
-  `Configure the environment </acquia-cloud/manage/configure>`__,
   including PHP settings, production mode, and more.
-  `Clear the Varnish cache </acquia-cloud/performance/varnish#clear>`__
   for the environment.
-  Make a `fresh Drupal installation </acquia-cloud/create/install>`__
   in the environment, overwriting your existing application code and
   database.
-  Activate `Live Development </acquia-cloud/develop/livedev>`__ mode
   for an environment.
-  `Rename </acquia-cloud/manage/environments/actions#rename>`__ the
   environment.
-  Understand your **Site health** by using `Uptime
   monitoring </acquia-cloud/manage/uptime>`__.

.. _type:

Environment types
-----------------

Beneath the **Environments** page title, |acquia-product:ac| displays
*badges* that indicate both the application type and your subscription
level.

|Environment badges|

These badges are assigned colors based on their type and value:

-  *Application type*

   -   **Drupal** - Blue
   -   **Node.js** - Green

-   Subscription level - White

    All |acquia-product:ac| subscription badges are white, and include the following subscription levels:

    -  `Free </acquia-cloud/free>`__
    -  `Professional </acquia-cloud/arch/compare-ace-acp>`__
    -  `Enterprise </acquia-cloud/arch/compare-ace-acp>`__
    -  `Site Factory </site-factory>`__

.. _info:

Information
-----------

Your **Environments overview** page also contains basic **Information**
about the server, including the following:

-  **Git URL** - Server Git URL
-  **SSH URL** - Server SSH URL
-  **IP Address** - Server physical IP address
-  **Region** - Region in which this server is located
-  **PHP version** - Current server PHP version
-  **Life Development mode** - Whether or not the environment is running
   in `Production </acquia-cloud/develop/livedev>`__ (Live Development)
   mode

|Server information box|

.. |Environment badges| image:: https://cdn2.webdamdb.com/md_gpgTTbHF9WG1.png?1527185235
   :width: 258px
   :height: 125px
.. |Server information box| image:: https://cdn3.webdamdb.com/1280_608sYNltuRf6.png?1527185282
   :width: 553px
   :height: 421px

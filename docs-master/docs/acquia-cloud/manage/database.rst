.. include:: /common/global.rst

Working with databases
======================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/manage/database/*

Your Drupal application's database contains the application's content,
configuration, and log information. When you import or create an
application in |acquia-product:ac|, you have multiple environments you
can use to develop and manage your application, with each environment
having its own database. Because of this, your application can have
multiple databases associated with it, depending on which environment
you're working in.

You can use the **Environments** page in the |acquia-product:ui| to copy
a database from one of your application's environments to another, just
by dragging the database between environments. You can use the
**Application > Environments** page to add, back up, and delete
databases, as well as view, restore, and delete database backups.

.. _add:

Adding a new database
---------------------

Drupal sets up the application's primary database when you install
Drupal. Your application might also require additional databases. You
can create additional databases by using the |acquia-product:ui|.

Note for |acquia-product:ccd| environments

You cannot create additional databases for `|acquia-product:ccd|
environments </acquia-cloud/cd/env>`__.

#. On the **Applications > Environments** page, click **Add Database**
   in the upper right.

   |Add a database|

#. Enter the database name, and then click **Add database**. This
   creates unique databases for each environment and adds a block for
   the database to the **Databases** page.

   -  If the database is for a new website using Drupal multisite, enter
      the website name. Then, add the include statement from the
      **Databases** page to the ``settings.php`` file in the multisite
      directory (for example,
      ``docroot/sites/[sitename]/settings.php``).
   -  If the database is for additional content for an existing
      application, enter a name (for example, for a postal code
      database, use "postalcodes"), and use
      ``db_set_active('[Database]')`` within Drupal to access it. Do not
      add the include statement from the **Databases** page to the
      ``settings.php`` file unless you intend the new database to be
      your application's default Drupal database.

.. _many:

Using many databases
~~~~~~~~~~~~~~~~~~~~

Running a large number of databases in the same application can
adversely affect the performance of the database servers or the
usability of the |acquia-product:ui|. *|acquia-product:ac| allows a
maximum of 100 databases per subscription.* If you believe you need a
larger number of distinct databases, you should split your sites to run
on multiple clusters. If you have any questions about your current
database usage or the limits on your account, `contact Acquia
Support </support#contact>`__.

.. _use:

Configuring your application to use environment databases
---------------------------------------------------------

On the **Applications > Databases** page, click **PHP** to display the
include statement (sometimes called the `require
statement </acquia-cloud/code/require-line>`__) for your database. The
include statement should be at the end of the ``settings.php`` file in
your ``/sites`` directory, but should precede any other
|acquia-product:ac|-specific entries in ``settings.php``, including
`Memcached configuration
code </acquia-cloud/performance/memcached#config>`__ or any code that
uses `|acquia-product:ac| environment
variables </acquia-cloud/develop/env-variable>`__.

|Database include statement|

The database include statement causes your application to use a unique
database for each environment. This allows you to use the same
``settings.php`` file in each of your |acquia-product:ac| environments.

When you use the |acquia-product:ui| to install a Drupal distribution or
import a site archive, or import an application using the
|acquia-product:anc|, |acquia-product:ac| creates the database include
statement in your ``settings.php`` file. Otherwise, you need to edit the
``settings.php`` file yourself to add the include statement. Do not add
the include statement unless you intend the new database to be your
application's default Drupal database.

.. _copy:

Copying a database across environments
--------------------------------------

As you develop your application, you may often want to update an
environment with the version of the database from a different
environment. Most commonly, you may want to update your Dev or Stage
environment databases with the content and configuration from your Prod
environment.

#. Open the **Applications > Environments** page for your application.
#. In the grid view, drag the source database container to the target
   environment that you want to contain the database copy. For example,
   drag the Prod database to the Dev environment.
#. If the application has more than one database, select the database
   you want to copy, or click **All** to select all of the databases.
   Then, click **Continue**.
#. Click **Copy** to confirm that you want to overwrite the target
   environment's database with the source environment's database. The
   database migration begins.

   Important

   After your application is live, it is generally not a good practice
   to copy a database into the Production environment. Doing so may lead
   to content loss on your application. While the database is being
   copied, requests that cannot be served from cache will fail.

   You cannot copy a database to your Production environment when your
   application is in Production mode. For more information, see `Using
   Production mode to protect your live
   application </acquia-cloud/manage/prod-mode>`__.

.. _credentials:

Viewing database information
----------------------------

To view information about your databases, complete the following steps:

#. Navigate to the **Applications > Databases** page.
#. If your environment has more than one database associated with it,
   click the name of the database that you want to view.
#. Click **Details** to display the connection information for the
   database.

   |Database details|

|acquia-product:ac| displays the environment-agnostic database name at
the top of the section, along with the following fields and their
values:

-  **SSH Host** - Fully-qualified domain name needed to SSH in to this
   environment
-  **MySQL Host** - For multi-tier subscriptions, the fully-qualified
   domain name of the database server; for single-tier subscriptions:
   ``127.0.0.1``
-  **Name** - Environment-specific name for this database
-  **Username** - Username needed to connect to this database
-  **Password** - Password needed to connect to this database; click
   **Show** to reveal the password

Note

|acquia-product:api| users need to use the database machine name for any
script functionality.

.. _backup:

Backing up your database
------------------------

The **Databases** page displays the date and time of the last created
backup for each database in each environment. You can also create
on-demand backups and view, download, restore, and delete backups. For
more information, see `Backing up your
application </acquia-cloud/manage/back-up>`__.

.. _delete:

Deleting a database
-------------------

You can use the **Databases** page to delete a database, so long as it
is not your Drupal application's primary database. You cannot delete the
primary database for your application. Doing so would prevent your
application from working. To delete a database, complete the following
steps:

Note for |acquia-product:ccd| environments

You cannot delete databases from `|acquia-product:ccd|
environments </acquia-cloud/cd/env>`__.

#. On the **Databases** page, find the database you want to delete and
   click **Delete**.
#. In the confirmation dialog, enter your |acquia-product:ac| password
   and then click **Delete**.

.. _access:

Monitoring and accessing your databases
---------------------------------------

|acquia-product:ac| provides several tools that you can use to monitor
and access your application's databases:

-  `Access the MySQL command
   line </acquia-cloud/manage/database/cli>`__. You have full grants on
   your application's database, giving you complete control of the
   application's database. These grants on your application's database
   do not grant you access to the entire database system, nor do they
   grant you permission to add users or modify permissions on the
   database system.
-  `Administer your database with a desktop application or
   phpMyAdmin </acquia-cloud/manage/database/tools>`__.
-  `View the slow query logs </acquia-cloud/monitor/slow-query>`__.
-  Trace database queries using an application monitoring tool, such as
   `New Relic </acquia-cloud/monitor/apm>`__.

.. |Add a database| image:: https://cdn3.webdamdb.com/1280_E9rluR5tQen7.png?1527200778
   :width: 1197px
   :height: 259px
.. |Database include statement| image:: https://cdn4.webdamdb.com/1280_ciyh2f99WPE9.png?1526475789
   :width: 720px
.. |Database details| image:: https://cdn4.webdamdb.com/1280_YxoU23wjgMp4.png?1526475569
   :width: 870px
   :height: 425px

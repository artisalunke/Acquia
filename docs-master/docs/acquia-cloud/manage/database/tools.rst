.. include:: /common/global.rst

Tools for administering your database
=====================================

This topic describes several different ways you can access and
administer your |acquia-product:ac| application's Drupal database. For
most of these tools, you will need the connection details and
credentials for the database. See `Viewing database
information </acquia-cloud/manage/database#credentials>`__ for
information about where to find these.

.. _desktop:

Desktop applications
--------------------

You can access and administer your application's Drupal database using a
desktop application that supports SSH tunneling. This means that you are
connecting to the database through an SSH connection, using the same
private key authentication you would use to SSH to the servers. Here are
some options to consider:

-  `MySQL Workbench <http://wb.mysql.com>`__ - MySQL Workbench is a
   free, cross-platform, visual database design tool developed by MySQL.
   It runs on Windows, macOS, and Linux.
-  `Navicat for MySQL <http://www.navicat.com>`__ - A well-designed and
   very popular commercial tool that runs on Windows, macOS, and Linux.
-  `Sequel Pro <http://www.sequelpro.com>`__ - Sequel Pro is a free,
   open source tool for macOS with a well-designed interface.

phpMyAdmin
----------

Another alternative is to install
`phpMyAdmin <http://www.phpmyadmin.net/home_page/index.php>`__ on your
server. This is a commonly used, open source database management tool
for MySQL. If phpMyAdmin is installed on your server, any security
vulnerabilities in phpMyAdmin can put your application at risk. If you
install phpMyAdmin, it is very important to restrict access and keep it
up-to-date with `security
updates <http://www.phpmyadmin.net/home_page/security/>`__. Acquia does
not manage security updates on phpMyAdmin, so this is the responsibility
of the customer.

.. _command:

Command line
------------

You can also access your database over SSH and use MySQL's command line.
For more information, see `Accessing your database from the command
line </acquia-cloud/manage/database/cli>`__.

Note

You cannot SSH directly into |acquia-product:ace| database servers.
Database servers generally have a server name that starts with ``fsdb``
or ``fsdbmesh``. For |acquia-product:ace| applications, you can check
the **Servers** page in the |acquia-product:ui| to verify the server
type. If the service for a server is listed as Database, you cannot SSH
directly into it. You can SSH into multi-tier web servers or single-tier
servers, which gives you access to the database on the command line.

.. _database:

Database tasks
--------------

You can use database management tools to perform the following tasks:

-  Rename, import, export, and otherwise manage databases and database
   tables directly in your web browser.
-  Export data in a range of formats, including CSV, Excel, XML, and
   OpenOffice.
-  Browse or search in your data.
-  Edit fields in your databases directly.
-  Import and export database snapshots for given releases in your
   development workflow.
-  Maintain your organization's policies on data backup and archiving.
-  Test database queries during module development and debugging.

You cannot use database tools to create new databases in
|acquia-product:ac|. If you need a new database, use the **Databases**
page in the |acquia-product:ui|.

.. _ace:

Using database tools on |acquia-product:ace|
--------------------------------------------

If you have an |acquia-product:ace| application, it includes a highly
available database cluster, using bi-directional replication between
database pairs. Each database has an active and inactive instance. If
you run intensive processes, such as database backups, against the
active instance of a live application, it could impair the performance
of your production website. Tools in |acquia-product:ac|, such as the
Cloud UI and the `Cloud API </acquia-cloud/api>`__, automatically run
against the inactive database instance, to avoid this performance
impact. However, if you use other database tools — for example, if you
run ``mysqldump`` or ``drush sql-sync`` from the command line — those
will run against the active database instance. Therefore, you should,
when possible, use the |acquia-product:ac| database tools for larger
operations like database dumps. For example, if you want to create a
database backup from the command line, you can use a Drush Cloud command
like this:

``drush @[site].[env] ac-database-instance-backup [db name]``

substituting your own site, environment, and database names. The
database backup will run against the inactive database, avoiding any
performance impact on your active database.

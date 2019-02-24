.. include:: /common/global.rst

Database connection
===================

Using a database, you can save information for later use, or query
existing data to provide a customized experience for your users. To use
a database `adaptor </journey/adaptors>`__ with your project, you must
first connect to your database by configuring a *database connection*.

For information about creating, configuring, or testing connections, see
|managing connections|_.

.. |managing connections| replace::
  Managing \ |acquia-product:aj|\  connections
.. _managing connections: /journey/connect

-  **Type** - The database type to which the connection is being made.
   The following types are available for your use:

   -  **MySQL** - Version 5.6 and above; includes Amazon Web Services
      Aurora
   -  **MSSQL** - Microsoft SQL Server 2008 and greater; includes SQL
      Azure
   -  **Oracle** - Version 10i and greater
   -  **PostgresSQL** - Version 9.X

-  **User Name** - Name of the user to log in to the database.

   .. admonition:: Note for SQL Server on Azure

    The username is ``user@server`` where ``server`` is the first part of
    the fully qualified domain name for the database. For example, if the
    server is ``demo.database.example.com`` and the user is ``acquia``,
    then the username would be ``acquia@demo``.

-  **Password** - Password of the user to log in to the database.
-  **Host Name** - Physical host name (IP address or fully qualified
   domain name) of the database server. In Oracle, the name of the load
   balancer.
-  **Port** - The port on which the database is listening for
   connections. The default ports for the supported databases are as
   follows:

   -  *MySQL* - ``3306``
   -  *MSSQL* - ``1433``
   -  *Oracle* - ``1521``
   -  *PostgresSQL* - ``5432``

-  **Database Name** - The name of the default database or schema to be
   connected to.

.. include:: /common/global.rst

Accessing your database from the command line
=============================================

You can access the databases of your |acquia-product:ac| application
using the ``drush ah-sql-cli`` command. The ``ah-sql-cli`` command is
exactly like the ``drush sql-cli`` command, except that ``ah-sql-cli``
does not require a functioning Drupal website.

#. Connect to an environment of your application using SSH. For more
   information, see `Managing applications using the command
   line </acquia-cloud/ssh>`__.
#. Open a connection to your database with a command like the following:

   ``drush @[site].[env] ah-sql-cli``

   You can also use the shorter alias, ``ah-sqlc``.

   Replace ``[site]`` with your application name and ``[env]`` with the
   name of the environment whose database you want to connect to
   (typically, ``dev``, ``test``, or ``prod``, for the Development,
   Staging, and Production environments, respectively). You can use the
   ``--db`` `option <#options>`__ to connect to a database other than
   your primary Drupal database. Note that unlike ``drush sql-cli``,
   ``ah-sql-cli`` does not support the ``--uri`` option.

   For example:

   -  If your site name is ``myexample`` and you want to connect to the
      primary database for your Production environment, use the
      following command:

      ``drush @myexample.prod ah-sql-cli``

   -  If your site name is ``myexample`` and you want to connect to the
      a secondary database named ``postal`` for your Staging
      environment, use a command similar to the following:

      ``drush @myexample.test ah-sql-cli --db=postal``

You can now run SQL commands from the ``mysql>`` prompt. Enter ``quit``
to leave when you are done.

In addition to ``ah-sql-cli``, |acquia-product:ac| includes another
Drush command to connect to your database: ``ah-sql-connect``. The
``ah-sql-connect`` command is exactly like the ``drush sql-connect``
command, except that ``ah-sql-connect`` does not require a functioning
Drupal website. The ``ah-sql-connect`` command takes the same
`options <#options>`__ as ``ah-sql-cli``. The output of
``ah-sql-connect`` is the MySQL command, with user name, password, and
database name, that you can use to connect directly to the database. For
example:

``drush @[site].[env] ah-sql-connect mysql -h free-1712 -u example1dev -pbfddVTKixQbn88i example1dev``

For another approach, you can use phpMyAdmin, a GUI-based MySQL database
management tool. For more information, see `Tools for administering your
database </acquia-cloud/manage/database/tools>`__.

.. _options:

Command options
---------------

The ``drush ah-sql-cli`` and ``ah-sql-connect`` commands take the
following options, in the format ``--option=value``:

+-----------------------+-----------------------+-----------------------+
| Option                | Description           | Value                 |
+=======================+=======================+=======================+
| ``--site``            | The site name for the | Use the `drush        |
|                       | database to connect   | ``@site.env``         |
|                       | to.                   | alias </acquia-cloud/ |
|                       |                       | drush/aliases>`__     |
|                       |                       | instead of specifying |
|                       |                       | this option directly. |
+-----------------------+-----------------------+-----------------------+
| ``--env``             | The environment for   | Use the `drush        |
|                       | the database to       | ``@site.env``         |
|                       | connect to.           | alias </acquia-cloud/ |
|                       |                       | drush/aliases>`__     |
|                       |                       | instead of specifying |
|                       |                       | this option directly. |
+-----------------------+-----------------------+-----------------------+
| ``--db``              | The                   | Defaults to the name  |
|                       | environment-agnostic  | of the default        |
|                       | database name. This   | primary Drupal        |
|                       | is the name displayed | database for the      |
|                       | on the **Databases**  | website.              |
|                       | page for the          |                       |
|                       | environment in the    |                       |
|                       | |acquia-product:ui|.  |                       |
+-----------------------+-----------------------+-----------------------+

Note

When you run ``drush ah-sql-cli``, |acquia-product:ac| may display the
following message:

``Reading table information for completion of table and column names You can turn off this feature to get a quicker startup with -A``

The ``-A`` option is a MySQL option and not a ``drush ah-sql-cli``
option. You should ignore it when you run ``drush ah-sql-cli``.

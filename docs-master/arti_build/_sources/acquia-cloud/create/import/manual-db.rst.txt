.. include:: /common/global.rst

Importing your database
=======================

.. container:: internal-navigation

  **Importing manually**

  * :doc:`Intro </acquia-cloud/create/import/manual>`
  * :doc:`Code </acquia-cloud/create/import/manual-code>`
  * Database
  * :doc:`Files </acquia-cloud/create/import/manual-files>`

This page describes manually importing the database of an existing
Drupal application into |acquia-product:ac|, as part of the process of
`manually importing the entire
application </acquia-cloud/create/import/manual>`__. For information
about other methods of importing an application, see `Importing an
existing application </acquia-cloud/create/import>`__.

To import a database using command-line tools, complete the following
steps:

.. _create:

#. Create a database dump file from the command line by using either 
   `Drush <https://www.drupal.org/project/drush>`__ or mysqldump:

   -  ***Drush***
       Go to the Drupal directory, and then enter the following command:

       ``drush sql-dump --gzip --result-file=../mysite.sql``

       | Drush saves the ``mysite.sql.gz`` site archive file relative to
        your current Drupal ``docroot``. If the command displays error
        messages, ensure that Drush has the required permissions to save
        files in that directory.
       | For more information, see the `Drush
        documentation <https://drushcommands.com/drush-8x/sql/sql-dump/>`__.

   -  ***mysqldump***
       Make a database dump file from your existing database using the
       ``mysqldump`` command-line tool.

      ``mysqldump -u [db_username] -p[db_password] [db_name]   | gzip > [db_filename].sql.gz``

      where:

      -  ``[db_username]`` is the account user name that manages the database.
      -  ``[db_password]`` is the password for the database account.
      -  ``[db_name]`` is your Drupal database.
      -  ``[db_filename]`` is the path and file name of the backed up
          database's dump file. Be sure to keep the ``.sql.gz``
          extension.

#. Using SFTP, scp, or `rsync </acquia-cloud/develop/rsync>`__, copy the 
   database dump file to your |acquia-product:ac| server. For example,
   using ``scp``, use a command in this form:

   ``scp [db_filename].sql.gz [site].[env]@[server]:./[db_filename].sql.gz``

   where:

   -  ``[db_filename]`` is the path and file name you choose to give
       your database dump file. Be sure to keep the ``.sql.gz`` extension.
   -  ``[site]`` is the site name, the string that precedes ``.dev``
      under **SSH address** listed in the |acquia-product:ui| on the
      **Servers** page for the environment.
   -  ``[env]`` is the environment you want to connect to (usually
      ``dev`` for the Development environment).
   -  [server] is the name of your |acquia-product:ac| server, which is
      listed on the **Servers** page of the |acquia-product:ui|. For
      example: ``ded-1234.network.hosting.acquia.com``.

   For example:
   ``scp abc_db.sql.gz abc.dev@free-1234.devcloud.hosting.acquia.com:./abc_db.sql.gz``

#. The easiest way to import a database dump file from the command line
   is to connect to your |acquia-product:ac| server with SSH and use the
   drush ``ah-db-import`` command. This command takes the following
   form:

   ``drush @[site].[env] ah-db-import [/path/to/db/dump/file]``

   where:

   -  ``[site]`` is the name of your application on |acquia-product:ac|.
   -  ``[env]`` is the environment into which you're importing your
      database. Acceptable values are ``dev`` (Development), ``test``
      (Staging), and ``prod`` (Production).

   For example, if you are importing a database into the Staging
   environment of an application named ``example``:
   ``ssh example.test@server-321.devcloud.hosting.acquia.com drush @example.test ah-db-import ~/dbdump.sql.gz``

   This presumes you have installed the `Drush
   aliases integration </acquia-cloud/drush/aliases>`__ for |acquia-product:ac|. 
   If not, you need to use the ``--site=[site]`` and ``--env=[env]`` arguments 
   with the ``ah-db-import`` command. For example:
   ``drush @example.test ah-db-import ~/dbdump.sql.gz --site=example --env=test``

   For more information, read `Importing using
   Drush </acquia-cloud/create/import/drush>`__.

.. _import-multisite:

Importing a database for a Drupal multisite installation
--------------------------------------------------------

To import a database for a Drupal multisite installation, run the
``ah-db-import`` command on your |acquia-product:ac| server:

``drush @[site].[env] ah-db-import --db=[db_name] --drop   --force [/path/to/db/dump/file]``

where:

-  ``[site]`` is the name of your application on |acquia-product:ac|.
-  ``[env]`` is the environment into which you're importing your
   database. Acceptable values are ``dev`` (Development), ``test``
   (Staging), and ``prod`` (Production).
-  ``[db_name]`` is the name of your database. Use the database name
   shown on the **Databases** page for the environment, not an
   environment-specific name. For example, if your site name is
   ``example``, your default database name will probably be ``example``,
   and you should use that rather than an environment-specific name like
   ``exampledev`` or ``exampletest``.

For more information, see `About Drupal multisite
installations </acquia-cloud/multisite>`__.

.. _connect:

Set up database connections
---------------------------

After you have imported your database, go to the |acquia-product:ac|
`**Databases** </acquia-cloud/manage/database#use>`__ page. Click
**PHP** to display the `require
statement </acquia-cloud/develop/code/require-line>`__ for your database, add 
that statement at the end of the ``settings.php`` file in
your ``/sites`` directory, and commit or push the changed file to your
application's |acquia-product:ac| code repository.

The database ``require`` statement causes your application to use a
unique database for each |acquia-product:ac| environment. This allows
you to use the same ``settings.php`` file in each of your
|acquia-product:ac| environments.

.. _next:

Next step
---------

After you import your database, you can `import
files </acquia-cloud/create/import/manual-files>`__ using SFTP, scp, or
`rsync </acquia-cloud/develop/rsync>`__.

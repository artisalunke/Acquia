.. include:: /common/global.rst

About UTF-8 support in Drupal 7
===============================

As of `version 7.50 <https://www.drupal.org/node/2488180>`__, Drupal
supports the use of multibyte UTF-8 characters. For reference,
|acquia-product:ac| and previous Drupal versions supported some versions
of UTF8, and Drupal 8 supports
`utf8mb4 <https://dev.mysql.com/doc/refman/5.5/en/charset-unicode-utf8mb4.html>`__
by default.

To ensure that your Acquia-hosted Drupal 7 website can use UTF-8,
complete the following steps:

-  

   .. raw:: html

      <div id="database">

   | Examine your database connections.
   | Acquia has already taken care of the basic server requirements for
     utf8mb4, namely the ``innodb_large_prefix``,
     ``innodb_file_format``, and ``innodb_file_per_table``
     configurations described in the `Drupal.org
     documentation <https://www.drupal.org/node/2754539>`__.

   .. raw:: html

      </div>

-  

   .. raw:: html

      <div id="connection">

   | Alter your database connection settings.
   | A variation on the normally-recommended database connection code in
     the ``settings.php`` file is required to ensure that the database's
     charset and collation are appropriate for utf8mb4 content.
   | Add the following code in place of our `regular include
     statement </acquia-cloud/manage/database#use>`__, ensuing that you
     edit the website and database names to match your own environment
     (for more information, see `Working with
     databases </acquia-cloud/manage/database#use>`__):

   ``// Note that SITE_NAME and DATABASE_NAME should be replaced accordingly in the following code: if (file_exists('/var/www/site-php')) {   // Delay the initial database connection.   $conf['acquia_hosting_settings_autoconnect'] = FALSE;   // The standard require line goes here.   require('/var/www/site-php/[DATABASE_NAME]/[DATABASE_NAME]-settings.inc');   // Alter the charset and collation of the databases.   $databases['default']['default']['charset'] = 'utf8mb4';   $databases['default']['default']['collation'] = 'utf8mb4_general_ci';   $databases['[DATABASE_NAME]']['default']['charset'] = 'utf8mb4';   $databases['[DATABASE_NAME]']['default']['collation'] = 'utf8mb4_general_ci';   // Now connect to the default database.   acquia_hosting_db_choose_active(); }``

   .. raw:: html

      </div>

-  If your website was upgraded from a version of Drupal before version
   7.5, the charset and collation for database tables are most likely
   not appropriate for utf8mb4. In this case, you must manually alter
   the tables, or instead use a tool such as `utf8mb4
   Convert <https://www.drupal.org/project/utf8mb4_convert>`__.

   Important

   During this activity we recommend that you first create a complete
   backup of your database(s), and then rehearse this step on
   non-production environments and ensure that production sites are set
   to maintenance mode.

-  | Ensure that your database backups will accept these characters.
   | The ``mysqldump`` command, used for creating database backups and
     copies, can use configuration overrides beyond those provided by
     |acquia-product:ac|. These overrides are made in a file called
     ``~/.my.cnf`` that you can create on the servers for one or more
     environments.
   | The contents of the ``~/.my.cnf`` file should be as follows:

   Note

   This file will apply to all websites in your environment. If you are
   using multisites and have not yet completed converting all of your
   websites to utf8mb4, there may be unpredictable results.

   ``[client] loose-default-character-set = utf8mb4  [mysqldump] default-character-set=utf8mb4``

   This file can be created in non-production environments for testing,
   prior to its creation in the home directory of your production
   environment.

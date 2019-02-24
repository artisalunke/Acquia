.. include:: /common/global.rst

Restoring a site from a backup
==============================

|acquia-product:edg| provides two types of backups from which you may
restore:

-  `Daily database-only backups <#restoring-from-a-nightly-database-backup>`__ - Contain only a daily
   snapshot of a website's database, but not the docroot, public files,
   or private files
-  `On-demand full backups <#restoring-from-an-on-demand-full-backup>`__ - Contain a single website's
   complete docroot, database, public files, and private files, as
   described in 
   `Backing up sites </site-factory/manage/website/backup>`__

Although you can restore an `on-demand full backup <#restoring-from-an-on-demand-full-backup>`__ from the
|acquia-product:sfi|, you must restore 
`nightly database backups <#restoring-from-a-nightly-database-backup>`__ by using command line instructions.


Restoring from an on-demand full backup
---------------------------------------

After you `create a backup </site-factory/manage/website/backup>`__ of
one of your |acquia-product:edg|-hosted websites, you can then restore
that website from its backup. Restoring a website from a backup creates
a new website, which you can then add to the same group and site
collection as the website from which you created the backup. The
original website from which the backup was created is not affected.

To restore a new website from a backup, complete the following steps:

#. Sign in to the |acquia-product:sfi|.
#. On the All my sites page, click **All my backups**.
#. On the Site Backups page, locate the backup from which you want to
   create a new website. You can sort the backups by date, backup name,
   components, or stack.
#. Click **Restore**.

   |Restore a new site from a backup|

#. In the **Name for the new site** field, enter the new website's name
   using only lowercase letters and numbers, ensuring that you do not
   use the name of another |acquia-product:edg| website.
#. In the **Components** section, select the components that you want to
   restore from backup. To successfully create a new site, you must
   select the **Database** option.
#. Click **Restore**.

.. note::  Restoring a website can take several minutes to complete for 
      small websites, but larger websites can take much longer to complete.

After |acquia-product:edg| restores your website, you will receive an
email stating that the new website is now available. You can add the new
website to a group or site collection, and make the new website the
primary website for its site collection (in place of the website whose
backup you used to create the new website).


Restoring from a nightly database backup
----------------------------------------

.. container:: message-status

     **ADVANCED** - Incorrect use of these instructions can cause data loss or 
     website downtime. `Contact Acquia Support </support#contact>`__ if you 
     need assistance.

To restore a nightly database backup for a single website, complete the
following steps:

#. `SSH into your environment </acquia-cloud/ssh>`__.
#. Navigate to your ``backups`` directory with the following command:

   .. code-block:: none

      cd /mnt/files/${AH_SITE_GROUP}.${AH_SITE_ENVIRONMENT}/backups

#. Create a new database backup of the website that you intend to
   restore by running the following command (where ``[SITEURL]`` is the
   URL for your website):

   .. code-block:: none

      drush -r /var/www/html/${AH_SITE_GROUP}.${AH_SITE_ENVIRONMENT}/docroot  --uri=[SITEURL] sql-dump --gzip --result-file=/mnt/files/${AH_SITE_GROUP}.${AH_SITE_ENVIRONMENT}/backups/site-backup.sql

#. Confirm that the backup exists and was archived correctly by
   executing the following command to confirm that a file matching the
   name ``site-backup.sql`` now exists in the directory:

   .. code-block:: none

      ls "`pwd`/site-backup.sql.gz" /mnt/files/${AH_SITE_GROUP}.${AH_SITE_ENVIRONMENT}/backups/site-backup.sql.gz

#. Identify the database name and site path values by executing the
   following command, substituting the ``[SITEURL]`` value with the URL
   of the website you want to restore:

   .. code-block:: none

      drush -r /var/www/html/${AH_SITE_GROUP}.${AH_SITE_ENVIRONMENT}/docroot --uri=[SITEURL] st | grep -E "Database name|Site path"
      
      Database name : customeracsdb123102
      Site path : sites/g/files/marketing101

   In the preceding output, your database name is
   ``customeracsdb123102`` and your path is ``marketing101``. These
   values will be required in the following steps.

#. Identify the file name of the database backup by using ``grep`` in
   your ``backups`` directory to search for the available database
   backup files that match the site path you identified previously,
   replacing ``[PATH]`` with your path:

   .. code-block:: none

      ls -lath | grep [PATH] | head

   The resulting files are the daily database backups available for restoration.

   .. code-block:: none

      -r--r----- 1 customername www-data 12M Dec 17 08:16 01live-marketing101-customerdb123102-2017-12-17.sql.gz
      -r--r----- 1 customername www-data 11M Dec 16 08:16 01live-marketing101-customerdb123102-2017-12-16.sql.gz
      -r--r----- 1 customername www-data 11M Dec 15 08:16 01live-marketing101-customerdb123102-2017-12-15.sql.gz

#. Run the following command to unzip the filename of the backup that
   you want to restore, replacing ``filename.sql.gz`` with the name of
   your file:

   .. code-block:: none

      gunzip filename.sql.gz

#. Ensure that the ``.sql`` file was successfully unzipped and verify
   the full path of the resulting ``.sql`` file by executing the
   following command, replacing ``filename.sql`` with the name of your
   file:

   .. code-block:: none

      ls "`pwd`/filename.sql"
      
      /mnt/files/${AH_SITE_GROUP}.${AH_SITE_ENVIRONMENT}/backups/01live-marketing101-customerdb123102-2017-12-17.sql

   If the file file system path to your newly-unzipped ``.sql`` file is
   not in the output of your command, verify that the file was unzipped
   successfully before attempting to proceed with restoring the backup.
   If you are unsure, `contact Acquia Support </support#contact>`__.

#. Drop the existing database.

   .. important:: This step destroys all data currently stored in the website's current
      database. After executing this command, your website will be
      inaccessible until database restoration is complete.

   To drop the existing database, execute the following command (where
   ``[SITEURL]`` is the URL for your website):

   .. code-block:: none

      drush -r /var/www/html/${AH_SITE_GROUP}.${AH_SITE_ENVIRONMENT}/docroot --uri=[SITEURL] sql-drop

   Drush will display the following confirmation message to confirm that
   you intend to drop the database:

   .. code-block:: none

      Do you really want to drop all tables in the database customeracsdb1231023? (y/n):

   If the database name matches the database name you identified in
   `Identify the database name and site path values <#values>`__, press
   ``Y`` to drop the database.

#. Restore the database backup that you identified by running the
   following command, using the full path to the ``.sql`` file that you
   verified when `preparing the database backup file for
   restoration <#prepare>`__:

   .. code-block:: none

      drush -r /var/www/html/${AH_SITE_GROUP}.${AH_SITE_ENVIRONMENT}/docroot --uri=[SITEURL] sqlc < /full/path/to/backup/filename.sql

   where:

   -  ``[SITEURL]`` - The full URL for your website
   -  ``/full/path/to/backup/filename.sql`` - The full file system path
      to your ``.sql`` backup file

Your database restoration is now complete.

.. |Restore a new site from a backup| image:: https://cdn2.webdamdb.com/1280_IcRmfNNLqjh6.png?1526475682
   :width: 500px
   :height: 423px

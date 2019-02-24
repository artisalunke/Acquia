.. include:: /common/global.rst

Backing up sites
================

Using the |acquia-product:sfi|, you can create backups of your
|acquia-product:edg|-hosted websites. Each backup may include the
website's complete docroot, database, public files, and private files,
all in a ``.tar.gz`` format that is also suitable for exports.

You can create and download website backups using the
|acquia-product:sfi|, as well as restore a website from a backup. You
can also use the `Site Factory REST API </site-factory/extend/api>`__ to
create, list, and delete backups and to restore a website from a backup.

For procedures that you can use to exclude sensitive credentials, keys,
or other private information from stored backups, see `Storing sensitive
information outside of your codebase </resource/secrets>`__.

.. note::  

   The `acsf-tools <https://github.com/acquia/acsf-tools>`__ repository
   (also included with |bltlink|_) provides an additional backup script for 
   |acquia-product:edg| websites using Drupal 8. For more information about 
   this toolkit, see 
   `Managing sites on a cluster with Drush </site-factory/extend/drush>`__.

.. |bltlink| replace:: \ |acquia-product:blt|\ 
.. _bltlink: /devtools/blt

Permissions
-----------

To create and download backups, you must have a
`role </site-factory/users/admin>`__ with the necessary permissions.

-  Users with the |platform admin|_ role have
   permission to create and download backups of all websites.
-  Users with the |site builder|_ role have
   permission to create backups of their websites and to download
   backups that they have created.

.. |platform admin| replace:: *platform admin*
.. _platform admin: /site-factory/users/admin/platform-admin

.. |site builder| replace:: *site builder*
.. _site builder: /site-factory/users/admin/site-builder

Creating a backup
-----------------

To create a backup of a website, complete the following steps:

#. Sign in to the |acquia-product:edg| interface.
#. Find the website that you want to back up, and then open its actions
   menu.

   |Select "Back up site" from the site actions menu|

#. Click **Back up site**.
#. In the **Create site backup** page, select all of the components you
   wish to back up:
   |Select components to back up|
#. Click **Back up**.

After your backup is complete, you will receive an email letting you
know that the backup is now available on the **Site Backups** page.
Backups can take several minutes to complete for small websites, but
larger websites can take much longer to complete.

Viewing available backups
-------------------------

You can view and download your website backups on the Site Backups page:

#. Sign in to the |acquia-product:edg| interface.
#. In the administrative menu at the top of the page, click **Sites**.
#. At the bottom of the left-hand column, click **All my site backups**.

The backups are created with the site name, plus a timestamp from when
the backup was created. To sort the table by name, by date, or by stack
(if you have more than one stack) click on the column heading you want
to sort by.

To restore a backup, identify the desired backup and in the **Actions**
column, click **Restore** in that backup's row:

|Viewing the list of backups|

.. note::  When you create backups using the Site Factory REST API, you can 
   use the ``label`` request parameter to modify the backup name.

Downloading backup files
------------------------

If you want to download a website backup file to your local computer, on
the Site Backups page find the backup that you want to download, and
then click its **Download** link.


Restoring from a backup file
----------------------------

For information about using a backup file to restore a website, see
`Restoring a site from a backup </site-factory/manage/website/restore>`__.

.. |Select "Back up site" from the site actions menu| image:: https://cdn3.webdamdb.com/1280_Ejb6d6HKUjz0.png?1526475522
   :width: 590px
   :height: 468px
.. |Select components to back up| image:: https://cdn2.webdamdb.com/1280_2SWeVa5Tqvw1.png?1526475876
   :width: 600px
   :height: 263px
.. |Viewing the list of backups| image:: https://cdn2.webdamdb.com/1280_cj5VzOcRzaV3.png?1526475738
   :width: 750px
   :height: 249px

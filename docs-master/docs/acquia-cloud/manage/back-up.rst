.. include:: /common/global.rst

Backing up your application
===========================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/manage/back-up/*

An |acquia-product:ac| application has three principal parts: code,
database, and files. Although each of these parts has a separate backup
strategy, you can also back up your entire application:

-  `Database backups <#db>`__
-  `Code backups <#code>`__
-  `File backups <#file>`__
-  `Backups of your whole application <#site>`__

.. _db:

Database backups
----------------

Daily backups from the last three days are always available to you. You
can make additional backups at any time, for example, for critical
stages of development. You should also periodically check to be sure
that backups are being successfully completed and test your ability to
restore websites from a backup copy.

-  Automatic backups
    |acquia-product:ac| makes daily backups of all databases in all
    environments and keeps them for three days. These backups are listed
    as **Daily** in the |acquia-product:ui| **Databases** page. These
    daily backups are required and cannot be disabled.
-  On-demand backups
    You can make on-demand backups of any database at any time in the
    |acquia-product:ui|, either on the **Applications > Environments**
    page, the **Applications > [Environment] > Overview** page, or on the
    **Databases** page. These backups are listed as **User** backups in
    the |acquia-product:ui| **Databases** page. |acquia-product:ac| keeps
    your on-demand backups until you delete them. Your backup copies
    count against the storage space of your account.

|acquia-product:ac| takes internal disaster recovery snapshots of all
data every hour and retains them on a diminishing schedule for three
months:

-  The most recent three backups are generally one, two, and three hours
   old.
-  One backup per day, taken as soon after midnight as possible, is kept
   for seven days.
-  One backup per week, taken as soon after midnight Sunday as possible,
   is kept for four weeks.
-  One backup per month, taken as soon after the first of the month as
   possible, is kept for three months.

In the unlikely event of a total data center loss or the loss of
multiple disk systems, |acquia-product:ac| would use these backups to
restore your applications to another location. |acquia-product:ac| does
not provide customer access to these backups and will not use these
snapshots to restore applications due to data loss or deletion by
customers.

.. _backup-db:

Creating a manual, on-demand database backup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can make on-demand backups of any database at any time in the
|acquia-product:ui| on any of these pages:

-  `Applications > Environments <#envs>`__
-  `Applications > [Environment] > Overview <#env>`__
-  `Databases <#dbpage>`__

.. _envs:

Making a database backup on the Applications > Environments page
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. In the |acquia-product:ui|, select your application.
#. On the card for the environment that you want to back up, click the
   backup button.

   |Backing up a database from the Environments page|

   |acquia-product:ac| displays a listing of the databases in the
   environment.

#. Select the database or databases that you want to back up, or click
   **All** to select all of the databases. Then, click **Continue**.
#. In the confirmation dialog, click **Back up**.

Making a database backup on an environment's Overview page

#. In the |acquia-product:ui|, select your application and environment.

   |Backing up from the Overview page|

#. In the Databases card, click **Back up**. |acquia-product:ac|
   displays a listing of the databases in the environment.
#. Select the database or databases that you want to back up, or click
   **All** to select all of the databases. Then, click **Continue**.
#. In the confirmation dialog, click **Back up**.

.. _dbpage:

Making a database backup on the Databases page
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. In the |acquia-product:ui|, select your application and environment,
   and then open the **Databases** page.
#. Find the database you want to back up, and then click its **Back up**
   link.

   |Back up a database|

#. In the **Back up a database** dialog box, click **Back up**.

After the backup is created, which may take a few minutes, you can view
the backup that you created by clicking **View all backups** for the
database.

Downloading, restoring, or deleting backups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the **Databases** page of the |acquia-product:ui|, you can download,
restore, or delete (remove) backups.

#. On the **Databases** page, locate the database you want to act upon.
#. Click **View all backups** for the database.

   On-demand backups are labeled **User**, while automatic backups are
   labeled **Daily**.

   -  To download a database backup, click **Download**.
   -  To restore a database backup, click **Restore**.
   -  To delete a database backup, select **Remove**.

.. _cli-download:

Downloading backups from the command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also download any of your database backups using either the
command line or an SFTP application. The database backups are stored in
the ``/backups`` directory for each of your environments.

-  *Development environment* &ndash
   ``/mnt/files/[sitename].dev/backups``
-  *Staging environment* – ``/mnt/files/[sitename].test/backups``
-  *Production environment* – ``/mnt/files/[sitename].prod/backups``

For more information, see `Downloading database backups from the command
line </acquia-cloud/manage/back-up/cli>`__.

.. _code:

Code backups
------------

Your code is maintained in a version control repository managed by
Acquia. Each time you commit code, a new tag is created in the version
control system. You can revert to an earlier tag at any time in any of
your environments.

.. _file:

File backups
------------

Your uploaded files are kept separate from your Drupal codebase and
database, using a symbolic link to your application's ``/files``
directory. The Git version control system can manage text files full of
code, but is less well suited for managing large collections of
user-uploaded objects, such as images, videos, or file attachments.

|acquia-product:ac| makes internal disaster recovery snapshots of your
files, but these are not available for customers for normal backup
purposes. If you want to back up your uploaded files, you can either do
so manually from the command line or create a cron task to make backups
on a regular schedule.

For more information, see `Working with
files </acquia-cloud/manage/files>`__ and `Backing up your Drupal file
system <%5Bacquia-product:kb%5Darticles/backing-your-drupal-file-system>`__.

.. _site:

Full application backups
------------------------

You can back up your whole application on an environment from the
command line, using Drush. The ``drush archive-dump`` command creates a
complete archive file of your application.

.. important:: 

   Running this command on a large website (with large numbers of files,
   large databases, or small gluster volumes) can lead to a full disk,
   which will cause the script to hang and will cause a website outage.

For example, to back up the Prod environment of an application named
example1:

.. code-block:: none

   drush @example1.prod archive-dump

By default, the backup file is saved to the ``drush-backups`` folder.
Use the ``--destination`` option to specify the full path and filename
in which the archive should be stored.

For more information, see |aboutdrush|_ and the `Drush
Commands <https://drushcommands.com/drush-8x/core/archive-dump/>`__
reference.

.. |aboutdrush| replace:: About Drush on \ |acquia-product:ac|\ 
.. _aboutdrush: 

.. _related:

Related topics
--------------

-  `Working with databases </acquia-cloud/manage/database>`__
-  `Working with files </acquia-cloud/manage/files>`__
-  `Backing up your Drupal file
   system <%5Bacquia-product:kb%5Darticle/backing-your-drupal-file-system>`__

.. |Backing up a database from the Environments page| image:: https://cdn4.webdamdb.com/1280_IUFPIXvE293.png?1526475754
   :width: 763px
   :height: 319px
.. |Backing up from the Overview page| image:: https://cdn4.webdamdb.com/1280_euhEQgd251.png?1526475744
   :width: 761px
   :height: 289px
.. |Back up a database| image:: https://cdn4.webdamdb.com/1280_2Q3xcWTeRw68.png?1526476025
   :width: 761px
   :height: 428px

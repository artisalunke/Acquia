.. include:: /common/global.rst

Downloading database backups from the command line
==================================================

An environment's **Databases** page in the |acquia-product:ui| lists
recent database backups for the environment. However, there is a delay
between the time when backups are created and when they are added or
removed from the **Databases** page. As a result, the most recently
created backups may not yet be listed, while older backups that have
been replaced and deleted may be listed, but not in fact be available
for download or for restoring the database. You can use SSH and command
line tools to confirm which database backups exist, and download backups
even if they aren't displayed on the **Databases** page.

You may also want to use command line tools to download backups if they
are very large (over 1 GB), since large downloads over HTTP from the
|acquia-product:ui| are more prone to failure.

.. _permissions:

Required permissions
--------------------

To run commands on an |acquia-product:ac| environment, you must have the
necessary *permission*. For non-production environments (``dev`` or
``stage``), you must have the **Add SSH key to non-production
environments** permission. For production environments (``prod``), you
must have the **Add SSH key to production environments** permission. By
default, administrators and users with the *Team Lead* or *Senior
Developer* roles have these permissions and users with the *Developer*
role do not. For more information, see `Working with roles and
permissions </acquia-cloud/teams/roles>`__.

.. _view:

Viewing available backups
-------------------------

To view which backups are actually available on an environment, complete
the following steps:

#. `Connect to your server using SSH. </acquia-cloud/ssh>`__ For
   example, you could use a command similar to the following:

   .. code-block:: none

      ssh clouddocs.dev@ded-1234.prod.hosting.acquia.com

#. Change directory to the ``/backups`` directory for the server and
   environment.

   -  Development environment - ``/mnt/files/[sitename].dev/backups``
   -  Staging environment - ``/mnt/files/[sitename].test/backups``
   -  Production environment - ``/mnt/files/[sitename].prod/backups``

   If you wanted to view backups for the Development environment, use a
   command similar to the following:

   .. code-block:: none

      cd /mnt/files/clouddocs.dev/backups

#. Run the ``ls`` command to determine which backup files are present.

You can then download the backup files you want using command line
tools.

.. _download:

Downloading backups with command line tools
-------------------------------------------

The following is a set of examples for downloading database backups with
several command-line tools. Be sure to either replace or set the
following variables in the examples:

-  ``sitename`` - Your application's site name
-  ``env`` - The |acquia-product:ac| environment. For most applications,
   one of ``prod`` (Production), ``test`` (Staging), or ``dev``
   (Development)
-  ``server`` - Your server name, which you can find on the **Servers**
   page. It will be something similar to ``ded-123``

You can instead use any GUI tool that supports these protocols, such as
Fetch or WinSCP.

SFTP
~~~~

To download with SFTP, use a command like the following:

.. code-block:: none

   sftp [sitename].env]@[server].prod.hosting.acquia.com:/mnt/files/[sitename]/backups/yourdatabase-date.sql.gz /path/to/your/backup/folder

If you want to download all of your backups at once, replace
``yourdatabase-date.sql.gz`` with an asterisk (*). You can also use SFTP
in interactive mode by omitting everything after ``hosting.acquia.com``.

The ``-i`` flag tells SFTP to use a specific key. Other useful flags are
``-b`` (batch mode) and ``-v`` (verbose, used for debugging issues). You
can find more information on these options
`here <http://www.linuxdevcenter.com/cmd/cmd.csp?path=s/sftp>`__, as
well as information on using SFTP in interactive mode from the command
line.

SCP
~~~

To download with SCP, use a command like the following:

.. code-block:: none

   scp -r  [sitename].[env]@[server].prod.hosting.acquia.com:/mnt/files/[sitename]/backups/ /path/to/your/backup/folder

The ``-r`` flag recursively copies the specified directory; if you're
using this command to copy files from your docroot, for example, this
will copy everything in subdirectories as well. Depending on your
version of SCP, this may include symbolic links, so use caution if there
are symbolic links to your files directories in the directory tree where
you're using ``-r``.

rsync
~~~~~

To download with ``rsync``, use a command like the following:

.. code-block:: none

   rsync -avz -e "ssh -i ${KEY}" [sitename].[env]@[server].prod.hosting.acquia.com:/mnt/files/sitename/backups/ /path/to/your/backup/folder

The ``-a`` flag uses archive mode, which is a series of options under
one flag that attempt to preserve as exactly as possible the file
structures being transferred. This includes copying symlinks as
symlinks, copying directories recursively, and preserving the
owner:group settings on files and directories. The ``-v`` flag provides
verbose output, useful in debugging or just keeping track of progress,
and ``-z`` compresses files during data transfer. The
``-e "ssh -i ${KEY}"`` part tells ``rsync`` to use SSH to pass key
information. There are other options that can be passed in the ``-e``
flag that can be useful for synchronizing data, such as
``--ignore-existing`` (do not update files that already exist on the
receiving end) and ``--delete`` (delete files from the destination
directory that do not exist in the source directory).

.. important:: 

   There is a full list of options
   `here <http://ss64.com/bash/rsync_options.html>`__, but be careful to
   practice on non-essential data, especially if using any of the
   synchronization or delete options.

.. _restoring:

Restoring backups from the command line
---------------------------------------

To restore the database in an |acquia-product:ac| environment from a
backup file, complete the following steps:

#. Ensure that your database backup is unzipped and that it is in
   ``.sql`` format.
#. Drop your existing database, using a `Drush </acquia-cloud/drush>`__
   command similar to the following:

   .. code-block:: none

      drush @[site].[env] ah-db-import --db=[db_name] --drop

   where:

   -  ``[site]`` is the name of your application on |acquia-product:ac|.
   -  ``[env]`` is the environment into which you're importing your
      database. Acceptable values are ``dev`` (Development), ``test``
      (Staging), and ``prod`` (Production).
   -  ``[db_name]`` is the name of your database. Use the database name
      shown on the **Databases** page for the environment, not an
      environment-specific name. For example, if your site name is
      ``example``, your default database name will probably be
      ``example``, and you should use that rather than an
      environment-specific name like ``exampledev`` or ``exampletest``.

#. Run the following Drush command to restore your backup:

   .. code-block:: none

      drush @[site].[env] ah-db-import /path/to/backup/file

After your database has been restored, |acquia-product:ac| displays the
following message:

.. code-block:: none

   Imported into database successfully

For information about database backup locations, see `Downloading
backups from the command
line </acquia-cloud/manage/back-up#cli-download>`__.

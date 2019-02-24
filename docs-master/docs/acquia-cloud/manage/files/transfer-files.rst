.. include:: /common/global.rst

Copying files to a different environment
========================================

Occasionally, you may need to move files from one |acquia-product:ac|
environment to another; for example, from your Development environment
to the Staging environment, or from Production to Staging. Although the
|acquia-product:ui| offers an easy way to `copy all files at
once </acquia-cloud/manage/files#copy>`__, you may need to copy only a
single file, a single multisite set of files, or a database backup. Here
are some available methods that you can use to do this:

.. _local:

Transferring using your local environment
-----------------------------------------

One option is to simply download the file to your local machine from one
environment and then upload the file the destination environment.

Because only one ``ssh`` connection is used at any point, this method
may be the simplest to complete. However, using your local environment
for file transfer can add time, overhead, and increased network traffic
to the process.

.. _scp:

Transferring using SCP
----------------------

You can use ``scp`` (Secure Copy) from a command prompt to transfer
files using the SSH protocol. Newer versions of ``scp`` have an option
(``-3``) to transfer files between two remote servers. This still uses
your network connection to tunnel the transfer (so you will still have
the latency), but is helpful because it will transfer the file using
only one command. If you need to transfer a single small file, this
might be the best solution. The command usage will be similar to the
following:

``scp -3 examplesite.prod@server-5678.prod.hosting.acquia.com:prod/backups/prod-backup.sql.gz examplesite.test@server-1234.prod.hosting.acquia.com:test/import/``

.. _agent:

Using agent forwarding and rsync
--------------------------------

As an alternative, you can use SSH with agent forwarding to directly
copy files from one environment to another. With agent forwarding, the
commands that you run on one server will use the same credentials to
access the other, and you do not need to put a private key in either
environment.

The following example assumes that you want to copy a database backup
from your Production environment to your Staging environment:

#. Connect to your Staging environment by using SSH with the ``-A``
   parameter to allow agent forwarding:

   ``ssh -A examplesite.test@server-1234.prod.hosting.acquia.com``

#. Use ``rsync`` to copy the database backup from Production to Staging:

   ``rsync [source server]:[backup path] [destination path]``

   For example:

   ``rsync --progress examplesite.prod@server-5678.prod.hosting.acquia.com:prod/backups/prod-backup.sql.gz test/import/``

   This copies the file ``prod/backups/prod-backup.sql.gz`` on the
   server for the Production environment to the ``test/import``
   directory of the current (Staging) server.

To copy a single multisite's set of files, use the ``rsync`` command
with the ``--recursive`` parameter in a command similar to the
following:

``rsync --progress --recursive examplesite.prod@server-5678.prod.hosting.acquia.com:prod/sites/othersite/files test/sites/othersite/files``

You can complete this all in one step by passing the entire ``rsync``
command as the arguments to the SSH command:

``ssh -A examplesite.test@server-1234.prod.hosting.acquia.com "rsync --progress --recursive examplesite.prod@server-5678.prod.hosting.acquia.com:prod/sites/othersite/files test/sites/othersite/files"``

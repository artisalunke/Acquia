.. include:: /common/global.rst

About disk storage in |acquia-product:ac|
=========================================

Disk storage in |acquia-product:ac|

-  About
-  `Manage </acquia-cloud/manage/servers/storage>`__

Each |acquia-product:ac| application has a set amount of disk storage
allocated that is assigned to it. This documentation page provides
information about how |acquia-product:ac| allocates and uses that
storage, and how you can determine how much of that storage is in use by
your application.

.. _usage:

Examining your disk storage usage
---------------------------------

You can review your disk storage from the command line. To do this,
connect to your |acquia-product:ac| environment `using
SSH </acquia-cloud/ssh>`__, and then run the following command:

``df -h``

The output will appear similar to the following:

``Filesystem                           Size  Used Avail Use% Mounted on /dev/xvda1                           9.9G  4.4G  5.4G  45% / udev                                 3.7G   12K  3.7G   1% /dev tmpfs                                723M  328K  723M   1% /run none                                 5.0M     0  5.0M   0% /run/lock none                                 3.6G     0  3.6G   0% /run/shm /dev/xvdb                             30G  823M   28G   3% /mnt /dev/xvdn                             25G  2.6G   23G  11% /vol/backup-ebs /dev/xvdm                             25G  2.4G   23G  10% /vol/ebs1 /dev/xvdo                             25G  2.6G   23G  11% /mnt/brick1144138 /etc/glusterfs/glusterfs-client.vol   25G  2.6G   23G  11% /mnt/gfs``

You can determine how large each region is and how much of it is used or
available.

For more information about examining your file system, see `Assessing
disk space
usage <%5Bacquia-product:kb%5Darticle/assessing_disk_space_usage>`__.

.. _region:

Filesystem regions
------------------

The filesystem regions that are used by |acquia-product:ac| depend on
whether you are using |acquia-product:ace| or |acquia-product:acs|, as
described in the following table:

+-----------------+-----------------+-----------------+-----------------+
| Partition       | Mount           | [acquia-product | [acquia-product |
|                 |                 | :ace]           | :acs]           |
|                 |                 | Function        | Function        |
+=================+=================+=================+=================+
| ``/dev/xvdm``   | ``/vol/ebs1``   | database        | database and    |
|                 |                 |                 | static files    |
+-----------------+-----------------+-----------------+-----------------+
| ``/dev/xvdn``   | ``/vol/backup-e | backups         | backups         |
|                 | bs``            |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| ``/dev/xvdo``   | ``/mnt/gfs``    | Gluster (static | *not used*      |
|                 |                 | files)          |                 |
+-----------------+-----------------+-----------------+-----------------+

.. _local:

Local storage
-------------

From the previous `disk storage usage example <#example>`__ on this
page, for the user there are two devices that are of primary interest:

-  ``/dev/xvda1``
-  ``/dev/xvdb``

These are the storage devices that are provided with your
|acquia-product:ac| instance itself — they are both local to the
instance, and have the quickest access. These devices are essentially
disposable (also known as *ephemeral storage*).

The ``root`` directory is mounted on ``/dev/xvda1``, is 10G in size, and
houses the operating system and basic functions. Everything here can be
recreated from |acquia-product:ac| files in the event that the instance
needs to be discarded or relaunched.

The ``/mnt`` directory is mounted on ``/dev/xvdb``, and is the
instance's remaining ephemeral disk space. The content in this location
is either something we can install using our puppet master (for example,
a copy of your Drupal code that actually runs under Apache) or is
considered disposable (such as logs or other temporary information).

Gluster
-------

The `Gluster <https://www.gluster.org/>`__ file system uses a physical
disk, where the files are actually stored. In the
`example <#example>`__, that partition is ``/dev/xvdo``. These
partitions are called *bricks*, and Gluster uses one or more bricks to
form its filesystem. Gluster ensures that when changes occur, those
changes are propagated to all defined bricks. This defines high
availability functionality — by having a pair of EBS volumes that
automatically stay in sync using the Gluster daemon.

For example, even though the example application has one brick on
``web-12345`` and another on ``web-67890``, all read and write
operations use the Gluster server itself, which is based in
``/mnt/gfs``.

Database
--------

The MySQL database has a separate volume in the `example <#example>`__:
``/dev/xvdm``. MySQL normally is run from ``/var/lib/mysql``. In the
example application, the following symlink exists to that volume:

``lrwxrwxrwx 1 mysql mysql 15 May  9 23:09 mysql -> /vol/ebs1/mysql``

Each server in the pair of ``web-*`` servers for Production have this
design, however, Drupal only knows about one server, which is the
location for reading/writing to the database. MySQL replicates the data
from the active to the passive (for example, from web-12345 to
web-67890) using normal binlog processes, which keep the databases
synchronized. In the event that ``web-12345`` is unavailable,
|acquia-product:ac| will fail over (by changing a settings file) to the
other server, and then inform Drupal that is should instead use
``web-67890``. This function provides high availability services for the
database, ensuring website uptime while the secondary server is returned
to service.

.. _backup:

Backups
-------

Because |acquia-product:ac| uses synchronized copies with MySQL server,
your application is well-protected from adverse situations. However,
catastrophic failures or other emergencies can occur, which is why
backing up your applications regularly is highly recommended.

|acquia-product:ac| takes Gluster file snapshots every hour and saves
them to ``/dev/xvdn``. These snapshots are generally needed only in the
event that both Gluster bricks fail. Database dumps are also stored
here.

To learn about how often backups occur on |acquia-product:ac| and how to
create your own, see `Backing up your
application </acquia-cloud/manage/back-up>`__.

.. _storage:

Storage space
-------------

The database in the `example <#example>`__ has 25 GB to store all of the
data, binlog files, and anything else that is associated with the usual
``/var/lib/mysql`` directory. If necessary, during a maintenance window,
that volume can be replaced with any size up to the maximum of 1 TB.

The Gluster volume is separate and is set to 25 GB — its maximum size
can be raised to 1 TB.

Acquia's infrastructure monitoring warns when the database, file, or
ephemeral disks reach 95% of capacity, and again at 100%. When this
occurs, Acquia creates proactive critical priority tickets. Acquia teams
will attempt to safely reduce disk space usage to prevent a system
outage by moving the oldest database backups to the ``/mnt/tmp``
directory.

Important

These backups are not safe from deletion, and you should be sure to
download and save the files if you still need them.

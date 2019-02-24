.. include:: /common/global.rst

About |acquia-product:ac| logging
=================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/monitor/logs/*

|acquia-product:ac| uses one or more servers to deliver your Drupal
application. Each server generates its own log entries and stores them
in its own log files. Other than the Drupal watchdog log, there's no
single log file you can download that contains data from all your
application's servers. You can, however, view all the log entries for an
|acquia-product:ac| environment with `streaming in real
time </acquia-cloud/monitor/logstream>`__ either on the **Applications >
[Environment] > Logs** page or from the command line. For information
about how to use the information in logs, see `Introduction to
troubleshooting with log
files <https://support.acquia.com/hc/en-us/search?utf8=%E2%9C%93&query=introduction-troubleshooting-log-files>`__.

You can access your application's logs on |acquia-product:ac| in several
ways:

-  `Downloading active log files from the Applications > [Environment]
   > Logs page <#download>`__
-  `Downloading historical logs <#cli>`__
-  `Streaming log entries in real
   time </acquia-cloud/monitor/logstream>`__

.. _list:

Log file listing
----------------

|acquia-product:ac| makes the following logs available for your use,
either by streaming, download, or both:


.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Log type
     - Description
   * - `Apache access log </acquia-cloud/monitor/logs/apache-access>`__
     - Contains a list of requests for your application that have bypassed 
       Varnish. These requests include pages, theme files, and static media 
       files.
   * - `Apache error log </acquia-cloud/monitor/logs/apache-error>`__
     - Records any Apache-level issues. The issues reported here are usually 
       caused by general server issues, including capacity problems, 
       ``.htaccess`` problems, and missing files.
   * - `Drupal page request log </acquia-cloud/monitor/logs/drupal-requests>`__
     - Records all Drupal page loads on your application.
   * - `Drupal watchdog log </acquia-cloud/monitor/logs/drupal-watchdog>`__
     - Records Drupal-related actions on your application. The watchdog log is 
       recorded on your server if you have enabled the ``syslog`` module.
   * - `FPM error log </acquia-cloud/monitor/logs/fpm-error>`__
     - Records server-level issues with FPM’s process management in PHP. For 
       application-level PHP issues, see the **PHP error log**.
   * - MySQL slow query log	
     - Contains a list of MySQL queries that have taken longer than one second 
       to complete. Since slow query logs are stored in a root-only MySQL 
       directory on your servers, you can only download them using the Logs 
       page, and you cannot access them directly on the server. For more 
       information, see Downloading your slow query log and 
       `Tools for parsing a slow query log 
       <https://support.acquia.com/hc/en-us/search?utf8=%E2%9C%93&query=tools-parsing-slow-query-log>`__.




.. admonition:: Logging in |acquia-product:edg|

    In addition to the log files mentioned on this page,
    |acquia-product:edg| offers additional audit and task logging. For more
    information, see `Monitoring your Factory </site-factory/monitor>`__.

.. _download:

Downloading active log files from the Logs page
-----------------------------------------------

You can download the most recent logs for each of an environment's
servers from the **Logs** page. On the Logs page:

#. Select the environment for which you want to download a log.
#. Click **Logs**, and then click **Download Logs**.

   |Downloading logs from the Logs page|

#. Click the **Download** link for the log you want to download. If
   available for immediate download, the log file will begin
   downloading; if the log file must be created on-demand, a dialog box
   will display with the status of the request:

   |Pending log dialog box|

#. Once the log file is ready for download, click **Download** to
   retrieve it.

The log file will be downloaded as ``logfilename-timestamp.tar.gz``.

.. _cli:

Downloading historical logs directly from the server
----------------------------------------------------

You can access logs using SSH, rsync, scp, or other tools.

Log files do not persist after a server is relaunched or resized

Historical logs are stored in a location on the server that is optimized
for fast read/write activity. While this works for actively and
simultaneously updating multiple log files, the directory will not
persist after a server is relaunched or resized. Log files do persist
when a server is rebooted. A relaunch can happen at any time (for
instance, in the event of hardware failure). For this reason, if you
want to ensure that logs are stored permanently, you should routinely
copy log files to permanent storage. For example, you could create a
cron task that periodically copies log files to a directory in your
|acquia-product:ac| file system (such as
``/mnt/gfs/[site].[env]/files-private/logs``), or to a remote location
(such as Amazon S3).

.. _location:

Location of log files
~~~~~~~~~~~~~~~~~~~~~

Each server maintains its own log files, with the exception of the
Drupal watchdog log. For each server, the log file is located at
``/var/log/sites/[site].[env]/logs/[servername]/[logname].log``. You can
find your site name and server names on the **Servers** page. For
example, the Apache error log for the Dev environment of a site named
``myexample`` on a server named ``srv-25`` would be:

``/var/log/sites/myexample.dev/logs/srv-25/error.log``

The available logs are named as follows:

+-----------------------------+-------------------------+
| Log type                    | Name                    |
+=============================+=========================+
| **Apache access log**       | ``access.log``          |
+-----------------------------+-------------------------+
| **Apache error log**        | ``error.log``           |
+-----------------------------+-------------------------+
| **PHP error log**           | ``php-errors.log``      |
+-----------------------------+-------------------------+
| **Drupal page request log** | ``drupal-requests.log`` |
+-----------------------------+-------------------------+
| **Drupal watchdog log**     | ``drupal-watchdog.log`` |
+-----------------------------+-------------------------+

All Drupal watchdog log messages are combined on the server whose name
has the lowest number. For example, if your application has servers
named ``srv-7``, ``srv-22``, and ``srv-23``, the Drupal watchdog log
would be found on srv-7.

Archived logs
~~~~~~~~~~~~~

|acquia-product:ac| creates a new server log every day and compresses,
archives, and saves old logs by date in the following format (YYYYMMDD):

-  ``access.log-20140527.gz``
-  ``error.log-20140527.gz``
-  ``drupal-requests.log-20140527.gz``
-  ``drupal-watchdog-20140527.gz``
-  ``php-errors.log-20140527.gz``

Log files are archived by file name; files in the ``logs`` directory
that don't have the default names will not be archived.

Accessing logs using SSH
~~~~~~~~~~~~~~~~~~~~~~~~

You can access log files on a server using SSH. For example, to view the
Apache access log on the specified server:

``less /var/log/sites/[site].[env]/logs/[servername]/access.log``

Downloading web server logs using the rsync command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the ``rsync`` command from your local machine to download
logs:

#. To list the log files on your web server, use the ``rsync`` command
   and substitute the correct values for your application, server, and
   |acquia-product:ac| SSH key pathname (typically ``~/.ssh/id_rsa``):

   ``rsync -avz -e 'ssh -i /path/private/keyfile' [username]@[host name]:[log path]``

   The ``rsync`` command produces a list like the following example:

   .. code-block:: none

      receiving file list ... done 
      drwxr-xr-x 4096 2010/01/26 19:34:05 . 
      -rw-r--r-- 83581323 2010/01/27 12:05:53 access.log 
      -rw-r--r-- 214919 2010/01/27 12:04:57 error.log 
      -rw-r----- 995 2010/01/27 04:15:29 php-errors.log

#. For each file that you want to download, use the ``rsync`` command
   and substitute the correct values for your application, server,
   |acquia-product:ac| SSH key, and the file that you want to download:

   ``rsync -avz -e 'ssh -i /path/to/private/key/file' [site name]@[host name]:[log path]/[file name].log``

   For example:
   
   .. code-block:: none

      rsync -avz -e 'ssh -i /Users/esymbolist/.ssh/id_rsa' example.prod@srv-1234.devcloud.hosting.acquia.com /mnt/gfs/home/example/logs/access.log-20151225.gz/access.log

Downloading an individual server log using the scp command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the ``scp`` command from your local machine to individual
logs. To download an individual server log, use the ``scp`` command and
substitute the values for your application, server, |acquia-product:ac|
SSH key pathname (typically ``~/.ssh/id_rsa``), and the file you want to
download:

``scp -i /path/to/private/key/file [site name]@[host name]:[log path]/[file name].log [local path]``

For example:

.. code-block:: none

   scp -i /Users/esymbolist/.ssh/id_rsa example.prod@srv-1234.devcloud.hosting.acquia.com:/mnt/gfs/home/example/logs/access.log-20151225.gz/access.log /Documents/logs

.. _other:

Additional (inaccessible) logs
------------------------------

Acquia uses additional logs from the logs previously mentioned on this
page that are not available to customers. These logs are inaccessible
for several reasons, including the potential for security issues related
to shared resources.

-  *binlogs* - Binlog (binary log) files are used to replicate data from
   the master database to a replica database. All statements that modify
   data (such as ``create``, ``update``, and ``delete`` statements) add
   lines to the MySQL binlogs. Queries that only read from the database,
   without changing the contents, do not add a line to the binlogs.
   Staging environments (which do not have redundant databases) also use
   binlogs, which helps keep feature and performance parity between
   non-production and production environments.
-  *Email logs* - Email logs are often a shared server resource and may
   contain sensitive information. Because of this, they are not
   generally available to customers.

.. _related:

Related topics
--------------

-  `Using logs </acquia-cloud/monitor/use-logs>`__
-  `Searching the error logs to troubleshoot
   problems <https://support.acquia.com/hc/en-us/search?utf8=%E2%9C%93&query=/searching-error-logs-troubleshoot-problems>`__

.. |Downloading logs from the Logs page| image:: https://cdn4.webdamdb.com/1280_MsD7gHjQB9e1.png?1526475711
   :alt: Downloading logs from the Logs page
.. |Pending log dialog box| image:: https://cdn4.webdamdb.com/1280_A3kwTRQcQv42.png?1527264625
   :alt: Pending log dialog box

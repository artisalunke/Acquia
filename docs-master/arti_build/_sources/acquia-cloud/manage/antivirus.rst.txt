.. include:: /common/global.rst

Enabling virus scanning for file uploads
========================================

You can enable virus scanning of file uploads for your
|acquia-product:ac| applications. |acquia-product:ac| virus scanning
uses `ClamAV <http://www.clamav.net>`__, an open source antivirus
engine. |acquia-product:ac| updates the ClamAV virus definitions daily.
After you have enabled virus scanning, ClamAV protects your application
from viruses uploaded by form file uploads and prevents uploaded files
from being saved if it detects a virus.

To enable virus scanning, using ClamAV, for file uploads to your
website, install, enable, and configure the
`ClamAV <http://www.drupal.org/project/clamav>`__ module, which connects
to the ClamAV executable on your |acquia-product:ac| server instance.

.. note::  

   |acquia-product:ac| does not include or support the use of ClamAV as a
   daemon.

.. _configuring:

Configuring the ClamAV module
-----------------------------

The ClamAV module (available for Drupal 7 and 8) connects with ClamAV to
scan files uploaded with CCK's ``filefield`` widget, CCK's
``imagefield`` widget, and normal Drupal form file uploads.

Install and enable the ClamAV Drupal module on your application, and
then configure the following settings:

#. Under the **Scan method** heading, select **Executable**.
#. Under the **Executable mode configuration** heading, in the
   **Executable path** field, enter ``/usr/bin/clamscan``.
#. Click **Save configuration**.

ClamAV thereafter scans all files uploaded to your application for
viruses. If ClamAV finds a virus, it displays a message to the user
reporting that the file could not be uploaded, and then logs the event
to ``stdout`` and ``stderr``, with the file name and virus name. You can
then find the entry in the |acquia-product:ac| ``drupal-watchdog.log``.

.. _current:

Scanning files that are already present
---------------------------------------

If you have uploaded files to your application using methods that differ
from the normal Drupal upload methods, you can still use ClamAV to scan
these files. Because this method uses CPU resources, Acquia recommends
that you copy the files to your development or staging environment and
scanning files there, rather than in production. To scan files on your
server, open a command prompt window and then enter the following
command:

``clamscan -ri``

The ``r`` parameter causes ClamAV to scan all files recursively, in the
current directory and subdirectories, and the ``i`` parameter displays
only the infected files, if any.

You can also use the following cron command to run regular scans for
your website:

.. code-block:: none

   --any--  0 * * * *   /usr/bin/clamscan -ri /mnt/tmp/ | mail -s "hourly website clam results" myemail@example.com

This command will scan files if run in ``/sites/default/files``. If you
want to scan code, the command must be run from the code directory.

For a more configurable and extensible version of this command, you can
`download and use this
script <https://gist.github.com/acquialibrary/35210077d42d11ca8c3b80e78253b7dd/archive/90662b7b0a9bac88eeb315041ae9e77574786ebe.zip>`__,
which provides configurable notification emails, in a cron command.

.. note::  

   Clamscan will not scan the database, because it does not read binary data.

   Even with a regular scan, malware may still be present in the database
   or in your ``/tmp`` directory.

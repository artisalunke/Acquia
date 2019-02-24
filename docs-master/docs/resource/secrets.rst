.. include:: /common/global.rst

Storing sensitive information outside of your codebase
======================================================

From time to time, your website may need access to sensitive
credentials, passwords, or other private information to be available in
order to function properly, but the information must not be stored in
your version control repository for privacy reasons.

For example, the following modules or third-party integrations may
require a secret or access key:

-  Drupal modules (Shield)
-  Amazon S3 configuration variables (``s3fs_awssdk2_access_key``,
   ``s3fs_awssdk2_secret_key``, ``s3fs_bucket``)
-  Google Cloud Messaging integration variables
   (``push_notifications_gcm_api_key``)
-  Google CAPTCHA variables (``recaptcha_secret_key``,
   ``recaptcha_site_key``)

To make this information available only to your website, while keeping
it out of your codebase, use one of the following methods:

-  |Create a secrets file|_
-  |Create nobackup directory|_ that contains your sensitive data

.. |Create a secrets file| replace:: Create a ``secrets.settings.php`` file
.. _Create a secrets file: #secrets-settings-php-file

.. |Create nobackup directory| replace:: Create a ``nobackup`` directory
.. _Create nobackup directory: #nobackup-directory


``secrets.settings.php`` file
-----------------------------

Storing sensitive credentials in a secrets file instead of your
website's database means your sensitive data will not be present in your
database backups, allowing you to distribute database backups to team
members who may need a database snapshot but not full access to external
systems.

To create and use a secrets file with your website, complete the
following steps:

#. `Connect to your server </acquia-cloud/ssh>`__ using SSH
#. Navigate to the ``/mnt/files/[sitename].[env]/`` directory, where
   ``[sitename]`` is your website's name and ``[env]`` is your website's
   environment.
#. Create the ``secrets.settings.php`` file if it does not already
   exist.

   .. important::  Do not create the file in 
      ``/mnt/gfs/[sitename].[env]/files/``, as files in that directory are 
      publicly accessible.

#. To make the secrets file available to your application, add the lines
   in the following example to the appropriate location based on your
   installed product:

   -  *Acquia Cloud* - To your website's ``settings.php`` file
   -  *Acquia Cloud Site Factory* - To a 
      `post-settings-php hook </site-factory/extend/hooks/settings-php>`__ 
      named ``secrets.php``

      .. code-block:: php

         $secrets_file = sprintf('/mnt/files/%s.%s/secrets.settings.php', $_ENV['AH_SITE_GROUP'],$_ENV['AH_SITE_ENVIRONMENT']);

         if (file_exists($secrets_file)) {
            require $secrets_file;
         }

   Because the code uses ``$_ENV['AH_SITE_ENVIRONMENT']`` to build the
   link to the ``secrets.settings.php`` file, it is possible to provide
   unique files for each of your website's environments.

.. important::  It is important you keep your own backups of your
   ``secrets.settings.php`` file. Because this location is outside of your
   website's files area, the |acquia-product:edg| 
   `full-website backups </site-factory/manage/website/backup>`__ will not 
   back up this file.


``nobackup`` directory
----------------------

You can also create a special ``nobackup`` directory where you can place
files that contain sensitive credentials. For information about using
this method, see 
`Storing private information in the file system </acquia-cloud/manage/files/system-files/private>`__.

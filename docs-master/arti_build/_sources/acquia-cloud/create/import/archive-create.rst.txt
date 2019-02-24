.. include:: /common/global.rst

Creating a Drupal site archive for import
=========================================

Importing a site archive

-  `Intro </acquia-cloud/create/import/archive>`__
-  `Prepare </acquia-cloud/create/import/prepare>`__
-  Create
-  `Import </acquia-cloud/create/import/archive-import>`__

`After you prepare your
application </acquia-cloud/create/import/prepare>`__, create a Drupal
site archive.

A Drupal site archive is a gzip-compressed ``.tar`` file that contains
the following structure:

-  A single top-level directory that contains your application's Drupal
   ```[docroot]`` <%5Bacquia-product:kb%5Darticles/docroot-definition>`__,
   including the ``index.php`` file, the modules and the ``/includes``
   directory, and ``sites/*``.

   |acquia-product:ac| imports your application's user-uploaded files
   from the ``[docroot]/sites/*/files`` directory of the directory that
   contains a ``settings.php`` file.

-  The uncompressed MySQL dump file from your Drupal application in the
   root of the ``.tar`` file. This file can have any name, but must have
   an ``.sql`` extension.

The following sample archive file shows the site archive structure of a
Drupal 7 application with the ``tar -tzf archive.tar.gz`` command that
lists the contents of the tar file:

``tar -tzf archive.tar.gz``

``./your-database-goes-here.sql ./drupal-7 ./drupal-7/index.php [... other Drupal files ...] ./drupal-7/sites ./drupal-7/sites/cleaninstall.localhost ./drupal-7/sites/cleaninstall.localhost/settings.php ./drupal-7/sites/cleaninstall.localhost/files/ ./drupal-7/sites/cleaninstall.localhost/files/myimage.jpg``

.. _drush:

Creating a site archive file with Drush
---------------------------------------

#. Verify that Drush version 4.5 or later is installed. Drush 8 is
   recommended. You can `download Drush from
   GitHub <https://github.com/drush-ops/drush>`__. You may need to
   `install
   Composer <https://github.com/drush-ops/drush#installupdate---composer>`__
   as a prerequisite for installing Drush. Drush is also included with
   `|acquia-product:add| </dev-desktop>`__.
#. Go to the Drupal directory and enter the following command:

   ``drush archive-dump --destination=../mysite.tar.gz``

   Drush saves the ``mysite.tar.gz`` site archive file to the parent
   directory of your current Drupal directory. If the command displays
   error messages, ensure that it has the required permissions to save
   files in that directory.

#. Copy ``mysite.tar.gz`` to your local computer.

.. _access:

Making the site archive file available
--------------------------------------

To import a site archive file using the |acquia-product:ui|, the file
must be located at a publicly accessible URL. You may be able to use a
service such as Dropbox or Google Drive, or a web server that you
control.

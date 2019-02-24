.. include:: /common/global.rst

Importing a Drupal site archive
===============================

Importing a site archive

-  Intro
-  `Prepare </acquia-cloud/create/import/prepare>`__
-  `Create </acquia-cloud/create/import/archive-create>`__
-  `Import </acquia-cloud/create/import/archive-import>`__

One method of `importing an existing Drupal
application </acquia-cloud/create/import>`__ to |acquia-product:ac| is
to create a Drupal site archive and then use the |acquia-product:ui| to
install the site archive. This method works best for applications that
aren't very large (website archives smaller than 100MB).

To import an existing Drupal application to |acquia-product:ac| using a
site archive file, complete the following steps:

#. `Prepare your application </acquia-cloud/create/import/prepare>`__
   before you export it from your current environment.

#. `Create a Drupal site archive file for
   import </acquia-cloud/create/import/archive-create>`__ by exporting
   your existing Drupal application.

   You can use the tools provided in your existing application
   environment (including |acquia-product:add|), or you can use the
   Drush ``archive-dump`` command. The ``archive-dump`` command is
   available in Drush 4.5 or later. For more information about importing
   your application using Drush, see `Importing an existing application
   using Drush </acquia-cloud/create/import/drush>`__.

#. `Import your website </acquia-cloud/create/import/archive-import>`__
   into the Development environment of your |acquia-product:ac|
   application. |acquia-product:ac| commits your application code to
   your |acquia-product:ac| code repository, installs the database, and
   uploads your files.

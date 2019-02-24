.. include:: /common/global.rst

Storing private information in the file system
==============================================

*The methods described on this page do not apply to
|acquia-product:edg|.
|acquia-product:edg| subscribers should instead use the procedures
described in `Storing sensitive information outside of your
codebase </resource/secrets>`__.*

You can store sensitive keys, certificates, and other credentials
securely on |acquia-product:ac| by using a ``nobackup`` directory that
is available in the file system. This is the best place to store
environment-specific keys, as it is not in the
`docroot <%5Bacquia-product:kb%5Darticle/docroot-definition>`__ or part
of the code repository, but is protected by SSH access.

Important

The ``nobackup`` directory is not protected or covered by
`|acquia-product:ac| disaster recovery
backups </acquia-cloud/arch/availability#automatic>`__.

To place this directory, complete the following steps:

#. Sign in to your server `using SSH </acquia-cloud/ssh/enable>`__.
#. Create the following directory:

   ``/mnt/gfs/[sitename].[env]/nobackup``

#. Create any required subdirectories in the ``nobackup`` directory for
   organizing your files, such as the following:

   -  ``/mnt/gfs/mysite.dev/nobackup/apikeys``
   -  ``/mnt/gfs/mysite.test/nobackup/apikeys``
   -  ``/mnt/gfs/mysite.prod/nobackup/apikeys``

You can now use the ``nobackup`` directory and any of its subdirectories
to store your private files.

.. _retrieve:

Retrieving sensitive keys
-------------------------

If you are storing required credentials in the ``nobackup`` directory,
you can use `Acquia-provided environmental
variables </acquia-cloud/develop/env-variable>`__ to retrieve those
credentials for your application. To enable this functionality, complete
the following steps:

#. In your ``nobackup`` directory or one of its subdirectories, create a
   PHP file. The PHP file can have any name, including the following
   example:

   ``/mnt/gfs/mysite.prod/nobackup/apikeys/mysite_apikeys.php``

#. Edit the PHP file and add one or more environmental variables,
   similar to the following:

   ``putenv('MY_API_KEY_NAME=[key_value]');``

#. Save the PHP file.
#. Edit your application's ``settings.php`` file and add code similar to
   the following to incorporate the new PHP file that you created into
   your ``settings.php`` file:

   ``if (isset($_ENV['AH_SITE_ENVIRONMENT'])) {   switch ($_ENV['AH_SITE_ENVIRONMENT']) {     case 'dev':       require '/mnt/gfs/mysite.dev/nobackup/apikeys/mysite_apikeys.php';       break;     case 'test':       require '/mnt/gfs/mysite.test/nobackup/apikeys/mysite_apikeys.php';       break;     case 'prod':       require '/mnt/gfs/mysite.prod/nobackup/apikeys/mysite_apikeys.php';       break;   } }``

#. Create settings variables for Drupal's use by adding the following
   lines to your ``settings.php`` file:

   -  *Drupal 8*

      ``$settings['mysite_apiname'] = getenv('SOME_API_KEY_NAME'); $settings['mysite_apikey'] = getenv('SOME_API_KEY');``

   -  *Drupal 7*

      ``$conf['mysite_apiname'] = getenv('SOME_API_KEY_NAME'); $conf['mysite_apikey'] = getenv('SOME_API_KEY');``

#. Save the ``settings.php`` file.

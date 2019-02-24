.. include:: /common/global.rst

Preparing a Drupal application for export
=========================================

Before you import your Drupal application to |acquia-product:ac|,
perform the following tasks to prepare your application for the import
process. This will help you better prevent, diagnose, and troubleshoot
issues that arise as you change your hosting environment.

To prepare your application for export:

#. Perform all outstanding Drupal core and module updates in your
   current environment.
#. Remove any disabled Drupal modules that you aren't using.
#. Reconfigure your application to use Memcached. |acquia-product:ac|
   servers use `Memcached </acquia-cloud/performance/memcached>`__. If
   you're coming from another hosting provider that uses
   `Redis <https://redis.io/>`__ or some other storage mechanism, you'll
   need to reconfigure your application to use Memcached.
#. Connect to |acquia-product:ais| to ensure that your application is
   ready to go for launch. We recommend that you install the
   `|acquia-product:anc| <https://www.drupal.org/project/acquia_connector>`__
   module, which feeds data to |acquia-product:ais|.
   |acquia-product:ais| has a long list of recommended configurations.
   Learn more about `installing the
   |acquia-product:anc| </acquia-cloud/insight/install>`__ and review
   the `Prelaunch
   checklist <%5Bacquia-product:kb%5Darticles/pre-launch-check-list>`__
   for more details about the checks we recommend and what
   |acquia-product:ais| looks for.
#. Test your application by clicking through your application and making
   sure features and performance are as expected. Make sure there are no
   JavaScript errors in your browser's console. Check the error logs to
   ensure that everything is running correctly.
#. Make sure you do not have a PHP memory limit set in your
   ``.htaccess`` or Drupal ``settings.php`` files. If your application
   is configured with a larger PHP memory limit than the memory limit
   configured on your |acquia-product:ac| server, it won't be able to
   start up.
#. Large files or directories in your
   ```[docroot]`` <%5Bacquia-product:kb%5Darticles/docroot-definition>`__,
   such as ``/photo`` or ``/video``, can cause problems when you send
   your codebase to |acquia-product:ac|. |acquia-product:ac| can fail
   when it attempts to send your code with large files to its web
   servers.

   Move these files and directories to a ``/files`` directory for your
   application, such as ``[docroot]/default/files``. After you move the
   files and directories, you can make symlinks to their relative
   locations on your local server, which will be maintained after you
   send your application to |acquia-product:ac|. For more information,
   see `Working with files </acquia-cloud/manage/files>`__.

#. Clear your Drupal caches.
#. Make a full back up of your application and store this copy in a safe
   place. Verify that you can revert to your backup copy.

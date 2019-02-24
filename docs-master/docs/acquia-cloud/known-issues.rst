Known issues in |acquia-product:ac|
===================================

This page describes known issues in |acquia-product:ac|:

- Some Drupal modules are not supported on |acquia-product:ac|
   The design of the Acquia platform can sometimes cause
   incompatibilities with Drupal contributed modules. Some Drupal
   modules are not supported on |acquia-product:ac|; these are listed in
   `Modules and applications incompatible with
   Acquia Cloud </acquia-cloud/develop/drupal/module-incompatibilities>`__.
   Other modules can be used on |acquia-product:ac|, but may require
   caution or special configuration; these are listed in `Modules to use
   with caution on
   Acquia Cloud </acquia-cloud/develop/drupal/module-caution>`__.
   For information about other software that is incompatible with
   |acquia-product:ac|, see `Unsupported
   software </acquia-cloud/develop/non-drupal#unsupported>`__.
- Drupal 8.4 and Drush
   Websites running Drupal versions 8.4 or later must be built using
   Composer, and updating using Drush will no longer be possible.
- Rebuild caches after updating Drupal
   Customers upgrading their websites to newer versions of Drupal 8
   should rebuild website caches after the upgrading. Unexpected errors
   and problems with some page displays may occur until caches are
   rebuilt.
- Drush 9 failures
   If you are using Drush 9 in an |acquia-product:ac| environment, you
   may encounter multiple errors such as:

   -  ``Fatal error: require(): Failed opening required '/var/www/site-php//D8--[sitename]-settings.inc'``
   -  ``Drush command terminated abnormally due to an unrecoverable error.``

  *Workaround*
   Drush 9 is not yet fully supported on the |acquia-product:ac|
   platform. You can check to see if this is a problem with using Drush
   9 by running the following two commands from a command prompt:

   -  ``drush 9 php-eval 'var_export($_ENV['AH_SITE_NAME'] , true);'``
   -  ``printenv 'AH_SITE_NAME'``

   These values should be equal. If they are not:

   #. Edit your website's ``settings.php`` file.
   #. Before the `Acquia
      require </acquia-cloud/develop/code/require-line>`__ line, add
      ``$_SERVER['PWD']=DRUPAL_ROOT;``.
   #. Save the ``settings.php`` file.

- Using vendored Drush may disable some Drush commands
   Including Drush in an |acquia-product:ac| application branch may
   create a conflict between the version installed in the ``vendor``
   directory and the version installed in |acquia-product:ac|,
   disabling some Drush commands. Most notably, it disables
   ``Install distribution``, which allows you to install a different
   version of Drupal into the deployed branch.

  *Workaround*
   Modify the existing branch by removing Drush from from the branch you
   wish to install a Drupal distribution into, or create a new branch
   without the Drush dependency.

   Drush is generally found in one of the following directories:

   -  ``vendor/drush``
   -  ``docroot/vendor/drush``

   If you are using Composer, you can use it to remove Drush by
   executing the following command:

   ``composer remove drush/drush``

   See `Vendored Drush known
   issue <https://support.acquia.com/hc/en-us/search?utf8=%E2%9C%93&query=vendored-drush-known-issue>`__
   for additional details.

- Drush aliases and on-demand environments
   Drush aliases for |acquia-product:ac| CD environments are only
   downloaded if the environment is active.
- Failures when running ``update.php`` with Drush
   Attempting to run ``update.php`` on Drupal 8 will fail with the
   following error message:
   ``In order to run update.php you need to either be logged in as admin or have set $settings['update_free_access']``
  *Workaround* - Use one of the following methods:
   -  Run ``drush updbs`` to complete database updates.
   -  Whenever you need to run ``update.php``, use your browser's cookie
      manager to grab the session cookie from your current authenticated
      Drupal session, and then remove the leading ``S`` from the session
      name.
   -  If you are running updates on your Dev or Stage environments,
      temporarily disable HTTPS while running updates.
   -  Edit your ``settings.php`` file to temporarily set
      ``$settings['update_free_access']`` to ``TRUE`` during your
      updates.
   -  **ADVANCED** - Add the following code to your ``update.php`` file
      (directly following the ``use`` statements) to force Drupal to
      acknowledge the ``X-Forwarded-Proto`` value when determining if
      the request should be treated as HTTPS:
      
      .. code-block:: php

          if (isset($_SERVER["HTTP_X_FORWARDED_PROTO"]) && 
             $_SERVER["HTTP_X_FORWARDED_PROTO"] == "https") {  
              $_SERVER['HTTPS'] = 'on';
             }

- Unicode characters and emoji are not supported in branch names
   If a branch name contains a Unicode character, such as an emoji, users will 
   receive a ``Failure due to fatal system error`` message when attempting to 
   switch to that branch. This error affects all |acquia-product:ac| systems, 
   including the pipelines feature.
- Deployed branches cannot be deleted
   |acquia-product:ac| does not allow you to delete branches that are
   deployed to an environment. If you attempt to delete a branch from
   the command line, an error message similar to the following will be
   displayed:

   ``remote: Operation rejected: remote: Git branch or tag test_branch cannot be deleted because it is currently deployed to testsite.prod``

- |acquia-product:anc| request timeouts
   When a Drupal website is connected to an |acquia-product:aqs|, it
   sends heartbeat requests during each cron run. By default, cron runs
   at the beginning of each hour, which can cause the
   |acquia-product:aqs| service to receive thousands of simultaneous
   connections across all subscriber websites. This can cause some
   requests to timeout. 
  *Workaround*
   If your subscription service is
   experiencing timeouts, Acquia recommends that you `modify your cron
   runs </acquia-cloud/manage/cron>`__ to not begin at the start of the
   hour.
- |acquia-product:anc| module conflicts with Remote stream wrapper module
   The |acquia-product:anc| module has a conflict with the `Remote
   stream
   wrapper <https://www.drupal.org/project/remote_stream_wrapper>`__
   module.
  *Workaround*
   Apply this `patch <https://www.drupal.org/node/2891977>`__, available on
   Drupal.org.
- Altering the ``$databases`` array causes connection errors
   Websites altering the ``$databases`` array in ``settings.php`` to
   enable third-party database connections may experience connection
   errors when the connection setup is delayed in ``settings.php``. For
   help, see `Modifying the database connections within
   Drupal <https://support.acquia.com/hc/en-us/search?utf8=%E2%9C%93&query=modifying-database-connections-within-drupal>`__.
- Deprecated memcache class in PHP 7
   Memcached support in PHP 7 environments is provided by the
   ``php-memcached`` extension. This provides the ``memcached`` PHP
   class for interacting with Memcached storage. It does *not* provide
   the ``memcache`` (no *d*) class, which was previously provided by the
   PECL memcache extension in PHP 5.x environments.
   This should not affect most users, as the `Memcache API and
   Integration <https://www.drupal.org/project/memcache>`__ module
   supports both classes. However, other tools may rely exclusively on
   the deprecated ``memcache`` class, which can cause website issues if
   PHP is upgraded to version 7. If you use SimpleSAMLPHP, be aware of
   the `work being done to address this
   issue <https://github.com/simplesamlphp/simplesamlphp/pull/395>`__.
- Legacy alerts from New Relic fail with the removal of TLS 1.0
   Legacy alerts from New Relic fail with the removal of TLS 1.0 from
   Acquia systems. For help in updating your alerts, see: `Transition
   from legacy alerting to New Relic
   Alerts <https://docs.newrelic.com/docs/alerts/new-relic-alerts/getting-started/transition-legacy-alerting-new-relic-alerts>`__
   and `Availability monitoring
   (legacy) <https://docs.newrelic.com/docs/alerts/new-relic-alerts/managing-notification-channels/availability-monitoring-legacy#limits>`__.
- Git checkouts fail after reporting non-existent changes to binary files
   Git checkouts fail with the following error when non-text files contain a 
   specific byte sequence and are not explicitly defined as binary files:
   ``Your local changes to the following files would be overwritten by 
   checkout. Please, commit your changes or stash them.``
  *Workaround*
   Edit the following section of your ``.gitattributes`` file:

   .. code-block:: none

      # Auto-detect text files, ensure they use LF. 
      *         text=auto eol=lf

   and then make one of the following changes:

   -  Remove the line beginning with ``*``
   -  Remove the ``eol=lf`` text
   -  Ensure that a specification line is added for every binary file
      extension used in your repository

- Error message when pushing code to Git
   When attempting to push code, some users may encounter errors
   similar to the following:

   ``remote: error: insufficient permission for adding an object to repository database ./objects``

   This can happen when a directory is owned by the *root* account instead of 
   the *siteuser* account. `Contact Acquia Support </support#contact>`__ to 
   correct the directory's ownership settings.

- Using Midnight Commander can cause gluster service interruptions
   |acquia-product:ace| customers who use GNU Midnight Commander can
   experience service interruptions when trying to access their GFS
   mount. Because of this, Acquia currently recommends that you do not
   use this software with your Acquia-hosted websites.
- Importing a site archive from a local file
   The [acquia-product:ui] does not support importing a site archive
   from a local file using the UI. Instead, you can `import a site
   archive from a URL </acquia-cloud/create/import/archive-import>`__ or
   `import using Drush </acquia-cloud/create/import/drush>`__.
- Theme change issues with Twig caches on Drupal 8
   Drupal 8 applications on |acquia-product:ace| can experience issues
   where cached Twig templates fall out of sync on different web
   server instances when changes to themes are being made and a code
   deployment has been performed. The problem arises from having
   separate copies of the compiled Twig templates on each web server
   instance and a related `Drupal core
   issue <https://www.drupal.org/node/2752961>`__.
  *Workaround*
   When you make changes to themes in Drupal 8 applications on 
   |acquia-product:ace|, connect to each web server instance, and then run a 
   command similar to the following to remove the outdated Twig templates:

   ``drush @[sitename].[prod] --uri=http://[site_URL]/ ev '\Drupal\Core\PhpStorage\PhpStorageFactory::get("twig")->deleteAll();'``

- Backups page may not list all available backups
   The **Backups** page in the [acquia-product:ui] lists recent backups
   for the |acquia-product:ac| environment. However, there is a delay
   between the time when backups are created and when they are added or
   removed from the **Backups** page. As a result, the most recently
   created backups may not yet be listed, while older backups that have
   been replaced and deleted may be listed, but not in fact be available
   for download or for restoring the database.
  *Workaround*
   You can connect to your server using SSH, SFTP, scp,
   or rsync, and download the backup files from the
   ``/mnt/files/[site].[env]/backups`` directory. For more information,
   see `Downloading database backups from the command
   line </acquia-cloud/manage/back-up/cli>`__.
- AuthUserFile in .htaccess is not supported
   The ``AuthUserFile`` directive in the Apache ``.htaccess`` file sets
   the name of a text file containing a list of users and passwords for
   user authentication. Using ``AuthUserFile`` is not supported in
   |acquia-product:ac|, since its value must be either an absolute path
   or a path relative to the server root, and therefore won't work
   across different |acquia-product:ac| environments.
- SymLinksIfOwnerMatch in .htaccess is not supported
   Due to the configuration of directory ownership and permissions for
   your |acquia-product:ac| application's codebase and files
   directories, use of the ``SymLinksIfOwnerMatch`` option in your
   application's ``.htaccess`` file will prevent your web server from
   being able to access any of the assets in your files directory. The
   ``FollowSymLinks`` option should be used instead.
- The server resize Cancel button does not always work
   In the legacy |acquia-product:ac| interface, when a user clicks
   **Resize** and then clicks **Cancel**, occasionally the cancel button
   does not dismiss the dialog box.
- Some environment names in the updated |acquia-product:ac| interface
   have changed
   After the updated |acquia-product:ac| interface was released on
   December 13, 2016, in a few cases some environment names changed to
   unexpected values.
  *Workaround*
   Rename the affected environment to use the
   desired name. For information about how to rename an environment, see
   `Working with
   environments </acquia-cloud/manage/environments#rename>`__.
- zlib "freed prematurely" message when inspecting tasks
   When inspecting the output of any successful or failed task, the
   final line is: ``zlib(finalizer): the stream was freed prematurely``.
   This message in the task's output does not indicate a specific issue,
   and can be ignored.

.. include:: /common/global.rst

Altering values in settings.php with hooks
==================================================

|acquia-product:edg| does not allow you to directly modify your website's ``settings.php`` file.

However, to enable you to make changes to the values included in the file, |acquia-product:edg| contains hooks at
the beginning and end of the ``settings.php`` file that allow you to execute custom code during the website's bootstrap
process.

.. important::

   * Files executed by these hooks must have a ``.php`` extension.

   * Because commands executed by these hooks are run for every request for the web node, commands in the hook files
     should be lightweight (for example, setting variables) and should not read or write to either databases or files.
     Accessing databases or files using the hook file can greatly impair your website's performance. If you need to access
     databases or files, you should use modules instead.

Using the ``settings.php`` hooks
--------------------------------

Like several of the other hooks in use by |acquia-product:edg|, you must create a script file and then place it in a
particular directory. The script file will be executed at the appropriate time when doing database updates for your
websites.

For detailed instructions, see `Executing your commands with a hook </site-factory/extend/hooks>`__.

Pre-``settings.php`` example script
-----------------------------------

Modify the following script to suit your needs in ``pre-settings-php`` hooks:

Conditionally increasing memory limits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Certain pages on your websites may require increased memory limits to function properly. To make this change with your
websites, use the following script:

.. code-block:: php

   <?php
   /**
   * Sets a higher memory limit for admin/structure/menu which frequently needs
   * an unusually high amount of memory to load, due to complexity.
   * For additional examples of changing memory limits for pages on your websites, see
   * https://docs.acquia.com/articles/conditionally-increasing-memory-limits
   */
   if (strpos($_GET['q'], 'admin/structure/menu/') === 0) {
      ini_set('memory_limit', '700M');
   }

For additional examples, see `Examples of conditional memory limit changes </articles/conditionally-increasing-memory-limits>`__.

Post-``settings.php`` example scripts
-------------------------------------

Modify the following scripts to suit your needs in ``post-settings-php`` hooks:

Enabling memcache
^^^^^^^^^^^^^^^^^

To enable memcache on your Acquia Cloud Site Factory websites, complete the following steps:

- Contact your Technical Account Manager or Account Manager to discuss your cluster's hardware needs.
- Add the Memcache module to your codebase.
- Modify the following script to provide the necessary configuration details for memcache:

.. code-block:: php

   $conf['cache_backends'][] = '<path to the memcache.inc file>';
   $conf['cache_default_class'] = 'MemCacheDrupal';
   $conf['cache_class_cache_form'] = 'DrupalDatabaseCache';

|acquia-product:edg| customers using Drupal 8 and |acquia-product:blt| should also apply the patch from `issue #2766509`_ on
Drupal.org, and use |this_example_from_blts_issue_queue|_ to update memcache to a recommended version.

.. _issue #2766509: https://www.drupal.org/node/2766509
.. |this_example_from_blts_issue_queue| replace:: this example from |acquia-product:blt|'s issue queue
.. _this_example_from_blts_issue_queue: https://github.com/acquia/blt/issues/1667

Importing a configuration directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To import configuration values into an |acquia-product:edg| website, modify the following script to point to the
cleardirectory (or directories) where your configuration values are stored:

.. code-block:: php

   <?php
   /**
   *  Set vcs and sync dirs to writable directories above docroot.
   */
   $config_directories['vcs'] = '../config/default';
   $config_directories['sync'] = '../config/default';

Customize Fast 404 extensions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, Drupal 8 core does not include ``.swf`` files in Fast 404 settings. If your websites use files with these
extensions, adding the ``.swf`` extension into the list of extensions handled by Fast 404 ensures that any missing files
with that extension will not cause a performance hit. To do this, use code similar to the following:

.. code-block:: php

   <?php
   /**
   * Taken from https://docs.acquia.com/site-factory/tiers/paas/workflow/hooks
   * Fast 404 paths: see comments in sites/g/settings.php for other settings.
   * Drupal 8 Core does not include .swf files, so we add those here.
   */
   $config['system.performance']['fast_404']['paths'] = '/\.(?:txt|png|gif|jpe?
   g|css|js|ico|swf|flv|cgi|bat|pl|dll|exe|asp|swf)$/i';

Drush compatibility with Sumologic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are forwarding your website's logs to Sumologic, this script alters the output from Drush requests in Drupal 7 or
Drupal 8 to match Sumologic's expected logging format:

.. code-block:: php

   <?php
   /**
   *
   * Add logging information for drush requests in drupal-requests.log on Acquia.
   * By default these requests show up with no REQUEST_METHOD or URI, which can
   * make splitting them up in Sumologic very hard.
   * Taken from https://gist.github.com/seanhamlin/47d49c59ca50c91c0aec3db5b4ae082d
   */
   if (isset($_ENV['AH_SITE_ENVIRONMENT']) && PHP_SAPI === 'cli' && function_exists('drush_main')) {
     // We are in a drush bootstrap, modify $_SERVER variables needed for
     // drupal-request.log.
     $_SERVER['REQUEST_METHOD'] = 'CLI';
     $drush_args = drush_get_arguments();
     $_SERVER['REQUEST_URI'] = 'drush ' . array_shift($drush_args);
   }

Drupal 7 cache lifetime per website
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To conditionally set the cache lifetime of each website in your |acquia-product:edg| cluster to individual values,
while not allowing a value of fewer than 5 minutes, see `this gist on GitHub`_

.. _this gist on Github: https://gist.github.com/seanhamlin/b4152e3ab88f47d39dcf0fb6f397b796

New Relic monitoring
^^^^^^^^^^^^^^^^^^^^

To enable New Relic monitoring in a multisite environment, like |acquia-product:edg|, create a ``post-
settings.php`` script named ``new_relic.php`` that contains the following code, replacing ``CURRENT_APP_NAME``
with the name of your application:

.. code-block:: php

   <?php
   if (extension_loaded('newrelic')) {
      $domain_fragments = explode('.', $_SERVER['HTTP_HOST']);
      $site_name = array_shift($domain_fragments);
      newrelic_set_appname("$site_name;CURRENT_APP_NAME", '', 'true');
   }

Storing credentials outside of version control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you need to store sensitive credentials outside of your codebase, you can create a ``secrets.settings.php`` file and then
make its contents available to Drupal with a ``post-settings.php`` hook (as described in `Storing sensitive information outside
of your codebase </resource/secrets>`__). By doing so, sensitive credentials will not be present in your database backups or your version control
repository, allowing you to distribute database backups or grant repository access to team members who should not possess
sensitive credentials.
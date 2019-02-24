.. include:: /common/global.rst

Increasing caching in |acquia-product:edg|
==========================================

By default, |acquia-product:edg| sets the maximum age for items included
in the Varnish page cache (``page_cache_maximum_age``) to 3600 seconds
(60 minutes). It is possible to customize this value based on your
website's needs:

-  `Increasing all cache lifetimes on all websites <#increasing-all-cache-lifetimes-on-all-websites>`__
-  `Per-environment cache lifetime increases <#per-environment-cache-lifetime-increases>`__
-  `Increasing cache lifetimes with Drush (Drupal 7 only) <#increasing-cache-lifetimes-with-drush-in-drupal-7>`__

Increasing all cache lifetimes on all websites
----------------------------------------------

To increase the cache lifetime value from the default for all websites
in your Factory, create a ``post-settings-php`` hook as described in
`Hooks triggered after website actions </site-factory/extend/hooks#actions>`__, 
setting a new value (in seconds) for ``page_cache_maximum_age``:

.. code-block:: none

   // For Drupal 7, uncomment this line to set a new cache lifetime:
   // $conf['page_cache_maximum_age'] = 21600;
   // For Drupal 8, uncomment this line to set a new cache lifetime:
   // $config['page_cache_maximum_age'] = 21600;

Items in the page cache will now persist for 6 hours (21,600 seconds).


Per-environment cache lifetime increases
----------------------------------------

To increase the cache lifetime value from the default for all websites
in your Factory, create a ``post-settings-php`` hook as described in
`Hooks triggered after website actions </site-factory/extend/hooks#actions>`__, 
altering the code to match your website's installed version of Drupal:

.. code-block:: php

    // Verify we're on an Acquia-hosted environment.
    if (file_exists('/var/www/site-php')) {
      if (isset($_ENV['AH_SITE_ENVIRONMENT'])) {
      
        // Alter '01dev,' '01test', and '01live' to match your website's environment names.
        // Alter the variable names to match your version of Drupal:
        //   Drupal 8 uses $config['page_cache_maximum_age']
        //   Drupal 7 uses $conf['page_cache_maximum_age']
        
        switch ($_ENV['AH_SITE_ENVIRONMENT']) {
          case '01dev': 
            // Cache settings.
            $config['page_cache_maximum_age'] = 0;
            break;
            case '01test':
            // Cache settings.
            $config['page_cache_maximum_age'] = 3600;
            break;
            case '01live':
            // Cache settings.
            $config['page_cache_maximum_age'] = 21600;
            break;
        }
      }
    }

Items in the page cache on the testing environment will now persist for
60 minutes (3,600 seconds), and items in the production environment will
persist for 6 hours (21,600 seconds). Items in the development
environment will not be cached.

Increasing cache lifetimes with Drush in Drupal 7
-------------------------------------------------

You can also use Drush to update your website's settings in Drupal 7.
First, create a ``post-settings-php`` hook as described in 
`Hooks triggered after website actions </site-factory/extend/hooks>`__:

.. code-block:: php

    <?php
    /**
    * @file
    *
    * This post-settings-php hook is created to conditionally set the cache
    * lifetime of Drupal to be a value that is greater than 300 (5 minutes).
    * It also does not let you set it to be lower than 5 minutes.
    *
    * This does not fire on Drush requests, as it interferes with site creation.
    * It also means that drush will report back incorrect values for the 
    * cache lifetime, so using a real browser is the easiest way to validate
    * what the current settings are.
    *
    * How to enable this for a site:
    *  - drush vset acsf_allow_override_page_cache 1
    *  - drush vset page_cache_maximum_age 3600
    */
    if (!drupal_is_cli()) {
      $result = db_query("SELECT value FROM {variable} WHERE name = 'acsf_allow_override_page_cache';")->fetchField();
      if ($result) {
        $acsf_allow_override_page_cache = unserialize($result);
        if ($acsf_allow_override_page_cache) {
          $result = db_query("SELECT value FROM {variable} WHERE name = 'page_cache_maximum_age';")->fetchField();
          // An empty array indicates no value was set in the database, so we ignore
          // the site.
          if ($result) {
            $page_cache_maximum_age = (int) unserialize($result);
            if ($page_cache_maximum_age > 300) {
              $conf['page_cache_maximum_age'] = $page_cache_maximum_age;
            }
          }
        }
      }
    }

After creating and uploading the ``post-settings-php`` hook, use one of
the following methods to implement the change:


.. |Update locally using Drush aliases| replace:: *Update locally using Drush aliases*
.. _Update locally using Drush aliases: /acquia-cloud/drush/aliases

-  | |Update locally using Drush aliases|_ |br|
   | From your local command line, run the following Drush commands,
     substituting in your website's details for the text in brackets:

   .. code-block:: none

      drush @[sitename].[env] --uri=[site.host.com] vset acsf_allow_override_page_cache 1
      drush @[sitename].[env] --uri=[site.host.com] vset page_cache_maximum_age 21600

   where:

   -  ``[sitename]`` - Your website's name
   -  ``[env]`` - Your website's environment (such as ``prod`` or
      ``01live``)
   -  ``[site.host.com]`` - Your website's URL

-  | *Update directly on your website's server* |br|
   | From the command line, `SSH into your
     environment </acquia-cloud/ssh>`__, and then run the following
     Drush commands, where ``[site.host.com]`` is your website's URL:

   .. code-block:: none

      drush --uri=[site.host.com] vset acsf_allow_override_page_cache 1
      drush --uri=[site.host.com] vset page_cache_maximum_age 21600

Items in the page cache will now persist for 6 hours (21,600 seconds).

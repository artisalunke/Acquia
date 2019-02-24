.. include:: /common/global.rst

Remote Administration environment
=================================

Acquia provides Remote Administration (RA) clients with an additional RA environment at no additional cost. This environment facilitates the deployment and testing of security updates without disrupting ongoing development in other environments. Updates are deployed based on your `RA preferences </ra/preferences>`__.

For |acquia-product:ace| clients, the RA environment is hosted on RA-specific shared Acquia servers and will have no impact on development, staging, or production servers. RA environments for |acquia-product:acs| customers are configured such that they will consume no critical system resources while the website sits idle, and all critical resources remain available to the production website.

.. note::

  The RA environment is not an additional development environment, as it may be overwritten at any time. If you require additional development environments for your website, either `contact Acquia Support </support#contact>`__ or contact your account manager to make the request.

Security update testing
-----------------------

Client testing of the initial step (see `Security updates </ra/security>`__) takes place on the RA environment. Clients and Acquia Support can push code to the deployed branch for testing. Testing should take into account that the RA environment may not be configured with the same specs as your Development, Stage or Production environments. This environment will be regularly overwritten by new security updates, and should not be used for any ongoing development, testing, or content creation. It is not possible to deploy code to this environment using the workflow interface.

.. important::

  After a security update has been tagged and is ready for deployment, the data and code will be removed from the RA environment until the next security release. Any code or data deployed to this environment is periodically removed. Data is not backed up before removal. As a result, this environment should never be used for testing anything other than automated RA updates. Acquia does not guarantee the preservation of any data or code deployed to this environment.

Databases
~~~~~~~~~

Databases copied to the RA environment will only remain as long as a Security Update branch is deployed and undergoing testing.

You can scrub your databases to prevent sensitive data from being copied into the RA environment. For more information about creating scrub scripts to clean any sensitive data, see the `Scrubbing a Drupal database environment <%5Bacquia-product:kb%5Darticles/scrubbing-drupal-database-environment>`__ article on the Acquia |acquia-product:lib|.

.. _database_automated:

Automated database changes
^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to ensure compatibility and testability in the RA Environment, certain changes are made to the copied database using drush. Database level changes on the RA Environment, such as creating new content or disabling modules, have no effect on the code or data deployed to any other environment. The update workflow never copies an RA environment into either the testing or production environments.

If the updated website uses modules dependent upon modules modified by automation, full testing of such functionality will need to take place on another environment. In such cases, the branch can be either deployed to another environment upon request, or such functionality can be tested once the branch has been tagged (step two).

-  `Secure Pages <https://www.drupal.org/project/securepages>`__ and
   `Secure login <https://www.drupal.org/project/securelogin>`__ |--| These modules are most often coded to point to the Production website, so leaving them enabled often confuses testing. As a result, these modules are disabled using drush when an update branch is deployed to RA. Modules dependent on Secure Pages and Secure Login should be tested on another environment.
-  Stage File Proxy - This module is added and enabled. See the following information for details.

.. _database_sub:

Subscription-specific database changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In situations where specific module functionality should be restricted or disabled on the RA Environment, Acquia recommends taking advantage of `environment-level variables </acquia-cloud/develop/env-variable>`__ in the ``settings.php`` file that can control functionality for each environment. It is possible to set either an environment-specific functionality using the ``AH_SITE_ENVIRONMENT`` variable or a to restrict changes to the non-production environment functionality by using ``AH_NON_PRODUCTION``'. These variables can be used to redirect secure pages for each environment, or set Acquia Search to `read-only <%5Bacquia-product:kb%5Darticles/read-only-apache-solr-search-index>`__ on the RA Environment, and so on.

Given the unique needs of each website, these variables should be set by the client. If needed, Acquia Support can offer suggestions and examples.

.. important::

  You can use `the environment examples </acquia-cloud/develop/env-variable#examples>`__ to set up your variables. Systems with an RA environment *must* include that environment in their declaration of variables or ``drush pm-update`` will fail and your website will not be updated.

Installations using the `Devinci <https://www.drupal.org/project/devinci>`__ module must configure that module to include an RA environment, or drush updates will fail.

Deploy hooks
~~~~~~~~~~~~

Hooks that are in the `common directory </acquia-cloud/api/cloud-hooks>`__ (usually ``hooks``) will run on all environments, including RA. Due to differences between the RA environment and the other environments, these hook scripts occasionally result in unexpected behaviors or task failures, which can cause the RA automated update process to fail.

If you have scripts in the common directory, they can be modified slightly to prevent them from running on the RA environment. The following example includes an ``if`` statement to include in the scripts that will allow them to run normally on all environments except for RA:

.. code-block:: none

  #!/bin/sh
  #
  #Standard hook variables here
  #
  site="$1"
  target_env="$2"

  if [ "$target_env" != "ra" ]; then
       drush @$site.$target_env updatedb --yes
  fi

Alternately, move any hooks located in the common directory to the development, stage and/or production directories instead.

Files and the Stage File Proxy module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Production files are not copied into the RA environment. Instead, the `Stage File Proxy <https://drupal.org/project/stage_file_proxy>`__ module is implemented. The module is added to the repository and enabled on the RA environment only. It has no effect on production environments. This module sends file requests to the production environment and copies the production file in the RA environment. This saves both time and space. Files uploaded by other means, or theme images or CSS using the Drupal file structure rather than a theme folder, will not appear in the RA environment.

.. note::

  Files uploaded directly to the RA environment will not work correctly.

Stage File Proxy is incompatible with the following modules:

-  `FileField Sources <https://www.drupal.org/project/filefield_sources>`__
-  `Fast 404 <https://www.drupal.org/project/fast_404>`__ |--| Adding the following to your website's ``settings.php`` file will ensure that Fast 404 does not interfere with the functionality of Stage File Proxy:

   .. code-block:: php
   
      if (!isset($_ENV['AH_SITE_ENVIRONMENT']) || $_ENV['AH_SITE_ENVIRONMENT'] != "ra") fast_404_ext_check();

Stage File Proxy does not support subfolders within your Drupal user files directory. Any images or other files within subfolders will not be displayed correctly in the RA environment.

If you are running these modules, you should deploy the Security Update to a different testing environment as soon as it is available.

Memcache disabled
~~~~~~~~~~~~~~~~~

Memcache is not enabled in the RA environment. It may be enabled in your other environments, but should result in little to no impact to your website(s) when testing in the RA environment. The `recommended memcache include statement </acquia-cloud/performance/memcached#enable>`__ should already be present in your ``settings.php`` file. Select the configuration appropriate for your version of Drupal:

.. note::

  Do not modify the ``memcache_key_prefix`` or ``memcache_servers`` settings in ``settings.php``. |acquia-product:ac| adds the correct values for these directives in Acquia-specific code called by ``settings.php``. When these values are set manually, unexpected behavior can result.

-  *Configuration for Drupal 8* |br| 

   .. code-block:: none

      if (isset($settings['memcache']['servers'])) { 
        // Memcache settings.
        $settings['cache']['default'] = 'cache.backend.memcache';
      }

-  *Configuration for Drupal 7* |br| 
   The first two of these settings cause Drupal to use Memcached instead of MySQL for data that is normally stored in database caches. The third setting (``cache_class_cache_form``) ensures that the ``cache_form`` table is assigned to non-volatile storage.

   .. code-block:: none

      if (isset($conf['memcache_servers'])) {
        $conf['cache_backends'][] = './sites/all/modules/memcache/memcache.inc';
        $conf['cache_default_class'] = 'MemCacheDrupal';
        $conf['cache_class_cache_form'] = 'DrupalDatabaseCache';
      }

Be sure to validate that the ``cache_backends`` path is the actual path to the Memcache module in your application's ``docroot``.

If you are using a different include statement related to memcache in any of your ``settings.php`` files, Acquia strongly recommends replacing it with the previous statement and deploying to your production environment. Once the change is deployed to production, websites deployed to the RA environment during `step one of the update process </ra/security-update-process#one>`__ will no longer be dependent on memcache while running on that environment.

Domains
~~~~~~~

The RA environment is provisioned with a single |acquia-product:ac| subdomain similar to your Development, Stage and Production environments. Additional domains can be added to the RA environment from the |acquia-product:ac| Domains page. Instructions for adding domains are available at `Managing your domains </acquia-cloud/manage/domains>`__.

Your DNS provider must point your domain names to the IP address of the RA environment to ensure requests for that domain name are directed to the correct location on the RA servers. You can `add the domain names to your local hosts file <%5Bacquia-product:kb%5Darticles/using-etchosts-file-custom-domains-during-development>`__ in order to test locally.

Authentication issues
---------------------

Customers using a Single Sign-On (SSO) solution for Drupal user authentication may encounter issues when signing in to websites on their RA environment that have not been configured with the SSO. Websites using `LDAP </acquia-cloud/develop/ldap>`__, SAML, or SimpleSAML solutions can also encounter the same issue.

If your testing in the RA environment is hindered by authentication issues, deploy the update branch to the preferred Testing environment as set in the `RA preferences </ra/preferences>`__. When creating your update ticket, be sure to request the deployment of update code to an environment other than RA. The RA team will deploy the update branch to your preferred environment and will notify you when you can continue testing.

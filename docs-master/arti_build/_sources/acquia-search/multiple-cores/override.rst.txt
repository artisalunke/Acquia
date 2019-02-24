.. include:: /common/global.rst

Overriding Solr core automatic connection switching
===================================================

.. container:: internal-navigation

      **Multiple Acquia Search cores**

      * :doc:`Use </acquia-search/multiple-cores>`
      * Override
      * :doc:`Share </acquia-search/multiple-cores/sharing>`
      * :doc:`Troubleshoot </acquia-search/multiple-cores/troubleshoot>`

In some cases, you may want to override the auto-switching behavior.
Example override scenarios include the following:

-  You are implementing a single search page that returns results from
   across many Drupal websites. For this you would need to have all
   websites read/write to a single Solr core (by also using a module,
   such as the `Apache Solr Multisite
   Search <https://www.drupal.org/project/apachesolr_multisitesearch>`__
   module), which also powers your search pages.
-  Your subscription level is not entitled to multiple
   |acquia-product:as| Solr cores, and you need to write into your
   single, available core from several environments.
-  You need read/write access from a local- or non-Acquia-hosted
   website.

.. important::

      Sharing a single Solr core across websites has risks. For more
      information, see `Sharing Solr cores in read/write
      mode </acquia-search/multiple-cores/sharing>`__.

To stop |acquia-product:as| from enabling auto-switching, use one of the
following methods:

-  `Using the Acquia Search Multiple Indexes
   module <#multiple-indexes-module>`__ (Drupal 7 only)
-  `Using code overrides to set the Solr
   connection <#code-override>`__ for |acquia-product:as| 
-  `Disabling auto-switching <#disable>`__

.. _multiple-indexes-module:

Using the Acquia Search Multiple Indexes module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Drupal 7-based websites, the easiest method to prevent
auto-switching is to use the `Acquia Search Multiple
Indexes <https://www.drupal.org/project/acquia_search_multi_subs>`__
module, which enables you to manually configure a different Solr core
connection for each |acquia-product:ac| environment. To use this module,
complete the following steps:

#. Download, install, and enable the `Acquia Search Multiple
   Indexes <https://www.drupal.org/project/acquia_search_multi_subs>`__
   module.
#. Navigate to the configuration page for this module in your Drupal
   website's administration pages.

   -  `Search API <https://www.drupal.org/project/search_api>`__
      module - Go to **Configuration > Search API settings**, and then
      for the |acquia-product:as| server you have configured, click
      **Edit**.
   -  `Apache Solr Search
      Integration <https://www.drupal.org/project/apachesolr>`__ module
      - Go to **Configuration > Apache Solr Search > Settings > Edit**.

#. Select the **Automatically switch when an |acquia-product:ac|
   environment is detected** check box.
#. Click **Save**.

.. _code-override:

Using code overrides to set the |acquia-product:as| Solr connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Customers can choose to manually configure the connections in the
``settings.php`` file by overriding variables. For non-hosted customers,
setting these variables is the only way to use multiple
|acquia-product:as| Solr cores.

.. admonition:: Code override requirements

      `Contact Acquia Support </support#contact>`__ to obtain the following
      values, which are required for any of the ``settings.php`` code
      overrides described in this section:

      -  ``[colony]``
      -  ``[core ID]``
      -  ``[derived key]``

The code override that you must use depends on your installed Drupal
version and the module in use. For the appropriate code override, find
your website's configuration from the following list:

-  *Drupal 8* - Search API Solr and |acquia-product:as| modules
    Use the ``acquia_search.settings.connection_override`` configuration
    object to define a connection. To override the variables in your
    ``settings.php`` file, add the following code *after* the Acquia
    include statement:

.. code-block:: php

   // For Drupal 8 using Search API Solr and Acquia Search 
   if (isset($_ENV['AH_SITE_ENVIRONMENT'])) {
      if ($_ENV['AH_SITE_ENVIRONMENT'] == 'prod') {
           $config['acquia_search.settings']['connection_override'] = [
                  'scheme' => 'https',
                  'port' => 443,
                  'host' => '[colony].acquia-search.com',
                  'index_id' => '[core_ID]',
                  'derived_key' => '[derived key]',
                  ];
            }
      elseif ($_ENV['AH_SITE_ENVIRONMENT'] == 'test') {
            $config['acquia_search.settings']['connection_override'] = [
                  'scheme' => 'https',        
                  'port' => 443,       
                  'host' => '[colony].acquia-search.com',       
                  'index_id' => '[core_ID]',       
                  'path' => '/solr/[core_ID]',       
                  'derived_key' => '[derived key]',     
                  ];
            }
      elseif ($_ENV['AH_SITE_ENVIRONMENT'] == 'dev') {
           $config['acquia_search.settings']['connection_override'] = [
                  'scheme' => 'https',        
                  'port' => 443,       
                  'host' => '[colony].acquia-search.com',       
                  'index_id' => '[core_ID]',       
                  'path' => '/solr/[core_ID]',       
                  'derived_key' => '[derived key]',     
                  ];
            } 
      } else {
         // Local or other non-acquia-hosted Drupal environment
            $config['acquia_search.settings']['connection_override'] = [ 
                'scheme' => 'https',      
                'port' => 443,     
                'host' => '[colony].acquia-search.com',     
                'index_id' => '[core_ID]',     
                'path' => '/solr/[core_ID]',     
                'derived_key' => '[derived key]',   
                ];
            }

-  *Drupal 7* - Search API Solr and |acquia-product:as| for Search API modules
    For Search API module, override using the
    ``search_api_acquia_overrides`` variable. To override the variables
    in your ``settings.php`` file, add the following code *after* the
    Acquia include statement (being sure to also replace
    ``'acquia_search'`` in the code with the machine name of the
    search_api server):

.. code-block:: php
   
   // For Drupal 7 using Search API Solr and Acquia Search
    if (isset($_ENV['AH_SITE_ENVIRONMENT'])) {
      if ($_ENV['AH_SITE_ENVIRONMENT'] == 'prod') {
            $conf['search_api_acquia_overrides']['acquia_search'] = array( 
                  'path' => '/solr/[core_ID]',       
                  'host' => '[colony].acquia-search.com',       
                  'derived_key' => '[derived_key]',     
                  );   
            }   
      elseif ($_ENV['AH_SITE_ENVIRONMENT'] == 'test') {
            $conf['search_api_acquia_overrides']['acquia_search'] = array(
                  'path' => '/solr/[core_ID]',       
                  'host' => '[colony].acquia-search.com',       
                  'derived_key' => '[derived_key]',     
                  );   
            }   
      elseif ($_ENV['AH_SITE_ENVIRONMENT'] == 'dev') {
           $conf['search_api_acquia_overrides']['acquia_search'] = array(
                  'path' => '/solr/[core_ID]',       
                  'host' => '[colony].acquia-search.com',       
                  'derived_key' => '[derived_key]',     
                  );   
            }
      } else {
         // Local or other non-acquia-hosted Drupal environment  
            $conf['search_api_acquia_overrides']['acquia_search'] = array(
                 'path' => '/solr/[core_ID]',     
                 'host' => '[colony].acquia-search.com',     
                 'derived_key' => '[derived_key]',   
                 );
            }

-  *Drupal 7* - Apache Solr Search Integration and |acquia-product:as| modules
    When using Apache Solr Search, override the ``apachesolr_environments`` 
    variable. To override the variables in your ``settings.php`` file, 
    add the following code *after* the Acquia include statement:

.. code-block:: php

   // For Drupal 7 using Apache Solr Search Integration and Acquia Search
    if (isset($_ENV['AH_SITE_ENVIRONMENT'])) {
      switch ($_ENV['AH_SITE_ENVIRONMENT']) {
       case 'test':
        $conf['apachesolr_environments']['acquia_search_server_1']['url']
            = 'http://[colony].acquia-search.com:80/solr/[core_ID]';
        $conf['apachesolr_environments']['acquia_search_server_1']['conf']
            ['acquia_search_key'] = '[derived_key]';
        break;
       case 'dev':    
        $conf['apachesolr_environments']['acquia_search_server_1']['url'] = 
            'http://[colony].acquia-search.com:80/solr/[core_ID]';
        $conf['apachesolr_environments']['acquia_search_server_1']['conf']
            ['acquia_search_key'] = '[derived_key]';   
        break;
       } 
      }  
      else {
       // Set index to read-only in local development environments   
        $conf['apachesolr_read_only'] = "1";
      }

.. _disable:

Disabling auto-switching
~~~~~~~~~~~~~~~~~~~~~~~~

You can use the Drupal variables or configuration objects to override
certain |acquia-product:as| module behaviors, described as follows:

.. important::
   These settings can have `data integrity
   implications </acquia-search/multiple-cores/sharing>`__ for your index.

-  *Drupal 8*
   Setting ``acquia_search.settings.disable_auto_switch`` to ``TRUE``
   avoids auto-switching, causing the production Solr core to be used in
   read/write mode. When the variable is not set or is set to ``FALSE``,
   setting ``acquia_search.settings.disable_auto_read_only`` to ``TRUE``
   avoids the automatic read-only behavior — however, switching to the
   right core will still be attempted.
-  *Drupal 7*
   Setting ``acquia_search_disable_auto_switch`` to ``TRUE`` avoids
   auto-switching. If you either do not have the `Acquia Search Multiple
   Indexes <#multiple-indexes-module>`__ module configured, or have
   another `code override <#code-override>`__ set, your website will
   connect to your production core.
   When the variable is not set or is set to ``FALSE``, setting
   ``acquia_search_disable_auto_read_only`` to ``TRUE`` avoids the
   automatic read-only behavior — however, switching to the right core
   will still be attempted.

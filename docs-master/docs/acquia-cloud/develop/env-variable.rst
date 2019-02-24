.. include:: /common/global.rst

Using environment variables in Drupal code and Drush commands
=============================================================

|acquia-product:ac| makes available a set of environment variables that
you can use both in your application code and in
`Drush <https://www.drupal.org/project/drush>`__ commands. These
variables make it easier to write code that is responsive to the
environment the code is running in. For example, you may have code that
should run in your Production environment, but not in the Development or
Staging environments.

.. important::

    Applications on |acquia-product:ac| have a special include statement in
    the ``settings.php`` file that is similar to the following:

    .. code-block:: php

       if (file_exists('/var/www/site-php')) {
          require '/var/www/site-php/sitename/sitename-settings.inc';
         }

    If you use environment variables in ``settings.php``, references to the
    environment variables should be placed *after* the preceding include
    statement, to ensure that they take effect in each of the desired
    contexts.

.. _variables:

Available environment variables
-------------------------------

|acquia-product:ac| includes the following environment variables:

.. list-table::
   :widths: 25 10 40 25
   :header-rows: 1

   * - Variable
     - Format
     - Description
     - Values
   * - ``AH_SITE_GROUP``
     - string
     - Specifies the site name, which is also the Unix user.
     -
   * - ``AH_SITE_ENVIRONMENT``
     - string
     - Indicates an |acquia-product:ac| environment
     - ``dev``, ``test``, ``prod``
   * - ``AH_PRODUCTION``
     - string
     - Indicates whether this is a Production environment. (Not available in 
       |acquia-product:edg|)
     - ``1`` for Production, ``undefined`` for non-Production
   * - ``AH_NON_PRODUCTION``
     - string
     - Indicates whether this is a non-Production environment
     - ``1`` for non-Production, ``undefined`` for Production
   * - ``AH_CURRENT_REGION``
     - string
     - The `Amazon Web Services region 
       <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html>`__
       in which the web server processing the current request is running.
     -
   * - ``AH_REALM``
     - string
     - The |acquia-product:ac| realm in which the application is running. The 
       realm is a required parameter in calls to the Cloud API. The value is 
       ``prod`` for |acquia-product:ace| and ``devcloud`` for 
       |acquia-product:acs|. The realm corresponds to the element before 
       ``hosting.acquia.com`` in the environment’s server names.
     -
   * - ``HTTP_X_REQUEST_ID``
     - string
     - Every web request received by |acquia-product:ac| is assigned a unique 
       request ID, which is set in the HTTP header ``X-Request-ID`` and is 
       available in the ``HTTP_X_REQUEST_ID`` environment variable; for more 
       information, see `Using HTTP request IDs 
       </acquia-cloud/develop/requestid>`__.
     -
   * - ``PATH``
     - string
     - If the environment is configured to use a specific version of PHP, that 
       version of PHP is first in the path (for example, 
       ``/usr/local/php7.1/bin``).
     -
   * - ``TEMP``
     - string
     - The tmp directory at ``/mnt/tmp/[site].[env]`` for the environment. 
       Use this, rather than ``/tmp``, which is smaller and may fill up rapidly.
     -

.. admonition:: |acquia-product:edg| subscriber notes

    Several examples from the preceding table require the following
    modifications to work with |acquia-product:edg|:

    -  The ``AH_SITE_ENVIRONMENT`` variable includes additional values for
       each environment, such as ``01live`` or ``01test``.
    -  Default domain names use ``acsitefactory.com`` instead of
       ``acquia-sites.com``.
    -  The ``AH_PRODUCTION`` variable is not available.

.. _htaccess:

Environment variables in ``.htaccess``
--------------------------------------

You can also use environment variables in your ``.htaccess`` file. In
the following example, we redirect HTTP requests to HTTPS only on the
production environment, and not in the development or staging
environments:

.. code-block:: none

    RewriteCond %{HTTPS} off 
    RewriteCond %{HTTP:X-Forwarded-Proto} !https 
    RewriteCond %{ENV:AH_SITE_ENVIRONMENT} prod 
    // Acquia Cloud Site Factory may require a different value for 
    // %{ENV:AH_SITE_ENVIRONMENT} depending on site configuration 
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

For more information, see `Redirecting visitor requests with the
.htaccess file </acquia-cloud/manage/htaccess#https>`__.

.. _faking:

Faking your environment variables for local testing
---------------------------------------------------

There may be situations where you want to specify a particular
|acquia-product:ac| environment variable during testing. In these
situations, you can *force* the environment variable by making a change
to your local ``settings.php`` file. The following example sets the
``AH_SITE_ENVIRONMENT`` variable to the ``dev`` environment:

``$_ENV['AH_SITE_ENVIRONMENT'] = 'dev';``

This is used in situations such as `overriding Solr core automatic
connection switching </acquia-search/multiple-cores/override>`__.

Examples
--------

For example, the following statement would let you switch code based on
the environment:

.. code-block:: php

    if (isset($_ENV['AH_SITE_ENVIRONMENT'])) {   
       switch ($_ENV['AH_SITE_ENVIRONMENT']) {     
         case 'dev':       
           // do something on dev       
           break;      
         case 'test':       
           // do something on staging       
           break;      
         case 'prod':       
           // do something on prod       
           // |acquia-product:edg| may require a different value depending on 
           // site configuration       
           break;      
         case 'ra':       
           // do something on ra - necessary if a Remote Administration environment is present       
           break;   
         } 
        }  
        else {     
        // do something for a non-Acquia-hosted application (like a local dev install).
    ; }

To make |acquia-product:as| read-only on your Development and Staging
environments, so the search index doesn't have duplicate copies of
content:

.. code-block:: php

    // place this after the Acquia require line 
    if (!isset($_ENV['AH_SITE_ENVIRONMENT'])  ||     
      'prod' != $_ENV['AH_SITE_ENVIRONMENT'])     { 
       $conf['apachesolr_read_only'] = "1"; 
       }

For another example, see `Setting $base_url without breaking the
Development and Staging
environments </acquia-cloud/develop/drupal/baseurl>`__.

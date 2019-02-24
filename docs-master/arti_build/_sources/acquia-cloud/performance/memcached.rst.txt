.. include:: /common/global.rst

Using Memcached
===============

Memcached is a general-purpose memory cache server daemon. It can
improve Drupal application performance by moving Drupal's standard
caches out of the database and by caching the results of other expensive
database operations.

The most common use of Memcached with Drupal is storing Drupal's cache
tables in Memcached instead of in the application database. This reduces
the load on the database with every page load.

Using Memcached may not make any noticeable difference to an application
that is already performing well at every layer in the server stack.
Memcached is most helpful to applications that need to reduce the load
on their database servers.

.. note:: 
  Disambiguation: memcached and memcache

  *Memcached* is the name of the server-side daemon; *memcache* is the
  name of the PHP extension that adds the libraries that create the PHP
  functions for communication with the daemon; there is also a PHP library
  called *memcached*, which facilitates communication with the daemon.
  |acquia-product:ac| runs the ``memcache`` libraries. In addition, the
  `PHP memcache project <https://www.drupal.org/project/memcache>`__ at
  Drupal.org uses the ``memcache`` libraries. For more information about
  how to communicate with the Memcached daemon using PHP, see the
  `Memcache reference <http://us2.php.net/manual/en/book.memcache.php>`__
  at php.net.

.. _acquia:

Memcached availability
----------------------

|acquia-product:ac| supports Memcached for subscriptions and products
based on the following table:

.. list-table::

  * - Product name  
    - Description
  * - `Acquia Cloud Professional </acquia-cloud/arch/compare-ace-acp>`__
    - You can `enable <#enable>`__ and manage Memcached for your applications.
  * - `Acquia Cloud Enterprise </acquia-cloud/arch/compare-ace-acp>`__
    - Acquia will configure your servers with an appropriate amount of memory 
      for Memcached. As an option, can purchase a dedicated Memcached server.
  * - `Acquia Cloud Site Factory </site-factory>`__
    - To use Memcached with your websites, contact your Technical Account 
      manager (TAM) or Account Manager to evaluate your hardware before 
      implementing a `post-settings.php hook </site-factory/extend/hooks/settings-php#memcache>`__.
  * - `Acquia Cloud Free </acquia-cloud/free>`__
    - Memcached is not supported. Learn more about |acquia-product:acfs| and
      `how to upgrade your subscription. </acquia-cloud/free>`__.
  * - `Acquia Cloud CD </acquia-cloud/cd>`__
    - |acquia-product:ccd| environments that meet certain `requirements <#ccd>`__
      can use Memcached.

.. _enable:

Enabling Memcached on |acquia-product:ac|
-----------------------------------------

To enable Memcached, complete the following steps:

#. To allocate memory to Memcached on |acquia-product:acs| and enable it
   to run, use the following procedure:

   .. note:: 
     Because |acquia-product:ace| configures your servers with an
     appropriate amount of memory for Memcached, you can skip this step.

#. Sign in to the |cloud-ui| and select your application and then the environment.
#. In the left menu, click **Servers**.
#. In the card for the web server, click **Configure**.

   |Configure Memcached memory allocation for a server|

#. Under **Memcached memory (MB)**, enter the amount of memory to allocate to 
   Memcached. A value of 64MB is sufficient for Drupal applications running on 
   |acquia-product:ac|.
#. Click **Save**.

#. You can `use PHP 5.6 or PHP 7 </acquia-cloud/manage/php>`__.
   To use memcached 2.2.0 with PHP 5.6, add the following code to your
   ``settings.php`` file:
     
   .. code-block:: php

      # Drupal 7 $conf['memcache_extension'] = 'Memcached';
      # Drupal 8 $settings['memcache']['extension'] = 'Memcached';``

   .. note::
      Memcached is not available for use with |acquia-product:acfs|.

#. Download, install, and enable the `Memcache API and
   Integration <https://www.drupal.org/project/memcache>`__ module on
   your |acquia-product:ac| application. When enabled, you can receive
   notifications when you need to update the module, as well as `view
   your application's Memcached statistics <#stats>`__. Keep the module
   up to date with the latest stable release.

   .. note::
      Drupal 8 requires that you enable the Memcache API and Integration
      module before the next step, or you will receive a
      ``ServiceNotFoundException:`` error.

#. Add the following configuration code to your ``settings.php`` file
   immediately after the Acquia database require statement, depending on
   your installed version of Drupal:

   .. note::

    Do not modify the ``memcache_key_prefix`` or ``memcache_servers``
    settings in ``settings.php``. |acquia-product:ac| adds the correct
    values for these directives in Acquia-specific code called by
    settings.php. When these values are set manually, unexpected behavior
    can result.

   -  *Configuration for Drupal 8*

      .. code-block:: php

        if (isset($settings['memcache']['servers'])) {
          // Memcache settings   
          $settings['cache']['bins']['bootstrap'] = 'cache.backend.memcache';   
          $settings['cache']['bins']['discovery'] = 'cache.backend.memcache';   
          $settings['cache']['bins']['config'] = 'cache.backend.memcache';    
          // Use memcache as the default bin   
          $settings['cache']['default'] = 'cache.backend.memcache'; 
        }

   -  *Configuration for Drupal 7*

      The first two of these settings cause Drupal to use Memcached
      instead of MySQL for data that's normally stored in database
      caches. The third setting makes sure that the ``cache_form``
      table is assigned to non-volatile storage.

      .. code-block:: php

        if (isset($conf['memcache_servers'])) {
         $conf['cache_backends'][] = './sites/all/modules/memcache/memcache.inc';
         $conf['cache_default_class'] = 'MemCacheDrupal';
         $conf['cache_class_cache_form'] = 'DrupalDatabaseCache';
          }

   Be sure the ``cache_backends`` path is the actual path to the
   Memcache module in your application's ``docroot``.

After you publish the ``settings.php`` file, Memcached is enabled.

.. _ccd:

|acquia-product:ccd| prerequisites for using Memcached
------------------------------------------------------

|acquia-product:ccd| customers can use Memcached, which is implemented
on a per-website basis and is secured using SASL credentials. If you
need Memcached support for your CD environment, the environment must
meet the following prerequisites:

-  The environment uses the PECL memcached extension.
-  The environment must include the `Memcache API and
   Integration <https://www.drupal.org/project/memcache>`__ module. If
   you are using Drupal 7, be sure to use version
   `7.x-1.6 <https://www.drupal.org/project/memcache/releases/7.x-1.6>`__
   or greater.

Once these requirements are met, CD applications can use the 64MB of
allocated memcache.

.. _stampede:

Enabling stampede protection and moving locks into memory
---------------------------------------------------------

The Memcache module can provide stampede protection for better
performance. This helps minimize the performance hit that can otherwise
occur if multiple requests simultaneously try to add the same item to
the cache. Stampede protection uses Drupal's locking layer, so that only
one process at a time can attempt to add an item to Memcache. However,
MySQL's InnoDB storage engine is not well-suited to managing locks in
the semaphore table under high loads, and therefore it is very important
that if you enable stampede protection, you also move lock management
out of the database and into memory.

Acquia strongly recommends that you review the Memcache module's
``README.txt`` file for complete documentation regarding its
configuration:

-  `README.txt -
   7.x <http://cgit.drupalcode.org/memcache/tree/README.txt?id=05c5f375eb908731066355e70bc96b70afcbd944>`__
-  `README.txt -
   8.x-2.x <http://cgit.drupalcode.org/memcache/tree/README.txt?h=8.x-2.x>`__

.. important::

  Enabling stampede protection without also moving locks into Memcache can
  cause severe performance degradation if Memcache locks and requires
  waiting for a retry. You can use Memcache for lock management without
  enabling stampede protection.

To implement both stampede protection and Memcache lock management in
Drupal, add the following code as specified:

-  *Drupal 8*
    - Add the following code to the ``settings.php``\ file:

    ``$settings['memcache']['stampede_protection'] = TRUE;``

   - Add the following code to the\ ``services.yml`` file to move lock
     management to Memcache:

.. code-block:: yml

  # Add in stampede protection services:
    lock:
     class: Drupal\Core\Lock\LockBackendInterface
     factory: ['@memcache.lock.factory', get]
    lock.persistent:     
     class: Drupal\Core\Lock\LockBackendInterface
     factory: ['@memcache.lock.factory', getPersistent]

- *Drupal 7* 
    - Add the following code to your ``settings.php`` file:

.. code-block:: php

  # Add in stampede protection 
  $conf['memcache_stampede_protection'] = TRUE;
  # Exclude some bins from stampede protection.
  # NOTE: This is an example. Please see module README.txt, as tweaking may be required!  
  # Proceed with caution. See https://www.drupal.org/node/2419757 
  $conf['memcache_stampede_protection_ignore'] = array(
    // Disable stampede protection for the some bins
        'cache_path',
        'cache_rules',
        'cache_views',
        );
  $conf['memcache_stampede_protection_ignore'] = array(
      // Ignore some cids in 'cache_bootstrap'.
        'cache_bootstrap' => array(
        'module_implements',
        'variables', 
          )
        );
    # Move semaphore out of the database and into memory for performance purposes $conf['lock_inc'] = './sites/all/modules/memcache/memcache-lock.inc';``

For more information, see `this discussion on
Drupal.org <https://www.drupal.org/node/1898204>`__.

.. _stats:

Tuning your Memcached settings
------------------------------

The Memcache Admin Drupal module, which is included in the `Memcache API
and Integration project <https://www.drupal.org/project/memcache>`__,
provides statistics about how Memcached is behaving on your application.
By analyzing these statistics, you can decide whether you may need to
allocate more memory to Memcached on your server.

To use the Memcache Admin module:

#. Enable the Memcache Admin module in the Memcache API and Integration
   project. There is no need to enable the Memcache module. However, if
   you do enable it, you can receive notifications when you need to
   update the module.
#. View the Memcache statistics on your Drupal application's
   **Administration > Reports > Memcache statistics** page.

Check the Memcache statistics page to see how the cache is behaving.
This page reports the following:

-  Amount of memory the Memcached daemon is using
-  Percentage of memcached memory used compared to the total memory
   allocated to it
-  Number of evictions since the last time the service was started or
   stats reset

   Compare the ratio of evictions to total memcache activity. If
   evictions are a high proportion of total memcache activity, consider
   whether you should `allocate more memory to Memcached <#memory>`__.
   Bear in mind, however, that if you allocate more memory to Memcached
   on your server, you'll have less memory for other server functions,
   including PHP. Proper memory allocation depends on your application
   configuration.

For more information, see `Memcache monitoring and flush using the nc
command <https://support.acquia.com/articles/memcache-monitoring-and-flush-using-nc-command>`__.

By default, with stampede protection enabled, when a thread encounters a
locked cache entry, it waits five seconds, and then tries to access the
cache entry again. The Drupal Memcache module includes a
``memcache_stampede_wait_time`` variable that you can use to modify the
time a thread waits before trying again, and a
``memcache_stampede_wait_limit`` variable to control how many tries are
made by a thread. You can also use configuration variables to disable
stampede protection for specific cache bins or patterns of cache IDs.
For more information, see the `ignore settings in the
module <http://cgit.drupalcode.org/memcache/tree/memcache.inc#n492>`__.
If your application is experiencing many threads in a lock wait state,
you may be able to improve performance by adjusting these settings.

.. _related:

Related topics
--------------

-  `Improving application performance </acquia-cloud/performance>`__
-  `Managing Acquia Cloud servers </acquia-cloud/manage/servers>`__

.. |Configure Memcached memory allocation for a server| image:: https://cdn2.webdamdb.com/1280_Aos2hFhPVwK0.png?1526475630
   :width: 750px
   :height: 352px

.. |cloud-ui| replace:: \ |acquia-product:ui|\
.. _cloud-ui: https://cloud.acquia.com

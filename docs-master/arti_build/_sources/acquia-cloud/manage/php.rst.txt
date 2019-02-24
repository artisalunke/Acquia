.. include:: /common/global.rst

Configuring PHP settings
========================

You can configure the PHP settings for each of your |acquia-product:ac|
environments.

To change an environment's PHP settings, complete the following steps:

#. `Sign in <https://cloud.acquia.com>`__ to the |acquia-product:ui|,
   and then select the application that you want to configure.
#. Click the name of the environment that you want to configure, and
   then click **Configure**.

   |Configure an environment|

#. Use the **PHP** section to configure PHP for your application's
   needs. Click one of the following available PHP settings for
   information about the item, including configuration options.

   -  :ref:`php-version`
   -  :ref:`max-exec`
   -  :ref:`php-mem`
   -  :ref:`opcode`
   -  :ref:`interned`
   -  :ref:`apcu`
   -  :ref:`max-input`
   -  :ref:`max-post`

   .. admonition:: |acquia-product:ace| and |acquia-product:acfs|

      |acquia-product:ace|
       The maximum input variables and maximum size of POST request are managed 
       for you by Acquia, and are not available in the user interface. If you 
       believe your application needs to have any of these values changed, 
       `contact Acquia Support </support#contact>`__.

      |acquia-product:acfs|
       Your application runs on a shared server, and you cannot configure your 
       PHP settings. To modify your PHP settings, upgrade your 
       |acquia-product:acfs| subscription to a paid |acquia-product:acs| 
       subscription.

#. Click **Save**.

.. _php-version:

Configuring the PHP version
---------------------------

Your Drupal application runs on the PHP programming language. You can
configure the version of PHP used by your application for each
environment.

.. _use:

Which PHP version to use
~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:ac| offers the following versions of PHP for your
applications' use:

-  **Acquia PHP 7.2** - The latest version of PHP 7.2, custom built for
   |acquia-product:ac|. Requires Drupal 8.5 or greater.
-  **Acquia PHP 7.1** (recommended) - The latest version of PHP 7.1,
   custom built for |acquia-product:ac|.
-  **Acquia PHP 5.6** - The latest version of PHP 5.6, custom built for
   |acquia-product:ac|.

.. note::  

   If you select PHP 5.6 for use, you cannot install Drupal 7 versions
   before Drupal 7.33.

As a general principle, use the latest available version of PHP. Each
new version of PHP includes both enhancements and bug fixes that can
improve the performance and security of your Drupal application.
However, you may be using custom or contributed Drupal modules that
depend on an earlier version of PHP. Although this is not common,
whenever you change your PHP version, you should always do so first on
your Development or Stage environment — not on your Production
environment — and test it to ensure that there are no compatibility
issues.

.. _diff:

Working with different PHP versions on different environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most PHP code should work fine on either PHP 5.6 or PHP 7. Some of your
code may work on one version of PHP, but not with another version. If
you plan on switching to a different version of PHP, do so first on your
Dev or Stage environment and test it thoroughly before changing your
production environment.

.. _advanced:

Advanced PHP settings
---------------------

The following settings are for advanced users. For most applications,
you should leave them at their default settings. Change them only if you
are advised to do so by Acquia Support, or if you are confident that you
know what you are doing. If you have |acquia-product:acfs|, your
application runs on a shared server, and you cannot configure your PHP
settings. You can upgrade your |acquia-product:acfs| subscription to a
paid |acquia-product:ac| subscription.

Configuring any of the following values involves either using a
setting's slider to modify the value in its field, or by directly
entering values in the field. To return any of the following settings to
their original value, click the **Reset** link by the value, and then
click **Save**.

.. note::  

   If you believe your application is experiencing PHP errors, see `PHP
   Error logs </acquia-cloud/monitor/logs/php-error>`__. To correct PHP
   memory issues, see `Finding/Resolving Memory Related PHP errors in
   Acquia
   Cloud <%5Bacquia-product:kb%5Darticle/findingresolving-memory-related-php-errors-acquia-cloud>`__

.. _max-exec:

Configuring max execution time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By modifying the **Max execution time** field, you can configure the
maximum amount of time any PHP process can take. If a PHP process does
not complete in this amount of time, it fails and sends an error. This
time limit helps to prevent PHP processes from becoming stuck and
unavailable to serve new requests.

The default setting for PHP maximum execution time (300 seconds, or 5
minutes) is adequate for most Drupal applications on
|acquia-product:ac|, and you should change it only when necessary.

The danger of allowing longer PHP maximum execution times is that
individual page loads can occupy process slots for long periods of time,
blocking other processes from using them.

.. _php-mem:

Configuring PHP memory limit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **PHP memory** limit is the maximum amount of RAM memory that a
single PHP process can use. The memory used by the MySQL client counts
against the PHP memory limit. The default setting for this value is
128MB per process.

The default setting for PHP memory is adequate for most Drupal
applications on |acquia-product:ac|, and you should only change it when
necessary. Increasing your PHP memory limit beyond 128MB on any one
environment may reduce the number of PHP processes available to handle
requests across all environments on your server. Your Drupal application
can run out of PHP memory. If it does, you'll see an entry in the PHP
error log stating that a process ran out of RAM memory.

If your application stops working and there is an *Out of Memory* error
in the PHP log, increase the PHP memory in small increments until your
application is working again, and then add a safety margin of additional
memory. The maximum setting is 512MB per process. `Contact Acquia
Support </support#contact>`__ if this setting needs to be higher.

If the *Out of Memory* error was caused by a one-time set of conditions
(for example, enabling a large set of modules), reduce the PHP memory
setting after the event. If you leave the PHP memory setting too high,
you won't be able to run more than a few PHP processes on a machine
without running out of RAM.

.. _opcode:

Configuring OPcache size
~~~~~~~~~~~~~~~~~~~~~~~~

Using an OPcache significantly improves PHP performance. Since PHP is an
interpreted programming language, each time a PHP script is called, it
has to be reinterpreted. An opcode cache saves these scripts as machine
code in memory the first time they are run, eliminating the time needed
for reinterpretation on subsequent requests.

Acquia's test results indicate that using an opcode cache generally
offers a three-fold to four-fold increase in performance. To improve
application performance, |acquia-product:ac| implements opcode caching
by default on all applications, using
`OPcache <http://php.net/opcache>`__.

The PHP OPcache is shared among all processes, and its default size is
96MB.

.. note::  

   Memory allocated to the PHP OPcache is not available for processes that
   are handling requests on your server, so there is a cost to making the
   cache size too large.

.. _interned:

OPcache interned strings buffer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Interned Strings buffer is the amount of the PHP OPcache memory that
is reserved for storing strings in OPcache. The amount of memory
allocated to the Interned Strings Buffer will reduce the total amount of
memory available for PHP OPcache.

The default setting is 8MB. If your OPcache is set to 96, this leaves
88MB for normal OPcache usage. If you need to increase the interned
strings buffer over 16MB, Acquia recommends increasing the OPcache by
the same amount.

To set the Interned Strings buffer higher than 32MB, please `contact
Acquia Support </support#contact>`__.

.. _apcu:

APCu size
~~~~~~~~~

This sets the amount of memory allocated to APC User Cache. This is a
smaller cache than PHP OPcache, and most applications will run well with
the default value (32MB). Drupal 8 makes more use of the APCu cache as a
local, short-term cache than previous versions of Drupal did.

To set a size higher than 96MB, please `contact Acquia
Support </support#contact>`__.

.. _max-input:

Maximum input variables (|acquia-product:acs| only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can set the maximum number of input variables that can be accepted.
This limit (the PHP ``max_input_vars`` setting) is applied separately to
``$_GET``, ``$_POST``, and ``$_COOKIE`` inputs. The default value is
1000.

You might want to change this value if your application includes very
large or complex form inputs and you are getting PHP warnings about
input variables exceeding the limit. The default value is 1000. The
highest value you can set in the |acquia-product:ui| is 2500. If your
application requires a higher value (or if you have an
|acquia-product:ace| application), you can file a ticket for Acquia to
set a higher value. However, higher values can lead to security
vulnerabilities, so we recommend that you do not set the value higher
than 5000. As an alternative, you should consider redesigning your
application's forms to be smaller and less complex.

.. _max-post:

Maximum size of POST request (|acquia-product:acs| only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can set the maximum size of a POST that can be accepted (the PHP
``post_max_size`` setting). This value affects the maximum size of file
uploads on your application. Generally, this value should be smaller
than the `PHP memory limit <#php-mem>`__. The default value is 256MB.
Larger sized POSTs are more susceptible to failure.

.. |Configure an environment| image:: https://cdn2.webdamdb.com/1280_sLlRRqa45z02.png?1526475944
   :width: 750px
   :height: 330px

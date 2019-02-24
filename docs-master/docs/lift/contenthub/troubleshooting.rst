.. include:: /common/global.rst

Content Hub troubleshooting guide
=================================

.. toctree::
   :hidden:
   :glob:

   /lift/contenthub/troubleshooting/*

There may be instances when you find that |acquia-product:ch| is not
working as expected. In these cases, you'll need to troubleshoot your
installation.

Content Hub diagnostic module
-----------------------------

The |acquia-product:ch| diagnostic module, when enabled, provides you with
information that ensures your installation has the proper basic
configuration.

The |acquia-product:ch| diagnostic module is included in the normal
installation. After the module is enabled, a new section will appear in
**Reports > Status report**.

|ch-diag.png|

If this report section is green, your |acquia-product:ch| installation
is set up correctly. If there are potential issues with your
installation, this report section will provide the corrections that need
to be made to ensure successful product use, and can include module
updates or patches.

Content Hub history logs
------------------------

|acquia-product:ch| tracks information about the service by using the
``/v1/history`` API endpoint. This information can help you troubleshoot
issues, and you can review the history logs for |acquia-product:ch| with
the |historymethod|_. For more information, see |usingapi|_.

.. |historymethod| replace:: ``/v1/history`` method
.. _historymethod: http://api.content-hub.acquia.com/#v1_history_get

.. |usingapi| replace:: Using the  \ |acquia-product:ch|\  API
.. _usingapi: /content-hub/api

Composer and Drupal 7
---------------------

We do not recommend using Composer to download Drupal 7 modules.
Downloading the tarball for Drupal 7 modules is the recommended method.

Fatal error when installing Composer dependencies with Drush
------------------------------------------------------------

Composer Manager depends on the Composer Drush extension to install the
Composer tool.

Possible cause: Outdated Composer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you run drush composer-manager commands and get errors like these,
your Composer Drush extension may be outdated.

.. code-block:: none

   [RuntimeException] 
   Could not load package...  
   [UnexpectedValueException] 
   Could not parse version constraint...

To resolve this issue, delete the current version of the Composer Drush
extension and reinstall it by running the following commands (note that
``8.x`` is the correct version):

.. code-block:: none
   
   rm -Rf ~/.drush/composer 
   drush dl composer-8.x

Then run the following command inside of your Drupal installation:

``drush composer-manager install``

Unable to verify certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you use both Composer Manager and the Composer tool directly, the
PHP version that ships with |acquia-product:add| may be unable to
validate the SSL certificate for GitHub and Packagist. This can display
an error similar to the following:

.. code-block:: none

   [Composer\Downloader\TransportException]                                                                                                           
   The "https://api.github.com/repos/acquia/content-hub-php" file could not be 
   downloaded: SSL operation failed with code 1. OpenSSL Error messages:
   error:14090086:SSL routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed
   Failed to enable crypto
   failed to open stream: operation failed

Solution
~~~~~~~~

Do not use the PHP that ships with |acquia-product:add| when running
``drush composer-manager`` or using the Composer command line tool
directly.

If you still have fatal errors when running
``drush composer-manager install``, you can use Composer directly in
order to install the required third party dependencies. In your
`docroot </articles/docroot-definition>`__, run
the following commands replacing ``[SITE-DIR]`` with your website's
directory, usually ``default``.

.. code-block:: none

   cd sites/[SITE-DIR]/files/composer
   curl -sS https://getcomposer.org/installer | php
   php composer.phar install --no-dev

AJAX errors with Views exposed filters
--------------------------------------

Views exposed filters may cause AJAX errors. This can be remedied by
either installing the latest -dev release of the Views module or by
`using this patch <https://www.drupal.org/node/1809958#comment-9905847>`__.

Local development
-----------------

If you are working with a local |acquia-product:ch| website and are
experiencing difficulties, see our 
`Best practices </content-hub/best-practices>`__ page.

.. |ch-diag.png| image:: https://cdn3.webdamdb.com/1280_AN5BhtksdNr4.png?-62169955200
   :width: 671px
   :height: 161px

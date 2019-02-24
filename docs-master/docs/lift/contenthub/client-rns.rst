.. include:: /common/global.rst

Release notes - Content Hub client
==================================

Looking for the latest and greatest new features and changes to the
`Content Hub <https://www.acquia.com/products-services/acquia-lift>`__
client? Read on and check back regularly to see what else we’ve done.

For |acquia-product:ch| service release notes, see the `Release notes -
Content Hub service </content-hub/service/release-notes>`__
documentation page.

.. |chapi| replace:: \ |acquia-product:ch|\  API
.. _chapi: http://api.content-hub.acquia.com/

Content Hub 8.x-1.25
--------------------------

*29 April 2018*

Feature
~~~~~~~~~~~~~~

-  **Drush 9 support** |br| 
   The |acquia-product:ch| client now works with Drush 9 on your Drupal 8-based websites.

Fixed issues
~~~~~~~~~~~~~~

-  When importing files, path names did not respect the file path
   settings on the publishing website.
-  The |acquia-product:ch| client executed the Common Data Format (CDF)
   normalizer twice for each CDF request.

Content Hub 8.x-1.24
--------------------------

*30 March 2018*

The |acquia-product:ch| client for Drupal 8
(`download <https://www.drupal.org/project/acquia_contenthub/releases/8.x-1.24>`__)
contains the following updates:

Change
~~~~~~~~~~~~~~

-  When exporting content, the parents of a taxonomy term are now
   included as a dependency.

Fixed issue
~~~~~~~~~~~~~~

-  Attempts to import ``text_long`` fields failed with Drupal 8.5 websites.


Content Hub 8.x-1.23
--------------------------

*14 March 2018*

The |acquia-product:ch| client for Drupal 8
(`download <https://www.drupal.org/project/acquia_contenthub/releases/8.x-1.23>`__)
contains the following updates:

Change
~~~~~~~~~~~~~~

-  The |acquia-product:ch| client now supports Drupal 8.5 for both
   installation and use.

Fixed issues
~~~~~~~~~~~~~~

-  When using the CDN module, URLs in the CDF (Common Data Format) were
   incorrect.
-  After re-uploading a media file, the file failed to syndicate.


Content Hub 8.x-1.22
--------------------------

*28 February 2018*

The |acquia-product:ch| client for Drupal 8
(`download <https://www.drupal.org/project/acquia_contenthub/releases/8.x-1.22>`__)
contains the following updates:

Changes
~~~~~~~~~~~~~~

-  Entities of type ``crop`` are no longer supported for syndication.

Fixed issue
~~~~~~~~~~~~~~

-  In some cases, attempting to import translated taxonomy terms would
   fail with an error message.
-  Occasionally, the |acquia-product:ch| attempts to process items in
   import queue failed with an out-of-memory error message.


Content Hub 8.x-1.21
--------------------------

*17 January 2018*

The |acquia-product:ch| client for Drupal 8
(`download <https://www.drupal.org/project/acquia_contenthub/releases/8.x-1.21>`__)
contains the following update:

Change
~~~~~~~~~~~~~~

-  Content discovery now includes the ability to filter by entity type
   and bundle. `Learn more </content-hub/discover>`__.

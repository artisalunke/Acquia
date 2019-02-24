.. include:: /common/global.rst

Release notes - |acquia-product:leb| client
============================================

.. toctree::
   :hidden:
   :glob:

   /lift/exp-builder/*
   
Looking for the latest and greatest new features and changes to the
`Experience Builder <https://www.acquia.com/products-services/website-personalization>`__
clients? Read on and check back regularly to see what else we’ve done.



Acquia Lift Drupal module 7.x-3.3
--------------------------------------------

*7 December 2017*

This |acquia-product:cha| module release for Drupal 7
(`download <https://www.drupal.org/project/acquia_lift/releases/7.x-3.3>`__)
contains the following updates:

.. admonition:: Upgrade Note

   Although you do not need to run ``update.php`` after you upgrade to this release, be sure to clear your Drupal website's cache after upgrading.

Change
~~~~~~~~~~~~~~

-  To deliver decisions without rendering content, the **Content
   replacement mode** now supports ``customized`` mode to return results
   as unrendered JSON.

Fixed issue
~~~~~~~~~~~~~~

-  For some nodes, incorrect taxonomy terms were displayed.



Acquia Lift Drupal module 8.x-3.6
--------------------------------------------

*7 December 2017*

This |acquia-product:cha| module release for Drupal 8
(`download <https://www.drupal.org/project/acquia_lift/releases/8.x-3.6>`__)
contains the following update:

.. admonition:: Upgrade Note

   Although you do not need to run ``update.php`` after you upgrade to this release, be sure to clear your Drupal website's cache after upgrading.

Change
~~~~~~~~~~~~~~

-  To deliver decisions without rendering content, the **Content
   replacement mode** now supports ``customized``
   `mode </lift/exp-builder/config/modes>`__ to return results as
   unrendered JSON.


Acquia Lift Drupal module 8.x-3.5
--------------------------------------------

*1 September 2017*

This |acquia-product:cha| module release for Drupal 8
(`download <https://www.drupal.org/project/acquia_lift/releases/8.x-3.5>`__)
contains the following update:

.. admonition:: Upgrade Note

   Although you do not need to run ``update.php`` after you upgrade to this release, be sure to clear your Drupal website's cache after upgrading.

Change
~~~~~~~~~~~~~~

-  Updated access permissions to increase the security for the views
   provided by this module. (LAT-841)


Acquia Lift Drupal module 7.x-3.2
--------------------------------------------

*1 September 2017*

This |acquia-product:cha| module release for Drupal 7
(`download <https://www.drupal.org/project/acquia_lift/releases/7.x-3.2>`__)
contains the following updates:

Change
~~~~~~~~~~~~~~

-  Updated access permissions to increase security for the views
   provided by this module. (LAT-841)

Fixed issue
~~~~~~~~~~~~~~

-  Aggregating the ``lift.js`` bootloader with other JavaScript files
   caused JavaScript syntax errors. (LAT-589)


Acquia Lift Drupal module 8.x-3.4
--------------------------------------------

*10 July 2017*

This |acquia-product:cha| module release for Drupal 8
(`download <https://www.drupal.org/project/acquia_lift/releases/8.x-3.4>`__)
contains the following updates:

.. admonition:: Upgrade Note

   Although you do not need to run ``update.php`` after you upgrade to this release, be sure to clear your Drupal website's cache after upgrading.

Change
~~~~~~~~~~~~~~

-  |acquia-product:leb| now supports page view UUIDs.

Fixed issue
~~~~~~~~~~~~~~

-  The Lift Inspector inherited CSS classes from inspected webpages,
   which caused display formatting problems.


Acquia Lift Drupal module 7.x-3.1
--------------------------------------------

*10 July 2017*

This |acquia-product:cha| module release for Drupal 7
(`download <https://www.drupal.org/project/acquia_lift/releases/7.x-3.1>`__)
contains the following update:

Change
~~~~~~~~~~~~~~

-  |acquia-product:leb| now supports page view UUIDs.


Acquia Lift Drupal module 7.x-3.0
--------------------------------------------

*17 March 2017*

This |acquia-product:cha| module release for Drupal 7
(`download <https://www.drupal.org/project/acquia_lift/releases/7.x-3.0>`__)
contains the following updates:

Change
~~~~~~~~~~~~~~

-  When enabled, the |acquia-product:cha| sidebar's positioning has been
   improved to reduce obscured content.

Fixed issue
~~~~~~~~~~~~~~

-  Website visitors may have encountered ``Mixed content`` warning
   messages due to the ``lift-collection.js`` file loading by HTTP
   instead of HTTPS. The file now loads using HTTPS. (LCS-242)



Acquia Lift Drupal module 8.x-3.3
--------------------------------------------

*17 January 2017*

This |acquia-product:cha| module release for Drupal 8
(`download <https://www.drupal.org/project/acquia_lift/releases/8.x-3.3>`__)
contains the following updates:

.. admonition:: Upgrade Note

   Although you do not need to run ``update.php`` after you upgrade to this release, be sure to clear your Drupal website's cache after upgrading.

Feature
~~~~~~~~~~~~~~

-  **Easily troubleshoot your personalization strategy** |br|
   Using the new Lift Inspector, you can examine how your website is
   working with |acquia-product:cha| and troubleshoot any issues that
   you may be having. `Learn more </lift/exp-builder/inspector>`__. As a
   content personalization debugger, it allows you to gather information
   about three key aspects of your personalization efforts:

   -  Data captures that your website sends to the |acquia-product:cha|
      service
   -  Current user segments in use on the page
   -  Decisions being made for your visitor by the service

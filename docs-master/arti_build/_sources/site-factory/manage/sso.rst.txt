.. include:: /common/global.rst

Setting up single sign-on
=========================

.. container:: message-status

      Applies only to Drupal 8-based websites hosted on |acquia-product:edg|

Setting up single sign-on (SSO) for Drupal 8 websites hosted on
|acquia-product:edg| enables users to sign in those websites by using
the `actions menu </site-factory/manage/website#actions>`__ in the Site
Factory Management Console.

Using SSO requires that you have a SAML service provider, which may be
either |acquia-product:ac| or an external provider. Although you can use
any SAML service provider that works with your Drupal 8 codebase,
|acquia-product:edg| directly supports the use of the `SAML
Authentication <https://www.drupal.org/project/samlauth>`__ module
(version 8.x-2.x).

.. note::  If you do not use the SAML Authentication module to connect to 
      your SAML service provider, you cannot use 
      `centralized role management </site-factory/users/admin>`__.


Installing the module
---------------------

Complete the following steps to use the SAML Authentication module with
SSO:

#. Download and add the following modules to your Drupal 8 codebase:

   -  |External Authentication|_
   -  `Acquia Cloud Site Factory Connector <https://www.drupal.org/project/acsf>`__, version
      8.x-1.35 or greater
   -  `SAML Authentication <https://www.drupal.org/project/samlauth>`__,
      version 8.x-2.0-alpha1 or greater

#. Add the modules from the previous step to your installation profile,
   along with the acsf_sso module, which is included with the
   |acquia-product:edg| Connector module.
#. Commit your changes back to your repository.

You can now use single sign-on with your |acquia-product:edg|-hosted
websites.

.. |External Authentication| replace:: External Authentication
.. _External Authentication: https://www.drupal.org/project/externalauth


Configuring authentication values
---------------------------------

When installing the ACSF SSO module or 
`staging your websites for testing </site-factory/workflow/staging>`__, |acquia-product:edg|
changes the ``samlauth.authentication`` configuration value to sign your
users in to the appropriate staged or live websites.

Do not modify the values for ``samlauth.authentication`` in active
configuration from those set by |acquia-product:edg|. For instance,
ensure you do not import stale or incorrect values for
``samlauth.authentication`` from configuration files stored in your
codebase when installing or staging a site.

Modifying ``samlauth.authentication`` in active configuration may cause
sign-in attempts to fail, or to sign users in to an environment other
than the one you intended.

.. _simplesaml:

SimpleSAMLphp and |acquia-product:edg|
--------------------------------------

Implementing single sign-on with the `simpleSAMLphp
Authentication <https://www.drupal.org/project/simplesamlphp_auth>`__
module for use with the acsf_sso module (included with the
|acquia-product:edg| Connector module), requires an Acquia Professional
Services engagement.

During your Professional Services engagement, after Acquia provides you
with the Service Provider (SP) data, you will perform the following
actions:

-  Install the Service Provider (SP) metadata with your Identity
   Provider (IdP).
-  Collaborate with Acquia regarding the testing of your SimpleSAMLphp
   configuration.
-  Ensure that Acquia has access to and knowledge of your IdP, if you
   are not using |acquia-product:ac| as your IdP.
-  Own your website's custom code.
-  Alter the ``config.php`` file to use
   ``/mnt/gfs/mydocroot.env/files-private/sites.json`` instead of the
   default ``creds.json`` path.
-  Test any custom workflows not provided by the `simpleSAMLphp
   Authentication <https://www.drupal.org/project/simplesamlphp_auth>`__
   module and the SimpleSAMLphp library.
-  Own the testing and validation of all Drupal configurations and
   workflows that integrate with `simpleSAMLphp
   Authentication <https://www.drupal.org/project/simplesamlphp_auth>`__
   module functionality.
-  Configure and activate the `simpleSAMLphp
   Authentication <https://www.drupal.org/project/simplesamlphp_auth>`__\ module
   for your website.

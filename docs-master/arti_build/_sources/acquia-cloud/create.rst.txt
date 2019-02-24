.. include:: /common/global.rst

Creating a new application on |acquia-product:ac|
=================================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/create/*

If you have a paid |acquia-product:acs| subscription, you can create a
new application in your subscription. You must be an `*Owner* or
*Administrator* </acquia-cloud/teams/organizations>`__ to create a new
application using the |acquia-product:ui|. You can also create an
`|acquia-product:acfs|
subscription <https://www.acquia.com/acquia-cloud-free>`__ at any time.

If you have an |acquia-product:ace| subscription, `contact Acquia
Support </support#contact>`__ to create a new application.

The number of applications that you can create in your subscription
depends on your subscription level. For more information, see
`|acquia-product:ac| Pricing <https://www.acquia.com/cloud-pricing>`__.

To create a new application, complete the following steps:

#. Sign in to the `|acquia-product:ui| <https://cloud.acquia.com/>`__.
#. On the **Applications** page, click **Add Application**.

   |Click the Add Application button|

   The **Add Application** page opens.

#. Select **Add a new application to an existing eligible subscription**
   and select the subscription the new application should belong to. As
   an alternative, you can create a new paid or free |acquia-product:ac|
   subscription.

   |Add an application|

#. Enter the **Application name** for your new application.

   The application name that you choose will be your application's UNIX
   username and code repository name. Application names must meet these
   requirements:

   -  Consist of at least four, but no more than 21, characters
   -  Consist only of lower-case, alphanumeric (a-z, 0-9) characters —
      special characters are not supported
   -  The first character must be alphabetic (a-z) and cannot be numeric

#. Click **Add**.

|acquia-product:ac| creates the application. All of your application's
environments initially contain a default welcome message. Use one of the
following options to create a working Drupal application:

-  `Install a new Drupal distribution </acquia-cloud/create/install>`__
-  `Import an existing application </acquia-cloud/create/import>`__

Don't forget to `set up SSH access </acquia-cloud/ssh/enable>`__ so you
can log in to your server using the command line.

.. |Click the Add Application button| image:: https://cdn2.webdamdb.com/1280_YjOtcJFV3mg4.png?-62169955200
   :width: 1276px
   :height: 139px
.. |Add an application| image:: https://cdn4.webdamdb.com/1280_Y6j0bEDR5dc9.png?-62169955200
   :width: 750px
   :height: 693px

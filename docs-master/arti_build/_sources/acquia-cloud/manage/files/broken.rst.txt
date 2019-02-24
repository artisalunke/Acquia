.. include:: /common/global.rst

Correcting broken file uploads
==============================

Resolving upload issues with |acquia-product:ace|

-  General
-  `VDE </acquia-cloud/manage/files/vde>`__

The |acquia-product:ace| architecture uses two or more load balancing
servers to handle incoming requests, routing them to the web servers in
a way that shares the load across multiple web servers.

|acquia-product:ace| users may experience problems with files that are
uploaded to their Drupal applications using Plupload, Webform, Views
Data Export, or other modules. The goal of these modules is to upload a
file to one directory, and then perform an action. This process occurs
in multiple steps. On multiserver platforms, this process may contact
server A for one part and server B on the next action. This can lead to
problems.

For example, when you use a module (such as the Plupload module) to
upload a large file, the file is divided into chunks that upload
separately. On |acquia-product:ace|, the user's requests could get
switched from one web server to another during the upload. As a result,
chunks of the uploaded file could arrive on different web servers, and
the web servers would not be able to put them back together.

Here are some ways to correct this in both Drupal and the
|acquia-product:ace| platform.

Notes

-  Several of the methods described on this page require changes to your
   website's ``settings.php`` file. Changing the ``settings.php`` file
   will affect *all* file uploads — not only large files — and in
   certain circumstances can have negative performance impacts.
-  The ``tmp`` folders referenced in these methods must be manually
   created before use. Setting variables will not automatically create
   the folders, and may cause upload issues until the folders are added
   manually.

.. _module-config:

Module configurations
---------------------

There are modules (including `Plupload <#plupload>`__ and
`Webform <#webform>`__) that can be configured to help work around these
issues on a permanent basis, which work by first creating a temporary
file for each uploaded file. After the temporary file is on the server,
the file is then moved to its final destination. For applications
running on a single instance, such as |acquia-product:acs| applications,
this works without any errors. For applications running on
|acquia-product:ace|, however, you may experience errors when some of
the uploaded files don't save properly.

Files added by these modules to |acquia-product:ace| applications are
saved to a temporary location that is not shared between the redundant
provisioned hardware. It is possible for the move process to take place
on a server different from the one that the file is uploaded to, which
causes that move to fail and the upload to appear broken.

This is a common scenario for websites hosted on either redundant
hardware or multiple servers. These modules allow you to overwrite the
temporary file location to create the temporary files at a location
shared between the hardware being used. The modules does not provide a
user interface to set the variable to do this, but the
`Drush <https://drupal.org/project/Drush>`__ utility allows you to
easily set the required variable, or the variable can be set in your
website's ``settings.php`` file.

-  *Plupload*
   `Plupload <http://www.plupload.com/>`__ is a popular plugin to
   enhance the file upload experience on a website. Plupload is also a
   popular choice for Drupal-based websites. To add the ``plupload``
   library functionality to Drupal, you must install and enable the
   `Plupload integration <https://www.drupal.org/project/plupload>`__
   module.
   To set the temporary variable with Drush, use the following command:

   ``drush @[docroot].[environment] vset plupload_temporary_uri '/mnt/gfs/[docroot].[environment]/tmp'``

   You can also set this in a more permanent fashion, by inserting code
   into your `application's ``settings.php`` <#settings-php>`__ file.

-  *Webform*
   The `Webform <https://www.drupal.org/project/webform>`__ module can
   have issues similar to what you may experience with
   `Plupload <#plupload>`__. Versions 7.x-4.x or greater and 8.x-5.x or
   greater of the Webform module include the ``webform_export_path``
   variable, which (depending on your Drupal version) you can set in
   your ``settings.php`` file in the same manner as you would with
   Plupload.

.. _settings-php:

Setting the directory in settings.php
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can permanently set your website's temporary files directory by
adding a setting to the website's ``settings.php`` file. The code for
you to use varies, depending on your Drupal version:

-  *Drupal 8*

   ``$config['system.file']['path']['temporary'] = "/mnt/gfs/{$_ENV['AH_SITE_GROUP']}.{$_ENV['AH_SITE_ENVIRONMENT']}/tmp";``

-  *Drupal 7*
   +-----------------------------------+-----------------------------------+
   | Module                            | Variable value                    |
   +===================================+===================================+
   | Plupload                          | ``$conf['plupload_temporary_uri'] |
   |                                   |  = "/mnt/gfs/{$_ENV['AH_SITE_GROU |
   |                                   | P']}.{$_ENV['AH_SITE_ENVIRONMENT' |
   |                                   | ]}/tmp";``                        |
   +-----------------------------------+-----------------------------------+
   | Webform                           | ``$conf['webform_export_path'] =  |
   |                                   | "/mnt/gfs/{$_ENV['AH_SITE_GROUP'] |
   |                                   | }.{$_ENV['AH_SITE_ENVIRONMENT']}/ |
   |                                   | tmp";``                           |
   +-----------------------------------+-----------------------------------+

.. _d8-editor-file:

D8 Editor File upload
---------------------

The `D8 Editor File
upload <https://www.drupal.org/project/editor_file>`__ module is
compatible with Drupal 8 and
`CKEditor <https://www.drupal.org/project/CKEditor>`__. It creates a
button in the toolbar to automatically link and upload data as part of
content creation, rather than manually linking a file.

.. _alt-stream-wrappers:

Alternative Stream Wrappers
---------------------------

The `Alternative Stream
Wrappers <https://www.drupal.org/project/alt_stream_wrappers>`__ module
for Drupal 7 allows Drupal to continue to use the built-in stream
wrappers (such as ``public://`` and ``temporary://``), but also use one
or more alternative stream wrappers — for cases including the shared
temporary directory. To use this module, complete the following steps:

#. Install and enable the module.
#. Edit your ``settings.php`` file and add code similar to the following
   to set a temporary directory:

   ``$conf['alt_stream_wrappers_alt-temp_path'] = "/mnt/gfs/{$_ENV['AH_SITE_GROUP']}.{$_ENV['AH_SITE_ENVIRONMENT']}/tmp";``

   Be sure to set the temporary directory to a value based on your
   website's installation, and the directory must both exist and be
   writable.

#. Save your changes to the ``settings.php`` file.

For an example of this, see `Using Views Data
Export </acquia-cloud/manage/files/vde>`__.

Alternative Stream Wrappers supports the Webform module. For more
information, see https://www.drupal.org/node/2221651 on Drupal.org.

.. _pin:

Temporary pin to a web server
-----------------------------

Important

This method is for *temporary use only* and should be removed when you
are not uploading critical files. Overuse of this method will cause
performance problems for your application and, in a shared environment,
any other customers on that server.

You can temporarily force all of your upload requests to the same
server. To do this, we suggest that you use one of the following
methods:

-  `Pinning to a web server without using the hosts
   file <%5Bacquia-product:kb%5Darticles/pinning-web-server-without-using-hosts-file>`__
-  `Using a temporary domain in your ``/etc/hosts``
   file <%5Bacquia-product:kb%5Darticles/using-etchosts-file-custom-domains-during-development>`__

.. _other:

Other modules
-------------

Other modules may also have issues in multiserver environments. For
example, the Views Data Export module does not always work as expected.
For more information, see `Using Views Data
Export </acquia-cloud/manage/files/vde>`__.

.. _sticky_sessions:

Sticky Sessions
---------------

Although in the past the `|acquia-product:ac| Sticky
Sessions <https://www.drupal.org/project/acquia_cloud_sticky_sessions>`__
module was suggested for use on |acquia-product:ac|, it is no longer
recommended, and the module is minimally maintained. Using the module
can put a burden on one server in the group, and can cause performance
problems for users whose sessions are directed to that server.

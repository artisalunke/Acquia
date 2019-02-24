.. include:: /common/global.rst

Importing an existing application using Drush
=============================================

Note

Before you import your application using Drush, read the `Import
overview </acquia-cloud/create/import>`__ to familiarize yourself with
the other available import approaches.

This procedure is for Mac and Linux platforms. If your Drupal
application is on a Windows platform, you'll have to `manually import
your application to
|acquia-product:ac| </acquia-cloud/create/import/manual>`__.

To import your application to |acquia-product:ac| using Drush, you must
create a site archive file, and then import the file to
|acquia-product:ac|.

.. _create:

Creating a site archive file
----------------------------

For information about how to create a site archive file with Drush, see
`Creating a Drupal site archive for
import </acquia-cloud/create/import/archive-create>`__. Copy
``mysite.tar.gz`` to your local computer.

.. _import:

Importing the site archive file with Drush
------------------------------------------

To import the site archive file with Drush, complete the following
steps:

#. Verify that you've `enabled SSH access </acquia-cloud/ssh/enable>`__
   to your |acquia-product:ac| server.
#. Copy ``mysite.tar.gz`` to ``/mnt/gfs/[site].[env]/import`` on your
   |acquia-product:ac| server, using the following ``scp`` command:

   ``scp mysite.tar.gz [site].[env]@[server]:/mnt/gfs/[site].[env]/import``

   where ``[site]`` is the site name of your application on
   |acquia-product:ac|, ``[env]`` is the |acquia-product:ac| environment
   (one of ``prod``, ``test``, or ``dev``), and ``[server]`` is the full
   DNS name of the server that hosts your site.

   To find your ``[site]`` and ``[server]`` name, sign in to the
   |acquia-product:ui| and view the **Servers** page for the
   environment.

#. Using SSH, log in to your environment on |acquia-product:ac|, using
   the SSH address displayed on the **Servers** page for the
   environment.
#. In this SSH session, use the following command to import your
   application.

   ``drush @[site].[env] ah-site-archive-import /mnt/gfs/[site].[env]/import/mysite.tar.gz``

   where:

   -  ``[site]`` is the same value from step 2.
   -  ``[env]`` is the environment you're updating. Acceptable values
      are ``dev`` (Development), ``test`` (Staging), and ``prod``
      (Production).

After you import your site archive, you can `import your
files </acquia-cloud/create/import/manual-files>`__ and `check out a
local copy of the application from your |acquia-product:ac| code
repository </acquia-cloud/develop/checkout>`__.

.. include:: /common/global.rst

Installing a Drupal module on |acquia-product:ac|
=================================================

One of the most common tasks you'll accomplish while developing or
maintaining a Drupal application is adding a Drupal contributed module.
If you are used to working in a local installation of Drupal, you may be
used to doing this directly in the Drupal admin interface, using the
core Update Manager module, or perhaps with Drush, using the
``drush dl`` command. If your application is hosted on
|acquia-product:ac|, the module directories are part of the code
repository, which is `not directly
writable <%5Bacquia-product:kb%5Darticles/file-permissions-while-using-acquia-cloud>`__.
This means that you can't directly add a module using the Update
Manager, ``drush dl``, or SFTP. Instead, you must commit your changes
using a version control system (Git).

There are several different approaches you can take. This topic
describes two of them:

-  `Add the module to your local code base, and then commit
   it <#local>`__
-  `Install the module on an |acquia-product:ac| environment using Live
   Development, and then commit it <#livedev>`__

Another useful approach is to develop your application locally using
`|acquia-product:add| </dev-desktop>`__, add new modules using local
tools like `Drush <http://www.drush.org/>`__ or the Update Manager, and
then `push the code to
|acquia-product:ac| </dev-desktop/cloud/working#push>`__ with
|acquia-product:add|.

.. _local:

Adding the module locally
-------------------------

To add a module to your local code base, and then commit it:

#. `Get SSH access </acquia-cloud/ssh/enable>`__ to your
   |acquia-product:ac| server, if you don't already have it.
#. Install `Git </acquia-cloud/develop/repository/git>`__ locally, if
   you haven't already done so.
#. `Check out a local copy of the code
   repository </acquia-cloud/develop/checkout>`__.
#. Change directory into the new local copy of the repository.
#. Create a feature branch to test the module. In this example, we'll
   assume that we're installing the Foo module, so we'll call the
   feature branch ``foo``.

   ``git checkout -b foo``

#. Change directory into your modules directory (``/sites/all/modules``
   or ``/sites/all/modules/contrib``).
#. Download and add the contributed module to the modules directory in
   the feature branch. For example:

   ``curl http://ftp.drupal.org/files/projects/foo.tar.gz | tar fz``

#. `Commit the new module code </acquia-cloud/develop/update>`__ into
   the |acquia-product:ac| repository.
#. Deploy the feature branch to your Development or Staging environment
   for testing.
#. Using the Drupal admin UI or Drush, enable and configure the new
   module.

.. _livedev:

Installing using Live Development
---------------------------------

Using Live Development mode, you can temporarily make the docroot of
your Development environment writable, so you can add modules or make
other changes.

Here are the steps for installing a module on an |acquia-product:ac|
environment using Live Development, and then committing it. It's very
important that you commit your changes to your |acquia-product:ac| code
repository before you disable Live Development. Otherwise, the new
module won't be part of your application's code base. If your
application's database thinks the new module is enabled, but it can't be
found, this can cause havoc.

#. `Enable Live Development </acquia-cloud/develop/livedev>`__ on your
   Development environment. Live Development is available for
   non-Production environments only.
#. Sign in to your Drupal application and go to the application's
   ``/admin/modules`` page.
#. Enable the Update Manager, if it isn't already enabled.
#. On the ``/admin/modules`` page, click **Install new module** and `use
   the Update Manager <https://drupal.org/node/895232>`__ to install the
   module.
#. Enable and configure the module, and then test it on your
   |acquia-product:ac| Development environment.
#. `Connect to your |acquia-product:ac| server using
   SSH </acquia-cloud/ssh/enable>`__.
#. Change directory to your application's live development directory,
   ``/mnt/gfs/[sitename].[env]/livedev``.
#. `Commit your changes </acquia-cloud/develop/update>`__ to your
   |acquia-product:ac| code repository.

.. include:: /common/global.rst

Troubleshooting application imports
===================================

As described in `Importing an existing
application </acquia-cloud/create/import>`__, there are several
different methods you can use to import a Drupal application into
|acquia-product:ac|. In the majority of cases, the import process works
quickly and smoothly. Here are some things you can do to make the import
work better and some things to check for in those cases where it does
not work.

.. _prep:

Before you import your application
----------------------------------

Read `Preparing your application for
export </acquia-cloud/create/import/prepare>`__, which lists recommended
steps to take before you import your Drupal application to
|acquia-product:ac|.

Use manual import process for multisite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multisite Drupal installations use a separate database for each website
within the docroot. The site import process used by |acquia-product:ac|
and |acquia-product:add| can import only applications with a single
database. If you want to import a multisite Drupal installation, you
need to import it using the `manual import
process </acquia-cloud/create/import/manual>`__.

Check for dependency on unsupported PHP libraries or unsupported PHP version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:ac| runs a specific set of PHP libraries on the versions
of PHP listed in `|acquia-product:ac| technology platform and supported
software </acquia-cloud/arch/tech-platform>`__. If your application
requires a later or earlier PHP version or PHP libraries that do not run
on |acquia-product:ac|, your application may not work on
|acquia-product:ac|.

Check your PHP memory limit
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:ac| configures a PHP memory limit for your servers. If
your application is configured with a larger PHP memory limit, it will
not be able to start. The PHP memory limit might be set in one of three
places:

-  The ``memory_limit`` parameter in ``php.ini``
-  The ``php_value`` parameter in ``.htaccess``
-  The ``memory_limit`` parameter in the Drupal ``settings.php`` file in
   ``sites/default/settings.php``

For |acquia-product:ac| applications, you should never set any of these
parameters in these files. |acquia-product:acs| customers can configure
the PHP memory limit for an environment. See `Configuring PHP
settings </acquia-cloud/manage/php#php-mem>`__. |acquia-product:ace|
customers can submit a support ticket requesting a change in the PHP
memory limit. If you have ``memory_limit`` settings in ``.htaccess`` or
``settings.php`` files, delete them before you import your application.

See also `Conditionally increasing memory
limits <%5Bacquia-product:kb%5Darticles/conditionally-increasing-memory-limits>`__
and `Memory consumption tracking
tools <%5Bacquia-product:kb%5Darticles/memory-consumption-tracking-tools>`__
for tips about controlling the amount of memory your application
requires.

.. _check:

Checking for import success
---------------------------

Importing an application into |acquia-product:ac| is usually fairly
quick, but it is not instantaneous. Depending on which import method you
choose, the import process has three major steps:

#. Creating a site archive
#. Sending the site archive to Acquia
#. Opening the site archive and creating the application from it

Depending on the size of your application and your Internet connection,
the first two steps can take from a few minutes to, in some cases, more
than an hour. You can check the progress by `signing in to the
|acquia-product:ui| <https://cloud.acquia.com/>`__, selecting your
application, and clicking the activity button. After the site archive
has arrived on the |acquia-product:ac| server, you should see an entry
like this in the activity log:

``Import [archive-filename].tar.gz to environment Dev``

In addition, you can see your site archive file on the server. Connect
to the server with SSH. You should be able to find the site archive file
in ``/mnt/gfs/[site]dev/import``.

One factor in how long a site import can take is the size of of your
site archive. You can minimize the size of the site archive by doing the
following:

-  Clearing your cache before you start the site import
-  Removing any Drupal modules that have been disabled and that you are
   not using

.. _nonstarter:

My application is on |acquia-product:ac|, but will not start
------------------------------------------------------------

If you have verified that your application's archive file has reached
|acquia-product:ac|, but your application does not start (will not serve
pages), here are some things you can check.

Get your application status with Drush
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. `Connect to your environment with SSH </acquia-cloud/ssh>`__.
#. From the command line, run the ``drush status`` command, targeting
   your Dev environment:

   ``drush @[site].dev status``

Examine the output of ``drush status`` for errors that may give you
clues about issues that are keeping your application from starting.

Look for errors in server and PHP logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can download your Apache server and PHP error logs from the **Logs**
page for examination. As an alternative, you can obtain the logs by
using SSH:

#. `Connect to your environment with SSH </acquia-cloud/ssh>`__.
#. Find your Apache server error log at
   ``/var/log/sites/[site].[env]/logs/[servername]/error.log`` and your
   PHP error log at
   ``/var/log/sites/[site].[env]/logs/[servername]/php-errors.log``.

Any displayed error messages should indicate the root cause of the
error. For more information, see `About |acquia-product:ac|
logging </acquia-cloud/monitor/logs>`__.

Disable problematic Drupal modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One common reason why a Drupal application might not start on
|acquia-product:ac| is a custom Drupal module that will not run on
|acquia-product:ac|. If you know which module is causing the problem,
you can disable it. For information about how to do this, see `Disabling
modules that block sites on
|acquia-product:ac| <%5Bacquia-product:kb%5Darticles/disabling-modules-block-sites-acquia-cloud>`__.

.. _connector:

Troubleshooting |acquia-product:anc| imports
--------------------------------------------

Here are solutions to some issues you may encounter in importing an
application using the |acquia-product:anc|.

The Migrate button doesn't do anything when you click it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the |acquia-product:anc| does not start to migrate your application
when you click **Migrate**, clear your Drupal cache, and then retry the
migration process.

To clear your Drupal cache, open your Drupal application's Performance
page at ``http://[site_URL]/admin/config/development/performance``.

You see an error message when you try to migrate your application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are experiencing errors while migrating your application, try
deselecting the **Migrate files directory** check box and selecting the
**Reduce database export size** check box, and then retry the migration
process. These options are not displayed unless you have already
attempted to migrate and encountered an error.

|Migrate dialog|

The following error messages describe the most common causes of problems
with the migration process. If you don't see your error message, or the
actions associated with the message don't allow you to migrate your
application, contact Support or `use a different application import
method </acquia-cloud/create/import>`__.

-  **Error message:** ``No compression libraries available``

   The application's installed PHP does not have available GZip or Zip
   libraries.

-  **Error message:**
   ``Cannot create temporary directory [file-system-directory] to store site archive``

   The |acquia-product:anc| cannot create a directory in the Drupal
   files directory. Examine the file system permissions for the Drupal
   files directory.

-  **Error message:** ``Server error, please submit again``

   The Acquia server did not respond. Retry the migration process. If
   the |acquia-product:anc| displayed this message at the end of the
   migration process, examine the |acquia-product:ui| Notifications
   panel to see if an import is in progress, and if so, you can ignore
   this error message.

-  **Error message:** ``Signature from server is wrong``

   Your |acquia-product:ac| application did not respond with a correct
   signature, indicating possible transmission corruption. Retry the
   migration process.

-  **Error message:**
   ``Server error, unable to retrieve environments for migration``

   Make sure that your Development environment does not have a tag
   deployed. Environments with tags deployed will be excluded from the
   eligible list of environments.

-  **Error message:** ``Transfer error``

   The |acquia-product:anc| encountered an unknown error during the site
   archive upload portion of the process. Retry the migration process.

-  **Error message:** ``AJAX Error regarding ReadyState``

   The Drupal batch process running the migration encountered an error.
   Consult Drupal logs for more information or retry the migration
   process.

.. |Migrate dialog| image:: https://cdn4.webdamdb.com/1280_cIycC62y8TU7.png?1527178989
   :width: 590px
   :height: 244px

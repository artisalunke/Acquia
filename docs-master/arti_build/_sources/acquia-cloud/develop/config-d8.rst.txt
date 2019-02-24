.. include:: /common/global.rst

Configuration management for Drupal 8
=====================================

Drupal 8's `Configuration
Management <https://groups.drupal.org/build-systems-change-management/cmi>`__
(CM) makes major improvements to how configuration is handled, compared
to earlier Drupal versions. This page describes the best ways to handle
Drupal 8 configuration management on |acquia-product:ac|.

For an introduction to CM, see `Lesson 3 - Configuration forms and
CM <%5Bacquia-product:kb%5Darticles/drupal-8-configuration-forms-and-cm>`__
in the `Building modules with Drupal
8 <%5Bacquia-product:kb%5Darticles/building-drupal-8-modules>`__ guide.

.. note:: 

    -  The examples on this page assume that you are using
       |acquia-product:ac| as your development environment. If you are using
       a local development environment, see `Managing configuration in local
       development <#local>`__.
    -  Although, by default, Drupal 8 uses the ``sync``\ directory for
       configuration, |acquia-product:ac| uses the ``vcs`` directory for
       that purpose.

.. _config:

Required ``config/default`` folder
----------------------------------

|acquia-product:ac| requires configuration of a default location for a
configuration directory to store Drupal 8 configuration information in
your code repository. This directory is usually in the following
location:

``config/[sitename]``

where ``config`` is a directory at the same level (sibling of) your
docroot directory. However, this directory does not exist by default in
the repository, and needs to be created. Without this directory, you may
receive a runtime requirement error similar to the following:

``The directory docroot/../config/default does not exist.``

Receiving the preceding error message indicates that you cannot execute
``update.php`` until you create the directory.

Because Git does not let you commit an empty directory, you also need to
add a small file (usually a text file named ``.gitkeep``) to the new
directory before you can commit it to your repository.

Once the directory is created, the structure at the ``docroot`` level
will look like:

.. code-block:: none

    /docroot/
    config/default/

.. _push:

Pushing configuration forward
-----------------------------

In this scenario, we assume that you are building or updating a Drupal 8
application named ``example`` in an |acquia-product:ac| Development
environment.

#. In your Development environment, use the tools of your choice to set
   the configuration of all the modules in your Drupal application.
#. When you are satisfied with how everything is configured (for at
   least this iteration), set your Development environment to Live
   Development mode, as described in `Using Live development mode to
   change code on your server </acquia-cloud/develop/livedev>`__.
#. In Live Development mode, export your application's configuration
   from the database to the file system using a command similar to the
   following:

   ``drush @example.dev.livedev config-export vcs --commit``

#. You can then review the changes before pushing them:

   ``drush @example.dev.livedev ssh git show``

#. If you are satisfied with the changes, push them using a command
   similar to the following:

   ``drush @example.dev.livedev ssh git push``

   If you are not satisfied with your changes, run commands based on the
   following:

   ``drush @example.dev.livedev ssh git reset --hard HEAD^1 drush @example.dev.livedev config-export vcs``

   Adjust your changes as needed, and then run these commands:

   ``drush @example.dev.livedev config-export vcs --commit drush @example.dev.livedev ssh git push``

#. Sign in to the |acquia-product:ui| and select your application.
#. Drag the **Code** element from **Dev** to **Stage** to push your
   configuration from the Development environment to the Staging
   environment.
#. Import the configuration from the file system to the database for the
   Staging environment by running a command like this:

   ``drush @example.test config-import vcs``

#. If required by your configuration changes, run ``update`` on your
   Staging environment with a command like this:

   ``drush @example.test updatedb``

.. _pull:

Pulling configuration from Production to Development
----------------------------------------------------

In this scenario, we assume that you have made configuration changes in
a Drupal 8 application named ``example`` in an |acquia-product:ac|
Production environment and you want to pull them back into your
Development environment, so that your development workflow is using the
current live configuration.

#. Set your Development environment to Live Development mode, if it is
   not already set.
#. Copy the configuration from your Production environment to the
   ``vcs`` folder on the Development environment with a command like
   this:

   ``drush config-pull @example.prod @example.dev.livedev --label=vcs``

#. Commit the configuration on the Development environment with a
   command like this:

   ``drush @example.dev.livedev ssh git commit -am "Copy config from Prod."``

#. Import the copied configuration into the Development environment with
   a command like this:

   ``drush @example.dev.livedev config-import vcs``

#. If all went well, run:

   ``drush @example.dev.livedev ssh git push``

   If not, run:

   ``drush @example.dev.livedev ssh git reset --hard HEAD^1``

.. _local:

Managing configuration in local development
-------------------------------------------

If you are developing a Drupal 8 application in a local environment,
keep in mind these tips:

-  Download the |acquia-product:ac| Drush integration aliases. For more
   information, see `Using Drush
   aliases </acquia-cloud/drush/aliases>`__.
-  Update your site aliases by running the following Drush command:

   ``drush acquia-update``

-  In the ``settings.php`` file for your application, add the following
   entry to the end of the file:

   ``$config_directories['vcs'] = $app_root . '/../config/' . basename($site_path);``

-  Replace ``@example.dev.livedev`` with ``@self`` in the previous
   procedures on this page.

Whenever you update the code in an environment, run the following:

``drush config-import vcs -y && drush updatedb -y``

.. _protect:

Protecting configuration in the Production environment
------------------------------------------------------

You can protect your Production environment from untested configuration
changes by using the `Configuration Read-only
mode <https://www.drupal.org/project/config_readonly>`__ module.

.. include:: /common/global.rst

Lightning
=========

.. toctree::
  :hidden:
  :glob:

  /lightning/modules
  /lightning/install
  /lightning/update
  /lightning/subprofile
  /lightning/known-issues
  /lightning/*

|lightning-icon.png|

|acquia-product:ld| is a packaged distribution of the open source `Drupal <https://www.drupal.org/>`__ social publishing system for Drupal 8. As a free collection of `useful modules </lightning/modules>`__ from Acquia and the Drupal community, |acquia-product:ld| offers you a quick on-ramp to begin building your website.

.. container:: message-status

 **QUICK LINKS:**   `Install </lightning/install>`__  |  `Update </lightning/update>`__  |  `Module listing </lightning/modules>`__  |  `Release notes </lightning/release-notes>`__

Lightning for Drupal 8
----------------------

In Drupal 8, we have taken advantage of new functionality and tightly coupled functional areas that comprise the new standard for enterprise authoring in Drupal, including layout, preview, workflow, and media. We have embedded hundreds of automated tests allowing developers to implement continuous integration pipelines that monitor major functionality, providing a safe environment to innovate with their own custom code additions to Lightning.

Development and Maintenance
---------------------------

Although many other Drupal installations and distributions rely on Drush for updates and development, |acquia-product:ld| requires the use of `Composer <https://getcomposer.org/>`__ commands with your installation.

Unlike Drush, Composer is a dependency manager system that you can use to prevent module mismatches and better ensure system reliability. As an example of this, if the *ModuleA* 8.x-1.0 module depends on *ModuleB* 8.x-3.2, Composer will not let you update *ModuleB* to version 3.3 or downgrade it to version 3.1.

The following table includes Composer command replacements for the Drush commands that you may already be familiar with:

.. list-table::
 :header-rows: 1

 * - Task
   - Drush (version <= 8 only)
   - Composer
 * - Fetch the latest version of a project
   - ``drush pm-download [project]``
   - ``composer require drupal/[project]:8.*``
 * - Fetch a specific version of a project
   - ``drush pm-download [project]-8.x-1.0-beta3``
   - ``composer require drupal/[project]:8.1.0-beta3``
 * - Update all projects and Drupal core
   - ``drush pm-update``
   - ``composer update``
 * - Update a single project
   - ``drush pm-update [project]``
   - ``composer update drupal/[project]``
 * - Updating Drupal core
   - ``drush pm-update drupal``
   - ``composer update drupal/core``

Drush is still in use, however, as it handles certain tasks, such as database updates (``drush updatedb``). This installer will install a copy of Drush (local to the project) in the ``bin`` directory.

Source Control
--------------

If you review the ``.gitignore`` file provided in the distribution, you'll see that certain directories, including all directories containing contributed projects, are excluded from source control. This might be disconcerting if you're used to Drush, but in a Composer-based project, you should not commit your installed dependencies to source control.

When you set up the project, Composer will create a file called ``composer.lock``, which lists which dependencies were installed, and which versions. Commit the ``composer.lock`` file to source control. When others want to install copies of the project, they simply need to run ``composer install``, which will install the correct versions of everything listed in ``composer.lock``. This ensures a consistent base development environment for all the members of a team.

Use the information on these pages as a guide as you install or upgrade to |acquia-product:ld|, connect your website to an |acquia-product:aqs|, and get introduced to Acquia's technical support and network services.

Committing ``settings.php`` to your repository
----------------------------------------------

Drupal websites use a ``settings.php`` file for basic configuration. Applications on |acquia-product:ac| have `a special include statement </acquia-cloud/develop/env-variable>`__ that configures your ``settings.php`` file to function properly in all of your environments that are hosted on |acquia-product:ac|. Unless you're building a distribution or deploying to multiple environments with different databases, Acquia recommends that you commit the ``settings.php`` file to your repository.

For an example of how to add a ``require`` line to ``settings.php`` to protect sensitive credentials from being stored in version control, see the `blt.settings.php <https://github.com/acquia/blt/blob/9.1.x/settings/blt.settings.php>`__ file in |acquia-product:blt|.

Getting started with |acquia-product:ld|
----------------------------------------

To start taking advantage of |acquia-product:ld|, select one of the following links:

-  `Installing Lightning </lightning/install>`__
-  `Updating a Lightning website </lightning/update>`__

.. |lightning-icon.png| image:: https://cdn3.webdamdb.com/1280_ADRQ40uouIn1.png?-62169955200
   :class: no-sb logo-pp float-right
   :width: 62px

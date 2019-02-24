.. include:: /common/global.rst

Acquia Automation: Composer builds
==================================

Because `Composer </resource/composer>`__ is the `widely accepted
standard for building Drupal 8
websites <https://support.acquia.com/article/using-composer-drupal-8-and-remote-administration>`__,
Remote Administration (RA) will be using only Composer builds and
updates to ensure that dependencies are included in any Drupal 8 core or
contributed module update.

Note, however, that RA will continue to use Drush to detect insecure
modules.

Requirements
------------

Installations of Drupal 8.3.0 or greater should be built with a fully
functional ``composer.json`` file that includes all code necessary to
run your codebase, and that contains no package conflicts.

.. important:: 
  Websites running Drupal 8.3.0 and greater may still be updated using
  Drush, depending on certain version requirements. Updating
  Drupal core using Drush does not guarantee that dependency
  updates are included, which may cause errors on your website.
  Acquia strongly recommends that websites running Drupal 8
  (specifically 8.3.0 and greater) be built and updated using
  Composer. Acquia can provide only limited troubleshooting
  support for websites that are updated on production environments
  using Drush.

.. _minimum:

Minimum requirements for an RA ``composer.json`` file
-----------------------------------------------------

The following outlines the minimum requirements for a ``composer.json``
file to be compatible with Remote Administration:

.. important::  The ``composer.json`` file for your website must be located above the
                ``docroot`` directory in your repository. Do not move the
                ``composer.json`` or ``vendor/`` directory that comes with
                Drupal core, located inside of the ``docroot`` directory.

-  The ``vendor`` directory should be located in the repository's root
   above the ``docroot`` directory. This directory must be managed
   through version control, and the proper autoloading must be set up to
   redirect Drupal to the new ``vendor`` location. For more information,
   see `Drupal
   scaffold <https://github.com/drupal-composer/drupal-scaffold>`__.
-  | A Drupal ``composer.json`` file must specify at least the following
     basic information:

.. code:: javascript

   "repositories": {
   "require": {
   "require-dev": {
   "conflict": {
   "extra": {
   "installer-paths": {

-  The require section of the ``composer.json`` file needs to list
   Drupal core as well as all contributed modules and packages required
   to run your Drupal website.
-  All Drupal code must be located within the
   `docroot <%5Bacquia-product:kb%5Darticles/docroot-definition>`__
   folder.
-  All non-Drupal files added to any directory must either be added as a
   `public
   repository <https://getcomposer.org/doc/05-repositories.md>`__, added
   as a `private
   repository <https://getcomposer.org/doc/articles/handling-private-packages-with-satis.md>`__,
   excluded using
   `drupal-scaffold <https://github.com/drupal-composer/drupal-scaffold>`__,
   or able to be recreated through
   `patches <https://github.com/cweagans/composer-patches#using-an-external-patch-file>`__
   that have been declared in your ``composer.json``.

.. important::  The RA ``composer.json`` `template <#template>`__ includes everything
                required to make your ``composer.json`` file compatible with RA. If you
                are building a new website or converting an existing website to a
                Composer build, we recommend that you use this template as a starting
                point.

.. _automation:

How RA Automation works with Composer
-------------------------------------

The Remote Administration update process performs a series of update
commands against your website on the RA environment, determines any
needed updates, applies the changes, and notifies you, as described in
these steps:

#. The latest production code and a copy of your production database are
   copied to the RA environment.
#. Your codebase is examined for a valid ``composer.json`` file above
   the ``docroot`` directory.

   -  If a valid ``composer.json`` is located, RA will proceed with the
      update process.
   -  If no ``composer.json`` file is located, RA's automation will
      revert to applying updates using Drush. `For Drupal 8 websites,
      refer to the important note regarding Drupal 8 and using Drush for
      updates <#drush>`__.

#. The code is scanned for the following types of updates with the
   ``drush pm-updatestatus`` command:

   -  Security updates for contributed modules
   -  Bugfix updates for specified contributed modules
   -  Bugfix and security updates for Acquia-managed modules

#. The most recent version of Composer is temporarily installed on the
   RA environment.
#. Composer updates are determined and applied with the
   ``composer update --dry-run`` command in your RA environment to
   ensure that your ``composer.json`` contains no errors that will
   prevent updates from completing. No changes are made to your
   codebase.
   If conflicts requiring resolution prior to applying updates are
   detected in your ``composer.json`` file, you will receive an Acquia
   Support ticket notifying you of these conflicts so that they can be
   resolved.
#. Composer performs the
   ``composer update package/name --with-all-dependencies`` command to
   update your package to the highest available version allowed by the
   version constraints in your ``composer.json`` file.
#. Database updates are applied with the ``drush updb`` command.
#. To provide faster security updates, the `Stage File
   Proxy <https://www.drupal.org/project/stage_file_proxy>`__ module is
   enabled to mirror files—instead of copying them—from your production
   environment to your RA environment.
#. If new updates are identified, you will be notified with an Acquia
   Support ticket when these updates are ready for testing.

.. _template:

RA ``composer.json`` template
-----------------------------

The `Acquia RA
Composer <https://github.com/acquia/acquia-ra-composer>`__ GitHub
repository contains an example ``composer.json`` file that you can use
as a starting point for creating your website's ``composer.json``. The
repository contains the following files:

-  ``composer.json`` – An example file for Composer
-  ``readme.md`` – How to use the ``composer.json``
-  ``annotated.composer.json`` – An annotated example file with
   explanations of the configuration sections

To use the example Composer file, you can download the file and copy its
contents into your own ``composer.json`` file, or clone the repository
and then copy the file to your website's repository.

.. important::  The example Composer file must be modified to include all of the
                modules that your website requires. Copying the example file
                into your code repository without modifications will prevent RA
                from providing you with updates, and may also cause website
                downtime.

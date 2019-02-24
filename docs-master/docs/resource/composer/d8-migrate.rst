.. include:: /common/global.rst

Migrating a Drupal 8 site into a Composer-managed build
=======================================================

Migrating an existing Drupal 8 website into a Composer-managed build
requires that you build a ``composer.json`` file that includes all of
the required packages for your website.

The structure of your repository should shift as follows:

|Repository Structure|

The key differences are the **new** top-level ``composer.json`` and
``composer.lock`` files, and the top-level location of the vendor
directory.

Before you start
----------------

It will be easier to compare changes made by Composer if you start with
a website that is generally structured the way you want the website to
end up.

-  *Contributed modules* - Drupal best practice is to place contributed
   modules in ``docroot/modules/contrib``. If your modules are not
   currently in that path, you should consider moving all contributed
   modules to ``docroot/modules/contrib/``.
-  *Custom modules* - Drupal best practice is to place custom modules in
   ``docroot/modules/custom``. If your modules are not currently in that
   path, you should consider moving all contributed modules to
   ``docroot/modules/custom/``.
-  *Themes* - Drupal best practice is to reflect the same
   ``custom/contrib`` structure for themes as for modules.
   Each one of these changes may require you to run ``drush cr`` to
   ensure your Drupal website knows the new ``module/theme`` location.
   It is best that you do this first to reduce potential complications
   in migrating to Composer.
-  *Custom code* - If you have made any modifications to Drupal core
   files or contributed module files, you **must** create patches for
   them and store them in a top level ``patches/`` directory. Composer
   update will **overwrite all core and contributed module** **files**,
   but it is able to also apply patches after an update is applied.
   Creating these patches now will save you trouble later.

If you have modified the Drupal ``composer.json`` file located at
``docroot/composer.json``, you must note these modifications and prepare
to add them to the top-level ``composer.json`` file. This file **will be
overwritten**, and patching it is unnecessary as you can simply add your
requirements to the top-level ``composer.json`` file.

All of these changes should be committed, tagged, and, if possible,
merged to master. This is your new, permanent, file structure.

Procedure
---------

#. Create a development branch that will contain your composer.json
   file. Do NOT do this on ``master``. This branch should contain all
   code required to work on production.
#. | Obtain a working template for you to use as reference.
     https://github.com/acquia/acquia-ra-composer/blob/master/composer.json
     is a great template to use. Save the file at the top level of your
     repository: ``repo/composer.json``

   .. note::  The instructions contained in this procedure are based on the 
      linked ``composer.json`` file.

#. To simplify the migration, Acquia strongly recommends that you
   install the *exact* version of Drupal and all contributed modules
   that already running on your website. This can be done by *pinning*
   your module to a specific version. To do this, open your
   ``composer.json`` file, and then edit the ``require`` section based
   on the following notes:

   .. code-block:: none 

      "require": {
          "drupal-composer/drupal-scaffold": "^2.0.0",
          "composer/installers": "^1.0"
      },

   -  *Drupal core* - Require Drupal core by changing
      ``"drupal/core": "^8.3"``, to your current Drupal version, i.e.,
      ``"drupal/core": "8.3.1"``.
      Specifying the entire version is called “pinning” a package.
      Pinning has the advantage of ensuring that this and only this
      version is installed, but it also prevents using the
      ``composer update drupal/core --with-dependencies`` command for
      updates. This should be *unpinned* after testing of the Composer
      migration is complete.
   -  | *Contributed modules* - All modules that are required to run
        your website on production should be listed in the ``require``
        section. Start with contributed modules.
      | Generate a list of all enabled contributed modules, which you
        can do with the following Drush command:

      ``drush pml --status=Enabled --no-core``

      If you are using multisites, evaluate all multisites to ensure
      that your list is complete. Results should appear similar to the
      following:

      .. code-block:: none

          Package           Name                              Type    Version
          Administration    Admin Toolbar (admin_toolbar)   Module  8.x-1.19
          Chaos tool suite  Chaos tools (ctools)            Module  8.x-3.0-beta2   
          Other             Pathauto (pathauto)             Module  8.x-1.0-rc1
          Other             Token (token)                   Module  8.x-1.0-rc1
          Other             MTM Foundation (mtm_foundation) Theme
          Other             ZURB Foundation 6 (zurb_foundation)Theme

      Each module and theme should be added to the ``require`` section.
      Using the previous example, your ``require`` section should appear
      similar to the following:

      .. code-block:: none

          "require": {
            "drupal-composer/drupal-scaffold": "^2.0.0",
            "drupal/core": "8.3.1",
            "drupal/admin_toolbar": "1.1.9",
            "drupal/ctools": "3.0.0-beta2",
            "drupal/pathauto": "1.0.0-rc1",
            "drupal/token": "1.0.0-rc1",
            "drupal/zurb_foundation": "6.x-dev",
            "composer/installers": "^1.0"
          },

   -  *Module paths* - Requiring ``composer/installers`` allows you to
      specify, in the extras section, where composer should download
      packages of a particular type:

      .. code-block:: none

          "extra": {
              "installer-paths": {
                  "docroot/core": ["type:drupal-core"],
                  "docroot/modules/contrib/{$name}": ["type:drupal-module"],
                  "docroot/profiles/contrib/{$name}": ["type:drupal-profile"],
                  "docroot/themes/contrib/{$name}": ["type:drupal-theme"],
                  "docroot/libraries/{$name}": ["type:drupal-library"]
              }
          }

      Drupal best practice is to place contributed modules in
      ``docroot/modules/contrib``. Your current branch should already
      reflect the decision you made `before you started this
      process <#before>`__. If your modules are not currently in that
      path, you will need to modify the installer path by removing
      ``/contrib``.

   -  *Libraries* - If contrib modules require the manual addition of
      libraries (in other words, the module does not utilize a
      ``composer.json`` to download its required libraries), you may add
      them directly to your require section. For an example, see
      ``enyo/dropzone`` in both the require section as well as the
      installer-paths section of this sample template:
      https://github.com/acquia/acquia-ra-composer/blob/master/composer-templates/composer-libraries.json
   -  *Custom modules and themes* - There are two ways to handle custom
      modules and themes:

      -  Circumvent Composer entirely and directly commit your custom
         modules and themes to your repository.
      -  Create them as Composer packages, ensure that they can be
         downloaded by the Composer, and then include them as you would
         other packages.

      | The first is far simpler than the second, but if your theme or
        module is going to be used by more than one Composer-built
        website, it may be more efficient and developer-friendly to
        create your custom code as discrete Composer packages.
      | In either case, custom code should live in clearly demarcated
        custom directories:

      .. code-block:: none

          docroot/modules/custom
          docroot/themes/custom

      This allows you to delete the contributed themes and modules by
      deleting the parent contributed directory entirely, and allow
      Composer to rebuild it from scratch.

#. Delete the following directories (including both the directories'
   contents and the directories themselves):

   .. code-block:: none

        docroot/core
        docroot/modules/contrib
        docroot/themes/contrib
        docroot/vendor

#. Run the following command:

   ``composer install``

   This should install all the packages required in the
   ``composer.json`` in the proper directory, create a ``composer.lock``
   file, and rewrite ``docroot/autoload.php`` to point to the new
   location of the vendor directory (this is what ``drupal-scaffold``
   does).

#. Test your now-working website by using ``git diff`` to compare
   directories or particular files. Compare carefully! If you pinned
   your modules and core, there should be little difference in module or
   core files (except ``autoload.php``). The entire vendor directory has
   moved, and it is likely that the packages in the vendor directory are
   different as there may be a more recent version than what is on your
   current website. This should be fine as the module itself is the
   same.
   Ensure that you verify all parts of your Drupal website, noting if
   you need to run ``drush cr``, or if modules appear to be missing.
#. Continue to delete, modify the ``composer.json``, and install until
   your website is fully working.
#. | Whenever your website is ready, you should be able to commit the
     ``composer.json``, ``composer.lock``, and all generated code (if
     you are using CI, this is a different process).
   | Remember that you are committing ‘pinned’ versions of your modules.
     This is to ensure that composer is installing the exact versions
     currently running your website. Your next step, either in this
     branch or after this branch, has been tested and merged to master,
     is to change all the versioning in the require section to using the
     ‘^’ and more open versioning:

   .. code-block:: none

      "require": {
          "drupal-composer/drupal-scaffold": "^2.0.0",
          "drupal/core": "^8.3",
          "drupal/admin_toolbar": "^1.1",
          "drupal/ctools": "^3.0",
          "drupal/pathauto": "^1.0",
          "drupal/token": "^1.0",
          "drupal/zurb_foundation": "^6.x",
          "composer/installers": "^1.0"
      },

At this point, if you were to run
``composer update drupal/core --with-dependencies``, Composer will
update your website to ``Drupal 8.3.2`` since in this example, we
installed ``8.3.1``. This is what you want, but only after you have
tested the migration with pinned versions.

.. |Repository Structure| image:: https://cdn3.webdamdb.com/1280_QDJpdYIvmzj5.png?-62169955200


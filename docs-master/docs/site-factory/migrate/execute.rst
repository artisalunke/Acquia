.. include:: /common/global.rst

Executing a migration into |acquia-product:edg|
===============================================

**ADVANCED** - *Incorrectly migrating a website without properly
preparing for the attempt can involve data loss or a website outage
event.*

Configuring and using |acquia-product:edg|

-  `Setup </site-factory/setup>`__
-  `Migrate </site-factory/migrate>`__
-  `Manage </site-factory/manage>`__
-  `Workflow </site-factory/workflow>`__
-  `Extend </site-factory/extend>`__
-  `Monitor </site-factory/monitor>`__

After you have completed the preparatory work described in `Preparing a
migration into |acquia-product:edg| </site-factory/migrate>`__ and
completing the items in the `Sprint 0
checklist </site-factory/migrate/plan>`__, you are ready to start the
process of importing a website into |acquia-product:edg|.

Note

The steps used for this website migration process depend on preparation
that is described on `Preparing a migration into
|acquia-product:edg| </site-factory/migrate>`__. Failing to review and
use that page before your website migration attempt may cause the
migration to fail.

.. _requirements:

Import requirements
-------------------

-  Create one target website at a time in your |acquia-product:edg|
   environment.
-  Prepare your source website for export as described at `Preparing a
   Drupal application for
   export </acquia-cloud/create/import/prepare>`__.
-  Verify that your code, configuration, and database do not have
   hard-coded paths to files in the ``files`` directory or theme, as
   these paths will change during the `database import
   process <#copydb>`__.

.. _proc:

Procedure
---------

Use the following steps to migration your website into
|acquia-product:edg|:

#. Initialize and deploy the theme repository. Although you can place
   your website's themes in your ``sites/all/themes`` directory, Acquia
   recommends that you use a `dedicated, external theme
   repository </site-factory/theme/external#connect>`__.
   If you create an external theme repository, complete the following
   steps:

   #. Create a dedicated directory for themes, which will contain
      subdirectories for the website-specific themes. If all base themes
      have been moved into the main target repository, you can use the
      ``sites/[domain.com]/themes`` directory.
   #. Add all the files in your theme to a Git repository that has been
      newly initialized with the following commands:

      ``git init git add . git commit -m "Example message: commit all themes"``

   For more information, see `Connecting to a theme
   repository </site-factory/theme/external#connect>`__.
#. Initialize and deploy your codebase. Acquia has identified the
   following best practices for preparing and deploying your website's
   codebase to |acquia-product:edg|:

   -  The versions of Drupal core and contributed modules on your source
      and target websites must be identical.
   -  All necessary modules and themes must be reachable for your target
      website, though their exact locations may differ.
   -  Custom modules must be in the `shared codebase across all
      websites </site-factory/migrate#structure-code>`__, and not in
      website-specific ``sites/[domain]/modules`` directories.
   -  Small, custom configuration files can remain in the
      ``sites/default`` directory.
   -  | Any customizations to your website's
        ``sites/default/settings.php`` file should be moved into another
        file or a `post-settings.php
        hook </site-factory/extend/hooks/settings-php>`__, as the
        ``acsf-init`` command in |acquia-product:edg| will overwrite the
        contents of this file and any customizations will be lost.

      Note

      For more information about ``acsf-init``'s role in code deploys,
      see `Updating with the ``acsf-init``
      command </site-factory/workflow/deployments/acsf-init>`__.

   After you have prepared your source website's codebase for migration,
   follow the instructions at `Building your Drupal
   distribution </site-factory/workflow/distro>`__ to import it.

#. Create a complete and recent back up all portions of your website,
   including the database, files directory, codebase, and themes.
#. If your website is active, enable maintenance mode before starting
   your migration. This action prevents your website's users from making
   changes to the website that may be lost during the migration process.
#. Simultaneously make a local backup of your website's files directory
   while copying the files to your target website by executing the
   following commands:

   ``mkdir /tmp/local-site-archive drush -v rsync @source:%files/ /tmp/local-site-archive/files/ drush -v rsync /tmp/local-site-archive/files/ @target:%files/``

   If you already have a local backup, you can copy your files directly
   from your source website to your target websites by executing the
   following command:

   ``drush -v rsync @local-source:%files/ @target:%files/``

#. | When migrating your website from one host to another, you should
     review your database for differences between your source
     environment and target environment, paying close attention to any
     tables that may include references to file system paths.
   | You should perform any needed changes on a local copy of your
     database, instead of your currently-live source website. To make a
     local backup of your website's database, execute the following
     commands:

   ``drush -v @target sql-drop drush @source sql-dump > /tmp/local-site-archive/archive.sql``

   Important

   Do not use the ``-v`` flag on the ``sql-dump`` command as it may
   corrupt your database export.

   Perform any needed changes (such as `Secure
   Pages <https://www.drupal.org/project/securepages>`__ settings or
   file paths) to the database on your local copy of the database, and
   then upload the database to your target environment with the
   following command:

   ``drush -v @target sql-cli < /tmp/local-site-archive/archive.sql``

#. Enable and configure |acquia-product:edg| modules by performing the
   following steps:

   #. Open a command prompt window, and then run the following Drush
      command, based on your installed version of Drupal:

      -  *Drupal 8* -
         ``drush @target pm-enable acsf acsf_duplication acsf_theme acsf_variables``
      -  *Drupal 7* -
         ``drush @target pm-enable acsf acsf_duplication acsf_theme acsf_variables acsf_pingdom acsf_openid``

   #. Sign in to |acquia-product:edg| as a user with the *Platform
      Admin* role.
   #. In the top menu, click **Sites**.
   #. Identify the target website that you want to modify, and then
      point the **Log In** link for the website. Your browser will
      display the numeric website ID for the **Log In** link.
   #. Visit ``[domain].acsitefactory.com/node/[ID]``, replacing
      ``[domain]`` with your Factory's domain name, and ``[ID]`` with
      the numeric website ID you identified in the previous step.
   #. Copy the ``acsf-connect-factory`` Drush command listed under
      **ACSF connect factory drush command**, which contains the
      following parameters:

      -  ``--include`` - Full path to your ACSF module
      -  ``--site-admin-mail`` - Email address of your
         |acquia-product:edg| administrator; this value will be set as
         the email address for user 1
      -  ``--site-owner-name`` - Drupal username of the user who created
         the website from the Factory user interface; this user will be
         able to sign in through the Factory user interface
      -  ``--site-owner-mail`` - Email address of the user who created
         the website from the Factory user interface

   #. Execute the ``acsf-connect-factory`` from the command line to
      update your target website with the information that you provided.
   #. If your website uses a per-website directory for private files,
      update the *Private file system path* as described at `Setting the
      private file directory on
      |acquia-product:ac| </articles/setting-private-file-directory-acquia-cloud>`__

   After initialization, themes in dedicated repositories connected as
   described in `Initialize and deploy the theme
   repository <#themedeploy>`__ should display properly.
#. Sign in to your migrated website as an administrator, and then test
   the website to ensure that the migration was completed successfully.
#. Disable maintenance mode on your newly-imported website.

Your website is now live on |acquia-product:edg|. You can `add a custom
domain name </site-factory/manage/website/domains>`__ to complete the
migration.

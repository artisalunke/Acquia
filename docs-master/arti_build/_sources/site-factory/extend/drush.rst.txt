.. include:: /common/global.rst

Managing sites on a cluster with Drush
======================================

Although |acquia-product:edg| `provides a user
interface </site-factory/manage/website/manage>`__ to manage websites on
a cluster, website maintainers that need to perform highly customized
website maintenance activities may instead want to leverage the power of
Drush to do these functions.

The `acsf-tools <https://github.com/acquia/acsf-tools>`__ repository
(also included with |bltlink|_) provides a
set of Drush scripts for Drupal 8 websites that are tuned both for
multisite management and |acquia-product:edg| concepts.

.. |bltlink| replace:: \ |acquia-product:blt|\ 
.. _bltlink: /devtools/blt

Installation and configuration
------------------------------

To add the ``acsf-tools`` repository to your codebase, perform the steps
outlined in the ``README.md``
file `included <https://github.com/acquia/acsf-tools>`__ in the
repository. Using its procedures will allow you to download and
configure scripts for use on your |acquia-product:edg| websites.

For information about adding a repository as a dependency in Composer,
see `Using Composer with Drupal 8 sites </resource/composer>`__.


Available toolkit scripts
-------------------------

The toolkit makes the following Drush commands available for your use:

-  ``acsf-tools-content-staging-deploy`` - Performs a content staging
   deployment to a non-production environment

   .. note::  

      Staging all of your websites at once may take a long time to
      complete. For more information about content staging, see `Staging a
      Factory to a non-production
      environment </site-factory/workflow/staging>`__.

-  ``acsf-tools-dump`` - Create Drush backups for all websites in your
   Factory instance
-  ``acsf-tools-generate-aliases`` - Generate Drush aliases for all
   websites in your Factory instance

   .. important::  

      Improper placement of this file can cause performance problems when
      executing Drush commands.

-  ``acsf-tools-get-deployed-tag`` - Display the version control tag
   currently deployed on an environment
-  ``acsf-tools-info`` - Display website-specific information, such as
   ID and database name, for all websites in your Factory instance
-  ``acsf-tools-list`` - Displays the details for all websites in your
   Factory instance
-  ``acsf-tools-ml`` - Perform a Drush command against all websites in
   your Factory instance
-  ``acsf-tools-sites-backup`` - Create a backup of any or all websites
   in your Factory instance
-  ``acsf-tools-stage-domains`` - Create non-production versions of
   production environment domains

For more information about the scripts included in the toolkit,
including usage instructions, see the ``README.md``
file `included in the acsf-tools repository <https://github.com/acquia/acsf-tools>`__.

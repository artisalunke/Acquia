.. include:: /common/global.rst

Release notes - |acquia-product:edg|
====================================

.. toctree::
   :hidden:
   :glob:

   /site-factory/release-notes/2017/
   /site-factory/release-notes/2016/

Looking for the latest and greatest new features and changes to 
`Acquia Cloud Site Factory </products-services/acquia-cloud-site-factory>`__?
Read on and check back regularly to see what else we’ve done.

.. container:: message-status
   
   Be sure to install and enable the latest version of the |Connector|_ module.

.. |Connector| replace:: \ |acquia-product:edg|\  Connector
.. _Connector: https://drupal.org/project/acsf

.. |sfi| replace:: \ |acquia-product:sfi|\ 
.. _sfi: /site-factory/extend/api

Acquia Cloud Site Factory 2.76
------------------------------

*6 June 2018*

Fixed issues
~~~~~~~~~~~~~

-  Certain websites or site collections (specifically those with either no owner 
   or having a blocked user be the owner) could not be staged to non-production environments.
-  Websites duplicated using the Site Factory API had no owner.
-  Attempts to sign in to the non-production |acquia-product:sfi| failed if the |acquia-product:sfi| was not the SAML identity provider.
-  In some circumstances, two-factor authentication failed to install correctly.
-  Attempts to create a website with invalid characters in the sitename failed with an error that did not indicate the invalid characters.


Acquia Cloud Site Factory 2.75
------------------------------

*11 May 2018*

.. container:: message-status

   Acquia recommends that as part of this release you upgrade your websites to 
   use the latest version of the |Connector|_ module.

Feature
~~~~~~~

-  **Programmatically control the termination of tasks** |br|
   Using the |sfi|_, you
   can now terminate running tasks and delete tasks by using the Task
   |acquia-product:sfa| endpoint.



Known issue
~~~~~~~~~~~~

-  For Drupal 8 websites, the |acquia-product:sfi| documentation
   information will not display when embedded in an iframe.

Fixed issues
~~~~~~~~~~~~~

-  Attempts to sanitize databases failed after 10 minutes.
-  In some circumstances, the private files directory became
   inaccessible during a release.
-  Occasionally, deleting a website did not delete the symlinks between
   environments.
-  After a failed attempt to duplicate a website, |acquia-product:edg|
   did not remove public and private files.
-  |acquia-product:edg| did not preserve newline characters in the task
   logs.
-  The task logs displayed HTML-encoded versions of executed commands.
-  Attempting to restore a website failed if the restoration task was
   executed on a server that had never executed a backup process.
-  When duplicating a website, the database wipe process repeated
   multiple times.



Acquia Cloud Site Factory 2.74.1
---------------------------------

*25 April 2018*

This hotfix release of |acquia-product:edg| contains the following
update for both |acquia-product:edg| and the included Gardens
distribution:

Resolved security alert
~~~~~~~~~~~~~~~~~~~~~~~~

-  `Drupal core - Highly critical - Remote Code Execution - SA-CORE-2018-004 <https://www.drupal.org/sa-core-2018-004>`__



Acquia Cloud Site Factory 2.74
-------------------------------

*25 April 2018*

This release of |acquia-product:edg| is scheduled for release on April
25, 2018. It contains the following updates:

Feature
~~~~~~~

-  **Drush 9 support** |br|
   |acquia-product:edg| now supports the use of Drush 9 with your Drupal
   8-based websites.

Changes
~~~~~~~

-  Improved error messaging when viewing the **Staging deployment** page
   in the |acquia-product:sfi| on non-production environments.
-  Deployment attempts that do not include the |Connector|_ will now fail.

Fixed issues
~~~~~~~~~~~~~~

-  If users with the *developer* or *release engineer* roles were
   assigned additional roles that included the ability to create a
   website from backup, these users could still access backups after the
   additional role assignments were removed.
-  When staging a secondary website from a site collection using the
   |acquia-product:sfa|, the primary website from the site collection
   failed to stage.
-  In some circumstances, code release tasks and site duplication tasks
   could block each other from progressing.



Acquia Cloud Site Factory 2.73
-------------------------------

*9 April 2018*

This release of |acquia-product:edg| is scheduled for release on April
9, 2018. It contains the following updates:

Features
~~~~~~~~~~~~~~

-  **Stage only the websites that you need to your non-production environment** |br|
   You can now copy individual, selected websites down to your
   non-production environment, instead of copying all websites from your
   production factory. `Learn more </site-factory/workflow/staging>`__.
-  **Automate website updates after staging** |br|
   After copying production websites to a non-production environment,
   you can now synchronize data structures and module updates with the
   |hook|_.

.. |hook| replace:: ``post-staging-update`` hook
.. _hook: /site-factory/extend/hooks/post-staging-update

Changes
~~~~~~~

-  The following included software was updated:

   -  SimpleSAMLphp was updated to 1.15.4
   -  |acquia-product:edg| 7.x module was updated to
      `7.x-1.46 <https://www.drupal.org/project/acsf/releases/7.x-1.46>`__
   -  |acquia-product:edg| Connector 8.x module was updated to
      <`8.x-1.46 <https://www.drupal.org/project/acsf/releases/8.x-1.46>`__

-  The Gardens distribution distributed with |acquia-product:edg| was
   upgraded to Drupal 7.57.

Fixed issues
~~~~~~~~~~~~~~

-  Using the ``acsf-get-factory-creds`` Drush command with Drush 8.1.16
   displayed output results twice.
-  Attempting to use repository checkout commands failed due to changes
   to line endings.
-  Users with the *developer* or *release engineer* roles could not
   access the **Access WIP task status** |acquia-product:sfa| endpoint.


Acquia Cloud Site Factory 2.72.1
---------------------------------

*29 March 2018*

This hotfix release of |acquia-product:edg| contains the following
update for both |acquia-product:edg| and the included Gardens
distribution:

Resolved security alert
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `SA-CORE-2018-002 <https://groups.drupal.org/security/faq-2018-002>`__


Acquia Cloud Site Factory 2.72
-------------------------------

*14 March 2018*

This release of |acquia-product:edg| is scheduled for release on March
14, 2018. It contains the following updates:

Changes
~~~~~~~~~~~~~~

-  Cron jobs now execute against the preferred domain when the **All
   sites** option is selected.
-  When clearing website caches from the |acquia-product:sfi|, the
   cache-rebuild commands use the website's preferred domain name.
-  SimpleSAMLphp was updated to version 1.15.3.

Fixed issues
~~~~~~~~~~~~~~

-  |acquia-product:edg| displayed an error message that a website was
   unavailable due to a filesystem issue even after the file system
   issue was resolved.
-  When cron jobs were performed with the **Sites with custom domains
   only** option, websites in a site collection with a custom domain
   name were not included.
-  In some circumstances, |acquia-product:edg| did not detect new
   install profiles.



Acquia Cloud Site Factory 2.71
-------------------------------

*21 February 2018*

This release of |acquia-product:edg| is scheduled for release on
February 21, 2018. It contains the following updates:

Changes
~~~~~~~

-  Task logs now display additional information about callback execution
   for tasks started from the Site Factory API.
-  Callbacks for tasks started from the Site Factory API now follow
   redirect requests.
-  Websites using Drupal 8.3 and greater will install with the Update
   core module disabled.
-  Releases that remove an install profile will not display the removed
   install profile as an option for website installation.
-  The Gardens distribution distributed with |acquia-product:edg| has
   been upgraded to Drupal 7.56, and uses PHP 7.1.

Fixed issues
~~~~~~~~~~~~~~

-  The `Site
   details <https://www.demo.acquia-cc.com/api/v1#Site-details>`__ Site
   Factory API endpoint failed to return site collection information for
   a website.
-  Whenever admins scheduled website deployments for more than two days
   in advance, the deployments would fail.
-  Removing a server from an environment caused cron runs to fail for 24
   hours.



Acquia Cloud Site Factory 2.70
-------------------------------

*31 January 2018*

This release of |acquia-product:edg| is scheduled for release on January
31, 2018. It contains the following updates:

Change
~~~~~~~

-  |acquia-product:edg| no longer requires that you use a specific
   version of PHP when executing Drush commands on Drupal 7 websites.

Fixed issues
~~~~~~~~~~~~~~

-  When users attempted to view task logs to review successful tasks,
   |acquia-product:edg| did not display human-readable messages.
-  In certain circumstances, cron tasks were executed twice.
-  Attempting to clear Varnish caches on path-based domains failed.
-  Enabling the |Connector|_ module on a
   non-|acquia-product:edg| website caused Drush error messages to
   display.

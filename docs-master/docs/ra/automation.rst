.. include:: /common/global.rst

Remote Administration automation
================================

.. toctree::
   :hidden:
   :glob:

   /ra/automation/*

Acquia is in the process of rolling out security update automation to all RA subscriptions. Acquia security update automation takes into account `RA preferences </ra/preferences>`__, and has specific compatibility requirements. Automation is the fastest way to ensure that a subscription receives security updates.

Compatibility Requirements
--------------------------

Meeting the following requirements allows a website to be updated through Acquia’s automated security update process:

-  **VCS** |--| The subscription VCS must use an Acquia-hosted VCS repository. Externally-hosted repositories can be merged manually by the client from the Acquia-hosted repository. Automated security updates are pushed to the Acquia-hosted repository only. It is the responsibility of your development team to merge this updates into any external repository.

   -  `Git is the preferred VCS </acquia-cloud/develop/repository/git>`__ for automation.
   -  Subscriptions using externally hosted Git repositories are not eligible for automated security updates.

-  **Clean core and contrib** |--| The automated update process will overwrite core and contributed files, and any modifications will be lost. Modified contributed modules should either be excluded from the update process or `correctly patched </ra/patching>`__. Drupal core updates cannot be locked and all modifications must be patched or they will be lost.
-  **Stable and working production code** |--| The Remote Administration service is targeted at released, production websites on which primary development is complete. Installations running the **Welcome** tag (``tag/WELCOME``) cannot receive automated updates. It is recommended that websites under current and active, initial development have upgrades applied as part of the development process by your development team so issues may be resolved as they arise and unnecessary merge tasks can be avoided. Websites in active development may be updated provided there is code on the Production environment. Your development team will need to merge updates from the update branch into the active development branch.
-  **Composer** |--| Starting with Drupal 8.3, Drupal 8-based websites must be built using Composer. Websites using Drupal 8.4 and greater also require Drush 9 to be installed in the docroot by Composer. RA cannot guarantee the compatibility of Drush updates provided to Drupal 8.3 or greater websites, and automated security updates are not available for websites using Drupal 8.4. Premium RA customers can request a manual update if the website contains a valid ``composer.json`` file configured above the docroot. For information about how to set up Composer for your website, see `Acquia Automation: Composer builds </ra/automation/composer>`__.
-  **Drush** |--| The command ``drush pm-updatestatus`` and ``drush pm-updatecode`` must be able to run on at least one multisite with the subscription and must work on all available environments. Broken custom modules or incorrectly configured include files in the ``sites.php`` and ``settings.php`` files can prevent automated update processes from functioning.
-  **Drupal docroot** |--| Drupal must be installed inside `[reponame]/docroot <https://knowledgebase.acquia.com/article/docroot-definition>`__. Installations outside this location will prevent automated update processes from functioning. Appropriately configured symlinks using a "vendor" structure that works with Drush are also acceptable.
-  **PHP 5.6** |--| The remote administration update script relies on Drush 8 and PHP 5.6 to check for and perform updates.
-  Distributions which are not compatible with Drush updates cannot be updated using automation at this time.

.. admonition:: Note for Premium subscribers

   Acquia can help troubleshoot incompatibilities with automation and help implement fixes through tickets.

What Acquia's update automation does:
-------------------------------------

-  Regularly provides security updates without customer initiation.
-  Updates all security vulnerabilities using Drush (``drush pm-updatestatus`` and ``drush pm-updatecode``). Be aware that Drush overwrites all core and contributed module modifications.
-  Detects non-Drupal files in the docroot folder, and ensures that they are not deleted.
-  Every core and module update receives its own discrete commit. This allows for the easy reversion of a particular update if it is found to be incompatible during testing and troubleshooting. This is not a Drush feature, but a feature of Acquia’s automation.
-  In addition to security updates, Acquia will implement bug-fix updates to the following modules, *even if the modules are disabled*, to ensure that your subscription is able to take advantage of Acquia’s services:

   -  `Acquia Connector <https://www.drupal.org/project/acquia_connector>`__
   -  `Acquia Cloud Site Factory Connector <https://www.drupal.org/project/acsf>`__
   -  `Apache Solr Search <https://www.drupal.org/project/apachesolr>`__
   -  `Acquia Search for Search API <https://www.drupal.org/project/search_api_acquia>`__
   -  `Acquia Lift Connector <https://www.drupal.org/project/acquia_lift>`__
   -  `Personalize <https://www.drupal.org/project/personalize>`__
   -  `Visitor Actions <https://www.drupal.org/project/visitor_actions>`__
   -  `Acquia Purge <https://www.drupal.org/project/acquia_purge>`__

   .. note::
   
      The Remote Administration `module upgrade policy </ra/scope#major>`__ may not apply to Acquia-supplied modules, as RA may support major version updates for these modules (such as upgrading |acquia-product:anc| from 7.x-2.17 to 7.x-3.0). This ensures continued compatibility with RA services and the |acquia-product:ac| platform.

      For some Acquia module update situations, RA may create non-deployed branches with the module for your testing. For more information, `contact Acquia Support </support#contact>`__ or create an RA `work request </ra/request>`__.

-  `Implements Stage File Proxy </ra/environment#sfp>`__ to manage file display.
-  Checks and reapplies patches in your `docroot <%5Bacquia-product:kb%5Darticles/docroot-definition>`__, and includes them in all updates. For this to work, you must follow the process described in `Patching core and contributed modules </ra/patching#patching>`__. It's your responsibility to ensure that patches are in place on the update branch.
-  Informs you through a ticket that an update is ready to test. The ticket delineates all applied updates.

What Acquia's update automation does not do:
--------------------------------------------

-  Automation does not automatically do bug-fix updates other than those listed above. Bug-fixes must be requested separately (RA Premium only) from security updates. An RA Support Engineer can use automation to initiate an update which includes specific updates.
-  Update automation will not detect modifications to either core or contributed modules. All modifications must either be `locked or properly patched </ra/patching>`__.
-  Apply existing patches other than those properly specified in `/reponame/patches.make </ra/patching>`__. All other patches will be overwritten by Drush unless module locking is also properly set up.
-  Update websites built on distributions. An attempt will be made to update such websites manually.
-  Update websites built with make files or build scripts. Custom builds dependent on manually updating individual files are considered custom code and cannot be update through automation or manual updates.
-  Update websites built using Continuous Integration (CI).

Who Receives Automated Updates?
-------------------------------

All Standard and Premium RA subscriptions are eligible for automated security updates, provided the subscription is compatible with Acquia’s automation.

-  Security updates for Standard RA subscriptions must use automation.
-  Premier RA subscriptions are not required to receive updates through automation at this time. However, Acquia’s automation is much more efficient than our manual process.
-  Acquia cannot guarantee a security update delivery timeline for subscriptions which are not compatible with Acquia’s security update automation.

Update Process
--------------

The Automation process closely follows our existing `Security Update Workflow </ra/workflow>`__. For the timeline regarding initiating security updates, see `ticket timelines </ra/security#timelines%20>`__.

After a website is queued for an automated update, the script will:

-  Scan the production website for pending security updates.
-  If a security vulnerability is detected, an update will be initiated.
-  RA Preferences for the subscription will be reviewed.

   -  If RA preferences are set to **Update Code**, a branch will be deployed to the RA Environment, updated, and a ticket will be sent to your team.
   -  If RA preferences are set to **Inform Only**, a ticket will be sent listing recommended security updates. You may request an update by changing your RA preferences and responding to this ticket, asking us to initiate a new update and ticket.

-  An updated branch will be available for testing within 24-48 hours of a Security Announcement on `drupal.org <https://www.drupal.org>`__. After a branch has been deployed, progress on the ticket is dependent upon client testing through all steps of the RA security update workflow.
-  If an update branch already exists, unless a new security update is announced, you will not receive a new ticket for two weeks.

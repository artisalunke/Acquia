.. include:: /common/global.rst

Requirements for Remote Administration
======================================

To efficiently troubleshoot client websites, update modules, and implement fixes, Acquia Support Engineers require several tools and Drupal modules. The absence of any one of these elements can delay and impede the delivery of Acquia Remote Administration (RA) services.

In addition to the above, Acquia’s `security update automation </ra/automation>`__ has specific requirements. Ensuring that your website complies with these requirements will ensure the efficient delivery of security updates.

Access
------

For Acquia to have the correct access to your websites, be aware of the following:

-  Clients need to provide Acquia with administrative-level access to all systems and accounts required to perform RA tasks.
-  Acquia will perform RA services from its own premises using remote electronic access to Client’s systems and accounts.
-  Acquia requires access to one or more development/testing servers to facilitate the testing and deployment of updates in connection with this service.
-  Acquia will assist with configuring two QA/development/test servers to support the test and deployment process using a code repository and revision control.
-  Acquia will deploy an `RA environment </ra/environment>`__ for each subscription which is used solely for the deployment of automated security updates by Acquia.
-  To administer your website from the user interface, Acquia requires an administrative-level user account on your Drupal website.
-  Acquia requires full access to your Acquia VCS repository.

Drupal and Module Requirements
------------------------------

Remote Administration has the following requirements for Drupal and its associated modules.

Drupal
~~~~~~

-  Each RA subscription may contain a single installation of Drupal. Multiple installs of Drupal will not be supported.
-  The Drupal installation must be located in ``[reponame]/docroot``. A symlinked docroot (typically to a “vendor”) is supported; however, `Drush <https://github.com/drush-ops/drush>`__ is required to work on all environments without error.

Module Installation
~~~~~~~~~~~~~~~~~~~

Acquia strongly encourages the implementation of `Drupal best practices <https://www.drupal.org/best-practices>`__ regarding module installation.

-  The default location of contributed modules must be ``[reponame]/docroot/sites/all/modules``. Modules can be further sorted into ``contrib`` and ``custom`` if desired.
-  Modules which should be available to only one website within a subscription can be installed in ``[reponame]/docroot/sites/sitename/modules``. This module will be inaccessible to all other websites.
-  Duplicate modules should be avoided unless a particular website must use a specific module version. In this case, this module must be in the website-specific module folder, and should be `*locked* <%5Bacquia-product:kb%5Darticles/using-drush-lock-files-contributed-modules>`__ to avoid automated updates.

Required modules
~~~~~~~~~~~~~~~~

Acquia RA has no specific module requirements for receiving updates. However, we strongly recommend that you install and enable the following module to assist with troubleshooting updates:

-  `Syslog <https://www.drupal.org/documentation/modules/syslog>`__ core module - Enabling the Syslog module writes several log messages to Acquia-hosted log files. This method saves database overhead, especially if the `Drupal database logging module (dblog) <https://www.drupal.org/documentation/modules/dblog>`__ is disabled. For more information about logging, see `About Acquia Cloud logging </acquia-cloud/monitor/logs>`__.

Clean core and contributed modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As Remote Administration does not cover modified core or contributed
modules, Acquia recommends that you implement any customizations using
custom modules or theming files. This allows the Remote Administration
team to implement updates, while allowing the client development team to
modify custom code without any loss of modifications.

If your website requires modification of Drupal core, or of contributed
modules, refer to `Patching and locking modules </ra/patching>`__ to
ensure that your website remains compatible with Acquia security
updates.

Drush
-----

Drush is required by RA automation to apply both code updates for Drupal
7 websites and database updates for Drupal 7 and 8 websites. Acquia
Support Engineers also use Drush to troubleshoot and scan websites.

Any of the following items should not interfere with running Drush
commands (such as ``drush pm-updatestatus`` or ``drush pm-updatecode``):

-  custom themes
-  custom modules
-  customizations to the ``settings.php`` or ``sites.php`` files
-  customizations to contributed modules

Installations of Drupal 8.4.0 or greater require that Drush 9 is
installed and configured in the website's codebase.

Composer
--------

Drupal 8 core, contributed modules, and distributions are increasingly
reliant on Composer to manage dependencies. Although Drush will continue
to be used to detect insecure modules, only Composer builds and updates
will ensure that dependencies are included in any Drupal core or
contributed module update.

Installations of Drupal 8.3 or greater require a functional
``composer.json`` file that includes all code necessary to run the
website, and no package conflicts. See `Acquia Automation: Composer
builds </ra/automation/composer>`__ for a full explanation of
requirements.

.. note::

  Updates using Drush on Drupal 8.3 and greater may still succeed — these builds should not be deployed to production, as Drush does not guarantee that dependency updates were completed.

Administrative language
-----------------------

Acquia’s Remote Administration service is currently delivered only in
English. For multilingual websites, you must ensure that the
administrative backend for Drupal is in English. This will significantly
improve our efficiency in troubleshooting and updating your website.

Continuous Integration (CI)
---------------------------

Acquia RA does not currently support applying updates when a website
uses CI. We recommend you either ignore or decline automated update
branches that are created based on the code that is currently deployed
to your production environment. To receive an automated notification of
available security updates, `set your RA
preferences </ra/preferences>`__ to "Inform only".

Version control system (VCS)
----------------------------

To carefully track changes to your code, Remote Administration requires
customers to use Git. Remote Administration will not modify code without
Git in place. Acquia-hosted clients are provided a `full repository of
their choice </acquia-cloud/develop/code>`__.

For recommendations about how to use version control, see `Recommended workflow </ra/workflow>`__.

Non-Acquia Environments
-----------------------

Acquia does not provide Remote Administration services to customers who are not on the |acquia-product:ac| Platform.

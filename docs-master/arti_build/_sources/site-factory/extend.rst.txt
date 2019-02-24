.. include:: /common/global.rst

Extending |acquia-product:edg|
==============================

.. toctree::
   :hidden:
   :glob:

   /site-factory/extend/*

.. container:: internal-navigation

   **Configuring and using Acquia Cloud Site Factory**

   * :doc:`Setup </site-factory/setup>`
   * :doc:`Migrate </site-factory/migrate>`
   * :doc:`Manage </site-factory/manage>`
   * :doc:`Workflow </site-factory/workflow>`
   * Extend
   * :doc:`Monitor </site-factory/monitor>`


As with any large website development effort, one of the most important
tasks is to be able to scale your organization’s efforts without having
to increase the number of people on your development team. To help you
accomplish this goal, |acquia-product:edg| supports the use of internal
and external tools that can allow you to automate many common
development and management requirements.

For example, you can leverage the advanced API and hook systems included
with |acquia-product:edg| and the command-line power of Drush to
simplify and streamline your development processes. You can then extend
your team's efforts by using the |acquia-product:blt| toolkit and
|acquia-product:ld| distribution, which enable you to scale your website
development efforts without scaling your development team.


Advanced features of |acquia-product:edg|
-----------------------------------------

Along with the |acquia-product:sfi|, |acquia-product:edg| provides
additional tools for users who want to leverage the power of
command-line scripting to further customize their platform to meet their
needs. The following tools are available for your use:

-  |restapilink|_ –
   Create and manage websites on your platform, trigger and monitor
   scheduled jobs, create backups, and clear caches on any website
   hosted on your platform.
-  |hooks|_ –
   Simplify code deployments, and trigger the execution of custom code
   at multiple points during website installation, deployment, and
   runtime.
-  `Drush </acquia-cloud/drush>`__ – Perform administrative and
   application maintenance tasks from the command line, instead of
   having to use the Drupal administrative interface.


.. |restapilink| replace:: \ |acquia-product:edg|\  REST API 
.. _restapilink: /site-factory/extend/api

.. |hooks| replace:: \ |acquia-product:edg|\  hooks
.. _hooks: /site-factory/extend/hooks


External Acquia-supported tools
-------------------------------

In addition to the tools included with |acquia-product:edg|, the
following Acquia-supported products are designed to speed up and
standardize development at scale:

-  |bltlink|_ – Provides additional
   continuous integration (CI) support, easier website creation with
   installation profiles, multisite-aware Drush aliases, simplified
   local development environment setup, and support for automated tests
   for code regressions.
-  |ldlink|_ – Provides a packaged
   distribution of Drupal with many `commonly-used
   modules </lightning/modules>`__ included and configured to reduce
   repetitive development tasks. This is the default Drupal distribution
   used by |acquia-product:edg|-hosted websites if another custom
   distribution is not supplied for use.


.. |bltlink| replace:: \ |acquia-product:blt|\ 
.. _bltlink: /devtools/blt

.. |ldlink| replace:: \ |acquia-product:ld|\ 
.. _ldlink: /lightning

Unofficial community-supported tools
------------------------------------

There are also several community-sponsored toolkits that
|acquia-product:edg| users have found useful or helpful when working
with their websites, including the following:

.. note::  Although Acquia cannot provide the same level of support for these community projects as we do our own products, they are included on this page because we are aware that many of our customers have found the following tools to be helpful.

-  `acsf-tools toolkit </site-factory/extend/drush>`__ – Provides a
   set of Drush scripts that are tuned both for multisite management and
   |acquia-product:edg| concepts.

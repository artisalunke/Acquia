.. include:: /common/global.rst

Workflows in |acquia-product:edg|
=================================

.. toctree::
   :hidden:
   :glob:

   /site-factory/workflow/git/
   /site-factory/workflow/distro/
   /site-factory/workflow/deployments/
   /site-factory/workflow/profiles/
   /site-factory/workflow/scrub/
   /site-factory/workflow/staging/
   /site-factory/workflow/version/   

.. container:: internal-navigation

   **Configuring and using Site Factory**

   * :doc:`Setup </site-factory/setup>`
   * :doc:`Migrate </site-factory/migrate>`
   * :doc:`Manage </site-factory/manage>`
   * Workflow
   * :doc:`Extend </site-factory/extend>`
   * :doc:`Monitor </site-factory/monitor>`

When developing for |acquia-product:edg|, you should follow a continuous integration (CI) workflow that allows you to build and test locally, release your builds to your non-production environment for quality assurance testing, and then release your builds to your production environment.

As part of your development work, you will want to configure your local environment with tools to speed development, such as
|bltlink|_ and install a supported feature-rich distribution of Drupal, such as |ldlink|_; configure your Acquia environments to work with your CI workflow; and learn how to execute full deployments as well as hotfixes.

.. |ldlink| replace:: \ |acquia-product:ld|\ 
.. _ldlink: /lightning

.. |bltlink| replace:: \ |acquia-product:blt|\ 
.. _bltlink: /devtools/blt

Development and preparatory work
--------------------------------

As you prepare to start developing your platform, you should configure
your Acquia code repository to follow best version control practices.
Once configured, select a distribution that will allow you to create
feature-rich install profiles that lower the amount of time needed to
create websites on your |acquia-product:edg| platform:

-  |accessyourrepo|_
-  |bestpractices|_
-  `Build your Drupal distribution </site-factory/workflow/distro>`__
-  `Install profiles on ACSF </site-factory/workflow/profiles>`__

.. |accessyourrepo| replace:: Access your  \ |acquia-product:edg|\  repository
.. _accessyourrepo: /site-factory/workflow/git

.. |bestpractices| replace:: Best practices for Git on  \ |acquia-product:edg|\ 
.. _bestpractices: /site-factory/workflow/git/practices


After selecting a distribution and creating install profiles, you can
start releasing code to your non-production environment for testing and
preparation for production deployments.


Managing environments, deployments, and code releases
-----------------------------------------------------

A *deployment* is the process of updating all websites in a |acquia-product:edg| subscription with updates to its code or configuration. A deployment can contain customer-initiated codebase updates, |engupdates|_, or both.

To learn more, see |deployments|_ or the following pages for more detail:

-  |overview|_
-  `Steps in performing a production deployment </site-factory/workflow/deployments/steps>`__ for the commands needed to perform a manual deployment
-  `Hotfixing a deployment in progress </site-factory/workflow/hotfix>`__

.. |engupdates| replace:: updates to the  \ |acquia-product:edg|\  platform that are created by Acquia's engineering team
.. _engupdates: /site-factory/workflow/deployments

.. |deployments| replace:: Deployments in  \ |acquia-product:edg|\ 
.. _deployments: /site-factory/workflow/deployments

.. |overview| replace:: Overview of the  \ |acquia-product:edg|\  deployment process
.. _overview: /site-factory/workflow/deployments/process
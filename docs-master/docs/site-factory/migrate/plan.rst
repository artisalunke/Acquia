.. include:: /common/global.rst

Checklist for migrating your sites to |acquia-product:edg|
==========================================================

.. container:: internal-navigation

   **Configuring and using Site Factory**

   * :doc:`Setup </site-factory/setup>`
   * Migrate
   * :doc:`Manage </site-factory/manage>`
   * :doc:`Workflow </site-factory/workflow>`
   * :doc:`Extend </site-factory/extend>`
   * :doc:`Monitor </site-factory/monitor>`

As you prepare to `migrate your websites </site-factory/migrate>`__ into |acquia-product:edg|, Acquia has identified a
common list of tasks to consider as part of your initial sprint (*Sprint 0*) planning. Although the activities described
on this page are not a complete list, the following task groupings can help you to identify the work that is necessary for
a successful launch, and also identify the tools (such as |bltlink|_) that can assist you:

.. |bltlink| replace:: \ |acquia-product:blt|\
.. _bltlink: /devtools/blt

-  `Setting up development processes <#setting-up-development-processes>`__
-  `Platform infrastructure and workflow management <#platform-infrastructure-and-workflow-management>`__
-  =`Platform base architecture <#platform-base-architecture>`__
-  `Platform administration <#platform-administration>`__
-  `User roles, permissions, and accounts <#user-roles-permissions-and-accounts>`__
-  `Global and base theming <#global-and-base-theming>`__
-  `Global components <#global-components>`__
-  `Editorial and content workflows <#editorial-and-content-workflows>`__
-  `Social media <#social-media>`__
-  `Forms <#forms>`__
-  `Security <#security>`__
-  `Performance <#performance>`__


Setting up development processes
--------------------------------

.. list-table::
   :widths: 5 25 70
   :header-rows: 1 

   * - 
     - Summary
     - Description
   * - □
     - Code repository creation and access
     - Create a private Github repository to serve as the canonical repository, and provide push and pull access as needed
   * - □
     - Grant developer access to environment
     - Provide the technical team with all needed tool and account access
   * - □
     - Install |bltlink|_
     - Install the most recent release of |bltlink|_
   * - □
     - Define configuration management strategy
     - Identify a |configuration management strategy definition|_, which may include features, CMI, config split, custom modules, and scripts
   * - □
     - Implement configuration management framework
     - Technical implementation of configuration management strategy
   * - □
     - Define deployment and release strategy
     - Define |deployment workflow|_, |release strategy|_, and communication plans
   * - □
     - Implement deployment strategy
     - Technical implementation of deployment and release automation
   * - □
     - Configure local development environment and virtual machines
     - Configure a |standard local development environment|_ and virtual machines (VMs)
   * - □
     - Install and configure Acquia BLT
     - Configure |acquia-product:blt| configured for local and |acquia-product:edg| environments, including Drush aliases and testing platform updates
   * - □
     - Define development workflow
     - `Define a code workflow <https://blt.readthedocs.io/en/latest/readme/dev-workflow/>`_, including ``git flow``, a branching strategy, and code review process definitions
   * - □
     - Document developer onboarding and configuration
     - Document the development team's configuration, local environments, development processes, and tool installation
   * - □
     - Configure |acquia-product:edg| environment
     - Initial deployment of base profile to |acquia-product:edg|
   * - □
     - Define environment access and governance
     - Define roles and responsibilities on all technical environments, including the |acquia-product:sfi|, |acquia-product:edg| code repository, and Github repository

.. |configuration management strategy definition| replace:: configuration management strategy definition
.. _configuration management strategy definition: https://blt.readthedocs.io/en/latest/readme/configuration-management/

.. |deployment workflow| replace:: deployment workflow 
.. _deployment workflow: https://blt.readthedocs.io/en/latest/readme/deploy/

.. |release strategy| replace:: release strategy
.. _release strategy: https://blt.readthedocs.io/en/latest/readme/release-process/

.. |standard local development environment| replace:: standard local development environment
.. _standard local development environment: https://blt.readthedocs.io/en/latest/readme/local-development/#local-development


Platform infrastructure and workflow management
-----------------------------------------------

.. list-table::
   :widths: 5 25 70
   :header-rows: 1 

   * - 
     - Summary
     - Description
   * - □
     - Configure continuous integration
     - |Set up continuous integration|_ using a tool such as TravisCI or the Acquia Cloud pipelines feature
   * - □
     - Automate deployments
     - |Configure end-to-end automation|_ with Acquia BLT, the Acquia Cloud pipelines feature, TravisCI, and GitHub
   * - □
     - 	Install platform configuration management helper modules
     - Identify and develop needed configuration management tools
   * - □
     - Set up automated testing
     - Set up a base Behat and PHPunit configuration for |local and continuous integration testing|_

.. |Set up continuous integration| replace:: Set up continuous integration
.. _Set up continuous integration: https://blt.readthedocs.io/en/latest/readme/ci/

.. |Configure end-to-end automation| replace:: Configure end-to-end automation
.. _Configure end-to-end automation: http://blt.readthedocs.io/en/latest/readme/ci/

.. |local and continuous integration testing| replace:: local and continuous integration testing
.. _local and continuous integration testing: https://blt.readthedocs.io/en/latest/readme/testing/


Platform base architecture
--------------------------

.. list-table::
   :widths: 5 25 70
   :header-rows: 1 

   * - 
     - Summary
     - Description
   * - □
     - Evaluate features of |acquia-product:ld|
     - Determine which features of |ldlink|_ will be used by the platform
   * - □
     - Install |acquia-product:ld|
     - Install the latest version of |ldlink|_
   * - □
     - Create master website profile
     - |Create the initial master profile|_ with |acquia-product:ld| overrides
   * - □
     - Configure master profile
     - Install modules needed by all websites on your platform
   * - □
     - Follow security and performance best practices
     - Install and enable security-related modules (such as |Shield|_, |Security Kit|_, and |Fast 404|_), and configure environment-specific overrides for local and non-production environments
   * - □
     - Create testing modules for development and QA
     - Create any needed modules for environment-specific testing and quality assurance
   * - □
     - Define demo content strategy
     - Determine requirements and evaluate solutions to deploy dependent content bundled with configuration, facilitate automated testing, and demonstrate platform functionality
   * - □
     - Develop modules for demo content
     - Develop modules to provide demo content, and integrate the modules into builds and deployments
   * - □
     - Define platform overrides strategy
     - Determine the strategy for configuration management overrides; evaluate solutions available in contributed modules and custom development, and evaluate the risk of technical debt
   * - □
     - Configure roles and permissions in configuration management
     - Configure the roles and permissions to be managed by configuration management; modify features and other configuration accordingly
   * - □
     - Develop platform override solutions
     - Create custom modules to provide default configuration that builders of individual websites may override, and configure the modules to override the default configuration of contributed modules when necessary

.. |ldlink| replace:: \ |acquia-product:ld|\
.. _ldlink: /lightning

.. |Create the initial master profile| replace:: Create the initial master profile
.. _Create the initial master profile: https://blt.readthedocs.io/en/latest/readme/acsf-setup/#acsf-setup

.. |Shield| replace:: Shield
.. _Shield: http://drupal.org/project/shield

.. |Security Kit| replace:: Security Kit
.. _Security Kit: https://www.drupal.org/project/seckit

.. |Fast 404| replace:: Fast 404
.. _Fast 404: https://www.drupal.org/project/fast_404


Platform administration
-----------------------

.. list-table::
   :widths: 5 25 70
   :header-rows: 1 

   * - 
     - Summary
     - Description
   * - □
     - Define |acquia-product:edg| site groups
     - Define and create |acquia-product:edg| site groups and site collections based on your website rollout strategy
   * - □
     - Create new platform website
     - Perform the technical tasks needed to create an initial |acquia-product:edg| website using the master profile
   * - □
     - Deploy platform updates
     - Identify technical strategies and perform tasks for platform updates, such as configuring |acquia-product:edg| hooks_ and |acquia-product:blt| tasks

.. _hooks: /site-factory/extend/hooks


User roles, permissions, and accounts
-------------------------------------

.. list-table::
   :widths: 5 25 70
   :header-rows: 1 

   * -
     - Summary
     - Description
   * - □
     - Create platform administration roles
     - Create platform user roles for |Platform administrator|_, |Site Builder|_, *Content Administrator*, *Content Editor*, *Anonymous User*, and *Authenticated User*
   * - □
     - Create website administrator roles
     - Create website roles for *Site Administrator*, *Content Administrator*, *Content Editor*, *Anonymous User*, and *Authenticated User*
   * - □
     - Create user accounts on the |acquia-product:sfi|
     - Define and assign roles to users in the |sfilink|_
   * - □
     - Create platform user accounts
     - Create platform user accounts
   * - □
     - Create Drupal website users
     - Create Drupal website accounts
   * - □
     - Configure user profile management
     - Enable users to change their account passwords and email addresses
   * - □
     - Test example features and content in new website
     - Confirm example features and content display properly in a new website


.. |Platform administrator| replace:: Platform administrator
.. _Platform administrator: https://kbv2.acquia.com/site-factory/users/admin/platform-admin

.. |Site Builder| replace:: Site Builder
.. _Site Builder: /site-factory/users/admin/site-builder

.. |sfilink| replace:: \|acquia-product:sfi|\
.. _sfilink: /site-factory/users/admin


Global and base theming
-----------------------

.. list-table::
   :widths: 5 25 70
   :header-rows: 1 

   * - 
     - Summary
     - Description
   * - □
     - Define platform base theme
     - Select and implement a base theme, such as Cog_ or Bootstrap_
   * - □
     - Create custom platform subtheme
     - Create a default subtheme for the platform to extend the base theme
   * - □
     - Define and configure a platform administration theme
     - Select, configure, and implement the theme to be used in the Drupal administration area of websites on your platform
   * - □
     - Configure front-end build tools for continuous integration
     - Configure tools for continuous integration, such as Yarn_ or Gulp_
   * - □
     - Define global theme regions
     - Determine and identify all the global theme regions implied in the wireframes
   * - □
     - Define themed layout of pages
     - Define the essential layout for all pages on the website with minimal theming
   * - □
     - Provide theme assets
     - Provide assets used in wireframing necessary for theme development, such as logos, images, icon fonts, color palettes, and fonts
   * - □
     - Theme base HTML elements
     - Define the styling for base text, base headings, list types, and tables
   * - □
     - Identify external libraries for base theme
     - Identify and implement external libraries for features in your base theme, such as |Responsive Menus|_ or Modernizr_
   * - □
     - Configure platform libraries	
     - Configure platform libraries in the build and deployment process
   * - □
     - Create page layout grid with 12-column layout
     - Develop the 12-column grid for basic page layouts to match the wireframes
   * - □
     - Manage committable and non-committable packages separately
     - Create a separate ``package.json`` file that stores committable libraries in a separate folder from the non-committable build tools libraries, for downloading when the |acquia-product:blt| front-end task runs
   * - □
     - Define a style guide
     - Identify tools for developing and managing a style guide, and implement a default style guide
   * - □
     - Establish browser breakpoints
     - Identify browser breakpoints to ensure optimum display for the devices that your theming is intended to support, while remaining cost-effective to maintain
   * - □
     - Identify fonts and assets for global theme
     - Add required fonts and assets to the style guide and default theme
   * - □
     - Style major blocks
     - Create default and mobile styling for the major blocks, such as the main menu navigation block and menu links block
   * - □
     - Style the footer and its blocks
     - Create default regions and theme blocks in the footer, including footer menus
   * - □
     - Configure Browsersync for browser testing
     - Configure Browsersync_, including Gulp tasks and any needed modifications to your build and deployment process

.. _Cog: https://www.drupal.org/project/cog
.. _Bootstrap: https://www.drupal.org/project/bootstrap
.. _Yarn: https://yarnpkg.com/en/
.. _Gulp: https://gulpjs.com/
.. _Modernizr: https://www.drupal.org/project/modernizr
.. _Browsersync: https://browsersync.io/

.. |Responsive Menus| replace:: Responsive Menus
.. _Responsive Menus: https://www.drupal.org/project/responsive_menus


Global components
-----------------

.. list-table::
   :widths: 5 25 70
   :header-rows: 1 

   * - 
     - Summary
     - Description
   * - □
     - Theme header contents
     - Theme common header contents, such as the main menu, logo, and contact information
   * - □
     - Theme form elements
     - Theme common form elements, such as buttons, text areas, and check boxes


Editorial and content workflows
-------------------------------

.. list-table::
   :widths: 5 25 70
   :header-rows: 1 

   * - 
     - Summary
     - Description
   * - □
     - Develop content moderation workflows
     - Develop content moderation workflows, including the ability to save drafts and send content for approval before publication


Social media
------------

.. list-table::
   :widths: 5 25 70
   :header-rows: 1 

   * - 
     - Summary
     - Description
   * - □
     - Create social media integrations
     - Identify social media platforms to integrate with and select the appropriate icons for display


Forms
-----

.. list-table::
   :widths: 5 25 70
   :header-rows: 1 

   * - 
     - Summary
     - Description
   * - □
     - Install dependencies for forms
     - Install and configure modules, such as Webform_

.. _Webform: http://drupal.org/project/webform


Security
--------

.. list-table::
   :widths: 5 25 70
   :header-rows: 1 

   * - 
     - Summary
     - Description
   * - □
     - Verify the security of anonymous user data
     - Ensure there is no collection of anonymous user or session information
   * - □
     - Implement and enforce SSL
     - Enforce SSL both on |acquia-product:edg| and all external services that integrate with it


Performance
-----------

.. list-table::
   :widths: 5 25 70
   :header-rows: 1 

   * - 
     - Summary
     - Description
   * - □
     - Identify CDN strategy
     - Determine your content delivery network (CDN) strategy, and migrate assets to it
   * - □
     - Configure Varnish management
     - Configure cache tags and reactive purging of Varnish to improve the display of recent content while preserving website performance
   * - □
     - Enforce CSS and JavaScript best practices
     - Ensure that CSS files are aggregated and JavaScript files are minified
   * - □
     - Enforce Drupal caching best practices
     - Configure Drupal's core caching capabilities
   * - □
     - Configure Memcache
     - Determine if Memcache is appropriate for your platform, and configure cache bins if so
   * - □
     - Implement performance and scalability improvements
     - Perform page load and performance benchmarking, and implement needed improvements


Next steps
----------

After reviewing this checklist, see |nextsteps|_.

.. |nextsteps| replace:: Executing a migration into  \|acquia-product:edg|\
.. _nextsteps: /site-factory/migrate/execute

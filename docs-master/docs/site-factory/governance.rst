.. include:: /common/global.rst

Governance on |acquia-product:edg|
==================================

.. container:: message-status
   
   This page provides |acquia-product:edg|-specific information relating to our `Acquia platform governance recommendations </resources/governance>`__.

To better ensure your success with |acquia-product:edg| it is important
to implement *platform governance* practices, which can help you and
your organization ensure that your platform is architected, built, and
maintained in a sustainable manner. Platform governance is a
decision-making framework that enables your organization to assign
ownership, set priorities, and define shared guidelines, standards, and
processes for all platform users.

As you review our general, product-agnostic `governance strategy documentation </resource/governance>`__ to prepare your product implementation plans, be sure to also incorporate the |acquia-product:edg|-specific features described on this webpage.

Before you determine the configuration that is most appropriate for your
organization, familiarize yourself with the |acquia-product:edg|
platform's layers and the facets of each layer that you should consider
when developing your governance plan.

.. note::   Acquia offers workshops and customized assistance in planning your organization's governance strategy. For details, contact your Account Manager.

Platform functionality by layer
-------------------------------

When determining what needs your platform will serve, you should examine
the websites you intend to migrate to your platform to determine their
common needs. These needs can be grouped into the following categories:

-  `Platform <#platform-layer>`__ - Core functionality of your platform, on
   which functionality is built
-  `Backend functionality <#backend-functionality-layer>`__ - Features and functionality
   available for managing, creating, and interacting with content
-  `Front-end layer <#front-end-layer>`__ - Content in your websites, and its
   formatting and display

Your planning should focus on identifying common, reusable features that
will be useful to all websites on your platform, instead of identifying
one-off needs for specific websites.

You should not begin your platform development until you have defined
your profile architecture. Developing without a plan increases both cost
and the likelihood of architectural mistakes that must be undone later,
costing your organization time and money.


Platform layer
~~~~~~~~~~~~~~

The *platform layer* is the core upon which your entire platform is
built. It is important to select stable, feature-rich technologies that
enable you to extend and customize features instead of forcing you to
work around limitations later as your needs grow:

-  *Acquia Cloud Site Factory* - Provides built-in support, monitoring, and
   website management tools
-  *Drupal core* - Standard release of Drupal, containing basic features
   common to content management systems
-  *Management tools* - Applications that automate project setup,
   enforce best practices, and speed platform setup (such as |BLT link|_)
-  *Base distribution* - Distribution built on Drupal core (such as |LD|_) that provides additional tooling and speeds development

.. |BLT link| replace:: \ |acquia-product:blt|\ 
.. _BLT link: /devtools/blt

.. |LD| replace:: \ |acquia-product:ld|\ 
.. _LD: /lightning

Backend functionality layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Building on the platform layer, the *backend layer* extends the platform
with additional features and customizations. Although organizations can
have different functionality needs, the following items are common:

-  *Base theme* - Theming framework, such as Cog or Bootstrap, which can
   be overridden by website-specific themes, to customize appearance and
   retain core structure and functionality
-  *JavaScript files* - Scripts provided by modules or themes to enhance
   functionality, often provided as part of global JavaScript modules
-  *Modules* - Core set of features available to all websites, including
   common features such as search, social sharing, and ratings
-  *Content types* - Blueprints for content types, including standard
   fields and architecture
-  *User management* - Functionality and appearance of user registration
   and management
-  *Analytics* - Common forms of measuring activity and engagement
-  *User forms* - Consumer-facing forms that users may fill out and
   submit
-  *Search engine optimization (SEO) features* - platform
   characteristics that follow SEO standards and conventions, such as
   ``robots.txt``, sitemap.xml, and schema files
-  *User data protections* - A secure and compliant system for the
   collection of personally identifying information (PII) and user
   account management, including single sign on (SSO) and social media
   sign-in
-  *Workflow management* - Set of standard workflow options,
   permissions, and roles for managing content approval and publication


Front-end layer
~~~~~~~~~~~~~~~

Your *front-end layer* includes your content, its formatting, and its
layout. This layer will involve, but is not limited to, the following
criteria:

-  *Content* - Text, images, and videos
-  *Look and feel* - Items such as objects, custom fonts, text colors,
   background colors, and logos that can be configured by variables
   inside of a website’s base theme
-  *Content layouts* - The arrangement of objects and components on a
   page, and how they react to changes in screen size
-  *Advanced Cascading Style Sheets (CSS)* - Any website-specific CSS
   styling that cannot be configured using variables in the website’s
   base theme

After identifying your needs in each of the layers, you can determine
which profile configuration is right for you.


Profile configuration on |acquia-product:edg|
---------------------------------------------

After reviewing the layers of your platform, you are ready to determine
the best profile configuration for your organization. Some common
profile configurations in |acquia-product:edg| are as follows:

-  *Baseline distribution with no profiles or sub-profiles* - Changes to
   the distribution immediately affect all websites on the platform, and
   individual features can be enabled or disabled on a per-website basis
-  *Single profile for all websites* - Features of the distribution can
   be overridden globally, and subthemes of the base theme can be
   provided
-  *Multiple profiles available to websites on the platform* - Features
   of the distribution can be overridden in some profiles but not
   others, and subthemes can be provided per profile, increasing
   flexibility
-  *Multiple profiles available to websites on the platform, with
   multiple nested sub-profiles* - Features of the distribution or of
   profiles can be overridden for groups of similar sites, increasing
   both flexibility and complexity

For information about creating sub-profiles when using
|acquia-product:ld| see `Lightning sub-profiles </lightning/subprofile>`__.

Additional information
----------------------

For additional, in-depth information about creating a governance
strategy, see `Planning your governance strategy </resources/governance>`__.

.. include:: /common/global.rst

Installation profiles on |acquia-product:edg|
=============================================

|acquia-product:edg| is based on using *installation profiles* to define
base functionality for your platform. Acquia recommends that you use the
`|acquia-product:ld| </lightning>`__ Drupal distribution as a base
profile in conjunction with the tools provided in
`|acquia-product:blt| </devtools/blt>`__. |acquia-product:ld| extends
Drupal 8 to provide profile inheritance, which enables you to create
sub-profiles that allow for creating distinct groups of websites that
share baseline global functionality, but may differ in information
architecture or features. After a profile has been deployed to
|acquia-product:edg| and enabled, site builders may select it when
creating a new website.

Depending on your needs, your |acquia-product:edg| platform can contain
a single profile for use on all websites, sub-profiles for large groups
of websites, or nested sub-profiles for more tailored functionality.
When designing your profiles, you should take the following aspects of
`website governance </site-factory/governance>`__ into account:

-  *`Platform </site-factory/governance#platform>`__* – Core
   functionality of your platform, on which functionality is built
-  *`Backend functionality </site-factory/governance#backend>`__* –
   Features and functionality available for managing, creating, and
   interacting with content
-  *`Front-end layer </site-factory/governance#frontend>`__* – Content
   in your websites, and its formatting and display

Important

To avoid development missteps and wasted effort, you should not begin
development on individual websites until you have defined your
platform's profile architecture as part of your `|acquia-product:edg|
governance strategy </site-factory/governance>`__.

When designing and implementing profiles, you should consider the
following items:

-  `Architecture considerations for profiles <#arch>`__
-  `Minimum requirements for profiles <#reqs>`__
-  `Creating an installation profile <#create>`__

For instructions about enabling installation profiles on your Factory,
or selecting a profile when creating a new website, see `Managing
installation profiles in your
Factory </site-factory/manage/preferences/profiles>`__.

.. _arch:

Architecture considerations for profiles
----------------------------------------

When selecting a profile architecture for your platform, consider the
following questions from a platform—not individual website—perspective:

-  What global configuration is valid across websites sharing a profile?
-  What configurations (such as modules and permissions) should differ
   across environments?
-  What default configurations, such as theme and website name, should
   site builders or administrators be able to configure?
-  Does your development and testing process account for creating new
   websites on the profile as well as providing updates to existing
   websites that were created with older versions of the profile?

.. _reqs:

Minimum requirements for profiles
---------------------------------

To work with |acquia-product:edg|, an installation profile must meet the
following requirements:

-  Based on Drupal 8 or Drupal 7 core
-  Include the `|acquia-product:edg|
   Connector <https://www.drupal.org/project/acsf>`__ module to provide
   necessary platform management functions, such as `the ``acsf-init``
   command </site-factory/workflow/deployments/acsf-init>`__
-  Includes an admin role

Drupal 7 installation profiles

For information about creating a Drupal 7 installation profile for use
with your codebase, see `How to Write a Drupal 7 Installation
Profile <https://www.drupal.org/node/1022020>`__ on Drupal.org.

.. _create:

Creating an installation profile
--------------------------------

The method you use for creating an installation profile depends on the
tools you have selected for use in your platform:

-  *With `|acquia-product:ld| </lightning>`__ and
   `|acquia-product:blt| </devtools/blt>`__* – Create a custom
   sub-profile as described at `|acquia-product:ld|
   sub-profiles </lightning/subprofile>`__ and implement it as described
   in the `|acquia-product:blt|
   documentation <https://blt.readthedocs.io/en/latest/readme/acsf-setup/#acsf-setup>`__
-  *Without |acquia-product:ld| and |acquia-product:blt|* – Create a
   custom sub-profile with `Drupal
   Console <https://hechoendrupal.gitbooks.io/drupal-console/content/en/commands/generate-profile.html>`__

Until you have added your installation profiles to `your custom
distribution </site-factory/workflow/distro>`__ and then `enabled the
installation profiles </site-factory/manage/preferences/profiles>`__,
|acquia-product:edg| will not display the installation profiles on the
**Create a new site** page.

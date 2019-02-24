.. include:: /common/global.rst

Understanding the scope of Remote Administration
================================================

.. _in-scope:

Tasks in the scope of Remote Administration (RA) services
---------------------------------------------------------

Clients may request that Acquia perform website modification tasks that
include making minor and occasional functionality adjustments typically
needed for an operating website. The following Drupal administration
tasks typically fall in the scope of Standard Acquia RA services:

-  `Automated security updates </ra/automation>`__ for unmodified Drupal
   core as released by the `Drupal Security
   team <https://www.drupal.org/security>`__.
-  Automated security updates to contributed modules as released on
   Drupal.org. All security updates are limited to those in the same
   major version release (for example: 7.x-3.1 to 7.x-3.3).
-  `Automated updates to Acquia-developed
   modules </ra/automation#acquia-modules>`__.

.. admonition:: Acquia product support notes

   Remote Administration has limitations regarding support for the following products:
   
   - *Acquia Cloud Site Factory subscribers* |--| |acquia-product:edg| supports only `standard RA services </site-factory/manage/ra>`__.
   - *Acquia BLT users* |--| Remote Administration supports |acquia-product:blt| only in `certain configurations </devtools/blt>`__.

Premium RA also includes the following items:

-  Manual security updates where an automated security update fails or
   is not possible.
-  Contributed module bug-fix updates (on request), limited to the same
   major version release (for example: 7.x-3.1 to 7.x-3.3, but not
   7.x-2.6 to 7.x-3.3).
-  Contributed module recommendation, installation, and configuration.
-  Creating and modifying views and content types (tasks must be
   completable in less than one hour).
-  Tuning website performance using the user interface (tasks must be
   completable in less than one hour).

Site modification tasks outside this scope of services can be handled by
the Client, through `Acquia’s Professional
Services <https://www.acquia.com/customer-success/acquia-professional-services>`__
(at an additional cost), or through an Acquia partner. For any
clarification on this scope of services, please `contact Acquia
support </support#contact>`__ for further assistance.

.. _scope-and-time:

Scope and Time (Premium)
------------------------

Acquia’s Premium Remote Administration agreement provides for 10 hours
of remote administration activity per month, including any time required
to deploy security updates. Website modification tasks are limited to
those that may be accomplished in the allotted RA Service Hours. Hours
in excess of the maximum RA Services Hours may be subject to Excess
Usage fees.

Remote administration Client requests can vary considerably. The
difference between administrative or maintenance tasks and larger tasks,
such as new development or project work, is not always clear. Acquia
uses the following guidelines to determine whether any single task is in
the scope of services, from a “time required” perspective:

.. list-table::
  :header-rows: 1

  * - Estimated time to complete the task
    - How Acquia will respond
  * - An hour or less
    - Acquia will complete the task as requested.
  * - Between one and four hours
    - Acquia will estimate the time required to complete the task, and request
      Client approval to use the estimated RA hours to complete the task.
  * - Greater than four hours
    - Tasks estimated at greater than four hours are generally out of scope.
      Acquia will recommend breaking the task into multiple tasks to be handled
      over time, or Acquia will determine that the task is out of scope and
      recommend that the Client use internal or third-party resources to
      complete the task.

Limited support areas (Premium)
-------------------------------

Remote Administration offers limited support to both development (dev)
and modified contributed (contrib) modules.

-  **Dev modules**

   If a problem can be traced back to a dev module that is fixed by a
   later version, the RA team may choose to support only the later
   version. The RA team may also offer to update to the later version.

   Acquia always recommends that, whenever possible, clients use stable
   releases over dev versions of contributed modules, unless there is a
   special feature in a dev version that is not included in subsequent
   stable releases.

   Troubleshooting and customization related to dev versions of modules
   is the responsibility of the Client's development team, or something
   that can be provided by the Acquia Professional Services team.

-  **Modified contrib modules** (known Drupal.org issues only)

   If a module is patched to address a known issue resolved in a later
   version of the module, the Remote Administration team can update the
   module to the later version.

   Contributed modules with code that does not match the official
   release of the identical version are considered custom code. These
   are not covered by our RA services. For more information, see
   `Out-of-scope areas <#out-of-scope>`__.

Out-of-scope areas
------------------

Acquia RA does not support websites, subscriptions, or
`docroots <%5Bacquia-product:kb%5Darticles/docroot-definition>`__ which
do not meet our `RA Requirements </ra/requirements>`__.

Certain website maintenance activities required to properly maintain a
fully functioning website fall outside the scope of RA Services and must
be handled by the Client. The Client is responsible for coordinating
with their own internal resources, or engaging either Acquia
Professional Services at an additional cost or a third-party vendor to
perform these tasks under a separate arrangement. These tasks include,
but are not limited to:

Major version upgrades
~~~~~~~~~~~~~~~~~~~~~~

-  Acquia RA does not support the updates of modules that include
   version jumps (such as upgrading the Services module from 7.x-3.18 to
   8.x-4.0). Major version upgrades are a development effort that is not
   in the scope of Remote Administration. If such modules require
   updates, a Support Engineer will recommend a discussion with the
   Account Management team, who can discuss a Partner developer or
   Professional Services agreement.
-  Acquia RA does not support core upgrades that include major version
   jumps. This is a major development effort.

Modified code
~~~~~~~~~~~~~

-  Customizations and modifications are considered custom code, which is
   out of the scope of RA. In addition, the Acquia update automation
   uses Drush, which overwrites customizations.
-  Acquia recognizes that at times, patches to core and contributed
   modules are necessary. Ideally, such customizations and alterations
   should reside in custom modules. Where this is not possible, Acquia
   RA will only support modified or patched code entirely at its
   discretion.

General policies regarding modifications:

-  Modifications recommended by Acquia Support Engineers will be given
   limited support, but must be correctly documented and patched.
-  Modifications that are not correctly documented and patched will not
   be supported.
-  Modifications to address bugs which have a solution other than a
   patch will not be supported.

Modified core
~~~~~~~~~~~~~

-  Core code which does not match the official release of the identical
   version is considered custom code and is only supported at the
   discretion of the Acquia RA team.
-  Core modifications may be a part of various Drupal distributions, and
   as a result, security updates services and/or general RA services may
   be limited or unavailable for websites built on these distributions.

Modified contributed modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Contributed modules whose code does not match the official release of
   the identical version are considered custom code. The RA team only
   applies updates to such modules at its discretion. Updating
   customized code may require a significant development effort that can
   be handled either by your internal development resources, through a
   separately contracted Acquia Partner, or through an `Acquia
   Professional
   Services <https://www.acquia.com/products-services/professional-services>`__
   engagement. If you would like a modified module to be updated, a
   Support Engineer will recommend a discussion with the Account
   Management team, who can discuss a Partner developer or Professional
   Services agreement.

Custom modules
~~~~~~~~~~~~~~

-  Custom modules are solely the responsibility of the client. Acquia RA
   can help troubleshoot issues that may arise from custom modules, as
   well as conflicts between custom modules and core or contributed
   module updates. However, in these instances, Acquia RA does not
   modify or fix custom code. If requested, a Support Engineer will
   recommend a discussion with the Account Management team, who can
   discuss a Partner developer or Professional Services agreement.

Additional out-of-scope areas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Significant changes to the design or architecture of the website(s)
-  New website creation
-  Data migration from other websites, systems, or versions of Drupal to the website(s)
-  In-depth performance or security analysis
-  Content management, creation, or translation
-  Graphic design
-  Usability or accessibility testing
-  Site load testing unless expressly included in an Order

Acquia will not configure, diagnose, administer, or repair:

-  DNS or domain names
-  Software not directly related to running Drupal
-  Integrations (will diagnose up to the Drupal integration point)

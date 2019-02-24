.. include:: /common/global.rst

Developing with the Cloud API
=============================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/develop/api/*

|acquia-product:ac| has two additional interfaces that developers can use to extend, enhance, and customize |acquia-product:ac|:

-  **Acquia Cloud API**

   The |acquia-product:api| is a RESTful web interface that allows developers to extend, enhance, and customize |acquia-product:ac|. It includes developer workflow, site management, and provisioning capabilities.

-  **Acquia Cloud Drush commands**

   The |acquia-product:ac| Drush commands allow you to use all features of the |acquia-product:api| either on the command line or from shell scripts using the excellent Drush command-line tool.

What can the Acquia Cloud API do?
-------------------------------------

You can use the |acquia-product:api| to do many of the tasks that are needed as part of your daily application development and continuous integration process.

-  **Workflow**

   Deploy code, databases, and user-uploaded files across your Development, Staging, and Production environments. The |acquia-product:api| lets you run any branch or tag from your Git repository in any environment, just as you can do from the |acquia-product:ui|. This allows you to automate these functions, instead of having to log in to the |acquia-product:ui| and manually drag elements from one environment to another.

-  **Backups**

   Create, restore, and delete backups of your application’s databases. |acquia-product:ac| fully supports Drupal multisite installations, with as many databases per codebase as you need.

-  **Information**

   Retrieve current information about your application and its environments, including deployed code, databases, backups, and tasks.

Even better, the real magic behind the Cloud API is its integration with `Cloud Hooks </acquia-cloud/api/cloud-hooks>`__, which lets you automate nearly any action to be performed along with your workflow actions. You can do the following:

-  Perform Drupal database updates or run your test suite when new code is deployed, and roll back to a previous release if the tests fail.
-  Scrub your Production database when it is copied to Development or Staging by removing customer emails or disabling production-only modules.
-  Integrate with third-party services, for example, by performing a Blitz.io performance test, when you deploy new code.

Getting Started
---------------

To get started with the |acquia-product:api|, do the following:

#. Find your Cloud API credentials, as described in `Cloud API authentication </acquia-cloud/api/auth>`__.
#. Download the |acquia-product:ac| Drush integration, as described in `Using Drush aliases </acquia-cloud/drush/aliases>`__.
#. Use your |acquia-product:api| credentials in the Drush Cloud commands described in the `Drush Cloud command reference </acquia-cloud/api/drush-reference>`__ or using the RESTful interface over HTTP, passing the credentials in the request using ``curl``, as in the examples in the `Cloud API reference <https://cloudapi.acquia.com/>`__.

Permissions
-----------

To use the Cloud API, a user must have the *Access the Cloud API* permission. By default, all users with the *Team Lead*, *Senior Developer*, and *Administrator* roles have this permission, while users with only the *Developer* role do not. Administrators can modify the permissions of existing roles, or add new custom roles with the desired permissions. For more information, see `Working with roles and permissions: Editing a role </acquia-cloud/teams/roles#edit>`__.

Users who have the *Access the Cloud API* permission can use the |acquia-product:api| to take most of the actions enabled by the |acquia-product:ui|, and are not constrained by any other permissions in their use of the |acquia-product:api|

API rate limits
---------------

To prevent a single user from adversely affecting shared resources, there is a rate limit for |acquia-product:api| calls. The rate limit varies by |acquia-product:ac| subscription level and is measured by authenticated calls per hour per |acquia-product:api| user (defined by the `private key </acquia-cloud/api/auth>`__ used with the call).

+-----------------------+------------+
| Subscription          | Rate limit |
+=======================+============+
| |acquia-product:ace|  | 1000       |
+-----------------------+------------+
| |acquia-product:acs|  | 360        |
+-----------------------+------------+
| |acquia-product:acfs| | 10         |
+-----------------------+------------+

Realm
-----

The ``realm`` is a required parameter in calls to the |acquia-product:api|. This is the |acquia-product:ac| realm the environment is running in. The value is ``prod`` for |acquia-product:ace| and ``devcloud`` for |acquia-product:acs|. The realm corresponds to the element before ``hosting.acquia.com`` in the environment's server names.

Additional resources
--------------------

-  `Cloud API reference <https://cloudapi.acquia.com/>`__
-  `Drush Cloud command reference </acquia-cloud/api/drush-reference>`__
-  `Cloud API authentication </acquia-cloud/api/auth>`__

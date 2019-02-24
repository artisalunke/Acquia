.. include:: /common/global.rst

About |acquia-product:ac| permissions
=====================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/teams/permissions/*

A *permission* grants a user the ability to perform specific operations
in an |acquia-product:ac| organization or application. Permissions are
grouped into roles. Roles are then assigned to team members. All the
team members who have the same roles have the same permissions.

Acquia defines over 40 separate, grouped permissions, listed in the
following `Permissions list <#list>`__ table. You can also view all the
available permissions by opening the **Roles** page for an organization
and viewing a role, as described in `Working with roles and permissions:
Viewing a role's permissions </acquia-cloud/teams/roles#view>`__.

Many permissions enable you to distinguish between team members who can
work on an application's production environment and team members who can
only work on the non-production (Dev and Stage) environments. For
example, the *Senior developer* role includes the permissions to pull
and deploy code in production and non-production environments, while the
*Developer* role grants permission to pull and deploy code only in
non-production environments. **Since |acquia-product:acfs| applications
do not have production environments, those permissions do not apply to
those applications.**

Permissions in |acquia-product:ac| do not control actions users take on
your Drupal website, such as:

-  Creating content
-  Enabling and configuring Drupal modules
-  Adding or removing Drupal users

Use the Drupal permissions administration to control access to Drupal
functions.

.. admonition:: Note for |acquia-product:edg| subscribers

   |acquia-product:edg| customers must use the `|acquia-product:edg|
   domains
   functionality </site-factory/manage/website/domains/point/cname-site>`__
   to add additional domains to their subscriptions. Domains added using
   the |acquia-product:ac| user interface will not work, and may be deleted
   by automated processes.

.. _list:

Permissions list
----------------

.. list-table::
   :widths: 20 40 20 10 10
   :header-rows: 1 
   :stub-columns: 1

   * - Category
     - Permission
     - |acquia-product:ace|
     - |acquia-product:acs|
     - |acquia-product:acfs|
   * - Administration
     - Access the Cloud API |br|
       Using the Cloud API, authorized users can bypass all other permissions by using command-line tools.
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Activate an Acquia subscription add-on
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Add or remove a user of a team |br|
       This includes the ability to assign a user's role, allowing a user with this permission give themselves any role, including Team Lead.
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Edit Remote administration
     - |yes|
     - |yes|
     - |no|
   * - 
     - View Remote administration
     - |yes|
     - |yes|
     - |no|
   * - Cron
     - Modify cron tasks for non-production environments
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Modify cron tasks for the production environment
     - |yes|
     - |yes|
     - |no|
   * - Databases
     - Add a database
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Create database backups for non-production environments
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Create database backups for the production environment
     - |yes|
     - |yes|
     - |no|
   * - 
     - Download database backups for non-production environments
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Download database backups for the production environment
     - |yes|
     - |yes|
     - |no|
   * - 
     - Remove a database
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Restore database backups for non-production environments
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Restore database backups for the production environment
     - |yes|
     - |yes|
     - |no|
   * - 
     - View database connection details (username, password, or hostname)
     - |yes|
     - |yes|
     - |yes|
   * - Domains
     - Add or remove SSL certificates for the non-production environments
     - |yes|
     - |yes|
     - |no|
   * - 
     - Add or remove SSL certificates for the production environments
     - |yes|
     - |yes|
     - |no|
   * - 
     - Add or remove domains for non-production environments
     - |yes|
     - |yes|
     - |no|
   * - 
     - Add or remove domains for the production environment
     - |yes|
     - |yes|
     - |no|
   * - Insight
     - Block Insight sites |br|
       Users with this permission can prevent applications from submitting data to Acquia Insight.
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Manage Insight alerts |br|
       Users with this permission can set Insight alerts to Ignore.
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Revoke Insight environment
     - |yes|
     - |yes|
     - |yes|
   * - Logs
     - Download logs for non-production environments
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Download logs for the production environment
     - |yes|
     - |yes|
     - |no|
   * - Pipelines
     - Execute pipelines
     - |yes|
     - |yes|
     - |no|
   * - SSH keys
     - Add SSH key to git repository
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Add SSH key to non-production environments
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Add SSH key to the production environment
     - |yes|
     - |yes|
     - |no|
   * - 
     - Manage SSH keys
     - |yes|
     - |yes|
     - |no|
   * - Search
     - Edit the search schema on a subscription
     - |yes|
     - |yes|
     - |no|
   * - 
     - Increase the search index limit on a subscription
     - |yes|
     - |yes|
     - |no|
   * - Server administration
     - Configure server
     - |no|
     - |yes|
     - |no|
   * - 
     - Reboot server
     - |no|
     - |yes|
     - |no|
   * - 
     - Resize server
     - |no|
     - |yes|
     - |no|
   * - 
     - Suspend server
     - |no|
     - |yes|
     - |no|
   * - Support
     - Create a support ticket
     - |yes|
     - |yes|
     - |no|
   * - 
     - Include as a collaborator on all tickets by default |br|
       *(Permission is assignable to no more than 20 users. Administrators have priority for inclusion.)*
     - |yes|
     - |yes|
     - |no|
   * - 
     - View and edit any support tickets for a subscription
     - |yes|
     - |yes|
     - |no|
   * - Workflow
     - Add an environment
     - |yes|
     - |no|
     - |no|
   * - 
     - Clear Varnish cache for non-production environments
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Clear Varnish cache for the production environment
     - |yes|
     - |yes|
     - |no|
   * - 
     - Configure non-production environments
     - |yes|
     - |yes|
     - |no|
   * - 
     - Configure production environment
     - |yes|
     - |yes|
     - |no|
   * - 
     - Delete an environment
     - |yes|
     - |no|
     - |no|
   * - 
     - Deploy code, files, or databases to the production environment
     - |yes|
     - |yes|
     - |no|
   * - 
     - Manage environment variables on a non-production environment
     - |yes|
     - |no|
     - |no|
   * - 
     - Manage environment variables on a non-production environment
     - |yes|
     - |no|
     - |no|
   * - 
     - Move files from non-production environments
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Move files from production environments
     - |yes|
     - |yes|
     - |no|
   * - 
     - Move files to non-production environments
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Move files to the production environment
     - |yes|
     - |yes|
     - |no|
   * - 
     - Pull and deploy code, files, or databases to non-production environments |br|
       Also grants the ability to enable or disable live development.
     - |yes|
     - |yes|
     - |yes|
   * - 
     - Pull files or databases from the production environment
     - |yes|
     - |yes|
     - |no|
   * - 
     - View environment variables on a non-production environment
     - |yes|
     - |no|
     - |no|
   * - 
     - View environment variables on a non-production environment
     - |yes|
     - |no|
     - |no|

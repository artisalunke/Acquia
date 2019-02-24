.. include:: /common/global.rst

Configuring your Acquia Cloud teams and permissions
===================================================

Each |acquia-product:edg| PaaS subscription includes an
|acquia-product:ac| subscription, which you can use to access your
*Prod* and *Test* |acquia-product:edg| environments.

As part of your |acquia-product:ac| subscription, for those users who
have accounts that allow them access to the |acquia-product:ac|
interface, you can assign different
`permissions </acquia-cloud/teams/permissions>`__ to them and group them
into teams of user accounts with similar permission sets.

If you use the permissions feature on |acquia-product:ac|, we encourage
you to enable or use only the following permissions depending on your
users' needs:

-  **Administration - Add or remove a user to a team**
-  **Domains - Add or remove SSL Certificates**
-  **Insight - Manage Insight alerts**
-  **Insight - Manage Insight site groups**
-  **Logs - Download logs for non-production environments**
-  **Logs - Download logs for the production environment**
-  **Search - Increase the search index limit on a subscription**
-  **Search - Edit the search schema on a subscription**
-  **SSH keys - Add SSH key to git repository**
-  **SSH keys - Add SSH key to non-production environments**
-  **SSH keys - Add SSH key to the production environment**
-  **Support - Create a support ticket**
-  **Support - View and edit any support tickets for a subscription**
-  **Support - Include as a collaborator on all tickets by default.**
-  **Workflow - Clear varnish cache for non-production environments**
-  **Workflow - Clear varnish cache for the production environment**

.. important::  

   Either using or allowing other user accounts to use the other available
   permissions in |acquia-product:ac| may interfere with your ability to
   manage your code in your environments' Factory interfaces.

For more information about |acquia-product:ac| teams and permissions,
see 
`Managing users, teams, roles, and permissions </acquia-cloud/teams>`__.

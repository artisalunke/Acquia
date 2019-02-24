.. include:: /common/global.rst

Viewing information about Drupal modules
========================================

.. container:: internal-navigation

   **Using Acquia Insight**

   * :doc:`Intro </acquia-cloud/insight>`
   * :doc:`Using </acquia-cloud/insight/using>`
   * :doc:`Alerts </acquia-cloud/insight/alerts>`
   * Modules
   * :doc:`Connector </acquia-cloud/insight/install>`
   * :doc:`Configure </acquia-cloud/insight/config>`

The **Insight > Modules** page in |cloud-ui|_ the provides information about all of the Drupal modules that you have installed in an
environment.

To view the Modules page, complete the following steps:

#. Sign in to the |cloud-ui|_.
#. Select your organization, application, and environment, and then, in
   the left menu, click **Insight**.
#. On the **Insight** page, under **Modules**, click **View**.
#. Click the column name to sort by that column, or use a filter to
   narrow the list.

|Insight modules page|

This page contains several filters to help you find what you need:

-  **Type** - The type of module: **All**, **Core**, **Contrib**, or
   **Custom**.
-  **Version** - The type of update available: **All**, **Update
   available**, **Security fixes available**, **Bug fixes available**.
   In the list, it will show the module version currently in use.
-  **Status** - Current module status: **All**, **Enabled\ **, or**
   Disabled**. In the list, **Enabled** modules have a green check mark
   under **Status**.

Modules that have available security updates or bug fixes can put your
application at risk and affect your overall Insight score. To filter the
module list to display only these modules, select the **Updates
available** check box.

You can also filter the modules list by core, contributed, or custom,
and by enabled or disabled modules.

.. |Insight modules page| image:: https://cdn3.webdamdb.com/1280_krqWWHX9117.png?1527027772
   :alt: Insight modules page

.. |cloud-ui| replace:: \ |acquia-product:ui|\ 
.. _cloud-ui: https://cloud.acquia.com

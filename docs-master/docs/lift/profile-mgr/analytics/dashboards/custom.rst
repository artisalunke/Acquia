.. include:: /common/global.rst

Custom reports in |acquia-product:lpm|
======================================

.. toctree::
   :hidden:
   :glob:

   /lift/profile-mgr/analytics/dashboards/custom/*

.. container:: message-status

   This feature is available only to |acquia-product:lplpo| or 
   |acquia-product:lplp| subscribers. To upgrade your |acquia-product:cha| 
   subscription to this level, contact your Account Manager.

.. container:: internal-navigation

   **Using reports dashboards in Profile Manager**

   * :doc:`Intro </lift/profile-mgr/analytics/dashboards>`
   * :doc:`Overview </lift/profile-mgr/analytics/dashboards/operational>`
   * :doc:`Details </lift/profile-mgr/analytics/dashboards/details>`
   * :doc:`Config </lift/profile-mgr/analytics/dashboards/config>`
   * Custom
   * :doc:`Fields </lift/profile-mgr/analytics/dashboards/custom/fields>`

Custom report authoring allows you to create analytics on-demand using a
Business Intelligence (BI) tool in the |acquia-product:lpm| user
interface. Unlike pre-existing reports, custom reports search your
website's data warehouse in real-time based on criteria that you
specify.

|Example of a custom report|

Custom reports include the following features:

-  **Dimensions** - Groups or *buckets* of data, such as an *Event Name*
-  **Measures** - Information about that bucket of data, such as *Event
   Count* for a total number of events
-  **Filters** - Conditions to limit the data returned in the search,
   such as *Events from the past 30 days*
-  **Visualizations** - Charts or graphs with a visual representation of
   your search

For a video walkthrough of custom reporting functionality from Acquia's
engineering team, see `Acquia Lift: Custom report
authoring <https://www.youtube.com/watch?v=XK_J2wcGETc>`__ on YouTube.

Managing permissions for custom reports
---------------------------------------

To enable access for a member of your team, perform the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface with an account with
   **Administrator** permissions.
#. In the top menu, click **Admin**.
#. Click the **Manage Permissions** link on the left side of the page
#. Click the name of the security group you wish to grant access to the
   custom report functionality
#. Scroll down to the **Linked Security Resources** section.
#. Click the **Select a resource** select box, and then select the
   appropriate permissions:

   -  *Analytics tab* - Provides access to reports
   -  *Explore Data* - Allows for report creation
   -  *Author reports* - Allows for reports to be saved

   .. note::  

      The permissions are additive in scope, and rely on one other.

      For example, failing to provide the *Analytics tab* permission to
      users who have the *Explore Data* permission will prevent those users
      from creating reports, as they do not have report access. Likewise,
      *Author reports* without *Explore Data* will prevent users from
      saving reports (as they cannot be created).

#. Click **Add**.
#. Click **Save** to save your changes.

For additional information about updating and managing permissions in
|acquia-product:cha|, see `Managing permissions in
Lift Profile Manager </lift/profile-mgr/admin/permissions>`__

Next steps
----------

After ensuring you have access to the custom reporting feature, explore
the following pages to build, modify, and maintain your custom reports:

-  Learn what `fields are available for
   use </lift/profile-mgr/analytics/dashboards/custom/fields>`__ in your
   reports
-  `Create and
   modify </lift/profile-mgr/analytics/dashboards/custom/build>`__ your
   reports
-  `Download, edit, or
   delete </lift/profile-mgr/analytics/dashboards/custom/manage>`__ your
   reports

.. |Example of a custom report| image:: https://cdn2.webdamdb.com/1280_oZSEIM9dTAN5.png?1526475736
   :width: 700px
   :height: 310px

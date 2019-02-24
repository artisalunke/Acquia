.. include:: /common/global.rst

Auditing |acquia-product:edg| events
====================================

To help you track development, maintenance, and usage information
regarding your websites, |acquia-product:edg| includes the Audit log,
which contains this information in a single location, which can be
filtered to display specific items.

Viewing the Audit log
---------------------

To display the Audit log, complete the following steps:

#. Sign in to the |acquia-product:edg| interface as a user with the
   *Platform admin* role.
#. In the admin menu, click **Administration**.
#. Click the **Audit log** link.

|Audit log overview webpage|

The Audit log page displays the following information about audited
actions in a table:

-  **ID** - Internal identification number for the action
-  **Message** - Descriptive message of the action that was taken
-  **Scope** - The feature affected by the action, from the following
   list:

   -  **both**
   -  **centralized role management**
   -  **factory**
   -  **require HTTP authentication**
   -  **site actions**
   -  **sites**
   -  **vcs_info**

-  **Context** - The website or site group (if applicable) for the
   action
-  **User** - The user or internal account associated with the action
-  **Time** - The date and time that the action was started

Filtering the displayed results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the Audit log page displays all of the audited actions for
the Factory and its websites. To better enable you to find information
that relates to your interest, you can limit the displayed information
using the following filter lists on the webpage:

-  **Scope**
-  **Context**
-  **User**
-  **Source** - The starting point for the action, from the following
   values:

   -  **Factory UI**
   -  **REST API**
   -  **Drush**

For example, if you wanted to display only those actions that relate to
a specific website, in the **Context** list, select the website in which
you are interested. The Audit log page will refresh, and the displayed
table will display only those actions that relate specifically to that
website.

.. _examine:

Examining audited items
-----------------------

To view additional information about a specific item, click the ID
number from the action's **ID** column. |acquia-product:edg| will
display additional details about the action, including the following:

-  **Before** - Data from the entity before a change (could be ``NULL``
   if there is no data)
-  **After** - Data from the entity after a change (could be ``NULL`` if
   there is no data)
-  **Source** - The starting point of the action

|Audit log item detail|

Tracked events
--------------

The following list contains several of the |acquia-product:edg| user and
system events which you can examine in the Audit log:

-  Creating, duplicating, or deleting a website
-  Adding or removing a domain from a website or site collection
-  Signing in to |acquia-product:edg|
-  Signing in to a website
-  Clearing a website's caches
-  Creating, downloading, or deleting a website archive
-  Exporting a website
-  Restoring a website from a backup
-  Transferring a website's ownership
-  Creating a site collection
-  Adding or removing a website from a site collection
-  Setting a website as the primary website in a site collection
-  Refreshing the theme repository
-  Starting the update process for the Factory, websites, or both
-  Adding, changing, or removing a Git theme repository
-  Enabling or disabling website-specific features, such as requiring
   HTTP authentication or enabling centralized role management
-  Changing website-specific settings, such as HTTP authentication
   variables
-  Assigning a specific hosted website role to a centralized Factory
   user
-  Creating, updating, or deleting a website variable
-  Creating, updating, or deleting a site group
-  Configuring the default (global) or per-website Terms of Service
   notice
-  Staging websites from production to non-production environments

.. |Audit log overview webpage| image:: https://cdn4.webdamdb.com/1280_2iEgtKqlSb45.png?1526476140
   :width: 1280px
   :height: 314px
.. |Audit log item detail| image:: https://cdn2.webdamdb.com/1280_ABVG81sjVb84.png?1526475618
   :width: 1280px
   :height: 640px

.. include:: /common/global.rst

Using |acquia-product:ais| to optimize your application
=======================================================

.. container:: internal-navigation

   **Using Acquia Insight**

   * :doc:`Intro </acquia-cloud/insight>`
   * Using
   * :doc:`Alerts </acquia-cloud/insight/alerts>`
   * :doc:`Modules </acquia-cloud/insight/code>`
   * :doc:`Connector </acquia-cloud/insight/install>`
   * :doc:`Configure </acquia-cloud/insight/config>`

Before you can use |acquia-product:ais|, you must `install and enable
the Acquia connector </acquia-cloud/insight/install>`__ in order to
connect your Drupal application to the |acquia-product:ais| service.
This connection provides access to your application's logging and
configuration, which |acquia-product:ais| then reads and evaluates as it
looks for alert conditions.

.. _start:

Getting started with |acquia-product:ais|
-----------------------------------------

#. Start using |acquia-product:ais| by signing in to the
   |cloud-ui|.
#. Select your organization, application, and environment.
#. In the left menu, click **Insight**.

   -  *If you have a single website* - you will be redirected to the
      |acquia-product:ais| page for that installation.
   -  *If you have a multisite installation* - your initial
      |acquia-product:ais| page is an overview of all of your
      environments, in a single, `easy-to-read chart <#multisite>`__. To
      view information for a specific installation, click the link in
      the **Origin URL** column.

      |Insight multisite list|

#. The **Insight** page for an environment displays the following
   information:

   -  The environment's current Insight Summary score.
   -  **Alert categories** with |acquia-product:ais| scores and alerts
      for Performance, Security, and Best Practices.
   -  A link to the `Modules page </acquia-cloud/insight/code>`__, which
      provides information about available updates for Drupal core and
      contributed modules.
   -  **Score history** - a chart showing how this environment's Insight
      score has changed over time.

.. _multisite:

The multisite chart
~~~~~~~~~~~~~~~~~~~

The multisite application list contains the following information:

-  **Origin URL** - The website's origin URL
-  **Last Updated** - The last time this application's score was updated
-  Scores for **Performance**, **Security**, **Best Practices**, and
   overall **Insight score**. These scores may also have a yellow
   triangle warning, or a red circle warning icon next to the scores,
   depending on the alert thresholds your application has set
-  Customers with websites not hosted on |acquia-product:ac| may click
   the **Rename** icon in the upper right corner to rename their
   environment
-  Use the **Display score settings** gear icon to change your
   application's alert thresholds.

.. _rating:

The |acquia-product:ais| score
------------------------------

|acquia-product:ais| inspects each of the environments that you've
connected to Acquia and rates them based on their performance, security,
and adherence to Acquia's identified best practices for Drupal
applications. |acquia-product:ais| displays an alert for each of the
items that it examines and creates an overall rating for the environment
based on the types of alerts it encountered. For more information, see
`Understanding the Insight score and
alerts </acquia-cloud/insight/alerts>`__.

.. |Insight multisite list| image:: https://cdn2.webdamdb.com/1280_Aw94EbZpSlo7.png?1527111375
   :alt: Insight multisite list
   
.. |cloud-ui| replace:: \ |acquia-product:ui|\ 
.. _cloud-ui: https://cloud.acquia.com
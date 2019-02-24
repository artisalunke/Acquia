.. include:: /common/global.rst

Using Stack Metrics to monitor platform health
==============================================

.. container:: message-status

   This feature is available to |acquia-product:ac|, |acquia-product:ace|, and 
   |acquia-product:edg| subscribers.


.. container:: internal-navigation

   **Using Stack Metrics graphs**

   * Intro
   * :doc:`Load </acquia-cloud/monitor/stackmetrics/load-balancing>`
   * :doc:`App </acquia-cloud/monitor/stackmetrics/application>`
   * :doc:`Database </acquia-cloud/monitor/stackmetrics/databases>`
   * :doc:`File </acquia-cloud/monitor/stackmetrics/file-system>`
   * :doc:`Metrics </acquia-cloud/monitor/stackmetrics/additional>`

The |acquia-product:ac| Stack Metrics feature provides real-time and
historical information about an application's performance, health, and
resource use.

Certain Stack Metrics graphs, such as CPU and Memory, are designed to
show the average reported value over a given period to prevent transient
spikes in utilization from inaccurately skewing data points. As a
result, instances may be utilizing higher CPU/memory than shown on the
graphs for short periods of time. While short-lived spikes usually do
not impact application performance, prolonged or frequent spikes can,
and if sustained, these spikes will appear in your graphs.

Stack Metrics graphs may differ slightly from those provided by Acquia
for diagnostic purposes as a result of differning granularity on our
internal monitoring services.

To use Stack Metrics, complete the following steps:

#. Sign in to the |cloud-ui|_.
#. Select your application and environment.
#. In the left menu, click **Stack Metrics**.

You can also use the list preceding the metrics charts to select a time
period to review. Available timeframes span from the **last hour** to
the **last 6 months**, or set a :ref:`Custom Range <custom-time>`.
Clicking a new timeframe in the list refreshes the charts based on your
selection.

These metrics reflect server-wide activity unless noted otherwise.

.. admonition:: Upsizing your servers

    If your application has problems that may be remedied by a server upsize
    while you troubleshoot the issue, see the following pages for how to
    resize your servers to meet your application's needs:

-  |acquia-product:acs| - `Managing Acquia Cloud
   servers </acquia-cloud/manage/servers>`__
-  |acquia-product:ace| - `Using a Cloud Service Management
   plan </acquia-cloud/csm>`__

.. _available:

Available graphs
----------------

You can view information about your website components on the Stack
Metrics page. Click the link for detailed information about the graphs
for each component, and troubleshooting suggestions:

-  `Load
   balancing </acquia-cloud/monitor/stackmetrics/load-balancing>`__ -
   Data metrics specific to your website's load balancers
-  `Application </acquia-cloud/monitor/stackmetrics/application>`__ -
   Data metrics specific to your website's application tier
-  `Databases </acquia-cloud/monitor/stackmetrics/databases>`__ - Data
   metrics specific to your website's databases and database servers
-  `File system </acquia-cloud/monitor/stackmetrics/file-system>`__ -
   Data metrics specific to your website's file system servers
-  `Additional
   metrics </acquia-cloud/monitor/stackmetrics/additional>`__ -
   Additional useful data metrics

.. _summary:

Summary graph
~~~~~~~~~~~~~

In addition to the previous graphs, |acquia-product:acs| customers have
a summary graph that gives a view of overall server health. These
statistics include the most recent values for:

-  CPU percentage (%) used
-  Memory percentage (%) used
-  Storage percentage (%) used

|Stack Metrics summary graph|

.. _custom-time:

Setting a customized time frame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To set a customized time span:

#. Click the time span.
#. Click **Custom Range**.
#. Select the date and time for the beginning and ending of your custom
   range.
#. Click **Apply**.

|Customize your graph time interval|

.. |Stack Metrics summary graph| image:: https://cdn2.webdamdb.com/1280_cWOvtVCugG30.png?1527179248
   :alt: Stack metrics summary graph
.. |Customize your graph time interval| image:: https://cdn4.webdamdb.com/1280_EVOpHrDvXCA3.png?1527027455
   :alt: Customize your graph time interval:

.. |cloud-ui| replace:: \ |acquia-product:ui|\
.. _cloud-ui: https://cloud.acquia.com

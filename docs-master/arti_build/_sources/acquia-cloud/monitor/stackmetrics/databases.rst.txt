.. include:: /common/global.rst

StackMetrics - Databases
========================

.. container:: internal-navigation

  **Using Stack Metrics graphs**

  * :doc:`Intro </acquia-cloud/monitor/stackmetrics>`
  * :doc:`Load </acquia-cloud/monitor/stackmetrics/load-balancing>`
  * :doc:`App </acquia-cloud/monitor/stackmetrics/application>`
  * Database
  * :doc:`File </acquia-cloud/monitor/stackmetrics/file-system>`
  * :doc:`Metrics </acquia-cloud/monitor/stackmetrics/additional>`

This set of graphs is responsible for monitoring requests to your
database, which stores your website’s content, user information, and
most website settings.

.. _metrics:

Database metrics
----------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Graph
     - Description
   * - `CPU and memory usage <#cpu>`__
     - CPU usage and memory usage for the environment’s database servers, as a percentage of the total available — This graph is not available for |acquia-product:acs| subscriptions, which are single-server
   * - `Storage % used <#disk>`__
     - File system storage for files and database, as a percentage of your available storage
   * - `Storage used <#disk>`__	
     - Line chart of the amount of storage used on your database servers, as compared to the total amount of available storage
   * - `MySQL slow queries <#slow>`__
     - The number of MySQL queries that take more than one second.

Troubleshooting
---------------

Use the information in this section to help you troubleshoot
database-related issues with your |acquia-product:ac| application.

-  **CPU and memory usage**
   These metrics can be used to determine how close your database
   instances are to capacity, and they are often impacted by traffic
   levels, cron activity, and both the frequency and the complexity of
   queries to your application’s databases.
   Although Acquia monitors for platform impairment, database instances
   are often able to continue responding to queries even when CPU and
   memory are at or near capacity. If you notice that your database tier
   is routinely hitting CPU or memory capacity, take the following steps
   to reduce resource utilization or to diagnose the root cause:

   -  If the CPU or memory spikes are associated with traffic,
      increasing your application’s external (Varnish) caching settings
      (including implementing or optimizing Drupal caching) can
      significantly reduce CPU and memory consumption.
   -  CPU and memory spikes can also be associated with frequent or
      resource-intensive cron jobs. Reducing the frequency or complexity
      of cron tasks can immediately reduce CPU and memory consumption.
   -  `Utilize an Application Performance Monitoring
      service </acquia-cloud/monitor/apm>`__ (such as New Relic) to
      identify if the spikes in CPU and memory are associated with
      specific complex or slow queries on your website. Reducing the
      complexity or frequency of queries sent by pages or features (such
      as Views) can often reduce application CPU and memory utilization,
      especially if those pages are popular destinations for your
      visitors.

   If it is determined that additional CPU or memory are required for
   your applications to remain performant, you can either `manually
   increase your server size </acquia-cloud/manage/servers>`__, or you
   can `contact Acquia Support </support#contact>`__ to determine what
   options are available.
-  **Storage % used** and **Storage used**  At 100% utilized
   storage, your applications will cease to operate normally. Acquia
   recommends that you remain under 90% storage utilization at all
   times, while also monitoring the rate that your instances are filling
   up. At 95% full, Acquia will perform an emergency proactive upsize
   for |acquia-product:ace| customers. However, if you want to schedule
   an upsize before your instances reach capacity, `contact Acquia
   Support </support#contact>`__.
-  **MySQL slow queries**
   At lower frequencies, these queries will not have a measurable impact
   on website performance. If, however, queries take significantly
   longer than one second to complete or if they happen in rapid
   succession, the queries can quickly stack up during periods of high
   traffic, causing uncached page requests to load more slowly. Use an
   `application performance monitoring
   service </acquia-cloud/monitor/apm>`__ (such as New Relic) or
   `analyze your slow query logs </acquia-cloud/monitor/slow-query>`__
   to determine the source of these queries, and to also determine if
   optimizations can be made to the code or features which trigger them
   to reduce their time to completion.

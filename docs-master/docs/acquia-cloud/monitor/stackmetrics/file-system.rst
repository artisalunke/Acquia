.. include:: /common/global.rst

StackMetrics - File System
==========================

.. container:: internal-navigation

  **Using Stack Metrics graphs**

  * :doc:`Intro </acquia-cloud/monitor/stackmetrics>`
  * :doc:`Load </acquia-cloud/monitor/stackmetrics/load-balancing>`
  * :doc:`App </acquia-cloud/monitor/stackmetrics/application>`
  * :doc:`Database </acquia-cloud/monitor/stackmetrics/databases>`
  * File
  * :doc:`Metrics </acquia-cloud/monitor/stackmetrics/additional>`

This table displays information about how your environment stores and
handles requests for media files uploaded to your application by website
visitors, administrators, and developers.

.. _metrics:

File System metrics
-------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Graph
     - Description
   * - `CPU and memory usage <#cpu>`__
     - CPU usage and memory usage for the environment’s servers, as a percentage of the total available. This graph is not available for |acquia-product:acs| subscriptions, which are single-server
   * - `Storage % used <#storage>`__
     - Storage for your application’s file system, as a percentage of your available storage capacity
   * - `Storage used <#storage>`__
     - Line chart of the amount of storage used by your application’s file system, as compared to the total amount of available storage

.. _trouble:

Troubleshooting
---------------

Use the information in this section to help you troubleshoot file
system-related issues with your |acquia-product:ac| application.

-  **CPU and memory usage**
   The metrics in this graph can be used to determine how close to
   capacity your file system instances are, and are often impacted by
   traffic levels, the number of files associated with your application
   (especially in cases where there are too many files in a single
   directory), the size of the files associated with your application,
   or the frequency of read/write/delete activity on your file system.
   Although Acquia monitors for hardware impairment, file system
   instances are often able to continue handing file requests even when
   CPU and memory resources are at or near capacity. If you notice that
   your file system tier is routinely hitting CPU or memory capacity,
   you can take the following steps to reduce resource utilization or
   diagnose the root cause:

   -  If the CPU or memory spikes are associated with traffic,
      increasing your application’s external (Varnish) caching settings,
      including implementing or optimizing Drupal caching. This action
      can significantly reduce CPU and memory consumption.
   -  CPU and memory spikes may also be associated with activities that
      involve large numbers of files, or files sized greater than 100MB.
      This includes instances where files are being read from, deleted
      from, or written to directories that contain more than 1,000
      files.
   -  `Utilize an Application Performance Monitoring
      service </acquia-cloud/monitor/apm>`__ (such as New Relic) to
      identify if the spikes in CPU or memory are associated with
      specific page requests or modules that invoke large numbers of
      files, or files that are sized greater than 100MB.

-  **Storage % used** and **Storage used**
   At 100% storage used, your applications will cease to operate
   normally. Acquia recommends that customers remain under 90% storage
   utilization at all times, and that they should monitor the rate that
   their instances are filling up. At 95% usage, Acquia will perform an
   emergency proactive upsize for |acquia-product:ace| customers.
   However, if you want to schedule an upsize before your instances
   reach capacity, `contact Acquia Support </support#contact>`__.

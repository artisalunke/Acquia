.. include:: /common/global.rst

StackMetrics - Additional metrics
=================================


.. container:: internal-navigation

  **Using Stack Metrics graphs**

  * :doc:`Intro </acquia-cloud/monitor/stackmetrics>`
  * :doc:`Load </acquia-cloud/monitor/stackmetrics/load-balancing>`
  * :doc:`App </acquia-cloud/monitor/stackmetrics/application>`
  * :doc:`Database </acquia-cloud/monitor/stackmetrics/databases>`
  * :doc:`File </acquia-cloud/monitor/stackmetrics/file-system>`
  * Metrics
  
This graph includes global metrics that do not fit specifically into one
of the other report sections.

.. _metrics:

Additional metrics
------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Graph
     - Description
   * - **Out of memory errors**
     - Number of times your cluster recorded a PHP Out of Memory error



Troubleshooting
---------------

Use the information in this section to help you troubleshoot load
general issues with your |acquia-product:ac| application.

-  **"Out of memory" errors**
   These errors occur when a process in your stack attempts to utilize
   more memory than the server has available. Often, that specific
   process will fail, but subsequent requests — and any processes
   running at the same time — will operate normally. In those
   circumstances, it can be difficult to identify the root cause. In
   some cases, however, frequent or recurring out-of-memory events could
   indicate that there is either an issue with the application, or a
   certain tier of the stack is too close-to-capacity to safely handle
   the activity taking place on it — for example, page requests, cron
   jobs, or even normal background operations. Random occurrences of
   this error are not uncommon and should not be a cause for concern.
   Repeat occurrences (more than a few times per day) can indicate that
   there is a problem with your application or the health of your stack.
   If these types of errors occur frequently on your cluster, the most
   common solution is a hardware upsize. Acquia Support may also be able
   to assist with diagnostics.

.. include:: /common/global.rst

Monitoring |acquia-product:edg|
===============================

.. toctree::
   :hidden:
   :glob:

   /site-factory/monitor/tasklog/
   /site-factory/monitor/auditlog/

.. container:: internal-navigation

   **Configuring and using Site Factory**

   * :doc:`Setup </site-factory/setup>`
   * :doc:`Migrate </site-factory/migrate>`
   * :doc:`Manage </site-factory/manage>`
   * :doc:`Workflow </site-factory/workflow>`
   * :doc:`Extend </site-factory/extend>`
   * Monitor

As you develop and maintain your |acquia-product:edg| websites, you will
want to monitor both the backend performance of your platform and its
code, and the actions taken by your users. |acquia-product:edg| offers
monitoring and logging tools to help you accomplish these tasks.

.. _monitor:

Monitoring services
-------------------

The following services enable you to assess the performance of different
aspects of your websites, from hardware to code:

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Service
     - Description
   * - |aislink|_
     - Evaluates your websites' configuration for performance, security, and search engine optimization best practices using the |anclink|_ module, included with |ldlink|_. You can either connect all of your |acquia-product:edg| websites to |acquia-product:ais|, or only a representative subset.
   * - |stacklink|_
     - Provides real-time and historical information about your hardware performance, health, and resource use. Returned information includes Varnish hit rates, total requests received, file system usage, CPU usage, slow MySQL queries, and out-of-memory (OOM) errors.
   * - `New Relic Application Performance Monitoring (APM) </acquia-cloud/monitor/apm>`__
     - Provides real-time and historical performance monitoring of your PHP-based application's performance. For additional configuration information for |acquia-product:edg| users, see `Using New Relic monitoring in a multisite environment </acquia-cloud/monitor/apm/multisite>`__.


.. |aislink| replace:: \ |acquia-product:ais|\ 
.. _aislink: /acquia-cloud/insight

.. |anclink| replace:: \ |acquia-product:anc|\ 
.. _anclink: https://www.drupal.org/project/acquia_connector

.. |ldlink| replace:: \ |acquia-product:ld|\ 
.. _ldlink: /lightning

.. |stacklink| replace:: \ |acquia-product:ac|\  Stack Metrics
.. _stacklink: /acquia-cloud/monitor/stackmetrics

Available logging
-----------------

Acquia provides several types of logging that enable you to review
actions taken by your users, changes made to your codebase, and look for
problems with your application's execution and performance:

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Log
     - Description
   * - |aclogs|_
     - Provides information about the execution of Apache, PHP, Drupal, and Varnish on a per-server basis. You can `stream these logs in real time </acquia-cloud/monitor/logstream>`__ or view them from the command line. Customers with both an `Elite subscription </guide/site-factory>`__ and an `Acquia Technical Account Manager <https://www.acquia.com/products-services/acquia-technical-account-manager>`__  are eligible to `forward these logs to a remote destination </acquia-cloud/monitor/logs/forwarding>`__ for additional custom processing and alerting.
   * - |actasklogs|_
     - Provides information regarding recent hosting tasks in the |acquia-product:ac| interface, such as code commits and Varnish cache clears.
   * - |acquia-product:edg| logs
     - Users with the `Release engineer </site-factory/users/admin/release-engineer>`__ or `Developer </site-factory/users/admin/developer>`__ roles can access the following |acquia-product:edg|-specific log files:
     
       * `Audit logs </site-factory/monitor/auditlog>`__ - Provides information about recent actions performed by users of your Factory, filterable to individual websites or users on your platform
       * `Task logs </site-factory/monitor/tasklog>`__ - Provides information about background tasks for website management and domain management, and user-initiated tasks (such as code deploys and website installations). These logs are also known as *Work Pool* logs or *Work In Progress (wip)* logs. To modify the settings for data retention on successful or failed tasks, see Configuring task log settings.

.. |aclogs| replace:: \ |acquia-product:ac|\  logs
.. _aclogs: /acquia-cloud/monitor/logs

.. |actasklogs| replace:: \ |acquia-product:ac|\  task logs
.. _actasklogs: /acquia-cloud/monitor/tasks
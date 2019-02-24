.. include:: /common/global.rst

Downloading a slow query log
============================

You can download your website's MySQL slow query logs from the
|acquia-product:ui| **Cloud > Logs** page. By analyzing the slow query
log, you can identify database-related issues that may be impairing your
website's performance. Slow queries are database queries that took
longer than one second.

To download the MySQL slow query log for an environment, complete the
following steps:

#. `Sign in <https://cloud.acquia.com/>`__ to the |acquia-product:ui|
   and select your application and environment.
#. In the left menu, click **Logs**, and then click **Download Logs**.

   |Click Download Logs|

#. In the **MySQL slow query log** line, click **Download**.

   |image1|

|acquia-product:ac| generates the slow query log. The slow query log
includes data generated since the last time the MySQL log was rotated,
which occurs daily. It should begin downloading as soon as it is
generated, with a file name of the form:
``slow_query_log_[sitename]_[timestamp:1349352001].sql``

A slow query log is generated on demand; unlike other logs on the Acquia
platform, slow query logs are not retained and can be accessed only by
using the **Download** button.

You can examine the slow query log using tools like Percona Tools
`pt-query-digest <http://www.percona.com/doc/percona-toolkit/2.1/pt-query-digest.html>`__
and the MySQL EXPLAIN statement. For more information, see `Tools for
parsing a slow query
log <%5Bacquia-product:kb%5Darticles/tools-parsing-slow-query-log>`__.

For another approach to identifying resource consumption issues and
bottlenecks, consider `using an application monitoring
tool </acquia-cloud/monitor/apm>`__, such as New Relic.

.. _related:

Related topics
--------------

-  `Tools for parsing a slow query
   log </articles/tools-parsing-slow-query-log>`__
-  `About |acquia-product:ac| logging </acquia-cloud/monitor/logs>`__
-  `Improving application performance </acquia-cloud/performance>`__

.. |Click Download Logs| image:: https://cdn3.webdamdb.com/1280_MsD7gHjQB9e1.png?1526475711

.. |image1| image:: https://cdn4.webdamdb.com/1280_IXBrQU7tOJg1.png?1526475702


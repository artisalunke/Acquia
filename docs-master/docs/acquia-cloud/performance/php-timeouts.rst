.. include:: /common/global.rst

Troubleshooting PHP timeouts
============================

A PHP timeout occurs when a Drupal or PHP request takes longer than five
minutes to produce output, terminates, and produces an HTTP 500 error.
Most web browsers, depending on the client, don't wait longer than two
minutes before discontinuing a request and displaying an error.

Long-running processes consume server resources. If there are too many
processes running, it impairs the performance of your application. The
|acquia-product:ac| web stack accommodates requests that require extra
time to complete, but does not to allow a process to run indefinitely.

The following are potential causes of PHP timeouts:

-  A ``cron.php`` request that runs too long
-  Complex database queries on large quantities of data; for example,
   multiple JOINs on large database tables
-  Extended database table locks; for example, explicit table locks or
   structural changes on large tables
-  Drupal Views that produce complex database queries on large databases
-  Calls to slow or unresponsive external service providers using RPC
   calls, the cURL library, ``file_get_contents($url)``, or similar
   methods
-  Processing very large database result sets in PHP code
-  File operations that involve very large files or directories
-  PHP bugs; for example, infinite loops or infinite recursions
-  Calls to the ``sleep()`` function for extended lengths of time; for
   example, as an exponential back-off throttle

Some potential solutions for PHP timeout issues include:

-  Use Drush cron instead of ``cron.php``. See `Using scheduled jobs to
   maintain your application </acquia-cloud/manage/cron>`__.
-  Enable Drupal's block cache and views cache. All standard caching
   techniques are also recommended.
-  Set the call timeout to external services to less than 30 seconds, in
   case the call becomes unresponsive.
-  Optimize your database queries to examine as few rows and tables as
   possible to produce the same result.
-  Profile your PHP code to find the functions that take extended
   amounts of time to complete.
-  Use cron jobs for long-running tasks. Consider moving long-running
   tasks into cron and caching the results.

.. _find:

Finding problematic pages
-------------------------

To find problematic pages, do the following:

-  `Use an application performance monitor
   tool </acquia-cloud/monitor/apm>`__ (such as New Relic) to monitor
   applications in production and troubleshoot potential performance
   issues.
-  Examine your application's Apache logs, which include a
   ``request_time`` field that indicates how many microseconds it takes
   to deliver each page of your application. Examine the Drupal request
   logs and look for requests with a long ``php_time`` or ``queue_wait``
   value. You can stream the Drupal request log in real time or download
   the Drupal request log from the |acquia-product:ui| **Logs** page.
   See `About |acquia-product:ac|
   logging </acquia-cloud/monitor/logs>`__ and `Streaming log entries in
   real time </acquia-cloud/monitor/logstream>`__.
-  To view page delivery performance details, use the Drupal Performance
   logging features in the `Devel
   module <http://drupal.org/project/devel>`__. Only use Devel for
   applications in non-production environments.

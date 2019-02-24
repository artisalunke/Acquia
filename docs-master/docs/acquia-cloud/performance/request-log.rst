.. include:: /common/global.rst

Analyzing the Drupal request log
================================

The Drupal request log reports information that can be very valuable in
identifying and resolving performance issues on your site. The log is
located at
``/var/log/sites/[site].[env]/logs/[server]/drupal-requests.log``. You
can stream the Drupal request log in real time or download the Drupal
request log on the |acquia-product:ui| **Logs** page for an environment.
See `About |acquia-product:ac| logs </acquia-cloud/monitor/logs>`__ and
`Streaming log entries in real
time </acquia-cloud/monitor/logstream>`__.

Log entries on the Drupal request log are written at the end of the
request and look like this:

``[21/Apr/2016:21:50:20 +0000] mysite.devcloud.acquia-sites.com GET /info.php query= uid=0 php_pid=5 php_time=0.000 queue_wait=0.000 request_id="abcdef123456"``

A log entry includes the following:

-  date
-  site domain
-  HTTP request method
-  URL requested
-  ``uid`` - The Drupal uid that made the request (more specifically,
   the global ``$user->uid`` when the request completes).
-  ``php_pid`` - The Unix ``processid`` that ran the request.
-  ``php_time`` - The time spent in PHP processing the request, in
   milliseconds.
-  ``queue_wait`` - The time this PHP request spent waiting for a PHP
   process to execute it, in seconds. When requests are being queued for
   a long time, it indicates that there are not enough PHP processes
   available for the application. Currently, digits after the decimal
   point are not significant and should be ignored.
-  ``request_id`` - An HTTP request ID assigned by |acquia-product:ac|.
   See `Using HTTP request IDs </acquia-cloud/develop/requestid>`__ for
   details.

.. _related:

Related topics
--------------

-  `About Acquia Cloud logging </acquia-cloud/monitor/logs>`__
-  `Troubleshooting PHP
   timeouts </acquia-cloud/performance/php-timeouts>`__
-  `Searching the error logs to troubleshoot
   problems <%5Bacquia-product:kb%5Darticles/searching-error-logs-troubleshoot-problems>`__

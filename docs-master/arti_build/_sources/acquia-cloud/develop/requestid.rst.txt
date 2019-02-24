.. include:: /common/global.rst

Using HTTP request IDs
======================

Every web request received by |acquia-product:ac| is assigned a unique
request ID, which is set in the HTTP header ``X-Request-ID``. The HTTP
request ID can help you diagnose problems by correlating log entries for
a given web request across multiple log sources. Even on a busy website,
the HTTP Request ID in the log files makes it very easy to correlate
various log entries with each other. Having the HTTP Request ID in the
PHP error log is particularly useful, because it enables you to identify
the specific page request that generated the PHP error, making it much
easier to reproduce and ultimately fix the bug causing it.

The HTTP Request ID is recorded in all logs directly related to the
request, including the Apache access log, Drupal request log, Varnish
request log, and even the PHP error log. All of these log files include
the HTTP request ID with the ``request_id=""`` syntax.

The unique HTTP request ID is assigned when the request first arrives at
|acquia-product:ac|, and is preserved from that point onward.
Alternatively, you can provide your own ``X-Request-ID`` header and
|acquia-product:ac| will use it instead. An HTTP request ID is 20 to 200
characters long and can include the characters a-z (lowercase), A-Z
(uppercase), 0-9, + (plus sign), / (slash mark), = (equal sign), or -
(minus sign).

Web requests can access the HTTP request ID using the
``HTTP_X_REQUEST_ID`` environment variable. In PHP, that is
``$_ENV['HTTP_X_REQUEST_ID']``. For more information, see `Using
environment variables in Drupal code and Drush
commands </acquia-cloud/develop/env-variable>`__.

.. _related:

Related topics
--------------

-  `Analyzing the Drupal request
   log </acquia-cloud/performance/request-log>`__
-  `Using environment variables in Drupal code and Drush
   commands </acquia-cloud/develop/env-variable>`__
-  `About Acquia Cloud logging </acquia-cloud/monitor/logs>`__

.. include:: /common/global.rst

Using logs
==========

Log messages can be very helpful with identifying and fixing problems on
your application. They can also be used to analyze trends in traffic.
Each log serves a different purpose, and you should use different tools
and techniques to gather useful data from them.

.. _levels:

Understanding errors, warnings, and notices
-------------------------------------------

Logs report entries with three levels of seriousness: *errors*,
*warnings*, and *notices*. It's important to know what are the most
common causes of log entries and how to resolve them.

You can find more information about using logs in `Introduction to
troubleshooting with log
files <%5Bacquia-product:kb%5Darticles/introduction-troubleshooting-log-files>`__.

.. _php:

PHP error log levels
--------------------

By default, an |acquia-product:ac| production environment does not log
Notice, Strict, or Deprecated entries in the PHP error log. Although
these log entries can be helpful during development to identify code
that needs to be tested and updated, these types of entries can slow
down production environments, by logging and debugging a large amount of
potentially unneeded information. On non-production environments,
however, all PHP errors are logged, including Notice, Strict, or
Deprecated entries.

To change this default behavior and log all PHP messages in the PHP
error log for your production environment, add the following code to
your ``settings.php`` file after the ``Acquia Require`` line:

.. code-block:: php

   <?php
   error_reporting(E_ALL);
   ?>

.. _slow:

Troubleshooting slow queries
----------------------------

Slow queries in MySQL are frequently the root cause of slowness in
Drupal applications. Most often, slow queries are generated either by
complex Views or custom code that require MySQL to process a large
volume of data.

While it's not ideal to have slow queries on your application, they are
not uncommon on many large or complex applications. When they are
infrequent or less severe, they will likely go unnoticed for a long
period of time. However, if they become more frequent, or get slower
over time, they may reach a point where they begin to stack up on each
other, causing sudden performance issues and potentially taking the
application offline for brief periods of time.

You can see trends in `slow
queries </acquia-cloud/monitor/stackmetrics/databases>`__ on the `Stack
Metrics </acquia-cloud/monitor/stackmetrics>`__ page. This can be useful
for monitoring trends over time, but you will need to take additional
steps to analyze this data further by downloading and analyzing the slow
query log. For more information, see `Downloading a slow query
log </acquia-cloud/monitor/slow-query>`__ and `Tools for parsing a slow
query
log <%5Bacquia-product:kb%5Darticles/tools-parsing-slow-query-log>`__.

.. _404:

Avoiding 404 errors
-------------------

While 404 errors are not uncommon in an application’s logs, if left
unaddressed, they can have a severe impact on performance over time. In
many cases, you can take simple steps to avoid this issue. For more
information, see `Avoiding 404 error messages in your
logs <%5Bacquia-product:kb%5Darticles/avoiding-404-error-messages-your-logs>`__.

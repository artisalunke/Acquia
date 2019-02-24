.. include:: /common/global.rst

PHP error logs
==============

The *PHP error log* records any issues that occur during the PHP
processing portion of a page load. Issues reported here are usually
caused by an application’s code, configuration, or content. The log
records issues with requests from both browsers and the command line,
unlike the `FPM error log </acquia-cloud/monitor/logs/fpm-error>`__,
which records server-level issues with the management of PHP processes
from web requests only.

Custom PHP scripts that execute separately from Drupal must include the
`Acquia require line </acquia-cloud/code/require-line>`__, which sets
the logging location, in order for errors to be logged to the PHP error
log.

For a list of the log files handled by |acquia-product:ac|, including
accessing these log files, log file retention, and their locations, see
|aboutlogging|_. You
can also review information about how to `streaming PHP error log
entries in real time </acquia-cloud/monitor/logstream>`__ from your
browser.

.. |aboutlogging| replace:: About \ |acquia-product:ac|\  logging
.. _aboutlogging: /acquia-cloud/monitor/logs

.. admonition:: Note for log streaming users

   Acquia’s log streaming feature displays the name of the server
   responding to a request at the beginning of each line — however, this
   information does not appear in the log file itself.

.. _example:

Parsing the log file
--------------------

The following line is a representative example of the data written into
your website's PHP error log:

.. code-block:: none

   [04-Jan-2017 14:29:27 America/New_York] PHP Fatal error:  Allowed memory 
   size of 367001600 bytes exhausted (tried to allocate 352591872 bytes) in 
   /full/path/to/module/notification.php on line 504 
   request_id="v-0000zzzz-d2b4-0000-b3a4-129zzzzd8266"

Each of the items in the PHP error log is noted in the following table,
along with its description:

.. list-table::
   :widths: 10 30 60
   :header-rows: 1 

   * - Position
     - Data
     - Description
   * - 0
     - ``[04-Jan-2017 14:29:27 America/New_York]``
     - The date and time of the request.
   * - 1
     - ``PHP Fatal error``
     - Type of message, indicating severity.
   * - 2
     - ``Allowed memory size of 367001600 bytes exhausted (tried to allocate 
       352591872 bytes) in /full/path/to/module/notification.php on line 504``
     - Full text of error message
   * - 3
     - ``request_id="v-0000zzzz-d2b4-0000-b3a4-129zzzzd8266"``
     - A unique ID attached to this request by the load balancer, which appears 
       in several |acquia-product:ac| log files — for more information, see 
       `Using HTTP request IDs </acquia-cloud/develop/requestid>`__

.. include:: /common/global.rst

Drupal request log
==================

The *Drupal request log* contains a list of requests that Apache has
sent to Drupal for processing and display.

For a list of the log files handled by |acquia-product:ac|, including
accessing these log files, log file retention, and their locations, see
|aboutlogging|_. You
can also review information about how to `streaming Apache log entries
in real time </acquia-cloud/monitor/logstream>`__ from your browser.

.. |aboutlogging| replace:: About \ |acquia-product:ac|\  logging
.. _aboutlogging: /acquia-cloud/monitor/logs

.. _example:

Parsing the log file
--------------------

The following line is a representative example of the data written into
your website's Drupal request log:

.. code-block:: none

   [03/Feb/2017:00:14:36 +0000] www.example.com POST /dashboard 
   http_code=302 query= uid=154496 php_pid=30961 php_time=0.203 queue_wait=0 
   request_id="v-0000zzzz-e9a5-11e6-98b5-0aeea9eaf9af"

Each of the items in the Drupal request log is noted in the following
table, along with its description:

Contents
--------

+-----------------------+-----------------------+-----------------------+
| Position              | Data                  | Description           |
+=======================+=======================+=======================+
| 0                     | ``[03/Feb/2017:00:14: | Date and time of the  |
|                       | 36 +0000]``           | request               |
+-----------------------+-----------------------+-----------------------+
| 1                     | ``www.example.com``   | Domain name of the    |
|                       |                       | request               |
+-----------------------+-----------------------+-----------------------+
| 2                     | ``POST``              | The HTTP method of    |
|                       |                       | the request, usually  |
|                       |                       | ``GET`` or ``POST``   |
|                       |                       | —``POST`` requests    |
|                       |                       | are form submissions  |
+-----------------------+-----------------------+-----------------------+
| 3                     | ``/dashboard``        | The path to the       |
|                       |                       | requested resource    |
+-----------------------+-----------------------+-----------------------+
| 4                     | ``http_code=302``     | The HTTP status code  |
|                       |                       | returned by this      |
|                       |                       | request               |
+-----------------------+-----------------------+-----------------------+
| 5                     | ``query=``            | The querystring,      |
|                       |                       | which is the portion  |
|                       |                       | of the                |
|                       |                       | ``request_uri`` after |
|                       |                       | the question mark.    |
+-----------------------+-----------------------+-----------------------+
| 6                     | ``uid=154496``        | The Drupal user ID    |
|                       |                       | initiating the        |
|                       |                       | request — ``0`` means |
|                       |                       | an anonymous user     |
+-----------------------+-----------------------+-----------------------+
| 7                     | ``php_pid=30961``     | The PHP process ID    |
|                       |                       | (``pid``) for this    |
|                       |                       | request               |
+-----------------------+-----------------------+-----------------------+
| 8                     | ``php_time=0.203``    | Time, in seconds,     |
|                       |                       | needed to process     |
|                       |                       | this request          |
+-----------------------+-----------------------+-----------------------+
| 9                     | ``queue_wait=0``      | The number of seconds |
|                       |                       | this request had to   |
|                       |                       | wait for a PHP        |
|                       |                       | process to become     |
|                       |                       | available to handle   |
|                       |                       | it                    |
+-----------------------+-----------------------+-----------------------+
| 10                    | ``request_id="v-bf1b9 | A unique ID attached  |
|                       | 6bc-e9a5-11e6-98b5-0a | to this request by    |
|                       | eea9eaf9af"``         | the load balancer,    |
|                       |                       | which appears in      |
|                       |                       | several               |
|                       |                       | |acquia-product:ac|   |
|                       |                       | log files — for more  |
|                       |                       | information, see      |
|                       |                       | `Using HTTP request   |
|                       |                       | IDs </acquia-cloud/de |
|                       |                       | velop/requestid>`__   |
+-----------------------+-----------------------+-----------------------+

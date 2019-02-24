.. include:: /common/global.rst

Drupal watchdog log
===================

The *Drupal watchdog log* records Drupal-related actions on your
application. The watchdog log is recorded on your server if you have
enabled the ``syslog`` module.

For a list of the log files handled by |acquia-product:ac|, including
accessing these log files, log file retention, and their locations, see
|aboutlogging|_. You
can also review information about how to `streaming Drupal watchdog log
entries in real time </acquia-cloud/monitor/logstream>`__ from your
browser.

.. |aboutlogging| replace:: About \ |acquia-product:ac|\  logging
.. _aboutlogging: /acquia-cloud/monitor/logs

.. _example:

Parsing the log file
--------------------

The following line is a representative example of the data written into
your website's Drupal watchdog log:

.. code-block:: none

   Aug 18 21:22:01 10.0.0.1 alphabeta: https://www.example.com|1503091321|
   custom_module|151.0.0.1|https://example.com/documents||0||Warning: Invalid 
   argument supplied for foreach() in views_join->build_join 
   request_id="v-00000000-845b-0000-8178-22000ab832c9"

Each of the items in the Drupal watchdog is noted in the following
table, along with its description:

+-----------------------+-----------------------+-----------------------+
| Position              | Data                  | Description           |
+=======================+=======================+=======================+
| 0                     | ``Aug 18 21:22:01``   | The date and time of  |
|                       |                       | the request           |
+-----------------------+-----------------------+-----------------------+
| 1                     | ``10.0.0.1``          | The internal IP       |
|                       |                       | address of the server |
|                       |                       | handling this request |
+-----------------------+-----------------------+-----------------------+
| 2                     | ``alphabeta``         | The internal Acquia   |
|                       |                       | site name this        |
|                       |                       | request is for        |
+-----------------------+-----------------------+-----------------------+
| 3                     | ``http://www.example. | The domain this       |
|                       | com``                 | request was for       |
+-----------------------+-----------------------+-----------------------+
| 4                     | ``1503091321``        | The Unix timestamp of |
|                       |                       | the request           |
+-----------------------+-----------------------+-----------------------+
| 5                     | ``custom_module``     | The name of the       |
|                       |                       | module issuing this   |
|                       |                       | message               |
+-----------------------+-----------------------+-----------------------+
| 6                     | ``151.0.0.1``         | The originating IP    |
|                       |                       | address of this       |
|                       |                       | request               |
+-----------------------+-----------------------+-----------------------+
| 7                     | ``https://example.com | The full URL of the   |
|                       | /documents``          | requested page.       |
+-----------------------+-----------------------+-----------------------+
| 8                     | *(blank)*             | The referrer for this |
|                       |                       | request (the example  |
|                       |                       | line is blank for     |
|                       |                       | this value)           |
+-----------------------+-----------------------+-----------------------+
| 9                     | ``0``                 | The Drupal user ID    |
|                       |                       | initiating the        |
|                       |                       | request — ``0`` means |
|                       |                       | an anonymous user     |
+-----------------------+-----------------------+-----------------------+
| 10                    | *(blank)*             | A relevant link, if   |
|                       |                       | one was passed to the |
|                       |                       | logging function      |
+-----------------------+-----------------------+-----------------------+
| 11                    | ``Warning: Invalid ar | Message               |
|                       | gument supplied for f |                       |
|                       | oreach() in views_joi |                       |
|                       | n->build_join``       |                       |
+-----------------------+-----------------------+-----------------------+
| 12                    | ``request_id="v-00000 | A unique ID attached  |
|                       | 000-845b-0000-8178-22 | to this request by    |
|                       | 000ab832c9"``         | the load balancer,    |
|                       |                       | which appears in      |
|                       |                       | several               |
|                       |                       | |acquia-product:ac|   |
|                       |                       | log files — for more  |
|                       |                       | information, see      |
|                       |                       | `Using HTTP request   |
|                       |                       | IDs </acquia-cloud/de |
|                       |                       | velop/requestid>`__   |
+-----------------------+-----------------------+-----------------------+

In Drupal 7, ``drush vget syslog_format`` displays information about the
ordering and content of fields in the watchdog logs. API documentation
about Drupal's watchdog log is also available for `Drupal
7 <https://api.drupal.org/api/drupal/includes%21bootstrap.inc/function/watchdog/7.x>`__
and `Drupal
8 <https://www.drupal.org/docs/8/api/logging-api/overview>`__

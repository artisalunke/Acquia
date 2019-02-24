.. include:: /common/global.rst

FPM error logs
==============

The *FPM error log* records server-level issues with FPM's process
management in PHP. It is closely related to the `PHP error
log </acquia-cloud/monitor/logs/php-error>`__, which records
application-level issues encountered while processing a request. The FPM
error log only handles web requests; command-line requests are logged in
the PHP error log.

For a list of the log files handled by |acquia-product:ac|, including
accessing these log files, log file retention, and their locations, see
|aboutlogging|_.

.. |aboutlogging| replace:: About \ |acquia-product:ac|\  logging
.. _aboutlogging: /acquia-cloud/monitor/logs

.. _example:

Parsing the log file
--------------------

The following line is a representative example of the data written into
your website's FPM error log:

.. code-block:: 

   [04-Jan-2017 18:45:13] NOTICE: [pool alphabeta] child 20069 exited with code 0 after 3832.234353 seconds from start

Each of the items in the FPM error log is noted in the following table,
along with its description:

+-----------------------+-----------------------+-----------------------+
| Position              | Data                  | Description           |
+=======================+=======================+=======================+
| 0                     | ``[04-Jan-2017 18:45: | The date and time of  |
|                       | 13]``                 | the request           |
+-----------------------+-----------------------+-----------------------+
| 1                     | ``NOTICE``            | The issue severity —  |
|                       |                       | possible values:      |
|                       |                       | ``ALERT``, ``ERROR``, |
|                       |                       | ``WARNING``,          |
|                       |                       | ``NOTICE``, ``DEBUG`` |
+-----------------------+-----------------------+-----------------------+
| 2                     | ``[pool alphabeta]``  | The FPM pool the      |
|                       |                       | error occurred in     |
+-----------------------+-----------------------+-----------------------+
| 3                     | *All other            | The message, which    |
|                       | information in the    | will vary from line   |
|                       | line*                 | to line               |
+-----------------------+-----------------------+-----------------------+

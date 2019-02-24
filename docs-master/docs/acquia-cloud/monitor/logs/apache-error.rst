.. include:: /common/global.rst

Apache error log
================

The *Apache error log* records any Apache-level issues, which are
usually general server issues, including capacity problems,
``.htaccess`` problems, and missing files.

For a list of the log files handled by |acquia-product:ac|, including
accessing these log files, log file retention, and their locations, see
|aboutlogging|_. You
can also review information about how to `streaming Apache log entries
in real time </acquia-cloud/monitor/logstream>`__ from your browser.

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
your website's Apache error log:

.. code-block:: none

   [Fri Aug 18 20:40:36.849360 2017] [access_compat:error] [pid 11069] 
   [client 10.0.0.1:19924] AH01797: client denied by server configuration: 
   /var/www/html/alphabeta/docroot/index.php

Each of the items in the Apache access log is noted in the following
table, along with its description:

.. list-table::
   :widths: 10 30 60
   :header-rows: 1 

   * - Position
     - Data
     - Description
   * - 0
     - ``[Fri Aug 18 20:40:36.849360 2017]``
     - The date and time of error.
   * - 1
     - ``[access_compat:error]``
     - The severity of this issue
   * - 2
     - ``[pid 11069]``
     - The process ID (``pid``) handling this request.
   * - 3
     - ``[client 10.0.0.4]``
     - The internal IP address of the balancer that forwarded the request to the server
   * - 4
     - *All other information in the line*
     - The message, which will vary from line to line


For more information about the expected format of Apache error logs, see
`Apache's
documentation <https://httpd.apache.org/docs/2.4/mod/core.html#errorlogformat>`__.

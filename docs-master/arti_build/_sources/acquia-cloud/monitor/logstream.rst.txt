.. include:: /common/global.rst

Streaming log entries in real time
==================================

In addition to downloading log files from the |acquia-product:ui|
**Applications > [Environment] > Logs** page or accessing logs using
command-line tools, as described in |aboutlogging|_, you can also stream logs in
real time on the |acquia-product:ui| 
**Applications > [Environment] > Logs** page. The **Logs** page stream shows 
log entries from all of the logs of an environment at once. In contrast, 
each of the log files that you can download shows a single log from a single 
server (aside from the Drupal watchdog log and the MySQL slow query log).

.. |aboutlogging| replace:: About \ |acquia-product:ac|\  logging
.. _aboutlogging: /acquia-cloud/monitor/logs

There are several methods that you can use to modify which log entries
are streamed:

-  Click **Stream** to select which logs are the source of log entries
   to be streamed. By default, the PHP error and Apache error logs are
   enabled.

   |Select which logs to stream|

-  Filter the log stream using `JavaScript regular
   expressions <http://www.w3schools.com/jsref/jsref_obj_regexp.asp>`__.
   Just type a regular expression and the log stream is filtered
   accordingly.
-  Click a log entry to see the full text of the entry.

   |Click a log entry to see its full text|

-  If you click a log entry or scroll down the log stream, new entries
   are not added to the display. Click **Show new messages** to return
   to the top of the log stream and show the most recent log entries.
-  Click **Pause** to pause the log stream, and **Restart** to restart
   the log stream. When you restart the log stream after pausing it, the
   Logs page displays current log entries and does not display all the
   entries that occurred while it was paused.
-  To clear all the log entries, click **Clear**.
-  To download a log file, click **Logs**, and then click **Download
   Logs**. See `Downloading log files from the Logs
   page </acquia-cloud/monitor/logs#download>`__ for more information.

   |Click the Download Logs button to download log files|

.. _color:

Color coding for log entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Log entries are displayed with different colored bars at the left
margin:

+------------------+-----------+
| Log source       | Bar color |
+==================+===========+
| Apache error     |   Red     |
+------------------+-----------+
| Apache request   |   Yellow  |
+------------------+-----------+
| Balancer request |   Green   |
+------------------+-----------+
| Drupal request   |   Yellow  |
+------------------+-----------+
| Drupal watchdog  |   Blue    |
+------------------+-----------+
| MySQL slow query |   Red     |
+------------------+-----------+
| Node.js error    |   Red     |
+------------------+-----------+
| Node.js stdout   |   Yellow  |
+------------------+-----------+
| PHP error        |   Red     |
+------------------+-----------+
| Varnish request  |   Green   |
+------------------+-----------+

.. _cli:

Streaming logs from the command line
------------------------------------

In addition to streaming logs on the **Logs** page, you can use the
Logstream Ruby gem, which provides a client-side API library and
command-line interface. `Learn more about how to install and use
Logstream <https://github.com/acquia/logstream>`__.

Note

The |acquia-product:ac| log streaming Chrome extension, although
available as a Chrome extension, is not supported.

.. _related:

Related topics
--------------

-  `About |acquia-product:ac| logging </acquia-cloud/monitor/logs>`__
-  `Searching the error logs to troubleshoot
   problems </articles/searching-error-logs-troubleshoot-problems>`__

.. |Select which logs to stream| image:: https://cdn4.webdamdb.com/1280_sx5wE91QBRy1.png?1526475801

.. |Click a log entry to see its full text| image:: https://cdn4.webdamdb.com/1280_6A8NNuFt2rB0.png?1526476027

.. |Click the Download Logs button to download log files| image:: https://cdn4.webdamdb.com/1280_MsD7gHjQB9e1.png?1526475711


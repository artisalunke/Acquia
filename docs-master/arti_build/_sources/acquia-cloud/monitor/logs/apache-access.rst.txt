.. include:: /common/global.rst

Apache access logs
==================

The *Apache access log* contains a list of requests for your application
that have bypassed Varnish. These requests include pages, theme files,
and static media files.

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
your website's Apache access log:

.. code-block:: none

   200.0.0.1 - - [04/Jan/2017:23:20:38 +0000] "GET /contact_us HTTP/1.1" 404 10117 
   "-" "Pingdom.com bot version 1.4 (http://www.pingdom.com/)" vhost=alphabeta.prod.acquia-sites.com 
   host=www.example.com hosting_site=alphabeta pid=26731 request_time=10186417 
   forwarded_for="200.0.0.1, 162.0.0.1" request_id="v-00000zzz-d2d4-11e6-9bed-0aeea9eaf9af"

Each of the items in the Apache access log is noted in the following
table, along with its description:

.. list-table::
   :widths: 10 30 60
   :header-rows: 1 

   * - Position
     - Data
     - Description
   * - 0
     - ``200.0.0.1``
     - Remote host (client IP)
   * - 1
     - ``-``
     - The identity of the user determined by ``identd``. Rarely used.
   * - 2
     - ``-``
     - The user name, determined by HTTP authentication
   * - 3
     - ``[04/Jan/2017:23:20:38 +0000]``
     - The date and time the request was received by the backend server
   * - 4
     - ``"GET /contact_us HTTP/1.1"``
     - The ``REQUEST`` line from the client, containing three parts:

       - The method of the request (``GET``)
       - The path requested (``/contact_us``)
       - The HTTP protocol (``1.1``)

   * - 5
     - ``404``
     - The HTTP status code sent from the server to the client
   * - 6
     - ``10117``
     - The total size, in bytes, of the response to the client
   * - 7
     - ``"-"``
     - The referer, which is the page (none in this case) that provided the link to this page
   * - 8
     - ``"Pingdom.com bot version 1.4 (http://www.pingdom.com/)"``
     - The user-agent, or browser identification string, encased in quotation marks as many browser names have spaces in them
   * - 9
     - ``vhost=alphabeta.prod.acquia-sites.com``
     - The underlying virtual host matching the requested domain name
   * - 10
     - ``host=www.example.com``
     - The domain name for the request, which does not have to match the vhost name
   * - 11
     - ``hosting_site=alphabeta``
     - The internal Acquia site name this request is for
   * - 12
     - ``pid=26731``
     - The process ID (``pid``) on the server that handled this request
   * - 13
     - ``request_time=10186417``
     - The time needed to serve the request, in microseconds (1/1000000 of a second)
   * - 14
     - ``forwarded_for="200.0.0.1, 162.0.0.1"``
     - The full set of IP addresses tracked as "requester IP," which will 
       contain the IP addresses of the following if they are in use by the 
       subscription:

       - Load balancer
       - ELB (Elastic Load Balancer)
       - Content Delivery Networks or Web Application Firewalls (WAFs) such as 
         `Acquia Cloud Edge <edge>`__)

   * - 15
     - ``request_id="v-00000zzz-d2d4-11e6-9bed-0aeea9eaf9af"``
     - A unique ID attached to this request by the load balancer, which appears 
       in several Acquia Cloud log files — for more information, see 
       `Using HTTP request IDs <acquia-cloud/develop/requestid>`__

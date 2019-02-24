.. include:: /common/global.rst

Balancer access logs
====================

The *Balancer access log* provides information about requests received
at the balancer level. Since most customers use shared load balancers,
Varnish logs are only available using the log stream feature and cannot
be downloaded from either the |acquia-product:ui| or your servers.

For a list of the log files handled by |acquia-product:ac|, including
accessing these log files, log file retention, and their locations, see
|aboutlogging|_. You
can also review information about how to `streaming Varnish log entries
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
your website's balancer access log:

.. code-block:: none

   127.0.0.1 - - [30/Dec/2016:18:12:20 +0000] "GET /names HTTP/1.1" 200 12750 "-" 
   "facebookexternalhit/1.1" http_host=www.example.com affinity="-"  upstream_addr="171.0.0.1:80" hosting_site=alphabeta request_time=1.263 forwarded_for="173.0.0.1, 172.0.0.1" upstream_status="200" 
   request_id="v-0000zzzz-cebb-0000-9948-0efda0c0zzzz" ssl_protocol="TLSv1.2" ssl_cipher="AES128-GCM-SHA256"

Each of the items in the balancer access log is noted in the following
table, along with its description:

.. list-table::
   :widths: 10 30 60
   :header-rows: 1 

   * - Position
     - Data
     - Description
   * - 0
     - ``127.0.0.1``
     - The IP address of the web client accessing the balancer
   * - 1
     - ``-``
     - The name of a remote log file, if used (``-`` is an empty value)
   * - 2
     - ``-``
     - The username the web client was authorized under, if used (``-`` is an empty value)
   * - 3
     - ``[30/Dec/2016:18:12:20 +0000]``
     - The date and time of the request
   * - 4
     - ``GET``
     - The method of the request — frequently ``GET`` or ``POST``
   * - 5
     - ``/names``
     - The document requested, relative to the docroot of the website
   * - 6
     - ``HTTP/1.1``
     - TheHTTP protocol used for the request
   * - 7
     - ``200``
     - The HTTP status code returned by the balancer — note that it may differ from the HTTP status code returned by the backend server the request was forwarded to
   * - 8
     - ``12750``
     - Size, in bytes, of the server's response
   * - 9
     - ``"-"``
     - The referrer URL, if any (``-`` is an empty value)
   * - 10
     - ``facebookexternalhit/1.1``
     - The user-agent of the request
   * - 11
     - ``http_host=www.example.com``
     - The requested domain name
   * - 12
     - ``affinity="-"``
     - The backend server this request was pinned to, if any (``-`` is an empty value)
   * - 13
     - ``upstream_addr="171.0.0.1:80"``
     - The backend server the balancer forwarded this request to
   * - 14
     - ``hosting_site=alphabeta``
     - The internal Acquia site name this request is for
   * - 15
     - ``request_time=1.263``
     - Time in seconds needed to complete this request
   * - 16
     - ``forwarded_for="173.0.0.1, 172.0.0.1"``
     - The full set of IP addresses tracked as "requester IP," which will 
       contain the IP addresses of the following if they are in use by the 
       subscription:
       
       - Load balancer
       - ELB (Elastic Load Balancer)
       - Content Delivery Networks or Web Application Firewalls (WAFs) such as `Acquia Cloud Edge </edge>`__)

   * - 17
     - ``upstream_status="200"``
     - The HTTP status code returned by the backend server the request was 
       forwarded to — note that it may differ from the HTTP status code returned by the balancer
   * - 18
     - ``request_id="v-0000zzzz-cebb-0000-9948-0efda0c0zzzz"``
     - A unique ID attached to this request by the load balancer, which appears 
       in several Acquia Cloud log files — for more information, see 
       `Using HTTP request IDs </acquia-cloud/develop/requestid>`__
   * - 19
     - ``ssl_protocol="TLSv1.2"``
     - The SSL protocol used for this request, if any
   * - 20
     - ``ssl_cipher="AES128-GCM-SHA256"``
     - The SSL cipher used for this request, if any

.. include:: /common/global.rst

Varnish request logs
====================

The *Varnish request log* displays the requests that have been served by
Varnish cache, and those that were not. Because most customers use
shared load balancers, Varnish logs are available only using the `log
stream </acquia-cloud/monitor/logstream>`__ feature and cannot be
downloaded from either the |acquia-product:ac| interface or your
servers.

For a list of the log files handled by |acquia-product:ac|, including
accessing these log files, log file retention, and their locations, see
|aboutlogging|_. You
can also review information about how to `streaming Varnish request log
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
your website's Varnish request log:

.. code-block:: none

   99.0.0.1 - - [30/Dec/2016:23:55:24 +0000] 
   "GET http://www.example.com/carousel.min.js HTTP/1.1" 304 0 
   "https://www.example.com/" "Mozilla/5.0 Safari/601.1" 0.000127316 hit hit 
   request_id="v-0000zzzz-ce7e-11e6-9fa2-22000ab8zzzz" "-" 
   forwarded_for="99.0.0.1, 10.0.0.1"

Each of the items in the Varnish request log is noted in the following
table, along with its description:


.. list-table::
   :widths: 10 30 60
   :header-rows: 1 

   * - Position
     - Data
     - Description
   * - 0
     - ``99.0.0.1``
     - The originating IP address of the request
   * - 1
     - ``-``
     - The remote log name, if any — will usually be ``-``
   * - 2
     - ``-``
     - The remote user, if any — will usually be ``-``
   * - 3
     - ``[30/Dec/2016:23:55:24 +0000]``
     - The date and time of the request in HTTP date/time format
   * - 4
     - ``"GET http://www.example.com/carousel.min.js HTTP/1.1"``
     - The method of the request (usually ``GET`` or ``POST``), the full URL of the request, and the protocol combined together and surrounded with quotation marks
   * - 5
     - ``304``
     - The HTTP status sent to the client
   * - 6
     - ``0``
     - The size of the response in bytes, excluding HTTP headers.
   * - 7
     - ``http://www.example.com/``
     - The referrer for this request, if any, in quotation marks
   * - 8
     - ``"Mozilla/5.0 Safari/601.1"``
     - The full user-agent for this request, in quotation marks, as many user-agent names contain spaces
   * - 9
     - ``0.000127316``
     - Time to first byte
   * - 10
     - ``hit``
     - Whether the request was a cache ``HIT`` or ``MISS`` — ``PIPE`` and ``PASS`` are considered misses
   * - 11
     - ``hit``
     - How the request was handled: cache ``HIT``, ``MISS``, ``PIPE``, ``PASS``, or ``ERROR``
   * - 12
     - ``request_id="v-0000zzzz-ce7e-11e6-9fa2-22000ab8zzzz"``
     - A unique ID attached to this request by the load balancer, which appears in several |acquia-product:ac| log files — for more information, see `Using HTTP request IDs </acquia-cloud/develop/requestid>`__
   * - 13
     - ``"-"``
     - This value is for Acquia internal use only
   * - 14
     - ``forwarded_for="99.0.0.1, 10.0.0.1"``
     - The full set of IP addresses tracked as "requester IP," which will contain the IP addresses of the following if they are in use by the subscription:

       - Load balancer
       - ELB (Elastic Load Balancer)
       - Content Delivery Networks or Web Application Firewalls (WAFs) such as `Acquia Cloud Edge </edge>`__)

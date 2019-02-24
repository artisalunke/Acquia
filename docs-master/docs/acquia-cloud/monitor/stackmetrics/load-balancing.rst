.. include:: /common/global.rst

StackMetrics - Load balancing
=============================

.. container:: internal-navigation

  **Using Stack Metrics graphs**

  * :doc:`Intro </acquia-cloud/monitor/stackmetrics>`
  * Load
  * :doc:`App </acquia-cloud/monitor/stackmetrics/application>`
  * :doc:`Database </acquia-cloud/monitor/stackmetrics/databases>`
  * :doc:`File </acquia-cloud/monitor/stackmetrics/file-system>`
  * :doc:`Metrics </acquia-cloud/monitor/stackmetrics/additional>`

Your load balancers are responsible for handling requests from either
visitors to your application or from your Content Delivery Network
(CDN). These instances use Nginx to route HTTP requests to Varnish,
which determines if it has a cached version of your application’s
content. Any requests that cannot be served from cache will be routed to
instances in your web tier.

.. note::  

   For customers with shared load balancer hardware, the displayed metrics
   reflect *all* activity on the load balancers, and not only the traffic
   for your applications. Because of this behavior, when troubleshooting
   issues graph data should be used only for context.

.. _metrics:

Load balancer metrics
---------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Graph
     - Description
   * - `Requests count <#requests>`__
     - Total number of requests made to Nginx and Varnish
   * - `HTTP responses <#http>`__
     - HTTP response codes, grouped by status range (2xx, 3xx, 4xx, 5xx)
   * - `Varnish cache hit rate <#varnish>`__
     - Varnish cache hit rate as a percentage of total requests
   * - `CPU and memory usage <#cpu>`__
     - CPU usage and memory usage for each of the environment's load balancers,
as a percentage of the total available

Troubleshooting
---------------

Use the information in this section to help you troubleshoot load
balancer-related issues with your |acquia-product:ac| application.

-  **Requests count** |br|
   Depending on an application’s HTTPS traffic and Varnish
   configuration, requests can hit Varnish, Nginx, or both. This data
   can be used to obtain a basic sense of traffic patterns. For more
   exact metrics regarding traffic to your websites, we recommend that
   you use a third-party service, such as Google Analytics. This data is
   useful for tracking general traffic patterns and identifying either
   spikes in traffic (which can be associated with promotional events or
   an attack), or sudden drops in traffic (which can be associated with
   issues in your network such as DNS, the CDN, or the load balancers).
-  **HTTP response codes** |br|
   The following numbers indicate the success or failure rate of content
   requests to the load balancer tier of your stack:

   -  **2xx Success** responses indicate successful content requests
   -  **3xx Redirect** responses indicate redirected traffic, which will
      then return a different response code, potentially including
      another 300
   -  **4xx Client Error** responses indicate client (browser) side
      errors, such as ``page not found``
   -  **5xx Server Error** responses indicate a server-side error caused
      by a failure in the application or its infrastructure

   As a general rule, an optimized website will have very few 3xx or 4xx
   responses, and should have no 5xx response codes.

   -  *Elevated 3xx response codes* - `Analyze your
      logs </acquia-cloud/monitor/logs/balancer-access>`__ to determine
      what is causing the 3xx responses. The most common sources are 301
      and 302 redirects. Redirects with a 301 response code utilize
      fewer resources because they can be cached by Varnish — 302
      redirects cannot be cached.
   -  *Elevated 4xx response codes* - These codes either mean that
      content has been removed and is no longer available, or someone is
      deliberately attempting to load content that does not exist.
      Examine your log files to determine the source, and then either
      utilize a Drupal module to reduce the impact of the these
      messages, or configure your CDN to block the source of the
      requests, if malicious.
   -  *Elevated 5xx response codes* - Review Stack Metrics to determine
      if the reported information corresponds to any tiers running out
      of CPU or memory, or sudden spikes in server error counts. If
      |acquia-product:ac| is the source of the issue, Acquia Support
      will open a ticket on your behalf and contact you with more
      information. Otherwise, you should assume a non-platform source
      for the problem, you you should attempt to determine what change
      might have triggered the errors. These errors are often due to
      changes in a website’s code, content, or configuration. You can
      also `utilize an Application Performance Monitoring
      service </acquia-cloud/monitor/apm>`__ (such as New Relic) to
      attempt to determine which specific layer (php, Memcache,
      database, or external calls) may be impacting the health of your
      application.

   For applications with load balancers shared with other applications,
   it is important to note that the response codes are recorded at the
   server level. Because of this behavior, other applications using the
   same load balancers may be to blame.

-  **Varnish cache hit rate** |br|
   This number indicates what percentage of requests to your load
   balancers are being served from Varnish. Depending on the needs of
   your websites, this number may range from a small value (for websites
   with mostly authenticated traffic or no caching) to almost 100% (for
   websites with no authenticated traffic and long durations set for
   their external caching values).
   A resilient application will have a cache hit rate of 80% or greater,
   while a rate greater than 95% is considered to be exceptionally
   resilient to spikes in traffic.
   It is normal for an application’s cache hit rate to fluctuate
   throughout the day. During off-peak hours, applications will
   generally serve fresh content as caches from peak hours begin to
   expire, and requests for popular pages happen less frequently.
   To reduce the amount of traffic hitting your other instances, attempt
   to `increase your website’s cache hit
   rate <%5Bacquia-product:kb%5Darticles/caching-overview>`__ to the
   highest possible value.
-  **CPU and memory usage** |br|
   Load balancers are generally very resilient, able to serve hundreds
   or thousands of requests per minute without any measurable increase
   in CPU or memory utilization. However, spikes in traffic, sustained
   high traffic, or large cached media files can all result in load
   balancers running out of CPU or memory. Although high CPU utilization
   will usually have a minor impact on website performance, running out
   of memory can lead to hardware impairment and should be avoided.
   Although Acquia monitors for impaired hardware, instances are often
   able to continue serving traffic indefinitely even when CPU or memory
   are at or near capacity. If you notice that your load balancers are
   routinely hitting CPU or memory capacity, `contact Acquia
   Support </support#contact>`__ to determine what options are available
   to increase your load balancer capacity.

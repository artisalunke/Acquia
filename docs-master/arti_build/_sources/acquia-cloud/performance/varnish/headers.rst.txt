.. include:: /common/global.rst

Varnish headers
===============

|acquia-product:ac| uses Varnish caching to increase an application's
perceived performance for visitors. For more information about Varnish,
see `Using Varnish </acquia-cloud/performance/varnish>`__. Using
developer tools integrated with your browser, you can examine the
Varnish caching headers sent with each page and item request to see how
Varnish caching is working with your application.

To examine what Varnish is doing (or not doing) on one of the pages in
your application, examine the values of the Varnish cache headers for
the page.

To view these headers, use one of the `development
tools </resource/browser-tool>`__ available for your web browser to view
a served web page's Varnish headers. Your installed browser may already
include a set of development tools that you can use. You can also run
the following command from a command prompt:

``curl -sSLIXGET urlname``

The following are some of the headers you should see:

-  **Age** - The amount of time the served item was in the cache, in
   seconds. If the age is zero, the item was not served from the Varnish
   cache
-  **Cache-Control** - The directives that must be applied by all
   caching mechanisms (from Varnish to the browser cache)

   .. note::

    If the field has the value
    ``no-cache, must-revalidate, post-check=0`` or ``pre-check=0``, this
    item instructs any upstream proxy layers (such as Acquia load
    balancers or a CDN) to not cache. This header generally is used when
    Drupal page caching is disabled. Acquia recommends that you verify
    that this value is present on all of your website's pages. If it is,
    enable caching, and consider using `Acquia
    Purge </article/installing-acquia-purge>`__ for cache invalidation.

-  **Server** - The web server application acting as a load balancer
   that is used to serve the content (currently ``nginx``)
-  **Via** - The version of HTTP over which the request was sent
   (currently ``1.1``)
-  **X-AH-Environment** - The Acquia environment that provides the page
   response (usually ``prod``, but could also be ``dev`` or ``stage``)
-  **X-Cache** - Either ``HIT`` or ``MISS`` depending on whether or not
   the item was served from the Varnish cache
-  **X-Cache-Hits** - The number of times this object has been served
   from cache. Higher numbers indicate that this URL has received more
   visitors.
-  **X-Drupal-Cache** - Similar to ``X-Cache``, this header indicates
   the outcome of Drupal's page cache with ``HIT`` or ``MISS`` values. A
   ``MISS`` value is `not unusual
   here </article/varnish-cache-hits-and-drupal-cache-miss>`__.
-  **X-Generator** - The software used to create the page (on
   |acquia-product:ac|, this says ``Drupal`` along with the core version
   number)
-  **X-Request-ID** - The request ID for a given request
-  **X-Varnish** - The ID numbers of the current request and the item
   request that populated the Varnish cache.
   If this field has only one value, the cache was populated by the
   request, and this is counted as a *cache miss*
-  **Vary** - The inbound HTTP request headers that need to be taken
   into account when caching a single URL.
   The most common example is ``Accept-Encoding`` — a header that
   browsers usually send to websites to indicate whether they want the
   returned page compressed using gzip or the deflate compression
   algorithm. This can prevent serving gzip-compressed pages from cache
   to older browsers that do not support it.

.. _other:

Other headers
-------------

Varnish on |acquia-product:ac| also contains headers that enable caching
for some HTTP response codes, in instances where this behavior is
necessary. The header is:

``X-Acquia-No-301-404-Caching-Enforcement``

.. important::

    Acquia strongly recommends against using these headers as they may
    compromise the stability of your website.

Your Acquia load balancers cache all ``HTTP 301`` and ``HTTP 404``
responses for a minimum of 15 minutes to prevent cache stampedes and
general performance degradation under high-traffic scenarios, such as
load tests and DDOS attacks. This behavior may theoretically be
undesirable in some cases; setting the
``X-Acquia-No-301-404-Caching-Enforcement HTTP`` response header can be
used to bypass this requirement.

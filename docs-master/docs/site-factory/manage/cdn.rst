.. include:: /common/global.rst

Content Delivery Network support
================================

A Content Delivery Network (CDN) is a network of servers that delivers
webpages to website visitors based on the geographic location of each
visitor and the origin of the webpages. Using a CDN allows your webpage
load times to be faster for global audiences — no matter where visitors
are located around the world, they will consistently see page load times
that are fast.

A CDN copies your webpages to a network of servers, and then sends them
to geographically different locations, caching the contents of each
webpage. When a visitor requests a webpage that is cached by a CDN
server, the CDN redirects the request from the originating website's
server to the server in the CDN that is closest to the visitor, and then
delivers the cached content. The CDN will also communicate with the
originating server to deliver any content that has not yet been cached.

|acquia-product:cfc| is a globally load balanced CDN that you can
purchase and use as an addition to your |acquia-product:edg|
subscription. For more information, see `Using
|acquia-product:cf| </acquia-cloud/edge>`__. If you have any questions
about using |acquia-product:cfc| or a different CDN with your
|acquia-product:edg| websites, contact your Acquia account manager.

.. _what:

What does a CDN do for your website?
------------------------------------

A Content Delivery Network accelerates the process that browsers use to
load your website, making it faster and more efficient. The closer the
CDN server is to the user, the faster the content delivery. CDN services
are invisible to your end users, except for the superior experience your
site delivers.

In addition, your website content is cached on the CDN servers, making
it more accessible and ensuring availability. In the event of routine
site maintenance or rare server failures, |acquia-product:edg|’s CDN
support will provide a read-only version of the site as long as
necessary.

Content delivery without a CDN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a visitor goes to your website, their browser requests a webpage
from the server that hosts the page. This starts the following chain of
events:

#. The web page request is sent to the visitor's Internet service
   provider (ISP).
#. The request then "hops," sometimes many times, to a server on its way
   to the web server that hosts the website.
#. At some point, the web server that hosts the website receives the
   request and sends the page back to the browser.
#. The page then "hops" to a server on its way back to the visitor's
   browser, sometimes many more times, until the browser receives the
   page.
#. The browser then scans the page and prepares to display the page for
   the site visitor. If the page includes embedded media, such as
   images, videos, and advertisements, the browser must send requests
   for each of the media items. The more media on the page, the longer
   the page takes to load.

Content delivery with a CDN
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To improve your page load times, the CDN anticipates the site visitor's
need for media so pages load faster and more efficiently.

When the browser requests a page accelerated by the CDN:

#. The web page request is sent to the visitor's ISP.
#. The request then "hops" to a server on its way to the web server that
   hosts the website.
#. The request reaches a CDN server, which then routes the request to a
   server close to the |acquia-product:edg| server, potentially skipping
   several "hops."
#. |acquia-product:edg| receives the request and sends the page back to
   the browser.
#. The request reaches a CDN server, which sends the page to a server
   close to the browser.

   The CDN server scans the web page, sends requests for the page's
   embedded media from |acquia-product:edg|, and keeps a copy of the
   media.

#. The browser receives the page and scans the page for display.
#. When the browser makes requests for embedded media, the request only
   goes to the CDN server that sends the copies of the media it already
   retrieved, potentially reducing the media retrieval time.

.. _enabling:

Enabling CDN support
--------------------

To enable CDN support for your website, contact your
|acquia-product:edg| advisor.

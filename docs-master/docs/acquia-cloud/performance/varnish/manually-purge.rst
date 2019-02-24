.. include:: /common/global.rst

Manually purging a page from Varnish cache
==========================================

.. important::

    Acquia strongly recommends using the preferred method of Varnish cache
    purging, `Acquia Purge <https://www.drupal.org/project/acquia_purge>`__.
    For more details, see `Purging Varnish cache on
    </acquia-cloud/performance/varnish/purging>`__ |acquia-product:ac|.

Varnish caching is intended to provide protection for your application,
and will continue to provide content for your users in some cases even
if your application is down for a short period. Sometimes this means
that you have content that you may need to remove more quickly than the
standard Varnish timeout for your application. Two methods you can use
to clear your Varnish cache are |acquia-product:ap| and by using command
line instructions.

.. _purge:

|acquia-product:ap| (recommended)
---------------------------------

The |acquia-product:ap| module is the easiest way to clear specific
pages or groups of pages from Varnish cache. See `Installing
Acquia Purge <https://support.acquia.com/hc/en-us/search?utf8=%E2%9C%93&query=installing-acquia-purge>`__
for installing and configuring this module.

.. _cli:

Command line
------------

If you must use the command line to manually purge the Varnish cache for
a specific page, the easiest and most straightforward way is to manually
purge the page using `cURL <https://en.wikipedia.org/wiki/CURL>`__ with
the regular ``-X PURGE`` request method to interact with the HTTP
server. Next, pass it to Acquia's custom ``X-Acquia-Purge`` header with
the Unix site name from which to purge the specified page.

Connect to one of your Acquia web servers using SSH and run one of the
following commands. Replace ``[sitename]`` with your Unix site name and
the path with either your front page or any page you wish to clear from
the Varnish cache. It is often useful to purge both a given path and its
related RSS feed, if there is any (``rss.xml`` by default). You will
need to run this command for each page that you want to purge from the
Varnish cache, since there is no way to pass it a list of pages to purge
all at once.

.. note::

    -  These commands will not work with the ``acquia-sites.com`` domains
       that are provisioned with |acquia-product:ac| environments.
    -  |acquia-product:edg| subscribers must use the command to `ignore the
       balancer's SSL state <#ignorestate>`__.

-  If you are not using an elastic load balancer (ELB):

   .. code-block:: none

      # Replace 'sitename' below with the appropriate value. 
      curl -X PURGE -H "X-Acquia-Purge:sitename" -H "Accept-Encoding: gzip" http://site.com/path/to/page

-  If your application uses an ELB, you must send requests to each
   active balancer, using the desired domain as a ``Host`` header.

   If you are trying to purge a page on example.com, and that domain is
   hosted on ``bal-1234.devcloud`` and ``bal-1235.devcloud``, you would
   use the following:

   .. code-block:: none
  
      curl -X PURGE -H "X-Acquia-Purge:[sitename]" --compress -H "Host: example.com" http://bal-1234.devcloud.hosting.acquia.com/foo/bar 
      curl -X PURGE -H "X-Acquia-Purge:[sitename]" --compress -H "Host: example.com" http://bal-1235.devcloud.hosting.acquia.com/foo/bar``

   To do this for your own servers, replace
   ``bal-1234.devcloud.hosting.acquia.com`` with the appropriate server.
   You can find the full list on the environment's
   `Servers </acquia-cloud/manage/servers>`__ page.

-  If your application is behind a content delivery network (CDN), such
   as Akamai, you must send a request to the active load balancer or the
   balancer's elastic IP address (EIP). To do this, use a command
   similar to the following:

   ``curl -X PURGE -H "X-Acquia-Purge:[sitename]" -H "Accept-Encoding: gzip" -H "Host: example.com" http://[eip_address]``

   Your ``[eip_address]`` is located on your |acquia-product:ac|
   `Servers </acquia-cloud/manage/servers>`__ page.

-  If your website redirects all traffic from HTTP to HTTPS, you may
   need to ignore the balancer's SSL state, and explicitly specify the
   HTTPS protocol, as follows:

   ``curl -k -X PURGE -H "X-Acquia-Purge:mysite" --compress -H "Host: www.mysite.com" https://bal-12345.prod.hosting.acquia.com/``

   .. note::

        |acquia-product:edg| subscribers *must* use this version of the
        command, replacing ``prod`` with the appropriate realm. If you need
        assistance determining the correct value for your subscription,
        `contact Acquia Support </support#contact>`__.

Considerations
~~~~~~~~~~~~~~

It is important to understand that the Varnish cache is stored per
domain, so if multiple domains are configured to reference the same
application (for example, ``www.mysite.com`` and ``cms.mysite.com``),
you need to make individual ``curl`` requests for each domain on which
the page to be cleared is referenced.

It is also important to understand that running these purge commands
will not invalidate Drupal caches. If Drupal cache objects are not yet
scheduled to be purged from the cache and Memcache, purging the Varnish
cache will not make any difference. Because of this, you will have to
think of a way to clear the relevant CID (cache id) for the cache
objects you need to purge first.

We recommend that you leverage Drupal's
`cache_clear_all <https://api.drupal.org/api/drupal/includes!cache.inc/function/cache_clear_all/7.x>`__
API function in a Rule or a custom module to specifically clear the
cache items that are going to be triggered by the Varnish cache purge.

.. important::

    We strongly recommend against simply clearing all Drupal caches, because
    it will have consequences for how the application performs during the
    cache rebuilding phase.

For more information about the different layers of caching, see the
`Caching overview </articles/caching-overview>`__ page.

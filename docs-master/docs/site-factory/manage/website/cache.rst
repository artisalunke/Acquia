.. include:: /common/global.rst

About caching in |acquia-product:edg|
=====================================

.. toctree::
   :hidden:
   :glob:

   /site-factory/manage/website/cache/*

To improve your website's performance, |acquia-product:edg| caches
several files and webpages that make up your website using both Drupal
caching (used directly by your website) and Varnish caching (top-level
cache used to increase general performance).

When a visitor views your website, if the webpage they request was
previously served to a different visitor and is in a cache,
|acquia-product:edg| provides the webpage directly from the cache. This
allows the visitor to see the page several times faster than if
|acquia-product:edg| had to prepare and send the page to the visitor
from its source files. Because pages are served faster, caching enables
more pages to be served to more visitors.

|acquia-product:edg| caches the following data types relating to your
website's structure:

-  Drupal website databases
-  Anonymous webpages and static content
-  CSS files
-  JavaScript files

.. note::  

   -  |acquia-product:edg| does not cache signed-in user webpages and dynamic content.
   -  If you are using a 
      `Content Delivery Network (CDN) </site-factory/manage/cdn>`__ with your 
      website, clearing Varnish and Drupal caches does *not* also clear your CDN cache.

Clearing the caches
-------------------

|acquia-product:edg| allows you to clear your websites' Drupal and
Varnish caches, which causes any visitor requested webpages and files to
be regenerated from the source files. Newly requested visitor items will
then be placed in the cache for use with future visitors.

Clearing caches also refreshes the thumbnail images of your websites on
the Factory interface, site collections, and groups webpages.

To clear your website's Varnish and Drupal caches, you can use the
|acquia-product:edg| user interface, the Site Factory API, or a
specially-formatted command from the command-line interface:

-  *Clearing caches through the user interface*
   To clear your website's caches (including Varnish caches) with the
   |acquia-product:sfi| interface, complete the following steps:

   #. `Sign in </site-factory/manage/login>`__ to the
      |acquia-product:sfi|, find the
      website for which you want to clear its caches, and then open its
      actions menu.

      |Site actions menu|

   #. Click **Clear caches**.
   #. To confirm that you want to clear the website's caches, click
      **Clear caches**.

-  *Clearing caches with the Site Factory API*
   The `Site Factory REST API </site-factory/extend/api>`__ includes a
   |cache-clear|_ for clearing a website's Drupal and Varnish caches
   programmatically.
-  *Clearing a single page from cache using the command line*
   For instructions about how to clear a single webpage with the command
   line, see `Manually purging a page from Varnish
   cache </acquia-cloud/performance/varnish/manually-purge#ignorestate>`__.

.. |cache-clear| replace:: ``cache-clear`` endpoint
.. _cache-clear: https://www.demo.acquia-cc.com/api/v1#Clear-a-site's-caches

Increasing the cache lifetime
-----------------------------

By default, |acquia-product:edg| sets the maximum age for items included
in the Varnish page cache (``page_cache_maximum_age``) to 3600 seconds
(60 minutes). See `Increasing caching in Acquia Cloud Site Factory </site-factory/manage/website/cache/modify>`__ for
several methods of increasing the cache lifetime value from the default.

.. |Site actions menu| image:: https://cdn2.webdamdb.com/1280_MolekfJrnUF5.png?1526475845
   :width: 750px
   :height: 356px

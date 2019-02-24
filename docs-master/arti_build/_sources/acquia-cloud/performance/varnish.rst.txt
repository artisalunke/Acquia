.. include:: /common/global.rst

Using Varnish
=============

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/performance/varnish/*

`Varnish Cache <https://varnish-cache.org/>`__ is a caching reverse
proxy which is installed in front of all |acquia-product:ac| load
balancing servers. Varnish® increases application performance by caching
anonymous user connections and serving them from memory instead of
making requests to the Apache web server. Serving pages from memory is
much faster than serving them from the Drupal/Apache/MySQL/PHP stack,
and also frees up resources on the server and database to handle the
dynamic requests that can't be handled by Varnish. If Varnish can't
fulfill a page request, it passes it through to the
Drupal/Apache/MySQL/PHP stack. If the response from Apache is cacheable,
Varnish stores it for faster responses to future requests.

For more information about using Varnish, see `Introduction to
Varnish <https://support.acquia.com/hc/en-us/search?utf8=%E2%9C%93&query=varnish-intro>`__.

.. _what:

What Varnish caches
-------------------

Varnish caches responses to anonymous user requests. It also caches
static assets, such as images, JavaScript, and CSS, both for anonymous
and authenticated user requests (so long as they are not in the Drupal
private file system). On |acquia-product:ac|, Varnish does not
cache PDF files, or any objects larger than 10MB. You should use a CDN,
such as `Acquia Cloud Edge </edge>`__, or another `external storage
system <https://support.acquia.com/hc/en-us/search?utf8=%E2%9C%93&query=using-external-storage-files>`__
for serving large assets or PDF files.

To determine how Varnish caching is working with your application, you
can examine the Varnish caching headers sent with each page and item
request. For more information, see `Varnish
headers </acquia-cloud/performance/varnish/headers>`__.

.. _configure-varnish:

Configuring Varnish
-------------------

You cannot configure Varnish yourself. Acquia has configured the shared
Varnish installation in a way we believe is optimal for most
applications. If you are an |acquia-product:ace| customer, and you have
dedicated load balancers, custom Varnish configurations may be available
through an Acquia Professional Services engagement. See `Custom Varnish
configuration for applications </acquia-cloud/performance/varnish/custom>`__ 
|acquia-product:ace| and contact your Acquia account manager for more 
information.

There is no need to install the
`Varnish <https://www.drupal.org/project/varnish>`__ Drupal module. It
will not work with |acquia-product:ac| applications because it requires
connections to the load balancers, which Acquia does not provide.

.. _drupalcache:

Configuring Drupal cache settings for Varnish
---------------------------------------------

To take advantage of Varnish, you need to configure your Drupal
application. To set your website cache options to external caching, open
your Drupal application's Performance page. The cache settings depend on
which version of Drupal that you are using:

.. admonition:: Note for |acquia-product:edg| users

    Changing |acquia-product:edg| caching settings requires that you `create
    a particular file in the factory-hooks/post-settings-php
    directory </site-factory/manage/website/cache#change>`__.

-  | *Drupal 8 cache settings*
   | On the Performance page at
     ``/admin/config/development/performance``, select a value in the
     **Page cache maximum age** list. This is the maximum time a page
     can stay in the Varnish cache. If you set this to **<no caching>**,
     the ``max-age`` header Drupal sends to Varnish is 0, which means it
     will not be cached. A reasonable setting is **6 hours** to **12
     hours**.

   |Drupal 8 cache settings|

-  | *Drupal 7 cache settings*
   | On the Performance page at **Configuration > Performance**, set
     values for the following items:

   |Drupal 7 cache settings|

   -  **Cache pages for anonymous users** check box - Select this item.
   -  **Minimum cache lifetime** list - The minimum cache lifetime
      prevents Drupal from clearing page and block caches after changes
      are made to nodes or blocks for a set period of time. This can
      cause unexpected behavior when editing content or when an external
      cache such as Varnish is employed. Therefore, minimum cache
      lifetime should be used with caution. If you are unsure, leave the
      minimum cache lifetime set to **0**.
   -  **Expiration of cached pages** list - This is the maximum time a
      page can stay in the Varnish cache. If you set this to **<none>**,
      the ``max-age`` header Drupal sends to Varnish is 0, which means
      it will not be cached. A reasonable setting is from **6 hours** to
      **12 hours**.

   .. important::

      For Drupal 7 and earlier versions, Acquia strongly recommends that
      you do not compress cached pages, as compression can cause problems
      with both Varnish caching and New Relic application monitoring.

.. _bypass:

Bypassing the Varnish cache
---------------------------

Sometimes you may have a few pages with random or dynamic content that
you want not to cache. You can selectively exclude certain paths from
being cached so that dynamic content is actually dynamic. For
information about how to do this, see `Bypassing the Varnish
cache <https://support.acquia.com/hc/en-us/search?utf8=%E2%9C%93&query=bypassing-varnish-cache>`__.

.. _ssl:

Varnish over SSL
----------------

Acquia provides Varnish for use with connections secured by SSL. To
enable Varnish caching for your SSL-enabled website, complete the
following steps:

#. Sign in to the |cloud-ui|_,
   and then select your application and environment.
#. On the **Overview** page for the environment, click the **Configure**
   gear icon.
#. In the **Varnish** section, select the **Varnish through SSL** check
   box.
#. Click **Save**.

The activity icon will indicate that the change is being made. After the
process complete, Varnish over SSL is enabled for the website.

.. _clear:

Clearing the Varnish cache
--------------------------

You can clear (flush or purge) the Varnish cache using the
|acquia-product:ui|:

#. Sign in to the |acquia-product:ui| and select your application and
   environment.
#. On the **Overview** page for the environment, click **Clear
   Varnish**.
#. In the **Clear caches** dialog box, select the domains for which you
   want to clear the Varnish caches.
   You can click **All** to clear the Varnish caches for all domains in
   this environment. Then click **Clear** to confirm. All check boxes
   will be selected by default, and your selections are maintained.

You can also purge individual pages using the Acquia Purge module user
interface, or with command-line commands. For more information, see
`Purging Varnish Cache on
</acquia-cloud/performance/varnish/purging>`__ |acquia-product:ac|.

*Varnish is a registered trademark of Varnish Software AB and its
affiliates.*

.. |Drupal 8 cache settings| image:: https://cdn4.webdamdb.com/1280_gzvLlzL6dXp6.png?1526475508
   :width: 750px
   :height: 576px
.. |Drupal 7 cache settings| image:: https://cdn4.webdamdb.com/md_EnSfVekeTt49.png?1526476013
   :width: 470px
   :height: 272px

.. |cloud-ui| replace:: \ |acquia-product:ui|\
.. _cloud-ui: https://cloud.acquia.com

.. include:: /common/global.rst

Managing subscription usage
===========================

The Subscription Usage page in the |acquia-product:sfi| displays how
many websites and site collections in your |acquia-product:edg|
subscription already have custom domain names assigned to them. If your
|acquia-product:edg| subscription has a limited number of websites, this
page will display the number of websites with custom domains on your
production and ``update`` environments, which are the websites that
count against your subscription's maximum number of websites limit. It
also displays the number of `dynamic requests <#requests>`__ served by
each Site Factory Stack per month.

To view the Subscription Usage page:

#. Sign in to the |acquia-product:sfi| using an account with the
   `*platform admin* </site-factory/users/admin/platform-admin>`__ role.
#. In the admin menu, click **Administration**.
#. Under **Site Factory management**, click the **Subscription Usage**
   link.

|Subscription usage page|

Viewing dynamic requests
------------------------

The **Dynamic requests** section of the **Subscription Usage** page
displays the number of dynamic requests served by each Site Factory
Stack during each month. Dynamic request data is available with up to a
two-day delay.

For this purpose, dynamic requests include all requests served by
Drupal, including:

-  successful page loads
-  redirections
-  image derivative generations
-  page not founds
-  failed page loads

Dynamic requests do not include:

-  requests served from Varnish cache or a CDN
-  requests for images, files, or other assets
-  cron runs (although these will be included in the future)

Downloading dynamic request reports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|Dynamic request reports|

Click the **CSV** button to download dynamic request reports in CSV
format. The downloaded report includes all of the time periods currently
displayed on the **Subscription Usage** page. By default, the name of
the downloaded file is ``dynamic-requests.csv``.

Using the REST API to obtain dynamic request reports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Site Factory REST API </site-factory/extend/api>`__ includes a
``Dynamic requests`` method (|getmonthly|_) that you can use to obtain more 
detailed dynamic request reports.

.. |getmonthly| replace:: ``GET /api/v1/dynamic-requests/monthly``
.. _getmonthly: https://www.demo.acquia-cc.com/api/v1#List-monthly-aggregated-dynamic-request-statistics

Related topics
--------------

-  `Adding custom domains to your
   site </site-factory/manage/website/domains>`__

.. |Subscription usage page| image:: https://cdn2.webdamdb.com/1280_c4hTzwuKJsv7.png?1526475595
   :width: 750px
   :height: 435px
.. |Dynamic request reports| image:: https://cdn4.webdamdb.com/1280_2G8SWmOaCF72.png?1526475876
   :width: 750px
   :height: 382px

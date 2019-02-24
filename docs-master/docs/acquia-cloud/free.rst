.. include:: /common/global.rst

Getting started with |acquia-product:acfs|
==========================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/free/*

|acquia-product:acfs| is built on the same infrastructure as |acquia-product:acs|, so you can use the `Acquia Cloud documentation </acquia-cloud>`__ to learn how to use it. As a general rule, you can use |acquia-product:acfs| to do anything you could do on |acquia-product:acs|, subject to the limitations listed on this page.

.. _upgrade:

|Upgrade link|\ Upgrading to a paid subscription
----------------------------------------------------------------------

To upgrade to a paid subscription and remove the feature limitations on your `Acquia Cloud Free subscription <https://www.acquia.com/acquia-cloud-free>`__, simply click the **Upgrade now** link in the empty Prod environment on your subscription's `Environments </acquia-cloud/manage/environments>`__ page. You can then select your new hardware and other |acquia-product:ac| features.

.. _compare:

Product comparison
------------------

Compare what you get with free or paid |acquia-product:ac|:

.. list-table::
 :widths: 50 50
 :header-rows: 1

 * - Free
   - Paid
 * - Two environments: Development and Staging; no Production environment
   - Three environments: Development, Staging, and Production (|acquia-product:ace| subscriptions can request additional environments). `Learn more </acquia-cloud/manage/environments>`__.
 * - No custom domain names
   - You can assign custom domain names to your environments. `Learn more </acquia-cloud/manage/domains>`__.
 * - Servers have limited CPU and disk storage. Your application's codebase, database, and file system are each limited to 1 GB of disk storage. See `Managing disk storage for Acquia Cloud Free </acquia-cloud/free/storage>`__ for information about how to work within the storage limit.
   - Depending on your subscription level, shared or dedicated servers with a wide range of CPU, memory, and storage capacities are available. `Learn more <https://www.acquia.com/cloud-pricing>`__.
 * - No support for Memcached, a general-purpose memory cache server daemon
   - Improve website performance using `Memcached </acquia-cloud/performance/memcached>`__, which moves Drupal's standard caches out of the database into memory and caches the results of other expensive database operations.
 * - You cannot send email from |acquia-product:acfs| websites. You can use `an external third-party email service </acquia-cloud/manage/email/3rdparty>`__ instead.
   - Your websites can send limited outgoing emails such as Drupal registration confirmation emails and node subscription emails. You cannot send mass emails such as marketing messages or newsletters. You should use external email services for mass mailings. `Learn more </acquia-cloud/manage/email>`__.
 * - You cannot use SSL (HTTPS) to serve your application.
   - You can set up your application to use SSL (HTTPS). `Learn more </acquia-cloud/ssl>`__.
 * - You must use Git to manage your code repository.
   - You must use Git to manage your code repository. `Learn more </acquia-cloud/develop/repository/git>`__.
 * - Your application is available for 30 days. See `Time limit <#limit>`__ for details.
   - Your application is available as long as you pay for it.
 * - Insight provides many, but not all, available alerts and more limited website analysis. Insight reports can't be downloaded.
   - `Insight </acquia-cloud/insight>`__ provides the full range of available alerts and website analysis. Insight reports are downloadable.
 * - Support unavailable from the Acquia Support team.
   - Support available from the `Acquia Support team <https://www.acquia.com/products-services/acquia-network/cloud-services/drupal-support>`__, with different levels of support.

.. _limit:

Time limits for free subscriptions
----------------------------------

Your |acquia-product:acfs| subscription provides access to the features of |acquia-product:ac| for 30 days. After 30 days, your application and any of its associated data and files will be permanently removed from |acquia-product:ac|. After removal, applications are unrecoverable. To preserve your application and prevent the loss of any data, be sure to either upgrade to a paid subscription or `export your application </acquia-cloud/manage/export>`__.

Support
-------

As a free offering, |acquia-product:acfs| does not entitle you to live or ticketed support. This is the case even if you also have a paid |acquia-product:ac| subscription. For more information about your |acquia-product:acfs| subscription, `review its documentation </acquia-cloud>`__.

.. note::

   The limitations on your |acquia-product:acfs| subscription apply to that subscription, even if you also have a paid Acquia subscription. For example, you cannot use for your |acquia-product:acfs| subscription support tickets you may have from a paid subscription.

.. |Upgrade link| image:: https://cdn2.webdamdb.com/1280_64VWsZ2KsvF0.png?1526475800
   :class: logo-pp float-right
   :width: 200px

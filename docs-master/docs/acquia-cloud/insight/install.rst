.. include:: /common/global.rst

Installing the |acquia-product:anc|
===================================

.. container:: internal-navigation

   **Using Acquia Insight**

   * :doc:`Intro </acquia-cloud/insight>`
   * :doc:`Using </acquia-cloud/insight/using>`
   * :doc:`Alerts </acquia-cloud/insight/alerts>`
   * :doc:`Modules </acquia-cloud/insight/code>`
   * Connector
   * :doc:`Configure </acquia-cloud/insight/config>`

Before you can access |ais|,
you have to connect your website to Acquia by installing and activating
the |acquia-product:anc| module. The |aic| is
a Drupal module package that allows your websites to exchange
information with Acquia.

Note

Enabling the |acquia-product:anc| module in a local, development website
can cause the website to be listed on your |acquia-product:ac|
subscription page along with your other applications.

To install the |acquia-product:anc|, complete the following steps:

#. Sign in to your Drupal website as an administrator.
#. | Install and enable the |anc|
     for your version of Drupal. (`Drupal 8
     instructions </resource/module-install-d8>`__ \| `Drupal 7
     instructions </resource/module-install-d7>`__)
   | When enabling your |acquia-product:anc| module in your Drupal
     website, enable the following modules on the Extend/Modules
     webpage, by Drupal version:

   -  *Drupal 8* – **Acquia connector**
   -  *Drupal 7* – **Acquia Agent** and **Acquia Site Profile
      Information**

   Note

   If you're using the |ld| Drupal
   distribution, the |acquia-product:anc| is already included, and you
   do not need to download it.

#. Go to the **Acquia Networ Connector** configuration webpage using the
   appropriate method, based on your installed Drupal version:

   -  *Drupal 8* – In the admin menu, go to **Configuration > Acquia
      Connector settings**.
   -  *Drupal 7* – In the admin menu, go to **Configuration > Acquia
      Subscription settings**.

#. If the Configuration page does not indicate that you are connected to
   an |acquia-product:aqs|, click **Get connected**, and then enter your
   Acquia email address and password.

   Note

   For multisite applications, it is helpful to enter a unique name in
   the **Site Identification** field. |acquia-product:ac|-hosted
   websites are provided with a name and machine name by default, which
   are displayed in |acquia-product:ui| pages, such as `Stack
   Metrics </acquia-cloud/monitor/stackmetrics>`__, to help identify
   individual installations.

#. Choose the subscription that you want to connect, and then click
   **Submit**.
   If you are using |acquia-product:anc| 7.x-3.x, and your website is
   not hosted on |acquia-product:ac|, you must enter a name for your
   website under **Site identification**, and then click **Save
   settings**.

.. _search:

Adding |acquia-product:as|
~~~~~~~~~~~~~~~~~~~~~~~~~~

The |acquia-product:anc| also includes the |acquia-product:as|
integration, a fully managed SaaS search offering that integrates
seamlessly with Drupal applications. Built on the enterprise-grade
Apache Solr search engine, |acquia-product:as| is hosted on
|acquia-product:ac|, providing a fully redundant infrastructure that
ensures search is a highly available feature of your website. Learn more
about |as|.

.. _connect:

Connecting
----------

Your website is now connected to Acquia. You may need to `run
cron <https://www.drupal.org/node/158922>`__ on your website before it
appears in |acquia-product:ais|. For more information, see `When the
Acquia connector connects to
Acquia </acquia-cloud/insight/config#interval>`__. See also `Using
Insight to optimize your
application </acquia-cloud/insight/using>`__.

.. _upgrade:

Updating the |acquia-product:anc|
---------------------------------

To get the greatest benefit from |acquia-product:ac|, you should keep
the |acquia-product:anc| module up to date with the latest stable
version.

Important

When you upgrade the |acquia-product:anc| module, be sure that you
install the upgraded version in the correct location in your docroot
directory. If you are using an Acquia-sponsored Drupal distribution,
such as |acquia-product:ld|, the |acquia-product:anc| module may be
already installed in ``[docroot]/profiles/acquia/modules`` and not in
``[docroot]/sites/all/modules``. Because of this you should upgrade the
module in the location where it is installed. Having different versions
of the module installed in more than one location can result in
confusion or inconsistent behavior.

.. |ais| replace:: \ |acquia-product:ais|\ 

.. |anc| replace:: \ |acquia-product:anc|\
.. _anc: https://www.drupal.org/project/acquia_connector

.. |ld| replace:: \ |acquia-product:ld|

.. |as| replace:: \ |acquia-product:as|
.. _as: /acquia-search

.. include:: /common/global.rst

About Acquia billing
====================

.. toctree::
   :hidden:
   :glob:

   /support/billing/*

Billing for |acquia-product:acs| consists of two components: an |acquia-product:aqs| and usage-based resource pricing.

.. note::

   This page describes |acquia-product:acs| billing.

   For information about |acquia-product:ace| or |acquia-product:edg| billing, contact your Acquia Account Manager or salesperson.

Your Acquia subscription
------------------------

An |acquia-product:aqs| gives you access to a suite of services, information, and support for your Drupal websites. |acquia-product:acs| requires a Developer or Professional |acquia-product:aqs|. Your |acquia-product:aqs| is charged monthly. See `Cloud pricing <https://acquia.com/cloud-pricing>`__ for details on the different subscription types and prices.

See the `Billing FAQ </support/billing-faq>`__ for answers to common questions regarding the |acquia-product:aqs| purchase process and billing.

Usage-based resource pricing
----------------------------

|acquia-product:acs| server instances, disk storage, and network data transfer (bandwidth) are billed based on actual usage. Server instance usage and disk storage are measured on an hourly basis, while data transfer is measured on a monthly basis. All usage-based charges are billed on a monthly basis. You aren't billed for shared resources, such as shared servers. The hourly charges for instances vary based on the region.

Measuring the instance size monthly means that if you have an instance at its normal size running for a month, you will be charged the hourly rate for that size for each hour in that month. If you increase the instance's size for one day, you will pay the higher hourly rate only for those hours when it was running at the larger size. All monthly instance prices are approximate; actual billing is based on hourly usage, and monthly charges will depend on the number of hours in the month. See the |pricing page|_ for current prices.

.. |pricing page| replace:: \ |acquia-product:ac|\  pricing page
.. _pricing page: https://www.acquia.com/cloud-pricing

Disk storage
------------

Disk storage costs $0.50/GB per month. This price includes additional storage space for backups. If you purchase "10GB" of storage for $5.00/month, Acquia provides 10GB for your primary storage plus an additional 10GB of backup storage directly on your instance. Acquia also makes frequent point-in-time snapshots of your disk and retains them for three months. These snapshots are for disaster recovery only (for example, in case the disk drives fail, the datacenter burns down, etc.) and are included in the $0.50/GB storage cost. For more information, see `Increasing disk storage </acquia-cloud/manage/servers/storage>`__.

Data transfer
-------------

All |acquia-product:acs| subscriptions include 50GB of data transfer per month. This included transfer limit is per subscription, not per server or per site; if you have three |acquia-product:ac| servers running seven different sites, you still have 50GB of included data transfer in total. Additional data transfer is $0.25/GB.

SSL support
-----------

SSL support costs $30 per month. This does not include the cost of your SSL certificate. You purchase your own SSL certificate from a certificate vendor and upload it to |acquia-product:ac|. For more information, see `Adding HTTPS (SSL) support to your website </acquia-cloud/ssl>`__.

Permanent IP addresses for web servers
--------------------------------------

Every |acquia-product:ac| site has a permanent IP address for its load balancers, but not for the web server behind the load balancers. Some users need permanent IP addresses for the web server (for example, so that outbound requests from the web can be identified appropriately by a firewall). If you need a permanent IP address for your web server, there is an additional charge of $5 per month.

Invoices
--------

All charges for a month appear on your credit card as a single transaction around the 11th day of each month. To see invoices for a subscription, you must be the *Owner* or `*Administrator* </acquia-cloud/teams/roles>`__ for that subscription. If you need to change the primary contact, open a ticket with Acquia Support.

To view detailed invoices, complete the following steps:

#. Click your name or picture in the upper-right corner of the Acquia user interface, and select **View profile** (or go directly to `cloud.acquia.com <https://cloud.acquia.com>`__).
#. Click **Invoices**.
#. Click **Download** to download an invoice.

|View your invoices|

The detailed invoice displays your **Subscription Identifier** to the left — this number corresponds to the number on your **Invoices** tab, under **Subscriptions**.

Billing example
---------------

Suppose that on May 20th you sign up for a monthly Acquia Developer subscription at $99/month, a 4 ACU server at $0.389/hour, and 10GB of storage at $5.00/month. On June 1, you will be charged (prices are approximate) the following:

-  $33 for the Developer subscription for 10 days of May
-  $99 for the Developer subscription for June
-  $93.36 ($0.389/hour \* 24 hours \* 10 days) for the server
-  $1.67 ($5.00/month \* 1/3 of May) for the 10GB of storage

Your server then runs for the entire month of June. However, you expect a large traffic spike on June 17 so you increase the server to 8 ACUs at $0.779/hour for 24 hours. On July 1, you will be charged (prices are approximate) the following:

-  $99 for the Developer subscription for July
-  $270.74 ($0.389/hour \* 24 hours \* 29 days) for the 4 ACU server for 29 days
-  $18.70 ($0.779/hour \* 24 hours) for the 8 ACU server for one day
-  $5.00 for the 10GB of storage

Billing ownership
-----------------

The owner of any subscription group that contains |acquia-product:acs| subscriptions should also be the billing owner. After the ownership of a subscription group has been transferred, the billing ownership will also transfer to the new owner.

The new owner must have a credit card associated with the account for the transfer to complete successfully. The next billing cycle will prorate the invoice between the previous and current owners.

For information about transferring billing ownership, see `Transferring control of a subscription </acquia-cloud/subs#transfer>`__.

Cancellation
------------

You can cancel your |acquia-product:acs| subscription at any time.

.. important::

   After you cancel your subscription, you will no longer be able to access your application or its files. Download a `backup of your application </acquia-cloud/manage/back-up>`__, any `log files </acquia-cloud/monitor/logs>`__, or anything else on your server that you want to keep *before* you cancel.

To cancel your account, complete the following steps:

#. Sign in to |acquia-product:ac|, and select your application.
#. On the **Applications > Environments** page, click **Cancel**.

   |Cancel|

#. On the confirmation page, enter your Acquia password, and then click **Continue**.
#. Help us improve |acquia-product:ac| by telling us why you are canceling.
#. Click **Finalize**.

Self-cancellation is available only for customers who pay with a credit card and for |acquia-product:acfs| subscriptions. Other customers who pay with a purchase order or under a contract must contact their Acquia Account Manager to cancel their subscriptions.

Effects of cancellation
~~~~~~~~~~~~~~~~~~~~~~~

Cancellation affects your |acquia-product:aqs| and usage-based resource charges differently.

-  Your |acquia-product:aqs| will be canceled within a few minutes of your request. You will be billed for the prorated portion of the final billing period in which your subscription was active. You will not be billed for additional periods for your subscription after the effective date of cancellation. Note that if you cancel a monthly subscription before the end of the *first* month of service, you will still be billed for the partial first month of service on the first day of the following month.
-  Your server will be terminated immediately, and all websites on it will no longer be available. At the beginning of the following month, you will be billed for the usage-based charges for however long your instance was running.

When you cancel an |acquia-product:ac| subscription, Acquia may retain a copy of your data for a few extra days in case you change your mind. If you request that Acquia restore your subscription, and if Acquia still has your data available, it will charge a one-time $100 un-cancellation fee.

Related topics
--------------

-  `Billing FAQ </support/billing-faq>`__

.. |View your invoices| image:: https://cdn4.webdamdb.com/1280_gpsybGQYWph2.png?-62169955200
   :width: 590px
   :height: 317px
.. |Cancel| image:: https://cdn2.webdamdb.com/1280_oebctIJMYop0.png?-62169955200
   :width: 750px
   :height: 316px

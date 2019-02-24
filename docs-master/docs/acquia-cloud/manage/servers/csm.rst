.. include:: /common/global.rst

Cloud Service Management plans
==============================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/manage/servers/csm/*

.. container:: message-status

   *Available only to Acquia Cloud Enterprise subscribers. Contact your account manager for more information*.

Drupal-based production environments in |acquia-product:ace| include the ability for you to scale server sizes, based on need, by using the |acquia-product:ac| user interface. |acquia-product:ace| includes `Cloud Service Management </acquia-cloud/csm>`__ (CSM) as an optional part of new Medium and Large |acquia-product:ace| subscriptions, providing you with direct control of the scaling of your |acquia-product:ac|-hosted application. Note that this feature does not affect the monitoring that Acquia does on its own to monitor the health of the |acquia-product:ac| managed application stack, and Acquia Support can continue to perform emergency scaling as needed.

|acquia-product:ac| customers with Cloud Service Management enabled can view statistics for CPU utilization, memory utilization, and PHP process count in the `Acquia Cloud management interface </acquia-cloud/monitor/stackmetrics>`__. The management console will also display PHP Max Children Reached error messages. By combining information about your website's performance during peak traffic periods with PHP Max Children Reached errors, you can determine if you should scale up your web tier.

.. note::

   Regardless of your CSM status, Acquia will increase capacity as needed to resolve emergency events, as described in our `Product Guide </guide/cloud/ace>`__, and will inform subscribers of emergency capacity increases using the standard ticketing process. Emergency capacity increases will be billed at the daily rate for additional capacity. The CSM functionality described on this page will be used to upsize the web tier.

When you scale up a production environment, you will be billed at the daily rate for a temporary increase until you scale the environment back to its minimum size. If you want to permanently increase your minimum size, contact your Account Manager; the change will be billed at the annual rate until the end of your contract term.

Features
--------

Cloud Service Management packages for |acquia-product:ace| include the following features:

.. list-table::
 :widths: 50 50
 :header-rows: 1

 * - Feature
   - Amount
 * - |acquia-product:ccd| development environments
   - One per application, up to the maximum number of supported applications
 * - Staging environments
   - One per application
 * - Production environments
   - One per application
 * - Production file storage
   - 120GB shared across all applications
 * - Production database storage
   - 100GB shared across all applications
 * - Staging file storage
   - 120GB shared across all applications
 * - Staging database storage
   - 100GB shared across all applications
 * - Access to the `Acquia Cloud pipelines feature </acquia-cloud/develop/pipelines>`__, a continuous integration and continuous delivery tool
   - 

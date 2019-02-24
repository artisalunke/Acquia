.. include:: /common/global.rst

Configuring performance monitoring tools
========================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/monitor/apm/*

|acquia-product:ac| provides configurations for the New Relic
application, a performance monitoring (APM) tool that you can use with
an environment.

.. _newrelic:

About New Relic
---------------

`New Relic <https://newrelic.com/application-monitoring>`__ Application
Performance Monitoring (APM) is a web application performance management
tool that lets IT teams monitor live Drupal (and other PHP)
applications, troubleshoot issues, and tune for optimal performance.

.. note::  

   -  This does not include the `New Relic Server
      Monitoring <https://newrelic.com/products/infrastructure>`__ service,
      which is not supported on |acquia-product:ac|.
   -  For issues with legacy alerts failing, see `Legacy New Relic
      alerts </acquia-cloud/known-issues#new-relic-tls>`__.
   -  By default, the Acquia Support team does not have access to
      subscribers' New Relic accounts. To enable Acquia Support to access
      New Relic for your applications, add the following email address to
      the list of users associated with your New Relic account:

      ``support-systems+newrelic@acquia.com``

.. _config:

Configuring New Relic performance monitoring for an environment
---------------------------------------------------------------

To configure New Relic as the APM tool for an environment, complete the
following steps:

#. `Sign in <https://cloud.acquia.com>`__ to your |acquia-product:ac|
   account.
#. Select an application.
#. | Select an environment, and then click **Configure**.
   | The **Performance monitoring** section includes the **New Relic Pro
     Account ID**.

   |New Relic account ID|

#. Send an email to acquia@newrelic.com from the account owner's email
   address that includes the following information:

   -  Your full name
   -  Your company name
   -  Your **New Relic Pro Account ID**
   -  Your company's email address
   -  Your account ID for your existing, paid New Relic APM
      subscription, if you have one.

The next steps depend on your whether or not you have an existing New
Relic subscription:

-  *If you are new to New Relic and do not have a paid Application
   Performance Monitoring (APM) subscription* |br|
   New Relic will contact you to discuss the subscription that fits your
   needs. You will be given temporary access to your data in the New
   Relic Pro account during this evaluation period. After you purchase
   APM, you will be provided indefinite access to your New Relic pro
   account, until you choose to cancel your paid APM subscription.
-  *If you already have a paid APM subscription* |br|
   Include your APM account ID in your email to New Relic. New Relic
   will make the New Relic Pro account a *sub-account* of your existing,
   paid New Relic account, which will enable your existing subscription
   to monitor your Acquia environment. You may need to purchase
   additional licenses, depending on how large your Acquia environment
   is and whether your current licenses are able to accommodate the
   additional hosts.

If you need to remove the New Relic code from your website due to a
conflict with JavaScript included in your codebase, `contact Acquia
Support </support#contact>`__.

.. note::  

   If your non-production environments are on shared hardware, performance
   data provided by these environments may be skewed by the activity of
   other websites on the instance during periods of high activity.

.. _additional:

Additional features
-------------------

In addition to monitoring your production website, enhanced capabilities
are also available:

-  `Non-production environments <#non-prod>`__ can be monitored with the
   same account
-  `Multisite installations <#multi>`__ are supported
-  `Drush and external calls <#drush>`__ can be monitored

.. _non-prod:

Non-production environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your non-production Acquia environments can also report to your existing
paid New Relic account. To set this up, `create an Acquia Support
ticket </support#contact>`__.

.. _multi:

New Relic multisite capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

New Relic can be used with multisite installations. See `Using New Relic
monitoring in a multisite
environment </acquia-cloud/monitor/apm/multisite>`__ for details. If you
are using |acquia-product:edg|, see the |acsfusers|_ section of
that article.


.. |acsfusers| replace:: \ |acquia-product:edg|\  users
.. _acsfusers: /acquia-cloud/monitor/apm/multisite#site-factory

.. _drush:

Using New Relic to monitor Drush
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use New Relic to monitor Drush and its use of external calls by
adding this code snippet to your ``drush.ini`` file:

.. code-block:: none

   extension=newrelic.so
   newrelic.license="[LICENSE_KEY]"
   newrelic.appname="[sitename].[env]"

where the ``[LICENSE_KEY]`` is your New Relic key, and
``[sitename].[env]`` is the environment that you want to monitor.

.. _compat:

Compatibility statement
-----------------------

|acquia-product:ac| is compatible with only the Application Monitoring
services provided by New Relic. Acquia does not support New Relic Server
Monitoring services, or any plug-ins.

.. note::  

   Acquia can not make changes to the New Relic agent on a per-client basis.

Acquia does not support the installation of New Relic on any non-web
instances, except for dedicated search instances. While New Relic
routinely make updates to their services and periodically adds new
features, Acquia updates the versions of this service running on
|acquia-product:ac| at most twice per year. This allows us to thoroughly
test updates when they do occur, and it helps us to ensure that any new
features or feature changes included in these updates are in a stable,
non-beta state prior to release.

.. |New Relic account ID| image:: https://cdn3.webdamdb.com/1280_guSa4YWBCxr0.png?1526476092
   :width: 620px
   :height: 216px

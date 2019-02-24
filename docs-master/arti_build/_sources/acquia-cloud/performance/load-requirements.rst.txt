.. include:: /common/global.rst

Load testing requirements
=========================

.. container:: internal-navigation

   **Load testing on Acquia Cloud Enterprise**

   * :doc:`Preparing </acquia-cloud/performance/load>`
   * Needs

For most applications, load and stress testing should be an integral
part of development. By sending a predetermined amount of simulated
traffic to an application, you can pinpoint slow pages using application
monitoring tools (such as New Relic), identify bugs in your code, and
determine if your existing hardware is able to withstand normal or
elevated traffic levels. Whether you can perform load and stress testing
on your application on |acquia-product:ac| depends on your subscription
level.

This page describes the different |acquia-product:ace| hardware
requirements for load testing, based on your subscription:

-  :ref:`Acquia Cloud Professional and Acquia Cloud Free <free>`
-  |acquia-product:ace| :ref:`with shared load balancers (Production
   environment is not yet live) <shareddev>`
-  |acquia-product:ace| :ref:`with shared load balancers (live Production
   environment) <sharedlive>`
-  |acquia-product:ace| :ref:`with dedicated load
   balancers <dedicatedload>`

After you have reviewed the requirements, see `Load
testing </acquia-cloud/performance/load>`__ for information about how to
prepare for and carry out load testing on |acquia-product:ace|.

.. admonition:: Definition: Load testing versus stress testing

    A true load test can be performed only with the hardware and
    configuration that matches your application's Production environment.
    You cannot expect to get the same results by running test traffic
    against a Staging environment. That said, if it is not possible to
    perform a load test, due to reasons of cost or other resources, an
    application stress test that runs a significant load of test traffic on
    a Staging environment can still help identify bottlenecks and other
    performance issues.

.. _free:

Testing for |acquia-product:acs| and |acquia-product:acfs|
----------------------------------------------------------

Because |acquia-product:acs| and |acquia-product:acfs| applications rely
on shared load balancing hardware that is being used by other customers,
and since dedicated load balancers are not available on these platforms,
Acquia does not permit any volume of load or stress testing on either
|acquia-product:acs| or |acquia-product:acfs| in any environment
(Production or non-Production). This allows us to better ensure that
other customers' applications are not impacted by any other
application's development efforts.

.. _shareddev:

|acquia-product:ace| with shared load balancers, not yet live
-------------------------------------------------------------

If you are an |acquia-product:ace| customer with shared load balancers
in front of your Production environment, Acquia offers two options that
can enable you to perform load testing, assuming your Production
environment is not yet live:

-  Acquia can provide one test load balancer for a single four-hour
   window. Although there is no charge for this option, you must request
   this by `filing a Support ticket </support/tickets>`__ with at least
   five business days' advance notice. This option is available one time
   per subscription, and you will need to configure a custom domain name
   with your DNS provider and point it to the IP address that Acquia
   provides prior to the provided window. The load test cannot start
   before or end after the window provided; otherwise it may impact the
   results of other customers who have also reserved the hardware for
   that day.
-  For an additional charge, Acquia can provision a pair of dedicated
   load balancers for a minimum period of one week. You must provide
   five business days' advance notice. Contact your Acquia Account
   Manager to obtain more information on pricing or to make this
   request.

You can perform load tests on your |acquia-product:ace| *Production*
environment only if you choose one of these two options. This is
necessary to ensure that other customers' live, production applications
aren't impacted by another application's load testing. Acquia does not
permit load tests on any non-Production environments on shared staging
servers.

.. _sharedlive:

|acquia-product:ace| with shared load balancers, live
-----------------------------------------------------

If you are an |acquia-product:ace| customer with shared load balancers
in front of your Production environment and your applications are
already live, Acquia offers several alternatives for application stress
testing:

-  If you have a dedicated non-production server (for example, if you
   have a dedicated server for your Development environment, Staging
   environment, or a custom non-Production environment), Acquia can
   provide one test load balancer for a single four-hour window.
   Although there is no charge for this option, you must request this by
   `filing a Support ticket </support/tickets>`__ with at least five
   business days' advance notice. This option is available one time per
   subscription, and you will need to configure a custom domain name
   with your DNS provider and point it to the IP address that Acquia
   provides prior to the provided window. The load test cannot start
   before or end after the window provided; otherwise it may impact the
   results of other customers who have also reserved the hardware for
   that day.
-  If your non-Production environments are on a shared server, for an
   additional charge Acquia can provision a pair of dedicated load
   balancers for a minimum period of one week. You must provide five
   business days' advance notice. Contact your Acquia Account Manager to
   obtain more information on pricing or to make this request.

For the most accurate results possible on a non-Production environment,
you may wish to consider a `dedicated load testing
environment <#dedicatedtest>`__ that duplicates your Production
environment.

.. _dedicatedload:

Testing on |acquia-product:ace| with dedicated load balancers
-------------------------------------------------------------

If you are an |acquia-product:ace| customer with dedicated load
balancers in front of any environment, you can perform an application
stress test at any time, as you first `file a Support
ticket </support/tickets>`__ and that ticket is acknowledged by Acquia
Support. This advance notice gives us a chance to notify all of our
technicians that a load test will take place and prevents Acquia from
blocking traffic that would look suspicious if we did not know it was a
test.

When you submit this request to Acquia Support, include the date and
times (including the time zone) of the planned test, and also indicate
whether the traffic will be either anonymous or authenticated.

If your application has not yet gone live, you can run a load test on
your Production environment. After your application has gone live,
consider using instead a `dedicated load testing
environment <#dedicatedtest>`__ that duplicates your *Production*
environment. This will provide the most accurate results possible on a
non-Production environment.

.. _dedicatedtest:

Testing with a dedicated load testing environment
-------------------------------------------------

For a true load test, you should test against either your *Production*
environment or a testing environment that duplicates your Production
environment. If you are an |acquia-product:ace| customer who cannot
perform load tests on a Production environment without impacting
existing live applications, Acquia strongly recommends that you arrange
for a dedicated load testing environment that duplicates your Production
environment.

While load testing on standard non-Production environments may help
identify general bottlenecks and issues, it is important to note that
non-production hardware does not usually match the hardware in place for
your Production environment, which can significantly skew your results.
To achieve the most accurate results possible, Acquia can provision a
dedicated load testing environment with hardware that is identical to
what is running in your Production environment. We require five business
days' advance notice, and there will be a charge for the additional
hardware. Contact your Acquia Account Manager to obtain more information
on pricing or to make this request.

.. _related:

Related topics
--------------

-  `Preparing for security and penetration
   testing <%5Bacquia-product:kb%5Darticles/preparing-security-penetration-or-load-testing>`__
-  `Getting started with
   BlazeMeter <%5Bacquia-product:kb%5Darticles/getting-started-blazemeter>`__

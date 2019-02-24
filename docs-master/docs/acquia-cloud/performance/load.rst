.. include:: /common/global.rst

Load and stress testing
=======================

.. container:: message-status

      *Load testing is available only for Acquia Cloud Enterprise-hosted
      applications*

.. container:: internal-navigation

   **Load testing on Acquia Cloud Enterprise**

   * Preparing
   * :doc:`Needs </acquia-cloud/performance/load-requirements>`

It is important to ensure that your application and its hosting platform
can handle the traffic that you expect. Using *load testing*, you can
evaluate your application's future performance under controlled
circumstances. You may also want to perform load testing if you expect
one of your applications to experience a surge in popularity for
whatever reason.

.. note::

      Be sure to `contact Acquia Support </support#contact>`__ before any
      `expected high-traffic events </support/traffic>`__.

This page describes how to prepare for and carry out load testing on
|acquia-product:ace|. Because |acquia-product:acs| and
|acquia-product:acfs| websites rely on shared load balancing hardware
that's being used by other customers, Acquia does not permit load or
stress testing with these applications. For more information, see
`Testing for Acquia Cloud Professional and
Acquia Cloud Free </acquia-cloud/performance/load-requirements#free>`__.

Even though you may have experience evaluating your application's
performance using `security and penetration
testing <%https://support.acquia.com/hc/en-us/search?utf8=%E2%9C%93&query=/preparing-security-and-penetration-testing>`__
or `vulnerability scans </acquia-cloud/arch/vuln>`__, load testing can
require a significant amount of additional preparation and resources.
For information about |acquia-product:ace| subscription and hardware
requirements, see `Load testing
requirements </acquia-cloud/performance/load-requirements>`__.

Applications with more than 5% authenticated and non-cacheable traffic
should have a load test that targets the most common use cases, and the
same is true for websites that have a large amount of anonymous traffic
or a significant number of editorial users. Ideally, you should perform
load tests before the following events:

-  Launching a new hardware configuration
-  Launching a major change to an application's code (including a new
   theme, a mobile version of the application, or a new splash page)
-  Initiating a major marketing campaign

.. _guide:

Guidelines for load testing
---------------------------

To perform a load test in the safest and most effective manner, review
the `load testing
requirements </acquia-cloud/performance/load-requirements>`__ for your
|acquia-product:ac| configuration, which are based on the following
guidelines:

-  **Use only dedicated equipment for a load test**
   |acquia-product:ace| customers can purchase dedicated equipment for
   testing. This includes the web stack, search farms, and load
   balancers. This prevents the extreme resource utilization generated
   by a load test from affecting other customers. `Contact Acquia
   Support </support#contact>`__ both to provision load test equipment
   and to schedule a load test. A load test is meaningful only if the
   test is run on a clone of the production stack. If there are no live
   applications on the Production environment, you can run tests
   directly on Production.
-  **Provide Acquia with at least five business days' notice before a
   load test**
   If temporary hardware is needed, Acquia will need more lead time to
   place the hardware. At a minimum, Acquia needs the date and time of
   the load test and the list of the individual originating IPs that
   will generate traffic. These IP addresses must be individual IP
   addresses, and can not be IP address ranges or CIDR blocks.

.. note::

      For |acquia-product:ace|, the bandwidth on the load balancer maxes out
      at approximately 50Mbps. On tests that are mostly hitting a few pages
      with anonymous traffic, that may be the cap for data. If more bandwidth
      is needed, you will need an elastic load balancer that will route
      traffic in a round-robin to the available load balancers, which
      effectively multiplies the available bandwidth. This differs from the
      normal configuration where the secondary balancer idles awaiting the
      failure of the primary.

.. _before:

Before you start a load test
----------------------------

A load test is only effective if you are fully prepared for it. Use the
following recommendations to help you prepare for your load test:

.. note::

      A load test should mirror the anonymous and authenticated traffic
      percentages, to ensure that the application stack can handle the load.
      Testing anonymous traffic on a website that will use authenticated users
      will give inaccurate results. Applications with more than 5%
      authenticated and non-cacheable traffic should have a load test that
      targets the most common use cases.

-  **Be sure that your application is ready** - Be sure that Drupal is
   ready for a load test by addressing any issues flagged in
   |acquia-product:ais|. Verify that the theme registry is not being
   rebuilt on every page load.
-  **Develop a test plan** - A load test plan is an essential component
   of a successful load test. The time it takes to configure a robust
   and meaningful load test increases with the variables that affect
   performance for an application. A load test plan should take into
   account the following variables:

   -  How many applications will be tested? Are there multiple
      applications? Are there multiple
      docroots on the same server? Are you using multiple domains with `Domain
      Access <https://www.drupal.org/project/domain>`__?
   -  How many customer roles will be tested? You may have multiple
      anonymous, comment-only users and editors.
   -  Are you testing multiple languages? Multilingual implementations
      often have big implications.
   -  What are the kinds of tasks each user role will be expected to
      accomplish?
   -  What is the workflow and what pages will be involved in navigating
      those tasks?
   -  Have you created a list of form submissions to be mimicked?
   -  Have you considered asynchronous JavaScript requests? Applications
      using AJAX often reduce, but never eliminate, performance issues.
   -  Have you investigated your cache-clearing frequency? How does the
      application respond under load when caches clear or pages expire?
   -  Have you developed specialized planning for applications that use
      JavaScript heavily (for example, for presentations)?

-  **Determine your test goals** - If you don't have concrete goals, you
   won't be able to determine if a load test is successful. Here are
   some examples of goal sets for testing:

   -  Government website - 500 concurrent users "baseline test."
      Determine the system breakpoint by loading up to 500 concurrent
      users over 15 minutes and monitoring user and system metrics.
   -  Entertainment news website - This test was designed to identify
      any performance bottlenecks in the application. The goal was to
      ramp up to 1,000 users and confirm that the database bottleneck
      identified in the previous test was resolved.
   -  Political campaign - Analyze the application performance against
      the environment in the following scenarios: S01, S02, S03, S04 and
      S05 with 10,000 users and a 40-minute ramp.

      -  S01 - Web Browser (70% of load)
      -  S02 - Web Donate 1 (7.5% of load)
      -  S03 - Web Donate 2 (7.5% of load)
      -  S04 - Web Petition (7.5% of load)
      -  S05 - Web Register (7.5% of load)

   -  Retail chain - Analyze the application performance in the
      following scenarios: A, B, C, D, E, and F with 2,500 users and a
      40-minute ramp. Use three different locations to generate the
      load: US East (Virginia), US West (Northern California), and
      London. Indicate that the user had a ``local_store`` cookie set to
      a random store location when first entering the application. This
      is designed to mimic a user returning to the application after
      selecting a default store.

      -  Scenario A, Scenario A Cookie (30% of the load)
      -  Scenario B, Scenario B Cookie (30% of the load)
      -  Scenario C, Scenario C Cookie (20% of the load)
      -  Scenario D, Scenario D Cookie (1% of the load)
      -  Scenario E, Scenario E Cookie (8% of the load)
      -  Scenario F, Scenario F Cookie (11% of the load)

.. _recs:

Load testing recommendations
----------------------------

Load testing is the responsibility of the customer. Customers can engage
Acquia Professional Services for a performance audit, which is a
week-long code examination that is geared specifically for performance
and scalability. After your analysis has provided the items that could
be adjusted to improve performance, you can also engage Professional
Services to make those technical adjustments. If you have a Technical
Account Manager (TAM), you can ask for suggestions on how to best test
the application or for some post-testing analysis.

.. _need:

What Acquia needs to know
-------------------------

Before you begin testing, the Acquia Support team needs to know the
following information:

-  Exact start and end dates and times (including timezone) of the
   planned testing
-  Individual originating IP addresses conducting the testing
-  Expected methodologies and specific tools to be used in the process
   of the testing
-  Contact information for any third party that is conducting the
   testing (if being done by a third party)

After you have collected the required information, `contact Acquia
Support </support#contact>`__ to create a ticket, and include this
information. Be sure to notify the Support team at least two business
days in advance of your testing.

.. note::

      If you start a test without notifying Acquia Support and the test
      generates sufficient load, the |acquia-product:ac| platform will treat
      the test as a presumed attack and will block it. You will then be asked
      to make arrangements to put a dedicated test balancer in place for the
      test. This takes at least two business days to arrange.

Acquia Support will engage other internal teams to prepare for your
tests, as necessary.

.. _diy:

Do-it-yourself testing
----------------------

You can outline and set up a testing suite on your own using freely
available tools. For example, you can use a service like
`BlazeMeter <https://www.blazemeter.com/>`__ (which allows up to 40 free
tests) to configure your load test plan using
`JMeter <https://jmeter.apache.org/>`__.

You can test the JMeter plan locally (with looping off and only one user
per scenario). If everything is working, fill in the desired number of
users, enable forever looping, and upload the plan to BlazeMeter for
testing.

When load testing with BlazeMeter, you will need to start one or more
BlazeMeter servers depending on how much traffic you intend to receive
(which will incur an additional cost from BlazeMeter). Roughly speaking,
a test needs one BlazeMeter *large* server per 1MM (1 million
page-views/month) expected traffic.

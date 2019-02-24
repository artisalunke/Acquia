.. include:: /common/global.rst

Three pillars of a successful launch
====================================

Your |acquia-product:onb| team will coach you along the path to a
successful launch. Our engagement with your team is structured around
the following three critical elements of an application’s readiness for
launch.

-  `Caching <#cache>`__
-  `Accurate sizing <#sizing>`__
-  `Load testing <#load_testing>`__

.. _cache:

Caching
-------

Acquia leverages `Varnish Cache </acquia-cloud/performance/varnish>`__
on your load balancers and
`Memcached </acquia-cloud/performance/memcached>`__ on your web servers
to ensure your application is as performant and scalable as possible.
Varnish works by eliminating the need for your backend web servers to
process every request sent to the application. Under high traffic
conditions, Varnish is able to serve requests from cache more quickly
than your web servers can. Memcached improves the performance of your
web servers when serving authenticated traffic. Applications with a high
percentage of authenticated users benefit most from this caching
technology.

Taken together, and properly configured, Varnish and Memcached are
critical elements of your application’s ability to scale and perform. We
encourage you to engage with us to help you determine how to make your
application as cacheable as possible, given your application’s
functional requirements.

.. _sizing:

Accurate sizing
---------------

When you purchased Acquia’s hosting services, you should have completed
an infrastructure questionnaire. Acquia uses this questionnaire to
estimate the appropriate hardware for your application, including the
following key information:

-  How many pageviews your application serves
-  ŽWhat percentage of your traffic is from authenticated users
-  ŽCurrent PHP memory limit

Other factors may affect your sizing, such as the number of applications
you have in a multisite configuration, and how many
`docroots <%5Bacquia-product:kb%5Darticles/docroot-definition>`__ are
hosted on a given server.

Unless we know otherwise, we assume that 90 percent of your anonymous
traffic is cached by Varnish. If your application doesn’t cache
efficiently, you may need to engage Acquia to reassess your sizing
before proceeding with load testing and launch.

If you are properly sized based on your traffic expectations and caching
efficiency, and your application continues to suffer from degraded
performance, Acquia will work with you to identify and remediate
performance-affecting conditions in your application’s code and
configuration.

.. _load_testing:

Load Testing
------------

The best way to understand how your application will perform at launch
is to create a load test that accurately simulates real-world
conditions. If your application is newly developed, you may not have
accurate data about how users access your application. In this case, you
must make educated guesses based on your understanding of your audience
and on patterns for similar applications.

Developing an accurate load test requires time, effort, and forethought.
Do not leave this activity until the last minute. Instead:

-  Plan to start testing early in your development cycle. Many
   successful teams test at the end of every cycle.
-  ŽReview your infrastructure questionnaire to be sure the traffic
   expectations are accurate. If you aren’t sure, ask an
   |acquia-product:onb| engineer to validate your sizing.
-  Calculate concurrent users based on actual traffic expectations, as
   indicated on your hosting questionnaire.
-  Understand how to calculate the number of concurrent users to test,
   based on the traffic you indicated in your hosting questionnaire.
-  Test all the major sections of your application that you expect to
   receive traffic. A test that loads only the homepage isn’t helpful
   unless you expect users to only visit the homepage.

The |acquia-product:onb| team is available to talk through all your
questions about load testing. For customers with shared load balancers,
Acquia provides limited support for load testing by offering
complimentary access to a dedicated balancer for a period of 48 hours.
The baseline expectations for load testing are:

#. Engage with your |acquia-product:onb| team well in advance of your
   test, so we can understand your goals and advise you of best
   practices. It takes time to design and implement a good load test, so
   do not leave this until the last minute.
#. Leverage our sample load test plan (provided by your Customer
   Onboarding Manager (COM)) to build a test plan that aligns with your
   goals and conforms to best practices.
#. Schedule your complimentary 48 hours of load balancer time for when
   your code is complete, but still leave enough time before launch to
   remediate any issues that your test may surface.
#. Engage with your Customer Onboarding Engineer (COE) to perform a site
   review at least 48 hours prior to conducting a test.
#. Share your load test results with your COE immediately, so we can
   assemble an analysis. This must be done promptly to avoid key data
   from rotating out of our logs before we can analyze them.

Ideally, you should secure dedicated balancers (if you don’t already
have them) for a period of time sufficient to load test at the end of
each development cycle. Acquia does not presently allow you to load test
on |acquia-product:acs| (ACP). If you are an ACP customer and load
testing is in your critical path (as it should be), you should contact
your |acquia-product:onb| team to discuss upgrading to
|acquia-product:ace|.

For additional information, see `Load and stress
testing </acquia-cloud/performance/load>`__.

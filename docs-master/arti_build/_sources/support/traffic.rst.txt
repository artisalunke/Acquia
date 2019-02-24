.. include:: /common/global.rst

Preparing for a high-traffic event
==================================

.. toctree::
   :hidden:
   :glob:

   /support/traffic/*

If you're an Acquia customer and are expecting an event that will send a significant amount of traffic to your website, we encourage you to `contact Acquia Support </support#contact>`__ well in advance, so that they can help you prevent a website outage by auditing your website's performance, and then, if necessary, scheduling an `upsize to your hardware </support/traffic/upsize>`__. Events that can cause enough traffic to affect your website's availability include:

-  Website launches
-  Marketing campaigns
-  Performances
-  Penetration testing

Creating a support ticket
-------------------------

To help prevent a website outage during a traffic event, `contact Acquia support </support#contact>`__ in advance of your event and provide as much of the following information as you can:

-  The date and time of the website launch or event (including the timezone).
-  The expected website traffic during the event.
-  Will traffic be primarily either authenticated user traffic or anonymous traffic?
-  Will the entire website see increased traffic, or just specific URLs?

If you are performing penetration testing, provide the following additional details:

-  Exact start and end dates and times (including timezone) of the planned testing
-  Originating IP addresses conducting the testing
-  Expected methodologies and specific tools to be used in the process of the security testing
-  Contact information for any third party that is conducting the testing (if being done by a third party)

The more accuracy that you can provide, the better Acquia Support's recommendations will be. For example, if your website expects mostly anonymous traffic during a high-traffic event, and not authenticated traffic, aggressive caching may be a better (and less expensive) option.

You may be asked if you would like for Acquia to upsize your server based on load for you. Because upsizing requires lead time and often involves an additional cost, you may want to involve your account manager. |acquia-product:ace| customers can be upsized without warning, based on their contract, to maintain service during unexpected demand.

.. note:: 

   Acquia recommends that you provide notice seven days before any penetration testing or other event that may require an upsize.

If you do not create a ticket with Acquia Support before starting a test and the test generates sufficient load, the |acquia-product:ac| platform will treat the test as a presumed attack, and will block it. You will then be asked to make arrangements to put a dedicated test balancer in place for the test.

Logs on |acquia-product:ac| are not kept in the event of upsizing. If you want to ensure that logs are stored permanently, you should routinely copy log files to permanent storage. `Learn more </acquia-cloud/monitor/logs#cli>`__.

If an upsize is requested, be as prepared with as many details as possible on the specific anticipated amount of authenticated versus anonymous high traffic.

For more information about resizing your server, see the `Resize section </acquia-cloud/manage/servers#resize>`__ of the `Managing your servers </acquia-cloud/manage/servers>`__ |acquia-product:ac| documentation.

If you are using elastic load balancers (ELBs), you may also find Amazon's suggestions on `pre-warming the load balancer <http://aws.amazon.com/articles/1636185810492479#pre-warming>`__ useful. ELBs are not intended to handle traffic spikes — they're intended to handle a steady increase in traffic. The balancers should be set to expect the highest level of traffic before the test begins.

If you think this may be necessary for your event, contact your Acquia account manager for details, and be prepared to provide the following information:

-  What is the DNS name for the ELB(s) that require manual scaling?
-  An approximate increase percentage in traffic, or expected requests/sec that will go through the load balancer (whichever is easier to answer).
-  The average amount of data passing through the ELB per request/response pair.
-  The rate of traffic increase expected. This can be a qualitative value such as "this should increase steadily over the span of an hour," or "we expect traffic to increase suddenly once our sale/event is announced."
-  Expected percent of traffic going through the ELB that will be using SSL termination.
-  Is the back-end currently scaled to the level it will be during the event?
-  When will your event start?
-  When do you expect the event will end?
-  A brief description of your use case, with a detailed explanation of your expected (if you're going to deviate from the normal request pattern) and normal traffic patterns.

For more information on preparing for an increase in traffic on your website, see `Load and stress testing </acquia-cloud/performance/load>`__.

Website launch recommendations
------------------------------

If your anticipated event is a website launch, we recommend reviewing the `prelaunch checklist </acquia-cloud/migrate/checklist>`__ to ensure that you have addressed the basics of website readiness requirements.

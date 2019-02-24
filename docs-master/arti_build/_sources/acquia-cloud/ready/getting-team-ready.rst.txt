.. include:: /common/global.rst

Getting your team ready
=======================

Even before you engage with the |acquia-product:onb| team, you can
undertake a few activities to prepare your teams and your application
for an efficient and low-friction onboarding process.

.. _prep:

Preparing your website
----------------------

+-----------------------------------+-----------------------------------+
| Action                            | Description                       |
+===================================+===================================+
| Review your subscription          | You can `access and review your   |
|                                   | subscription </acquia-cloud/subs> |
|                                   | `__                               |
|                                   | even before we conduct the        |
|                                   | welcome call, network             |
|                                   | walkthrough, and technical        |
|                                   | review. Write down any questions  |
|                                   | you have, so we can focus on the  |
|                                   | right topics with you.            |
+-----------------------------------+-----------------------------------+
| Locate and bookmark Acquia’s      | Acquia has an extensive knowledge |
| online documentation              | base. A good place to get started |
|                                   | is the `|acquia-product:ac|       |
|                                   | documentation </acquia-cloud>`__. |
+-----------------------------------+-----------------------------------+
| Review our online training        | Acquia `offers                    |
| courses                           | training <https://training.acquia |
|                                   | .com/>`__                         |
|                                   | covering key platform and Drupal  |
|                                   | concepts.                         |
+-----------------------------------+-----------------------------------+
| Install                           | |acquia-product:anc| allows your  |
| `|acquia-product:anc| <https://ww | application to connect to         |
| w.drupal.org/project/acquia_conne | Acquia’s network to enable        |
| ctor>`__                          | |acquia-product:ais|,             |
|                                   | |acquia-product:as|, and other    |
|                                   | key features of your              |
|                                   | subscription. **This activity is  |
|                                   | included with                     |
|                                   | `|acquia-product:onb| Concierge   |
|                                   | service <https://www.acquia.com/r |
|                                   | esources/collateral/acquia-ready- |
|                                   | concierge-data-sheet>`__.**       |
+-----------------------------------+-----------------------------------+
| Install                           | **This activity is included with  |
| `Memcached </acquia-cloud/perform | |acquia-product:onb| Concierge    |
| ance/memcached>`__                | service.**                        |
+-----------------------------------+-----------------------------------+
| Enable `New                       | Enabling an application           |
| Relic </acquia-cloud/monitor/apm> | performance monitoring tool like  |
| `__                               | New Relic is a critical step in   |
|                                   | getting your application ready    |
|                                   | for testing and launch. Your      |
|                                   | |acquia-product:onb| team can     |
|                                   | help you with this.               |
+-----------------------------------+-----------------------------------+
| Ensure your Drupal core and       | Keeping your code up to date is a |
| contributed modules are up to     | critical maintenance task that    |
| date                              | you should be performing          |
|                                   | regularly. The                    |
|                                   | |acquia-product:onb| team applies |
|                                   | security updates where needed,    |
|                                   | but to get a head start on the    |
|                                   | process, you can do this in       |
|                                   | advance of engaging us.           |
+-----------------------------------+-----------------------------------+
| Validate your caching strategy    | Acquia leverages Varnish Cache to |
|                                   | ensure your application is highly |
|                                   | available and scalable. You       |
|                                   | should plan your `caching         |
|                                   | strategy <%5Bacquia-product:kb%5D |
|                                   | articles/caching-overview>`__     |
|                                   | carefully, and you should avoid   |
|                                   | building features that prevent    |
|                                   | your application from being       |
|                                   | cacheable.                        |
+-----------------------------------+-----------------------------------+
| Validate your search requirements | |acquia-product:as| wraps Apache  |
|                                   | Solr. If you already know you     |
|                                   | will rely upon a particular       |
|                                   | version of Solr, or if you have   |
|                                   | `customizations in your Solr      |
|                                   | configuration </acquia-search/con |
|                                   | fig>`__,                          |
|                                   | you should work with us to ensure |
|                                   | those customizations are          |
|                                   | compatible with                   |
|                                   | |acquia-product:ac|.              |
+-----------------------------------+-----------------------------------+
| Plan for SSL                      | Understand your security and      |
|                                   | privacy requirements. Be clear    |
|                                   | about your options for SSL and    |
|                                   | supporting modules.               |
+-----------------------------------+-----------------------------------+
| Plan for `load                    | Acquia requires at least 48 hours |
| testing </acquia-cloud/performanc | of lead time for many load        |
| e/load>`__                        | test-related activities,          |
|                                   | including load test balancer      |
|                                   | provisioning, site review, and    |
|                                   | load test analysis.               |
+-----------------------------------+-----------------------------------+

You may also find some of the suggestions outlined in `Preparing your
site for
|acquia-product:ac| <%5Bacquia-product:kb%5Darticles/preparing-your-site-acquia-cloud>`__
helpful. Your |acquia-product:onb| will help you with some of these
tasks, but you should evaluate your applications individually.

.. _engage:

Engage with |acquia-product:onb|
--------------------------------

Once you engage with |acquia-product:onb|, the following activities are
critical to a successful onboarding. Your COM guides you through these
activities, but please pay close attention to all requirements, as some
of these activities are time sensitive and need careful planning to
complete successfully.

+-----------------------+-----------------------+-----------------------+
| Activity              | Timing requirements   | Responsibility        |
+=======================+=======================+=======================+
| Provision             | Within two business   | |acquia-product:onb|  |
| subscription and      | days of final order   |                       |
| hardware              | receipt               |                       |
+-----------------------+-----------------------+-----------------------+
| Attend welcome call   | Within three business | |acquia-product:onb|, |
|                       | days of welcome email | with business         |
|                       | deployment            | stakeholders          |
+-----------------------+-----------------------+-----------------------+
| Perform network       | Can be combined with  | |acquia-product:onb|  |
| walkthrough           | technical review call | with development team |
|                       | (below)               | and other technical   |
|                       |                       | stakeholders          |
+-----------------------+-----------------------+-----------------------+
| Perform technical     | Minimum two business  | |acquia-product:onb|  |
| review call           | days before initial   | with development team |
|                       | migration. Can be     | and other technical   |
|                       | combined with network | stakeholders          |
|                       | walkthrough (above)   |                       |
+-----------------------+-----------------------+-----------------------+
| Perform initial       | Validated by Customer | |acquia-product:onb|  |
| migration (available  | Onboarding Engineer   |                       |
| with optional         | (COE) upon receiving  |                       |
| Migration Services    | access                |                       |
| add-on)               |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Perform intermediate  | Validated by COE and  | |acquia-product:onb|  |
| migration (available  | dependent on          |                       |
| with optional         | development timeline  |                       |
| Migration Services    |                       |                       |
| add-on)               |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Inform Acquia of      | Minimum of four       | Development team      |
| plans to load test    | business days before  |                       |
|                       | scheduled load test   |                       |
+-----------------------+-----------------------+-----------------------+
| Perform code freeze   | Minimum of two        | |acquia-product:onb|  |
| and site review       | business days before  | conducts site review. |
|                       | scheduled load test   | Development team      |
|                       |                       | finalizes all changes |
|                       |                       | prior to site review  |
+-----------------------+-----------------------+-----------------------+
| Perform load test     | Minimum of seven      | Development or load   |
|                       | business days prior   | testing team          |
|                       | to scheduled website  |                       |
|                       | launch to allow       |                       |
|                       | opportunity to        |                       |
|                       | remediate any         |                       |
|                       | discovered issues     |                       |
+-----------------------+-----------------------+-----------------------+
| Perform load test     | Up to two business    | |acquia-product:onb|  |
| analysis and          | days after load test  |                       |
| recommendations       |                       |                       |
+-----------------------+-----------------------+-----------------------+
| Launch website        | Provided by customer  | Customer              |
+-----------------------+-----------------------+-----------------------+

.. _help:

Getting help
------------

During your Acquia platform walkthrough, |acquia-product:onb| shows you
how to `contact Acquia Support </support#contact>`__. Most of your
day-to-day access to our team is conducted through tickets to ensure all
communication is recorded and trackable. Our support engineers are able
to answer all questions about the |acquia-product:ac| platform and
Drupal best practices.

If you bought Concierge-level or migration services, an
|acquia-product:onb| engineer may be able to make certain modifications
to your application on your behalf. However, |acquia-product:onb| is not
able to engage in development services, including any direct
modification of code on your servers.

In addition to support tickets, we encourage you to set up `advisory
time </support/guide#advisory_services>`__ to discuss Drupal and
especially |acquia-product:ac| platform best practices. Common advisory
call topics include SSL, caching, module recommendations, load testing,
and many other topics. See the `Support User's Guide </support/guide>`__
for full details on working with the Acquia Support team.

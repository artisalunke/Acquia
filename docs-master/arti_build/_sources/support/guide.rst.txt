.. include:: /common/global.rst

Support Users Guide
===================

.. admonition:: Revision date: 2 April 2018

   To view the most current version of this guide, visit `http://docs.acquia.com/support/guide </support/guide>`__.


This Support Users Guide describes the specific Support services
provided by Acquia to our customers. Acquia will update this guide from
time-to-time to reflect enhancements to our service and policy updates.

-  `Contacting Acquia Support <#contact_support>`__

   -  `Hours of operation <#hours>`__
   -  `Problem definition categories <#problem>`__
   -  `Site launches <#launches>`__
   -  `Submitting critical support requests <#critical_requests>`__
   -  `Submitting all other support requests <#other_requests>`__
   -  `Local language support <#language>`__

-  `Scope of Support services <#scope_support>`__

   -  `Overview of Acquia subscriptions <#overview_subscriptions>`__
   -  `Supportability matrix <#supportability>`__
   -  `Supported software life cycle <#supported_lifecycle>`__
   -  `Life cycle description <#lifecycle_description>`__
   -  `Supported software environments <#supported_environments>`__
   -  `Platform maintenance and security
      upgrades <#platform_maintenance>`__
   -  `Root cause analysis <#rca>`__
   -  `Installation of custom PHP extensions <#php-extensions>`__
   -  `Installation of custom VCLs <#custom-vcl>`__
   -  `Drupal docroot support <#docroot-policy>`__
   -  `Node.js runtime version support <#node>`__
   -  `Out-of-scope applications <#out-of-scope_applications>`__
   -  `Infrastructure support <#infrastructure_support>`__
   -  `Use of shared resources <#shared_resources>`__
   -  `Removal from monitoring due to chronic application
      issues <#removal>`__
   -  `Long-running queries <#slow-queries>`__
   -  `Advisory services <#advisory_services>`__
   -  `Ticket limitations <#ticket_limitations>`__
   -  `Emergency hardware resizing <#resizing>`__

-  `Escalation process <#escalation_process>`__
-  `Customer resources <#customer_resources>`__

   -  `|acquia-product:lib| <#library>`__
   -  `Support Portal <#support_portal>`__
   -  `Support policies <#support_policies>`__
   -  `Customer success tips <#customer_success>`__

-  `Remote Administration <#ra>`__

   -  `Overview of service <#ra_overview>`__

.. _contact_support:

Contacting Acquia Support
-------------------------

.. _hours:

Hours of operation
~~~~~~~~~~~~~~~~~~

Standard hours of operation for Acquia Support are as follows:

+-----------------------+-----------------------+-----------------------+
| Region                | Hours                 | Phone Number(s)       |
+=======================+=======================+=======================+
| Americas              | 8am - 8pm Eastern     | +1-844-373-2128       |
|                       | Time Monday-Friday    |                       |
+-----------------------+-----------------------+-----------------------+
| Europe                | 8am - 6pm Central     | +44 -1865-520-011     |
|                       | Europe Time           |                       |
|                       | Monday-Friday         |                       |
+-----------------------+-----------------------+-----------------------+
| Asia-Pacific and      | 8am - 6pm AEST        | +61-2-8319-9389       |
| Japan                 | Monday-Friday         |                       |
+-----------------------+-----------------------+-----------------------+

.. note::  Coverage for `major holidays <https://holidays.acquia.com>`__ is limited
   to Critical issues only.


Customers with Starter, Basic, Business, Premium, and Elite
Subscriptions or legacy Elite, Enterprise and Professional Plus
subscriptions, or |acquia-product:cha| subscriptions are entitled to
24x7x365 for Critical issues. For complete information on how to open a
ticket with Acquia Support, see `How to file a support
ticket </support/tickets>`__.

For more information, see `Coverage Areas and Hours of
Operation <https://www.acquia.com/drupal-support/coverage-areas-and-hours-operation>`__.

.. _problem:

Problem definition categories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Acquia describes the urgency of support requests as indicated in the
following table. Acquia responds to the submitted ticket based on the
urgency indicated by the Customer at the time of ticket/issue
submission.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Urgency
     - Description
   * - Critical
     - Customer's production system is inoperative; or Customer's production operations or productivity are severely impacted with no available workaround; or is a critical security issue. Critical issues are eligible for 24x7 support for certain Acquia subscriptions.
   * - High
     - Customer’s production system is operating but issue is causing disruption of Customer’s business operations; workaround cannot be used for an extended period. This is the highest designation available for development and help desk questions
   * - Medium
     - Customer's system is operating and the issue’s impact on the Customer's business operations is moderate to low; a workaround or alternative is available.
   * - Low
     - Issue is a minor inconvenience and does not impact business operations in any significant way; issues with little or no time sensitivity.


For more information, see `Issue Urgency
Definitions <https://www.acquia.com/drupal-support/issue-urgency-definitions>`__.

.. _launches:

Site launches
~~~~~~~~~~~~~

Support coverage outside normal business hours is limited to the
mitigation of Critical issues as outlined previously in the `Problem
definition categories <#problem>`__ section. Customers are highly
encouraged to launch during normal business hours when technical teams
are fully staffed and the scope of coverage goes beyond limited Critical
issue mitigation.

Acquia treats issues that prevent a website from launching as critical
and eligible for 24x7 support if all of the following conditions apply:

-  The deployed website code and configuration have passed functional
   and load tests by the customer’s project team. (Site development is
   complete.)
-  The Customer Risk Report (CRR) provided by Acquia Ready includes no
   critical (red) items.
-  Launch is less than three calendar days away.
-  Launch date has been registered and confirmed with either Acquia
   Support or Acquia Ready at least seven days prior to expected launch.
-  Customer subscription level provides for 24x7 critical support.

.. _critical_requests:

Submitting critical support requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For issues that meet the criteria of a Critical, Customers may report
the issues using an online ticket (preferred method) or by telephone.
24x7x365 support is available only to Customers with or Starter, Basic,
Business, Premium, and Elite Subscriptions, or legacy Pro Plus,
Enterprise or Elite Support subscriptions. Refer to your current order
form or contact your Account Manager if you are unsure.

-  *Online Ticket* - Tickets designated with Critical urgency initiate
   internal alerts and designate the request for a priority response.
-  *Phone* - When filing a Critical request by phone, press **6** from
   the main menu. This is a silent option not listed in the voice
   prompt. You will be directed to the Critical support voicemail. Leave
   a message with the name and phone number of the technical contact to
   be contacted, Website name, and a description of the issue. Be sure
   to include a clear description of the symptoms and any actions taken
   that may be related to the cause or attempted remedies.

Acquia’s on-call support team member will take the following actions:

-  *Initial action* - Contact the Customer reporting the issue or as
   otherwise designated.
-  *Before changes are made* - Request confirmation in a ticket for
   changes to the website or configuration that were requested verbally.
-  *Ongoing action* - Issue regular Customer and internal updates until
   resolution.

.. note::  Automated ticket submissions generated by internal or external infrastructure or website monitoring applications are not permitted. Acquia no longer accepts new support requests through acquia.com email addresses and only supports updates to tickets submitted online through this channel. Receipt of excessive automated email to any acquia.com address will result in the sender's address being blocked.


.. _other_requests:

Submitting all other support requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for all non-Critical issues is available during Acquia business
hours. You can submit these tickets either by online ticket or a phone
call:

-  *Online Ticket* - Customer will make requests of Acquia support
   through Acquia’s online ticket management system.
-  *Phone* - Monday – Friday (determined by Customer’s address).
   Developer and Partner subscriptions are not entitled to phone
   support.
-  *Email* - Acquia no longer accepts new support requests by email and
   requests that all customers submit new support requests either online
   or by phone. This allows us to associate important subscription and
   priority information with the request so that our teams can
   expediently handle the request. Acquia may still handle replies and
   updates to support tickets submitted online by email provided that
   the email body is retained in the reply.

Issue submission process:

-  When submitting a ticket, the Customer provides a description of the
   issue or request, a description of the mission impact, and designates
   the level of urgency of the request as Critical, High, Medium, or Low
   pursuant to the urgency categories set forth in the `Problem
   definition categories <#problem>`__ section.
-  Acquia evaluates the request and provides an initial response in the
   time determined by the Customer subscription’s service response
   levels.
-  The Customer works with Acquia to provide additional information
   about reported issue (for example, website functionality, related
   applications as needed to diagnose the issue, and
   infrastructure-related information).
-  Acquia tracks progress notes and related communications in the online
   ticket system through the resolution of the issue or request.
-  Acquia contacts the Customer either by phone or by using the online
   ticket system to confirm details and initiate diagnosis.
-  If the Customer makes a request by phone, Acquia opens a ticket on
   the Customer's behalf to track the issue through resolution. If
   changes to the website or configuration are requested verbally,
   confirmation will be requested in a ticket before the changes are
   made.
-  Issues not submitted to Acquia either through the online ticket
   portal or by phone bypass our standard request handling and default
   to Medium or Low priority. This may cause a delay in the desired
   response time.

.. _language:

Local language support
~~~~~~~~~~~~~~~~~~~~~~

In order to provide the most consistent, high quality support to our
Customer across the globe, Acquia has set the following standards for
communications with our Customer:

-  All written communications will be in English. This ensures that all
   Support team members can work on all Critical issues, and experts can
   be engaged in a Customer situation without delay.
-  Acquia Support can participate in English language discussions with
   Customers across all geographies 24/7.
-  Spanish language conversations are available in the Americas during
   business hours (8am-8pm Eastern) pending resource availability.
-  Acquia Support may be available to converse with Customers in the
   following languages during Europe's business hours (8a-6p CET),
   pending resource availability:

   -  French
   -  German
   -  Dutch

-  Acquia continually reviews Customer requirements and staff skills in
   this area so that we may be in the best position to support our
   Customers.

.. _scope_support:

Scope of Support services
-------------------------

.. _overview_subscriptions:

Overview of Acquia subscriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 14 14 14 14 14
   :header-rows: 1 

   * - 
     - Starter
     - Basic
     - Business
     - Premium
     - Elite
   * - **Critical urgency timeframe**
     - 2 hours
     - 1 hour
     - 1 hour
     - 1 hour
     - 30 minutes
   * - **High urgency timeframe**
     - *8 hours\**
     - *4 hours\**
     - *3 hours\**
     - *2 hours\**
     - *1 hour\**
   * - **Medium urgency timeframe**
     - *1 business day\**
     - *1 business day\**
     - *6 hours\**
     - *4 hours\**
     - *2 hours\**
   * - **Low urgency timeframe**
     - *2 business days\**
     - *2 business days\**
     - *1 business day\**
     - *1 business day\**
     - *1 business day\**
   * - **Acquia Support**
     - Unlimited
     - Unlimited
     - Unlimited
     - Unlimited
     - Unlimited
   * - **Remote Administration**
     - Add-On
     - Standard
     - Standard
     - Premium
     - Premium
   * - **Advisory Hours**
     - 0
     - 2
     - 4
     - 12
     - 16
   * - **Search queries per year**
     - 150K
     - 500K
     - 1MM
     - 10MM
     - 50MM
   * - **Search documents indexed per year**
     - 25K
     - 75K
     - 150K
     - 250K
     - 500K
   * - **Bandwidth per month (|acquia-product:ace|)**
     - 125GB
     - 500GB
     - 1TB
     - 2TB
     - 5TB


*\* 8:00am to 5:00pm, Monday through Friday only*

Note that a Developer Subscription/Partner Subscription is limited to
support of the Acquia Infrastructure only, with no Drupal support.
Support for this subscription level is available during regular business
hours (8am - 5pm) only. Support can be obtained by using the Acquia Help
Center; no phone support is available.

Remote Administration is not available to customers with an
|acquia-product:ais| Subscription (application not hosted on
|acquia-product:ac|).

Gratis subscriptions provided to the Drupal community are not eligible
for tickets, advisory hours, or Remote Administration, and are subject
to our Terms of Use.

Some legacy subscriptions included entitlements for a limited number of
tickets. These limits are no longer enforced.

.. _overview_legacy_subscriptions:

Overview of legacy Acquia subscriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Service                           | Description                       |
+===================================+===================================+
| Elite                             | -  24/7 support for Critical      |
|                                   |    issues                         |
|                                   | -  Highest level of response time |
|                                   |    available                      |
|                                   | -  Unlimited support tickets      |
|                                   | -  Access to Technical Account    |
|                                   |    Manager                        |
|                                   | -  Remote Administration (RA)     |
|                                   |    included                       |
|                                   | -  Bundled Advisory Hours per     |
|                                   |    your agreement                 |
|                                   | -  Access to |acquia-product:ac|  |
|                                   |    & |acquia-product:lib| tools   |
|                                   | -  Requires |acquia-product:ace|  |
|                                   | -  Phone support                  |
+-----------------------------------+-----------------------------------+
| Enterprise                        | -  24/7 support for Critical      |
|                                   |    issues                         |
|                                   | -  Enhanced support response time |
|                                   | -  Unlimited support tickets      |
|                                   | -  Remote Administration included |
|                                   | -  Bundled Advisory Hours as per  |
|                                   |    your support agreement         |
|                                   | -  Access to |acquia-product:ac|  |
|                                   |    & |acquia-product:lib| tools   |
|                                   | -  Requires |acquia-product:ace|  |
|                                   | -  Phone support                  |
+-----------------------------------+-----------------------------------+
| Pro Plus                          | -  24/7 support for Critical      |
|                                   |    issues                         |
|                                   | -  Limited bundle of Advisory     |
|                                   |    Hours per your agreement       |
|                                   | -  Access to |acquia-product:ac|  |
|                                   |    & |acquia-product:lib| tools   |
|                                   | -  Phone support                  |
+-----------------------------------+-----------------------------------+
| Professional                      | -  Business hour support (by      |
|                                   |    ticket only)                   |
|                                   | -  Access to |acquia-product:ac|  |
|                                   |    & |acquia-product:lib| tools   |
|                                   | -  No phone support               |
+-----------------------------------+-----------------------------------+
| |acquia-product:ace|              | -  24/7 support for with          |
|                                   |    proactive response to website  |
|                                   |    issues                         |
|                                   | -  Unlimited infrastructure       |
|                                   |    support tickets                |
|                                   | -  24/7 infrastructure monitoring |
|                                   | -  High availability options      |
|                                   | -  Drupal tuned stack             |
|                                   | -  Drupal developer tools         |
|                                   | -  Phone support                  |
+-----------------------------------+-----------------------------------+
| |acquia-product:acs|              | -  Self-service support and       |
| (formerly |acquia-product:ac|     |    server management              |
| standard)                         | -  Unlimited infrastructure       |
|                                   |    support tickets                |
|                                   | -  Monitored to ensure server     |
|                                   |    availability                   |
|                                   | -  Drupal tuned stack             |
|                                   | -  Drupal developer tools         |
|                                   | -  No phone support               |
+-----------------------------------+-----------------------------------+

.. _supportability:

Supportability matrix
~~~~~~~~~~~~~~~~~~~~~

Acquia supports the following applications and versions as listed in the
following table. |acquia-product:edg| applications and versions `are
listed separately <#supportability_site_factory>`__.

.. list-table::
   :widths: 15 15 15 40 15
   :header-rows: 1 

   * - Application
     - Component
     - Versions Supported
     - Support Scope
     - Subscription Information
   * - Drupal
     - Drupal core
     - 7.x and greater
     - Unmodified core, and major Drupal.org distributions are supported
     - 

       * Starter
       * Basic
       * Business
       * Premium
       * Elite

   * - Drupal
     - BLT
     - 8.x and greater
     - Acquia Support will answer general questions about the installation and use of BLT, clarify the best practices implemented in the tool, and offer insight regarding workflows and development testing. Acquia Support does not assist with the installation task, the writing of tests, or deploy issues that do not occur on Acquia’s platform. Acquia is supporting BLT as an open source project and assistance is provided by Acquia and the community through BLT’s Github issue queue.
     - 

       * Starter
       * Basic
       * Business
       * Premium
       * Elite

   * - Drupal
     - Community-Contributed Modules and Themes
     - 7.x and greater
     - Acquia provides diagnostic services for troubleshooting contributed modules. If a bug/issue is discovered in a contributed module, Acquia will submit an issue to the Drupal.org module issue queue on the Customer's behalf. Acquia may choose to address the issue directly if the solution is simple (can be addressed in one hour or less), and in those cases Acquia may submit a patch, too. The module maintainer controls whether the patch is accepted and included in a subsequent release, or not. If the maintainer chooses not to include it in a release, then the Customer is solely responsible for the module's maintenance and the merging of any security update changes. Support for modules that are not marked as recommended or are in a beta/development state is limited to basic diagnostics only. Acquia does not "finish" modules, code new features, or fix major bugs. Acquia can help diagnose issues with theme output, however, may not be able to assist with troubleshooting or fixing browser rendering issues.
     - 

       * Starter
       * Basic
       * Business
       * Premium
       * Elite

   * - Drupal
     - Custom Modules and Themes
     - 7.x and greater
     - Acquia provides diagnostic services for troubleshooting custom modules. As part of our service, Acquia will identify website issues that are linked to custom code, and Acquia may identify particular aspects of custom code that are responsible for the reported issue. In some cases Acquia may suggest a fix or fix approach, but it is the responsibility of the Customer to fix issues with custom modules. Acquia Support does not provide code review services, but those are available from Acquia Professional Services. Acquia can help diagnose issues with theme output, however, may not be able to assist with troubleshooting or fixing browser rendering issues.
     - 

       * Starter
       * Basic
       * Business
       * Premium
       * Elite

   * - Drupal
     - Third-Party Integration Module (for example, LDAP, external service connectors)
     - 7.x and greater
     - Acquia will assist the Customer to ensure that all Drupal modules function properly. Acquia may be able to assist with configuring the module to connect or operate with the third-party service. However, it is the Customer's responsibility to ensure that the configuration is complete and functional.
     - 

       * Starter
       * Basic
       * Business
       * Premium
       * Elite

   * - Acquia Services
     - |acquia-product:vpc|
     - N/A
     - Acquia will provide configuration of the connection between |acquia-product:ace| and one Customer-defined gateway device point. Changes to the customer end point after configuration will incur additional setup fees.
     - 

       * Elite
       * Enterprise

   * - Acquia Services
     - |acquia-product:cf| powered by CloudFlare
     - N/A
     - Acquia Cloud Edge consists of two products:

       * |acquia-product:cfp| for DDOS protection and Web Application Firewall (WAF) services
       * |acquia-product:cfc| for website acceleration

       |acquia-product:cfp| and |acquia-product:cfc| can be purchased together or individually.
       
       Acquia will assist the Customer with the configuration and troubleshooting of the |acquia-product:cf| product for which they are entitled. |acquia-product:cf| will be supported for use with domains of websites delivered through |acquia-product:ac|. |acquia-product:cf| does not require the use of any CloudFlare-related modules from Drupal.org. If the Customer chooses to employ such a module, and during the course of troubleshooting a bug/issue is discovered in the contributed module, Acquia will do one or both of the following: submit an issue to the Drupal.org module issue queue on the Customer's behalf, or recommend discontinuation of the module's use.
       
       If the Customer is entitled to the |acquia-product:cfp| product, CloudFlare may initiate contact with the Customer directly in the case where a malicious attack is detected against a Customer domain, and immediate action is required to mitigate the attack. In such a case, CloudFlare will also alert Acquia, and Acquia will initiate the escalation process with the Customer.
     - 

       * Elite
       * Premium
       * Business

   * - Acquia Services
     - |acquia-product:dam|
     - Drupal 7.x, 8.x
     - Acquia Support will provide the following support for |acquia-product:dam|:

       * Diagnose problems with the |acquia-product:dam| application and its add-ons
       * Assist with configuration when connecting |acquia-product:dam| to Drupal using the Drupal 7 and Drupal 8 integrations. Acquia will assist the Customer to ensure that the Drupal integration modules function properly.
       * Diagnose problems with using |acquia-product:dam| assets with |acquia-product:lepp| and |acquia-product:lepc|.

       Acquia Support will not be responsible for troubleshooting code-level integrations between |acquia-product:dam| and other applications.

     - |acquia-product:dam| Starter, |acquia-product:dam| Professional
   * - Acquia Services
     - Git
     - N/A
     - We provide support on its interoperability as it relates to our hosting platform. We do not provide general advice on how to use version control systems or provide support for Git outside of the Acquia-hosted environment.
     - 

       * Starter
       * Basic
       * Business
       * Premium
       * Elite

   * - Acquia Services
     - PHP Extensions and Libraries
     - 5.5 and greater
     - We support the integration of PHP extensions with the Customer's Drupal implementation. The Customer is responsible for compiling compatible php extensions and for providing ``.so`` files in their code repository. See `Adding non-Drupal PHP extensions or libraries to your application </acquia-cloud/develop/non-drupal>`__. Customer is responsible for troubleshooting any resulting PHP functionality issues.
     - 

       * Starter
       * Basic
       * Business
       * Premium
       * Elite

   * - Acquia Services
     - |acquia-product:as| Platform
     - 4.x and greater
     - This includes the functionality to connect to |acquia-product:as| Platform. There may be limited customization and configuration options in the |acquia-product:as| Platform, as referenced in the `Custom Solr configuration </acquia-search/config>`__ documentation page.
     - 

       * Starter
       * Basic
       * Business
       * Premium
       * Elite

   * - Acquia Services
     - |acquia-product:cha| Classic
     - Drupal 7.x
     - Acquia Support will diagnose problems with the |acquia-product:cha| module, the |acquia-product:cha| administrative interface, or customer-created personalizations. Acquia Support will not be responsible for troubleshooting code-level integrations between |acquia-product:cha| and Drupal. Acquia Support can discuss configuring campaigns or understanding |acquia-product:cha| reports as part of advisory hours.
     - 

       * |acquia-product:cha|
       * |acquia-product:cha| Premium

   * - Acquia Services
     - |acquia-product:cha| 
     - Drupal 7.x, Drupal 8.x
     - Acquia Support will provide the following support to these |acquia-product:cha| components:

       * |acquia-product:lpm| - Diagnose problems with the |acquia-product:alw| Administrative interface.
       * |acquia-product:leb| - Diagnose problems with the |acquia-product:cha| module, |acquia-product:leb| UX, and associated customer-created rules and segments.
       * |acquia-product:ch| - Unlimited product support when connected to Drupal using Acquia-provided connector modules.

       Acquia Support will not be responsible for troubleshooting code-level integrations between |acquia-product:cha| and Drupal. Acquia Support can discuss configuring campaigns or understanding |acquia-product:cha| reports as part of advisory hours.
     - 

       * |acquia-product:lpls|
       * |acquia-product:lplpw| Premium

   * - Acquia Services
     - |acquia-product:cha| 
     - Drupal 7.x, Drupal 8.x
     - Acquia Support will provide the following support to these |acquia-product:cha| components:

       * |acquia-product:lpm| - Diagnose problems with the |acquia-product:alw| Administrative interface.
       * |acquia-product:leb| - Diagnose problems with the |acquia-product:cha| module, |acquia-product:leb| UX, and associated customer-created rules and segments.
       * |acquia-product:ch| -
       
         * Acquia ensures application availability and provides unlimited support for Content Syndication infrastructure issues which impact application availability or functionality as outlined in the documentation.
         * Acquia provides Content Syndication application support when connected to Drupal using Acquia-provided connector modules. Application support means Acquia will assist with diagnosis and repair of standard application functions including configuration, syndication of content between Content Hub-connected Drupal sites, and server resource troubleshooting during syndication.
         * Acquia will address "how-to’s" and best practices questions to assist customers in obtaining the most value from the system.
         * When using the Content Syndication API, support is limited to verifying network connectivity between Content Syndication and the connected application and to troubleshooting data flow issues through log analysis of Acquia applications. Acquia does not diagnose custom or third-party applications connected to Content Syndication.
         * The health or integrity of customer content is a customer responsibility apart from Acquia's scope of service, which is limited to assuring the system can distribute content. Content Syndication includes a configurable email notification of stale content per website for customer awareness.
         
       Acquia Support will not be responsible for troubleshooting code-level integrations between |acquia-product:cha| and Drupal. Acquia Support can discuss configuring campaigns or understanding |acquia-product:cha| reports as part of advisory hours.
     - 

       * |acquia-product:lplp|
       * |acquia-product:lplpo|

   * - Acquia Services
     - |acquia-product:ccd| 
     - Drupal 7.x, Drupal 8.x
     - |acquia-product:ccd| has two components:

       * CD environments (CDEs) for rapid creation of development environments
       * CD pipelines for continuous delivery activities

       Acquia supports the underlying infrastructure, user interface, and functionality of each component, but is not responsible for integrations to external systems or external code repositories. A Customer may use their allotted Advisory Support hours to engage Acquia on strategies for external integrations. Acquia may be able to advise on strategies for external integrations by using Advisory Hours. CDEs do not support load testing.
     - All
   * - Acquia Application Services
     - Node.js runtime 
     - 6.x and greater, based on the Node.js `end-of-life schedule <https://github.com/nodejs/LTS#lts-schedule1>`__
     - Acquia will host Node.js applications on the |acquia-product:ac| platform, which is subject to the same Service Level Commitment as your subscription.
     
       Support of the Node.js service includes the following:

       * Availability of the infrastructure required to run Node.js inclusive of memory, storage, computing power, operating systems.
       * Support of |acquia-product:ac| functionality and APIs

       At this time, Acquia does not provide code support or troubleshooting for Node.js application issues or related custom code. Acquia will partner with our customers to determine if there are problems with the |acquia-product:ac| environment or the application layer, but Acquia is currently unable to assist with Node.js code-related issues.
       
       Acquia will not provide patching or update services for Node.js applications. Updates to Node.js applications and code are the responsibility of the customer.
     - All


These applications are supported for Customers using the Acquia
infrastructure and for Customers that choose to host their own
applications.

.. _supportability_site_factory:

|acquia-product:edg|
~~~~~~~~~~~~~~~~~~~~


.. list-table::
   :widths: 15 15 15 40 15
   :header-rows: 1 

   * - Application
     - Component
     - Versions Supported
     - Support Scope
     - Subscription Information
   * - Drupal
     - |acquia-product:dg| distribution
     - 7.x
     - Acquia maintains and provides diagnostic services for troubleshooting the |acquia-product:dg| distribution. If a bug/issue is discovered in the distribution, Acquia will provide hotfixes for critical issues and otherwise schedule fixes as appropriate.
     - 

       * SaaS tier
       * PaaS tier

   * - Drupal
     - Drupal core
     - 7.x
     - Unmodified core and major Drupal.org distributions are supported.
     - PaaS tier
   * - Drupal
     - Community-Contributed Modules and Themes
     - 7.x
     - Acquia provides diagnostic services for troubleshooting contributed modules. If a bug/issue is discovered in a contributed module, Acquia will submit an issue to the Drupal.org module issue queue on the Customer's behalf. Acquia may choose to address the issue directly if the solution is simple (can be addressed in one hour or less), and in those cases Acquia may submit a patch. The module maintainer controls whether the patch is accepted and included in a subsequent release, or not. If the maintainer chooses not to include it in a release, then the Customer is solely responsible for the module's maintenance and the merging of any security update changes. Support for modules that are not marked as recommended or are in a beta/development state is limited to basic diagnostics only. Acquia does not "finish" modules, code new features, or fix major bugs. Acquia can help diagnose issues with theme output, however, may not be able to assist with troubleshooting or fixing browser rendering issues.
     - PaaS tier
   * - Drupal
     - Custom Modules and Themes
     - 7.x
     - Acquia provides diagnostic services for troubleshooting custom modules. As part of our service, Acquia will identify website issues that are linked to custom code, and Acquia may identify particular aspects of custom code that are responsible for the reported issue. In some cases Acquia may suggest a fix or fix approach, but it is the responsibility of the Customer to fix issues with custom modules. Acquia Support does not provide code review services, but those are available from Acquia Professional Services. Acquia can help diagnose issues with theme output, however, may not be able to assist with troubleshooting or fixing browser rendering issues.
     - PaaS tier
   * - Drupal
     - Third-Party Integration Modules (such as LDAP or other external service connectors)
     - 7.x
     - Acquia will assist the Customer to ensure that all Drupal modules function properly. Acquia may be able to assist with configuring the module to connect or operate with the third-party service. However, it is the Customer's responsibility to ensure that the configuration is complete and functional.
     - PaaS tier
   * - Acquia Services
     - |acquia-product:cf|
     - N/A
     - |acquia-product:cf| consists of two products:

       * |acquia-product:cfp| for DDOS protection and Web Application Firewall (WAF) services
       * |acquia-product:cfc| for website acceleration

       |acquia-product:cfp| and |acquia-product:cfc| can be purchased together or individually.

       Acquia will assist the Customer with the configuration and troubleshooting of the |acquia-product:cf| product for which they are entitled. |acquia-product:cf| will be supported for use with domains of websites delivered through |acquia-product:ac|. |acquia-product:cf| does not require the use of any CloudFlare-related modules from Drupal.org. If the Customer chooses to employ such a module, and during the course of troubleshooting a bug/issue is discovered in the contributed module, Acquia will do one or both of the following: submit an issue to the Drupal.org module issue queue on the Customer's behalf, or recommend discontinuation of the module's use.

       If the Customer is entitled to the |acquia-product:cfp| product, CloudFlare may initiate contact with the Customer directly in the case where a malicious attack is detected against a Customer domain, and immediate action is required to mitigate the attack. In such a case, CloudFlare will also alert Acquia, and Acquia will initiate the escalation process with the Customer.
     - 

       * PaaS tier
       * SaaS+ tier
       * SaaS tier

   * - Acquia Services
     - Git
     - N/A
     - We provide support on its use as it relates to |acquia-product:edg|. We do not provide general advice on how to use version control systems or provide support for Git outside of the Acquia-hosted environment.
     - PaaS tier
   * - Acquia Services
     - |acquia-product:as| platform
     - 4.x and greater
     - This includes the functionality to connect to the |acquia-product:as| platform. There may be limited customization and configuration options in the |acquia-product:as| platform, as referenced in the `Custom Solr configuration </acquia-search/config>`__ documentation page.
     - PaaS tier

.. _supportability_acquia_cloud_cd:

|acquia-product:ccd|
~~~~~~~~~~~~~~~~~~~~

|acquia-product:ccd| is a development environment and is treated as such
for the purposes of support ticket urgency and triage. Your
|acquia-product:ccd| subscription will inherit the ticket response time
from your |acquia-product:ace| subscription. For guidance purposes,
please refer to the following examples when filing support requests
related to |acquia-product:ccd|:

.. list-table::
   :widths: 30 20 50
   :header-rows: 1 

   * - Example
     - Ticket Urgency
     - Acquia Response
   * - CDE is slow
     - Normal or High
     - Acquia will investigate, per the entitlement level of the Customer’s |acquia-product:ace| subscription.
   * - |acquia-product:ccd| feature is not performing as expected
     - Normal or High
     - Acquia will investigate, per the entitlement level of the Customer’s |acquia-product:ace| subscription.
   * - CDE is unreachable or down
     - Critical
     - Acquia will investigate system availability as Critical issue, per the entitlement of the Customer’s |acquia-product:ace| subscription.
   * - Cannot create new CDE
     - Critical
     - Acquia will investigate, per the entitlement level of the Customer’s |acquia-product:ace| subscription.


.. _supported_lifecycle:

Supported software life cycle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Acquia reserves the right to retire support for certain versions of the
supported applications. As a standard, Acquia will support the current
major version of Drupal (N) and the immediately preceding major version
(N-1). For example, Acquia will support Drupal 8.x and Drupal 7.x
simultaneously. This ensures that Customers receive the best possible
support and are able to take advantage of the latest features and
security enhancements in the software.

Acquia will provide full support to earlier versions (N-2) until the
Drupal Community chooses to stop providing security fixes for version
N-2. To ensure that our Customers experience smooth migrations to newer
versions of Drupal, Acquia may provide Transition Support for version
N-2 for a period of no less than 12 months. Prior to retiring support
for any Drupal version, Acquia will provide at minimum of 12 months
notice to our Customers. Notice will be provided in one or more of the
following ways: on the |acquia-product:ui|, through documentation, or
through Customer notice (email) to registered users of
|acquia-product:ac|. After a version is retired, Support will be limited
to preexisting documentation.

As we continue to implement new products and services and upgrade
technologies on the |acquia-product:ac| platform, we will implement
end-of-life (EOL) deadlines that may require action on your part. For
specific information on software versions and upgrade plans, see the
`Software end-of-life schedule </support/eol>`__.

.. _lifecycle_description:

Life cycle description
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 80
   :header-rows: 1 

   * - Cycle
     - Attributes
   * - Acquia Support
     - Applies to N and N-1 major Drupal versions. For Drupal 8 and later, applies to N minor and N-1 minor versions within a major version (Drupal core follows Semantic Versioning).

       * Acquia provides comprehensive support coverage per subscription entitlement and support scope.
       * A full range of Remote Administration services are available.
       * Remote Administration not guaranteed to be compatible with N-2 minor versions for Drupal 8 or later.
       * Remote Administration Security updates are only available for the N minor version for Drupal 8 or later.
   * - Transition Support
     - Applies to N-2 major Drupal version

       * Acquia continues to provide support of the N-2 major Drupal version.

         * Acquia |acquia-product:lib| will remain available.
         * Transition support will be available only for a limited time.
         * Acquia may provide additional services as part of a transition support offering.

       * Remote Administration services are not available.

   * - End-of-Life
     - N-2 major Drupal version upon completion of Transition Support term and earlier versions

       * |acquia-product:lib| documentation is available.
       * There is no active support by Acquia.


.. _supported_environments:

Supported software environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Acquia-hosted environments
^^^^^^^^^^^^^^^^^^^^^^^^^^

In all cases, applications that are hosted on the |acquia-product:ac|,
|acquia-product:ace|, and |acquia-product:edg| platforms will be running
on supported software environments. The Acquia team maintains these
environments and will notify Customers when we require a change to the
underlying software due to an end-of-life notification. In those cases
we will provide Customer with advance notice prior to upgrading our
systems. For the current list of supported software and versions for
Acquia-managed environments, see |actech|_.

.. |actech| replace:: \ |acquia-product:ac|\  technology platform and supported software
.. _actech: /acquia-cloud/arch/tech-platform

Customer-hosted environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This includes environments hosted by the Customer or any non-Acquia
third party. Acquia strongly recommends that Customers maintain current
and supported versions of all the software required to run their
website. Acquia does not place any restrictions on which non-Drupal
software and versions that Customer run in self-hosted environments. The
Acquia Support Subscription does not cover support, configuration, or
installation advice for any non-Drupal application. The Customer must
retain adequate resources and expertise to support and manage the
non-Drupal applications and access key logs (or any other items) that
are required for diagnostic activities. Acquia `does not troubleshoot
issues in locally-hosted development
environments </support/guide#local-env>`__.

.. _drupal8:

Drupal 8
^^^^^^^^

Drupal 8 was released for general availability (GA) on 25 November 2015
and is fully supported on the |acquia-product:ac| platform. Support for
Drupal 8 Alpha, Beta, and RC versions is limited to providing advice on
upgrading or reimplementing a pre-GA implementation to a GA release of
Drupal 8.

Support for Drupal 8 contributed modules is subject to Acquia’s standard
support policy for contributed modules as referenced in the
Supportability matrix.

The |acquia-product:ac| Platform and |anclink|_ module may require updates as Drupal 8 continues to be developed. Any updates required to support Drupal 8 or optimize the platform for Drupal 8 will be made through our normal development, quality assurance and release cycle.

.. |anclink| replace:: \ |acquia-product:anc|\ 
.. _anclink: https://www.drupal.org/project/acquia_connector


.. _platform_maintenance:

Platform maintenance and security upgrades
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scheduled maintenance
^^^^^^^^^^^^^^^^^^^^^

Regular Platform maintenance and infrastructure improvements are
scheduled in advance. Affected Customers are provided a start time and
stop time for the applicable maintenance window and are notified at
least forty-eight hours prior to beginning of the maintenance window.
Acquia will proactively notify the Customer if maintenance will exceed a
previously scheduled maintenance window or if maintenance needs to be
postponed. Maintenance is scheduled from 11:00 PM (23:00) to 7:00 AM
(07:00) local time for the following service regions — if you are not
sure what service region your application is in, see `Viewing server
information </acquia-cloud/manage/servers#info>`__:

-  Sydney (AP-Southeast-2)
-  Singapore (AP-Southeast-1)
-  Tokyo (AP-Northeast-1)
-  EU-Central (EU-Central-1 - Frankfurt)
-  EU-West (EU-West-1 - Dublin)
-  US-East (US-East-1)
-  US-West (US-West-2)
-  São Paulo (SA-East-1)

Emergency (unscheduled) maintenance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In circumstances where security upgrades or other urgent maintenance
must be performed, we undertake best efforts to notify Customers prior
to beginning maintenance and to provide technical information as it is
available. In these circumstances, maintenance windows begin immediately
and continue until the emergency maintenance is completed. Customers are
notified after this maintenance is complete and provided any additional
instructions regarding required Customer actions. Acquia Global Support
is available to clarify any questions or follow-up actions that are the
result of the unscheduled maintenance.

.. _rca:

Root Cause Analysis
~~~~~~~~~~~~~~~~~~~

Acquia will provide a Root Cause Analysis (RCA) to a customer, upon
request, for customer impacting issues where a root cause is deemed to
be an Acquia Platform issue or where an Acquia action resulted in a
customer impacting issue. RCAs will be delivered within three business
days (exclusive of Acquia regional holidays) of the resolution of an
issue. If Acquia is reliant upon a third party for critical RCA
information, the delivery time may increase to 5-7 business days. In
some cases, the RCA may be updated one or more times after it is
delivered if additional information is discovered or third-party data
becomes available. Incidents tracked and communicated on
`status.acquia.com <https://status.acquia.com>`__ will be closed with a
summary of the incident resolution and will not receive separate RCA
documentation unless otherwise noted.

Acquia does not provide an RCA for events or downtime for a customer’s
application issues or for third-party services not managed by Acquia.
Services, tools, and events not covered by an SLA are not eligible for a
formal RCA. In these instances, Acquia will investigate and report using
our standard customer request processes. In addition, Acquia may, at its
discretion, provide an RCA for a sustained issue with a service or tool
not reported on `status.acquia.com <https://status.acquia.com>`__.

For issues that do not qualify for a formal RCA, a summary of events
will be available in the associated tracking ticket.

.. _php-extensions:

Installation of custom PHP extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for adding custom PHP extensions to our platform is deprecated
on Acquia Hosting, and will removed entirely in the near future.
Customers needing PHP extensions not provided as part of Acquia hosting
should follow the instructions at `Adding non-Drupal PHP extensions or
libraries to your application </acquia-cloud/develop/non-drupal>`__ and
`file a Support ticket <http://insight.acquia.com/support/tickets/new>`__ to have them
enabled.

.. _custom-vcl:

Installation of custom VCLs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:ace| and |acquia-product:edg| customers with dedicated
load balancers can request that custom VCL files be added to their load
balancers. Customers that need custom VCL files must follow the
instructions at |customvarnish|_.

.. |customvarnish| replace:: Custom Varnish configuration for \ |acquia-product:ace|\  applications
.. _customvarnish: /acquia-cloud/performance/varnish/custom

.. _docroot-policy:

Drupal docroot support
~~~~~~~~~~~~~~~~~~~~~~

Acquia offers support for Drupal *only* when it is installed at the top
level of the `docroot </article/docroot-definition>`__ (``/docroot/``).
Drupal installations either in other folders or nested in a docroot are
not supported configurations, for the following reasons:

-  Alternate or nested docroots create a poor and risky development
   workflow.
-  Diagnosing issues is substantially more complicated, due to shared
   logs and other factors.
-  Acquia diagnostic and automation tools operate only on the top-level
   docroot.
-  Remote Administration automated security updates cannot be applied to
   alternate docroots.
-  Performance of all websites is likely to be compromised, and proper
   functioning of |acquia-product:ac| functionality is not tested or
   assured.

Where applicable, additional websites can be developed using a multisite
configuration. Additional websites using another instance of the Drupal
codebase may also be developed in a completely separate codebase.
Subscription levels and purchased codebases determine the number of
codebases available in the scope of your |acquia-product:ac|
subscription.

.. _node:

Node.js runtime version support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As part of Acquia’s Node.js service, Acquia is able to host Node.js
applications on the |acquia-product:ac| platform. |acquia-product:ac|
will run Node.js versions 6.x and greater, and Acquia will follow the
`end-of-life schedule <https://github.com/nodejs/LTS#lts-schedule1>`__
provided by Nodejs.org. Versions of Node.js that have reached their
Maintenance End dates will not be supported by Acquia.

.. _out-of-scope_applications:

Out-of-scope applications
~~~~~~~~~~~~~~~~~~~~~~~~~

The following applications are not supported by Acquia. This list is not
fully inclusive, but is meant to be representative.

Although Customers may choose to install/implement these applications in
their environment as part of their comprehensive solution, Acquia will
not troubleshoot these or other installed and non-supported
applications, and reserves the right to ask Customers to disable these
applications if it is preventing troubleshooting efforts. If the
application is hosted on an Acquia platform, Acquia reserves the right
to disable the application as part of diagnostic and recovery
operations.

Applications on |acquia-product:ac| must be compatible with
high-availability databases. |acquia-product:ac| does not support
applications that write to a subordinate (slave) database.

The following are considered out-of-scope for Acquia’s support offering:

-  CiviCRM
-  Disqus
-  Magento
-  Moodle
-  phpBB
-  phpMyAdmin
-  piwik
-  Shibboleth
-  vBulletin
-  Applications that require compiled standalone libraries (not php
   extensions)
-  Custom (non-Drupal) modules constantly running ingestion scripts and
   or search indexing scripts
-  Version control applications that are not Git
-  WordPress

The following applications are not supported and cannot be installed on
|acquia-product:ac|:

-  Aegir
-  Behat
-  Custom daemons or services, such as Jabber or Microsoft Exchange
-  Java applications
-  Hudson / Jenkins
-  MongoDB
-  Perl/Python/Ruby scripts that require additional libraries
-  Redis

.. _local-env:

Local environments
^^^^^^^^^^^^^^^^^^

With the exception of |acquia-product:add|, troubleshooting issues in a
local environment is out-of-scope for Acquia Support.

Some of the previously listed unsupported applications (such as Behat or
Jenkins) offer SaaS implementations, or can be installed in your local
environment and then integrated externally with your Acquia workflow
environment. Acquia Support does not provide support for specific
implementation and use of integrations. Acquia Support can, however,
provide general guidance on using the |acquia-product:api|. To implement
specific integrations, you can schedule a Professional Services
engagement.


.. note::  There may be limitations to using MySQL views, custom MySQL functions, stored procedures and triggers in the Acquia environment. If your application requires the use of these features, review this with the Acquia Customer Support or Acquia Customer Onboarding teams prior to launching your website or deploying updated code.

.. _decoupled:

Decoupled Drupal
^^^^^^^^^^^^^^^^

Acquia Support will assist with diagnosis and repair of "decoupled"
Drupal applications and the Acquia environment in which they run. There
are two ways you can decouple Drupal: first, progressive decoupling. It
consists of interpolating a JavaScript framework into the Drupal front
end without leveraging server-side rendering via Node.js. Second, fully
decoupled Drupal, which involves a complete separation of concerns
between the structure of your content and its presentation, thus
allowing front-end developers to have more control and freedom, but also
results in a loss of some out-of-the-box CMS (Content Management System)
functionality such as in-place editing or content preview.

Troubleshooting non-Drupal front-end applications, whether hosted on the
Acquia Cloud environment or not, is currently out of scope if not
explicitly covered under an Acquia Support contract. Customers are
responsible for the proper functioning, performance, diagnosis and
repair of non-Drupal front-end applications in a decoupled
configuration.

The following diagram shows areas of responsibility for a Node.js
application:

|Decoupled Drupal support scope|

.. |Decoupled Drupal support scope| image:: https://cdn4.webdamdb.com/1280_6j5QU8FYn7D9.png?-62169955200
   :width: 960px

.. _cdn:

Content Delivery Networks
^^^^^^^^^^^^^^^^^^^^^^^^^

Acquia Support can review general best practices for usage of Content
Delivery Networks (CDNs) within |acquia-product:ac| and discuss Varnish
caching and other website performance aspects on a general level.
Website-specific performance evaluations, determination of requirements,
or configuration reviews are beyond the scope of Acquia Support. Acquia
fully supports the |acquia-product:cf| solution, but does not configure
or manage third-party CDN configurations on behalf of Customers.
In-depth reviews, configuration, or investigation of CDN issues are
available at Acquia’s standard professional services rates.

.. _load_tests:

Load tests
^^^^^^^^^^

Acquia strongly encourages customers to perform `load
tests </acquia-cloud/performance/load>`__ in a clone of the production
environment in advance of any major code release. Certain performance
impacting issues can be only be found through proper load testing and it
is the best way to reduce launch risk. For more information about
readying your website for a significant future event, see `Preparing for
a high-traffic event </support/traffic>`__.

Acquia Support can provide best practice advice on the process of load
testing, and best practice advice on how to resolve specific findings
from load testing. Acquia Support does not design, conduct, or monitor a
load test, nor does Support interpret or analyze the results of load
tests; however, all of these services are available from Acquia as
separate engagements. Contact your Account Manager for details.

For valid results, load tests must be conducted on a clone of your
website's production environment, or in the current production
environment if the website is not yet launched. Acquia provides access
to dedicated load balancers specifically for load testing purposes by
prior arrangement. Customers cannot use shared hardware for load testing
as this will negatively impact production websites for other customers.
Contact Acquia Support to request access to a dedicated load balancer
for testing purposes.

.. _infrastructure_support:

Infrastructure support
~~~~~~~~~~~~~~~~~~~~~~

Acquia provides full infrastructure support to any Customer running its
applications on |acquia-product:ac|, |acquia-product:ace|, or
|acquia-product:edg| platforms. Because Acquia's platform configuration
files contain Acquia's intellectual property and are very specific to
our infrastructure, these files cannot be shared with Customers or
partners.

Development and staging environments are designed and intended only for
development and testing. Running production websites on development or
staging environments is not supported, because they are not sized for
production traffic and loads. In addition, development and staging
environments may include shared resources which, if impacted by
production-level traffic, may be in violation of terms of service.
Acquia offers High-Availability and multi-region failover environments
for customers with such requirements.

If a Customer chooses to host their application internally or with a
third-party provider, Acquia Support is unable to provide
troubleshooting or support assistance with the infrastructure. This
limitation includes reviewing the Customer's hardware, settings, and
non-supported software infrastructure. Acquia Professional Services is
able to provide assistance in these areas as well as with overall
infrastructure architecture.

.. _vcl:

Modification of the Varnish Configuration Language (VCL) Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The |acquia-product:ac| Platform provides a universal and optimized
Varnish Configuration Language (VCL) configuration which cannot be
customized on the shared Platform. Customers with dedicated load
balancers may provide a `customized, tested VCL
configuration </acquia-cloud/performance/custom-varnish>`__ for Acquia
to implement on the Customer's dedicated load balancers.

Acquia does not test customized VCL configurations. It is the Customer's
responsibility to test VCL changes in advance of supplying the
configuration to Acquia. Prior to implementing the modifications on the
Customer's live balancer, Acquia will implement the VCL configuration
changes on a load-testing balancer. It is the Customer's responsibility
to test these changes, confirm they are working as expected, and grant
Acquia written permission to implement the changes on the live balancer.
Acquia deploys custom VCL files on a set schedule so turnaround time to
implement a custom VCL may be up to one week. Acquia may reject a
modified VCL file if the modifications prove disruptive to the Platform
or generate high levels of Platform alerts.

.. _acquia_search:

|acquia-product:as|
^^^^^^^^^^^^^^^^^^^

|acquia-product:as| provides for limited customization to accommodate
Customers with more complex needs than the standard |acquia-product:as|
configuration provides.

Acquia Support will assist with implementing such changes according to
the following process and guidelines:

-  Acquia will implement limited |acquia-product:as| `customizations for
   Customers </acquia-search/config>`__. Only the parameters referenced
   in this link may be customized.
-  Customer requests to implement |acquia-product:as| customizations are
   processed weekly. Requests submitted by the end of Acquia business
   hours in the local Acquia support region each Monday will be
   processed on Wednesday of the same week.
-  An Acquia Search customization request ticket must include the
   following information:

   -  One or multiple Solr configuration files attached to the ticket.
   -  Files must be UTF-8-encoded without a Byte Order Mark (BOM), with
      LF (Unix-style) line endings.
   -  Can request changes to multiple Solr indexes, as long as all files
      are to be deployed equally to all mentioned indexes at the same
      time.
   -  One or more Acquia Search index IDs or URLs. These can be found:

      -  in the Drupal administrative UI under (for Search API) **Config
         > Search API** and then select the server page, or (for
         ApacheSolr) under **Config > Apache Solr Search Integration >
         Settings**.
      -  If you sign in to your |acquia-product:ais|, under **Sites**,
         select a Sitename, and then click **Search**.

-  Customers are responsible for pre-testing configuration changes
   before submitting them to Acquia. Customizations that do not pass
   Acquia’s automated basic configuration integrity test will be
   rejected without additional investigation. The customer will be
   notified of the failure and is responsible for modifying the custom
   configuration file and testing it locally.
-  Acquia does not perform testing to ensure search configuration
   modifications will perform as intended. It is the responsibility of
   the customer to perform this testing.

.. _shared_resources:

Use of shared resources
~~~~~~~~~~~~~~~~~~~~~~~

Customers using the |acquia-product:acs| (formerly
“|acquia-product:ac|”), |acquia-product:ace|, or |acquia-product:edg|
platforms may choose to use hardware that is shared with other
customers. Sustained usage of any shared resource (such as, but not
limited to: staging servers, load balancers, and version control
servers) in excess of 20% of overall capacity gives Acquia the
discretion to move the customer to dedicated hardware at the customer’s
expense, in order to preserve uptime for other customers also using the
shared hardware.

Shared resources may include, but are not limited to:

-  Memory (RAM)
-  CPU
-  Disk
-  Network capacity

Customers with websites using the |acquia-product:as| platform have
limits for some or all of the following resources: total queries,
documents, and disk space. If these limits are consistently met or
exceeded, Acquia reserves the right to restrict the website's use of the
shared Search resources or move the customer's website to a dedicated
|acquia-product:as| instance at the customer’s expense.

.. _removal:

Removal from monitoring due to chronic application issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a website has issues with application stability and performance due
to application issues which cannot be remedied by Acquia’s intervention,
and as a result generates frequent alerts within the |acquia-product:ac|
Platform monitoring system, Acquia will issue a CRR (Customer Risk
Report). This will identify and recommend measures to resolve or
mitigate the issues causing the repeated alerts with an expectation that
there is a mutual interest in stabilizing the website as soon as
possible.

If a customer elects to take no action towards addressing the issues,
Acquia will initiate a process for temporarily removing the website from
monitoring. Three notifications will be sent and if no corrective action
is taken then the website will be removed from monitoring. When a
website is removed from monitoring, Acquia does not have visibility into
the condition of your |acquia-product:ac| instances and we cannot
provide proactive alerts on certain issues impacting your application's
performance and availability.

Customers who have been removed from monitoring may request to be added
back to monitoring after demonstrating the underlying issues have been
addressed. Normal support services will be provided to customers
independent of website monitoring status.

.. _slow-queries:

Long-running queries
~~~~~~~~~~~~~~~~~~~~

Database queries can be both generated by Drupal in response to website
visitors displaying pages on which selective data is displayed, and
through administrative or maintenance actions taken by a website
developer or administrator.

Any query with a running time of greater than one second is a
long-running query. A single particularly long-running query or a high
volume of shorter long-running queries may negatively impact overall
website performance, and can result in an interruption of a website's
availability. For recommendations about how to resolve slow queries, see
the `How to fix slow queries </articles/how-fix-slow-queries>`__ Acquia
|acquia-product:lib| article.

Terminating a task that contains a long-running query can result in data
loss or a *split-brain* condition between databases in a High
Availability environment. Due to these potential consequences, Acquia
Support will not proactively terminate long-running queries without
customer authorization.

In the event a long-running query is impairing website performance,
Acquia Support will attempt to contact the customer to obtain permission
to terminate the query. Acquia Support will not terminate a query
without confirmation from the customer and an acknowledgement of the
potential consequences.

If Acquia Support cannot obtain confirmation from the customer, the
query will be allowed to run. If the query impacts performance, website
instances will be upsized as necessary to ensure stability.

.. _advisory_services:

Advisory services
~~~~~~~~~~~~~~~~~

Some Acquia Support subscriptions include Customer Advisory hours. These
hours may also be purchased separately.

Advisory services entitles the Customer to engage an Acquia expert in a
discussion of best practices for generic topics including security,
migration, performance tuning, module development, and Drupal website
architecture. Advisory support is limited to knowledge that can be
communicated during a real-time conversation or by follow-up email. If
applicable, advisory support may include current documentation.
Website-specific research, implementation/installation activities, and
creation of any new deliverable(s) are out-of-scope for advisory
support. Advisory support does not generate any deliverables. Customer
is entitled to the number of advisory hours set forth in their
order/\ `subscription </acquia-cloud/subs>`__.

Examples of advisory support topics:

-  Security best practices
-  Module selection advice
-  Migration best practices
-  Performance best practices
-  Architecture best practices
-  Module development best practices

Advisory hours may be consumed in blocks of time not to exceed two (2)
hours unless there is prior approval from Acquia Support Management.
Time is applied against Advisory hours in the following manner:

-  *Time spent* - For example, for each hour of discussion between
   Acquia and the Customer, one hour is consumed.
-  *Preparation time* - For each Advisory session greater than one hour,
   Acquia may charge the Customer an additional 30 minutes of
   preparation time.
-  *Follow-up* - Acquia reserves the right to charge the Customer for
   time spent if session follow-up requires 30 minutes or more of the
   Advisory expert’s time.

Customers must make requests for Advisory sessions at least three
business days in advance of the desired meeting team. Acquia will make
all efforts to schedule Advisory Calls based on the Customer's requested
timing, but reserves the right to schedule at a mutually agreed
alternative date if necessary.

Advisory hours expire if not used during the subscription term and may
not banked for usage outside of the contracted subscription term. We
request that Customer limit advisory requests to no more than eight
hours in any single month or two hours in any given week.

.. _ticket_limitations:

Ticket limitations
~~~~~~~~~~~~~~~~~~

Application support tickets apply to:

-  Requests for diagnostic support provided on Drupal applications and
   related Acquia offered products.
-  Support issues generated by Customer-driven change such as new code
   deployments and custom configuration requests.
-  Tasks handled upon request by Acquia Support that Customer may
   otherwise handle through self-service options.

Upon resolution, the root cause of an issue determines what category a
ticket falls in to.

Customers have the ability to open several different types of tickets
with Acquia:

.. list-table::
   :widths: 27 30 43
   :header-rows: 1 

   * - Ticket Type
     - Description
     - Ticket Allowance
   * - Drupal Application Support
     - Diagnostic support of the Customer's Drupal applications
     - Tickets are unlimited.
   * - Acquia Platform / Services
     - Diagnostic, change request, and break/fix tickets related to Acquia’s hosted infrastructure or tools
     - This includes the diagnosis and remediation of product-related issues and bugs related to the Acquia Platform and SaaS tools such as |acquia-product:ais|, |acquia-product:cha|, |acquia-product:as|, and |acquia-product:add|. Tickets are unlimited.
   * - Advisory Hours
     - Request for Customer Advisory sessions
     - Total Advisory hours are limited per Subscription.
   * - Remote Administration
     - Customer files a request for a Remote Administration activity
     - For Customers with the Premium Remote Administration service option. Subscriptions with Remote Administration have an allocation of 10 total hours per month. Basic Remote Administration Customers may file tickets for security updates only.
   * - Event Notification
     - 
     - Tickets related often to time-sensitive subscription activities such as, but not limited to, website traffic warnings, environment testing, scans, or releases; tickets are unlimited.
   * - Subscription
     - Non-billing inquiries
     - Tickets are unlimited.
   * - Billing
     - Financial inquiries
     - Tickets are unlimited.

Developer and Partner subscriptions are entitled to tickets for Acquia
Platform / Services, Subscription, and Billing only.

.. _resizing:

Emergency hardware resizing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Acquia monitors traffic and capacity for |acquia-product:ace|
subscriptions. If Acquia detects that your website has gone down or is
in imminent danger of going down for any reason (such as a significant
increase in web traffic or poor performing code), Acquia will add
additional server capacity to your website. We will contact you about
upsizing your website, but will not wait for your prior approval. You
will be responsible for any additional costs for the additional
hardware, and any upsizing will remain in effect for a minimum of one
week.

|acquia-product:ace| customers with qualified subscriptions can use
`Cloud Service Management </acquia-cloud/csm>`__, a self-service scaling
feature that allows web capacity to be managed at any time.

Acquia does not manage server capacity for |acquia-product:acs|
subscriptions. |acquia-product:acs| is a self-service platform, and
customers are responsible for monitoring their server capacity and
resizing as needed. For more information, see `Managing your
servers </acquia-cloud/manage/servers>`__.

.. _escalation_process:

Escalation process
------------------

Acquia recognizes that, on occasion, Customers may encounter critical
problems that require a higher level of communication and interaction.
We have established an effective process to support these special
situations.

If at any time you are not satisfied with the current plan of action for
an active issue, you may request that it be escalated to management
directly through your Acquia Support point of contact. You may also
request to review the matter with an Acquia Support manager.

The following actions take place when you escalate an issue:

#. The Acquia Support Leadership team is notified of the situation, and
   when appropriate, the Customer's Account Manager is notified as well.
#. A review of your business needs and technical case is conducted and
   an action plan is formulated with the goal of driving your issue to
   the most rapid resolution possible.
#. Communication of the action plan is discussed with the Customer,
   including deliverables and, if appropriate, timelines.
#. If the communication is not acceptable, the Customer may request to
   speak with the next level of management:

   -  First Level - Regional Manager
   -  Second Level - Director, Acquia Support
   -  Third Level - Managing Director, Global Support
   -  Fourth Level - VP Customer Solutions

All cases that are submitted as “Critical’ copy the Acquia Support
Leadership team. This helps ensure that these situations receive
management attention immediately.

.. _customer_resources:

Customer resources
------------------

Your Acquia subscription entitles you to access our enhanced support
resources.

.. _library:

|acquia-product:lib|
~~~~~~~~~~~~~~~~~~~~

The |liblink|_ is your source for technical documentation of Acquia’s service offerings as well as access to our knowledge base of troubleshooting tips, best practices, and solutions to known Acquia and Drupal issues. This is a great starting point for researching any non-critical issues you may be encountering.

.. |liblink| replace:: Acquia  \ |acquia-product:lib|\ 
.. _liblink: http://docs.acquia.com

Our |acquia-product:lib| includes:

-  Product documentation
-  Knowledge Base articles
-  Podcasts
-  Videos
-  Whitepapers
-  Training and webinar information

.. _support_portal:

Support Portal
~~~~~~~~~~~~~~

This is the launching pad for you to submit issues to Acquia Support. To
access the portal, visit http://insight.acquia.com/support/tickets.

.. _support_policies:

Support policies
~~~~~~~~~~~~~~~~

-  *Conference Bridge Participation* - Acquia understands that some of
   our Customers have a policy to open a conference bridge when an issue
   is defined and remain on that bridge until the problem is solved or
   the severity lessens. We have found that the bridge format is not
   conducive to orderly troubleshooting and often delays the resolution
   of critical issues. In order to provide all of our Customers with the
   highest quality of support possible, it is our policy to not
   participate in these bridge calls until a complete problem
   description has been provided. This may be done online or through a
   phone call. After Acquia receives this information, it will select
   the appropriate resource to join the call. Acquia management reserves
   the right to not assign resources to participate in bridge calls that
   are outside the scope of Acquia support.
-  *Customer chat channels* - Acquia Support will not establish or join
   customer chat channels.
-  *Conference Calls* - There are times when direct communication over a
   conference call or similar meeting is the best means of addressing a
   specific issue or clarifying recommendations that have been provided.
   Conference calls can be requested and scheduled by a request to a
   Customer Advisor or Support Leadership.
-  *Access to Customer Systems* - For the purposes of providing
   diagnostic support, Acquia Support may request read-only access to a
   Customer's environment. In limited situations, Acquia Support may
   make changes directly to a Customer's systems; however, action will
   not be taken until the Customer confirms by using the active support
   system that they understand the change to be made and authorize
   Acquia to make the change.

.. _customer_success:

Customer success tips
~~~~~~~~~~~~~~~~~~~~~

-  Maintain two or more team members (staff or contractors) that are
   familiar with all Customer-controlled code and infrastructure. This
   will assist Acquia Support with troubleshooting actions and
   facilitate the implementation of recommended solutions.
-  Ensure that subscription contacts are current.
-  Use the escalation process and contact channels previously described
   because they are the fastest way to drive action without any delay.
-  Ensure that multiple resources are registered to submit issues under
   your Acquia subscription.
-  Always respond to support tickets using the email address that's
   registered with Acquia.
-  Ensure that Customer resources are available to participate in the
   issue resolution process and are accessible for the duration of time
   that the incident remains open.
-  Ensure that all Customer designated resources understand the scope
   and conditions of Acquia's support prior to contacting Acquia.
-  Do one or both of the following prior to conducting a conference call
   with Acquia Support: define the questions/issues to be discussed, or
   complete as many outstanding action items as possible.
-  Check the Acquia Customer Portal often to stay up-to-date on training
   and the latest product updates and announcements.
-  If at any time you do not understand a request being made by Acquia
   Support, be sure to ask for a clarification or explanation.
-  Notify Acquia Support, Technical Account Manager, or the Onboarding
   team of any impending launches or significant website events. If
   possible, Acquia prefers a two-to-three day lead time. This allows
   Acquia to ensure that teams are notified and prepared for the event
   to provide critical support as needed.

.. _ra:

Remote Administration
---------------------

.. _ra_overview:

Overview of service
~~~~~~~~~~~~~~~~~~~

Acquia’s remote site administration (RA) service provides for Acquia to
handle typical and routine administration tasks that include normal
maintenance tasks and minor website modifications that would typically
be handled by an on-site administrator for a fully designed and
operating website. This includes proactive, timely security updates for
Drupal core and contributed modules. Modified core or contributed
modules are supported at Acquia's discretion, and run the risk of being
overwritten by Acquia automation unless properly configured by the
Customer.

Levels of RA support
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 35 65
   :header-rows: 1 

   * - Service
     - Description
   * - Premium Remote Site Administration
     - This covers security updates for Drupal core and contributed modules, module installation and configuration, creation and modification of views and content types, performance tuning, and recommendations for bug fixes to modules installed on Customer applications.
   * - Standard Remote Site Administration
     - This covers automated security updates for Drupal core and contributed modules. Testing is the responsibility of the Customer.

For more information about Acquia’s Remote Administration requirements
and standard practices, see the Acquia `Remote Administration </ra>`__
documentation pages.

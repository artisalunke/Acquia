.. include:: /common/global.rst

Acquia Cloud Edge Product Guide
===============================

.. container:: message-status

   |Acquia Cloud logo| For additional information about |acquia-product:cf|, see its `product documentation </edge>`__.

**Last updated: November 2, 2016**

Acquia will provide |acquia-product:cfp| and/or |acquia-product:cfc| services only if purchased by Customer, as indicated in the Order. A prerequisite for use of any |acquia-product:cf| Powered by CloudFlare service is one or more production Domains using |acquia-product:ace| or |acquia-product:edg|. Please note, Acquia reserves the right to remove any other Domain from |acquia-product:cfp| and |acquia-product:cfc|.

For purposes of this section, “Domain” means a Customer production domain configured for use with the |acquia-product:cf| service that maps to IP addresses or CNAME records provided by Acquia. Acquia treats each of the following as a separate Domain:

- ``example1.com``
- ``example2.com``
- ``example3.com``

.. note::

   All subdomains are included, so the subdomains below would all be one Domain for Acquia’s subscription tiers:

- ``example1.com``
- ``www.example1.com``
- ``blog.example1.com``
- ``store.example1.com``

#. **Acquia Cloud Edge Protect**

   |acquia-product:cfp| is a service that provides a web application firewall (WAF) and distributed denial-of-service (DDOS) protection designed to help mitigate the effects of online threats and optimize legitimate visitor requests for protected websites. In the event |acquia-product:cfp| does not automatically mitigate a DDOS attack against a Customer website, Acquia may create a custom WAF rule for the Customer to dilute the attack so the website remains as accessible to as many legitimate visitors as possible.

   Acquia will provide the |acquia-product:cfp| service for up to the number of Domains specified in the applicable Order.

   Customers may configure up to one development and one staging domain for each Domain.

   In the event Customer exceeds the number of permitted Domains, Acquia will notify Customer (including by email) of such excess and, within 10 days of such notice, Customer will either (i) provide Acquia with an Order for the applicable number of additional Domains required and pay all applicable fees in accordance herewith or (ii) remove the Domains necessary to comply with its then-current subscription. Acquia reserves the right to remove Domains in the event that Customer does not comply with the foregoing.

#. **Acquia Cloud Edge CDN**

   The |acquia-product:cfc| service provides a global content delivery network (CDN) and web content optimization (WCO) service designed to accelerate the delivery of Customer website content to the visitor and decrease website load times. The |acquia-product:cfc| service utilizes data centers around the world, except mainland China, to accelerate the delivery of the Customer website content. If the Customer requires fast website load times within mainland China through the use of mainland China data centers, an optional |acquia-product:cfc| China Network Access service is available. Use of the |acquia-product:cfc| China Network Access service requires the Customer to have or obtain a valid Internet Content Provider (ICP) license from the Chinese government.

   Customers may configure up to one development and one staging domain for each Domain.

   |acquia-product:cfc| is customized for each Customer based on Customer-specific factors including: number of Domains accelerated; monthly traffic throughput (TB/mo) for all Domains; number of Domains that require SSL protection; and the geographic distribution of global traffic from which visitors will access the Domains. Acquia reserves the right to change pricing to Customer, including in any renewal, to the extent Customer’s usage in any of such factors increases beyond the subscription purchased.

#. **Acquia Cloud Edge Service Level Agreement**

   The following |acquia-product:cf| Service Level Agreement ("Edge SLA") sets forth Acquia’s commitment to provide a level of service to each |acquia-product:cf| Customer. Acquia will use commercially reasonable efforts to make |acquia-product:cf| Services available 100% of every calendar month during the applicable Subscription Term. In the event Acquia does not meet the Edge Service Level, Customer will be eligible to receive an Edge Service Credit as described below.

#. **Edge SLA Definitions**

   Capitalized terms used in this Edge SLA and not otherwise defined have the meanings ascribed to them in the Subscription and Services Agreement.

   -  **Affected Customer Ratio** is calculated as follows: |br| 
      Affected Customer Ratio = (Unique Visitors as measured by IP address affected by Unscheduled Service Outage) / (Total unique visitors as measured by IP address)
   -  **Claim** means a claim submitted by Customer to Acquia pursuant to this Edge SLA that an Edge Service Level has not been met and that an Edge Service Credit may be due to Customer.
   -  **Customer** refers to the organization that has signed a Subscription Services Agreement under which it has purchased Edge Services from Acquia.
   -  **Customer Support** means the services by which Acquia may provide assistance to Customer to resolve issues with the Edge Services.
   -  **Edge Service** means Acquia Cloud Edge Protect and/or Acquia Cloud Edge CDN services, as further described in an Order Form.
   -  **Edge Service Credit** is the percentage of the monthly service fees for the Edge Service that is credited to Customer for a validated Claim.
   -  **Edge Service Level** means standards Acquia chooses to adhere to and by which it measures the level of service it provides as specifically set forth below.
   -  **Force Majeure** refers to any downtime minutes that are the result of events or conditions beyond Acquia’s reasonable control. Such events might include but are not limited to any acts of common enemy, the elements, earthquakes, floods, fires, epidemics, and inability to secure products or services from other persons or entities.
   -  **Incident** means any set of circumstances resulting in a failure to meet the Edge Service Level.
   -  **Outage Period** is equal to the number of downtime minutes resulting from an Unscheduled Service Outage.
   -  **Planned Downtime** is downtime specified by the Customer or Acquia that is to be excluded from any calculation of an Outage Period. This would apply to any time when the Customer has requested Edge Service access suspended from their environment. This also covers outages caused by Acquia’s scheduled maintenance (typically 11pm to 7am at the datacenter location identified on Customer’s Order), provided Acquia notifies Customer 48 hours prior to the commencement of the maintenance work (there will be no more than two hours of scheduled maintenance downtime per calendar year).
   -  **Scheduled Availability** is the total number of minutes in the month minus any Planned Downtime, and downtime caused by Force Majeure.
   -  **Unscheduled Service Outage** are those interruptions to the Edge Service that have not been previously communicated to the Customer and that result in the Customer's application being unavailable to its customers or users. Unscheduled Service Outages exclude downtime minutes resulting from Planned Downtime or downtime cause by Force Majeure.

#. **Edge Service Credit Claims**

   Acquia provides this Edge SLA subject to the following terms.

   In order to be eligible to submit a Claim with respect to any Incident, the Customer must first have notified Acquia Support Services of the Incident via Acquia’s support procedures as described in the Support Users Guide within three business days following the Incident.

   To submit a Claim, Customer must contact Acquia Support Services and provide notice of its intention to submit a Claim. Customer must provide to Acquia all reasonable details regarding the Claim, including but not limited to, detailed descriptions of the Incident(s), the duration of the Incident, network traceroutes, the URL(s) affected, and any attempts made by Customer to resolve the Incident.

   In order for Acquia to consider a Claim, Customer must submit the Claim, including sufficient evidence to support the Claim, by the end of the billing month following the billing month in which the Incident that is the subject of the Claim occurs.

   Acquia will use all information reasonably available to it to validate Claims and make a good faith judgment on whether the Edge SLA and Edge Service Levels apply to the Claim.

#. **Edge SLA Exclusions**

   This Edge SLA and any applicable Edge Service Levels do not apply to any performance or availability issues:

   a. due to factors outside Acquia reasonable control
   b. that resulted from Customer's or third party hardware or software
   c. that resulted from actions or inactions of Customer or third parties
   d. caused by Customer's use of the Edge Service after Acquia advised Customer to modify its use of the Edge Service, if Customer did not modify its use as advised
   e. during beta and trial Services (as determined by Acquia)
   f. attributable to the acts or omissions of Customer or Customer's employees, agents, contractors, or vendors, or anyone gaining access to Acquia’s Service by means of Customer's Authorized Users' accounts or equipment

#. **Edge Service Credits**

   Edge Service Credits are Customer's sole and exclusive remedy for any violation of this Edge SLA. The total amount of Edge Service Credits awarded in any yearly billing period shall not, under any circumstance, exceed six (6) months of a Customer's cumulative total monthly service fees. Edge Service Credits for this Edge SLA will only be calculated against monthly recurring fees associated with the Edge Service.

#. **Edge Service Credit Calculation**

   For any and each Outage Period during a monthly billing period Acquia will provide as an Edge Service Credit an amount calculated as follows:

   Edge Service Credit = ((Outage Period minutes) * (Affected Customer Ratio)) / (Scheduled Availability minutes)

#. **Methodology**

   Acquia is not responsible for comprehensive monitoring of Customer Content; this responsibility lies with Customer. Acquia will review data on a Customer's reported Outage Periods as determined by any commercially reasonable independent measurement system used by the Customer. Acquia will use all information reasonably available to it in order to calculate the Affected Customer Ratio during an Outage Period, including analysis of Edge Service data immediately prior to the Outage Period to estimate the ratio of a Customer's visitors that were affected during an Outage Period at one or more of Acquia’s data centers.

#. **Acquia Cloud Edge Quick Start**

   |acquia-product:onb| will provide the |acquia-product:cf| Quick Start services below only if purchased by Customer, as indicated in the Order.

   Customer must purchase a Quick Start for each Order that includes |acquia-product:cfp| or |acquia-product:cfc| services. The Quick Start services are performed over the course of two weeks and include:

   - |acquia-product:cf| initial account provisioning assistance, including set up for (i) one initial Customer account, (ii) one initial Customer Domain, and (iii) up to ten additional users, with role assignments.
   - Familiarization with |acquia-product:cfp| and/or |acquia-product:cfc| through an introduction and guided walkthrough of the administration dashboard, to be scheduled with an |acquia-product:onb| Customer Success Manager.
   - Initial configuration of the first production website Domain hosted through |acquia-product:ace| or |acquia-product:edg| within |acquia-product:cf| using either the CloudFlare nameserver or CNAME approach.
   - Assistance with discovering and implementing |acquia-product:cf| features (for example, page rules for business specific caching policy) for up to one Domain, up to a maximum of five hours.

.. container:: message-status

   Acquia Inc. reserves the right to change the Products and Services Guide based on prevailing market practices and the evolution of our products. Changes will not result in a degradation in the level of services provided during the period for which fees for such services have been paid.

.. |Acquia Cloud logo| image:: https://cdn4.webdamdb.com/1280_s0InPk2T0pQ2.png?1527270742
   :class: no-sb
   :width: 30px

.. include:: /common/global.rst

Acquia Journey Product Guide
============================

.. container:: message-status

   |Acquia Journey logo| For additional information about |acquia-product:aj|, see its `product documentation </journey>`__.

**Last updated: October 16, 2017**

|acquia-product:aj| is a *customer journey orchestration* solution that empowers brands to own the customer journey from end to end, to meet the increasing demands for individualized experiences. |acquia-product:aj| allows brands to map out and orchestrate intelligent, data-driven customer journeys by unifying decision logic across systems, touchpoints and channels. (For example, with |acquia-product:aj|, a brand can monitor an individual’s actions and create Facebook ad groups and trigger targeted ads or generate a personalized email or SMS text with a targeted offer, in context to one or more previous journey steps.)

|acquia-product:aj| enables brands to plan customer journeys and orchestrate experiences (digital and physical) that deliver best-next actions to the customer, at the right time, to keep people engaged and moving toward their goals. |acquia-product:aj| provides a nervous system for the entire marketing stack, allowing real-time responses to events and triggers across siloed devices and channels, ensuring every data point is captured and incorporated so that what customers see and experience is in context to their journey in that moment.

#. **Acquia Journey Elements**
   A subscription to |acquia-product:aj| includes the following elements to support orchestration initiatives:

   - *Profile Manager* - Capture and unify customer data into a single visitor profile
   - *Journey Hub* - Map, orchestrate, manage and analyze omni-channel customer journeys

   1.1 **Profile Manager**
      |acquia-product:lpm| unifies person profile data collected from Customer’s Drupal or non-Drupal websites and, if the Customer purchases |acquia-product:lplp| or |acquia-product:lplpo|, from other sources, such as customer relationship managers (CRMs) and email. |acquia-product:lpm| tracks the behavior of anonymous and identified customers throughout their customer journey — from first point of interaction as an anonymous person through to becoming a repeat, loyal customer. |acquia-product:lpm| creates a unified profile for each person based on their historical and real-time behavior, described as follows:

      -  Real-time profiling and segmentation:

         -  Real-time collection of data and behavior for anonymous and identified people
         -  Person profile configuration and search
         -  Segment builder and size estimation tool
         -  Real-time person segmentation
         -  JavaScript API
         -  Ability to export up to 31 days of person-data using the user interface

      -  Analytics:

         -  Pre-built reports and dashboards that provide information about people's behavior and trends, including person, touch and events, segments, conversion, and engagement

      -  Data retention:

         -  Person profile behavioral data (touches and events) is retained for 13 months

      The data collected by |acquia-product:lpm| is non-personal information typically about user's online activity and interests, similar to web analytics (for example, a user read a specific article, opened an email newsletter, or prefers content related to movies). The IP address of the person is stored in order to determine their geography, but optionally can be masked before being stored. Additional information can be collected about a person solely at the discretion of Customer. To unify profile data from other sources such as marketing automation, identifiers such as email addresses or user ids can also optionally be stored. It is solely at Customer's discretion to determine which identifiers they wish to store in |acquia-product:lpm|, if any. Identifiers can also optionally employ a one-way encryption hash. |br| 
      |acquia-product:lpm| data is stored in the cloud in a NoSQL database and a data warehouse, in order to support the real-time profiling and segmentation, and analytics functions described above. Depending on the Subscription purchased, this data can be viewed using the |acquia-product:lpm| user interface and optionally accessed using APIs and data warehouse connection. |acquia-product:lpm| data is owned by Customer.
   #. **Journey Hub**
      The Journey Hub allows customers to map, orchestrate, manage and analyze customer journeys. This includes the following discrete capabilities.

      - *Journey Editor* - Map customer journeys, export them as files, create and report on key performance indicators
      - *Graph Editor and Graph Engine* - Design, configure, and deploy Journey Graphs for real time decisioning, including versioned graphs, testing console, multiple environments, and service alerts
      - *Admin, Configuration and Strategy Collaboration Interfaces* - Manage users, groups, connections, and projects, and display appropriate controls based on user and group roles
      - *Journey Metrics* - Define and measure key performance indicators, and view those measures on dashboards and overlaid on journey maps

#. **Subscription Packages** |br| 
   Subscriptions to |acquia-product:aj| include the |acquia-product:aj| Hub and |acquia-product:lpm| elements described above, as well as support and onboarding services described in sections 3 through 5. Subscriptions are tiered based on Monthly Unique Persons. |br| 
   Monthly Unique Persons (MUPs) shall mean the total number of Persons who are Active in a given month, where (i) *Person* means a record, identified by either a single identifier or multiple merged identifiers (for example, anonymous cookie ID, email address, account ID or other similar reference), and (ii) *Active* means having an event recorded against such Person’s profile (for example, page view, email, ad impression, or other activity) in the applicable calendar month.
#. **Support Services** |br| 
   Customer’s subscription to |acquia-product:aj| includes unlimited diagnosis support for |acquia-product:aj| as described in the `Supportability Matrix </support/guide#supportability>`__ in the Support Users' Guide. Customer can contact Acquia Support in accordance with the `Support Users Guide </support/guide>`__ and in accordance with stated `Urgency Levels </support/guide#problem>`__. Initial response times for support requests vary on the urgency level and Customer’s Subscription tier as described in the `Support Users Guide </support/guide>`__.
#. **Service Level Policy**

   4.1 **Service Commitment**
      Acquia will use commercially reasonable efforts to make |acquia-product:aj| available for 99.9% during any calendar month during the applicable Subscription Term (the *Service Commitment*). In the event Acquia does not meet the Service Commitment, Customer will be eligible to receive a Service Credit as described below. |br| 
      System Availability will be based on the availability to Customer of |acquia-product:aj| and is not a guarantee that any particular End Customer developed process will execute correctly. System Availability is measured separately for two distinct services, both considered a 50% contribution to overall availability; firstly, availability of the user and admin interfaces for building customer journeys (*Hub*); and secondly, availability of engines to execute customer journey processes (*Engine*).
   4.2 **Definitions** |br| 
      *Availability* will be calculated per calendar month, as follows: **((total – nonexcluded – excluded) / (total excluded) \* 100) ≥ 99.9%** |br| 
      where:

      - **total** means the total number of minutes for the calendar month \* number of clients
      - **nonexcluded** means downtime/unavailability that is not excluded \* number of affected clients
      - **excluded** means the Service Commitment exclusions defined below

      *Unavailability* means that the SaaS infrastructure is unresponsive or responds with an error.
      *General Availability* is calculated per calendar month as follows: **(Hub Availability / 2) + (Engine Availability / 2)**
   4.3 **Service Credits** |br| 
      In the event |acquia-product:aj| does not meet 99.9% General Availability for a calendar month, for each one-half hour of unavailability Customer will receive a service credit equal to the prorated portion the Subscription Term for the period of unavailability (each a *Service Credit*). To properly claim a Service Credit, Customer must inform Acquia within thirty days of the purported outage and provide a description of the service interruption. If Customer has accumulated Service Credits during two consecutive months or three months in any six month period, Customer may terminate the applicable order upon written notice to Acquia.
   4.4 **Service Commitment Exclusions** |br| 
      The Service Commitment does not apply to any unavailability, outage, suspension or termination of any SaaS performance issues: (i) any outages solely attributable to flaws in Customer’s environment (including the underlying code) where, despite reasonable notification from Acquia that such flaws are adversely impacting availability and Customer fails to correct such flaws (for example, failure to upsize to recommended hardware configuration), (ii) any outages lasting less than one minute but no more than 3 such outages in a 24 hour period; (iii) any outages resulting from scheduled maintenance (typically 11pm to 7am at the datacenter location applicable to Customer), if Acquia notified Customer 96 hours prior to the commencement of the maintenance work (there will be no more than two hours of scheduled maintenance downtime per calendar year); (iv) Unavailability that relates to any malware, viruses, Trojan horses, spyware, worms or other malicious or harmful code in the website that (1) was not introduced by Acquia or (2) was not introduced as a result of Acquia’s failure to perform the Services in compliance with the standard included herein or in the Agreement; or (v) acts or omissions caused by Customer’s CDN. |br| 
      In the event of any outages described above, Acquia will use commercially reasonable efforts to minimize any disruption, inaccessibility and/or inoperability of the website in connection with outages, whether scheduled or not. Such efforts will include instances in another availability zone if available.

#. **Onboarding and Add-on Services**

   5.1 **Onboarding** |br| 
      Onboarding for |acquia-product:aj| includes an new product introduction call (performed remotely) to ensure the Customer has accounts and links to documentation and to schedule on-site training. Onsite training consists of a two day meeting for Marketing and Marketing IT that includes a demonstration of the product, a facilitated meeting to the use of |acquia-product:aj| for communication between Marketing and IT, and technical training for |acquia-product:aj| implementers to implement pre-defined journey jumpstarts. Onboarding concludes with up to two weeks of on-demand implementation assistance to reach the point where the journey jumpstarts could go live. Onboarding is included as part of the |acquia-product:aj| subscription.
   5.2 **Add-on Service: Acquia Journey Technical Implementation** |br| 
      Customers who desire technical assistance implementing additional Journey maps or graphs can purchase |acquia-product:aj| integration services. These services will be scoped and priced individually based on the Customer requirements.
   5.3 **Add-on Service: Acquia Journey Strategy Consulting** |br| 
      Customers who desire consulting services on how to use |acquia-product:aj| as part of their marketing strategy can purchase strategy services from Acquia as an add-on service. Such services will be scoped and priced individually based on the Customer requirements.
   5.4 **Add-on Service: Acquia Journey Implementation Training** |br| 
      Customers who desire in-person training beyond what is included in onboarding for their implementation teams on |acquia-product:aj| can purchase |acquia-product:aj| implementation training. Such services will be scoped and priced individually based on the Customer requirements.
   5.5 **Add-on Service: Acquia Journey Onboarding On-Demand** |br| 
      Customers who wish to refresh onboarding for their existing team or onboard a new team onto |acquia-product:aj| can purchase onboarding services on demand. Such services will be scoped and priced individually based on the Customer requirements.

.. container:: message-status

   Acquia Inc. reserves the right to change the Products and Services Guide based on prevailing market practices and the evolution of our products. Changes will not result in a degradation in the level of services provided during the period for which fees for such services have been paid.

.. |Acquia Journey logo| image:: https://cdn2.webdamdb.com/1280_UYxgctc1ja61.png?-62169955200
   :class: no-sb
   :width: 30px

.. include:: /common/global.rst

Acquia Lift Product Guide
=========================

.. container:: message-status

   |Acquia Lift logo| For additional information about |acquia-product:cha|, see its `product documentation </lift>`__.

**Last updated: February 12, 2018**

|acquia-product:cha| unifies Customer content and profile data from multiple sources to deliver in-context, personalized experiences across any channel or device.

Acquia will provide the |acquia-product:cha| Subscription Service described below only if purchased by Customer, as indicated in the Order.

#. **Acquia Lift Elements** |br| 
   A subscription to |acquia-product:cha| includes the following elements that will enable the Customer to assist with its content personalization and content distribution goals:

   - **Profile Manager** - Capture and unify customer data into a single visitor profile
   - **Experience Builder** - Interface for creating and executing personalized digital experiences
   - **Content Hub** - Distribute content and discover existing content

   1.1 **Profile Manager** |br| 
      |acquia-product:lpm| unifies person profile data collected from Customer’s Drupal or non-Drupal websites and, if the Customer purchases |acquia-product:lplp| or |acquia-product:lplpo|, other sources, such as CRM and email. It tracks the behavior of anonymous and identified customers throughout their customer journey — from first point of interaction as an anonymous person through to becoming a repeat, loyal customer. |acquia-product:lpm| creates a unified profile for each person based on their historical and real-time behavior, described as follows:

      - Real-time profiling and segmentation:
             - Real-time collection of data and behavior for anonymous and identified people
             - Person profile configuration and search
             - Segment builder and size estimation tool
             - Real-time person segmentation
             - JavaScript API
             - Ability to export up to 31 days of person-data using the user interface

      - Analytics:
             - Pre-built reports and dashboards that provide information about people's behavior and trends, including person, touch and events, segments, conversion, and engagement.

      - Data retention:
             - Person profile behavioral data (touches and events) is retained for 13 months.

      - Up to 100,000 monthly unique people. Additional people require add-on packs.

      The data collected by |acquia-product:lpm| is non-personal information typically about user's online activity and interests, similar to web analytics (for example, a user read a specific article, opened an email newsletter, or prefers content related to movies). The IP address of the person is stored in order to determine their geography, but optionally can be masked before stored. Additional information can be collected about a person solely at the discretion of Customer. |br| 
      In order to unify profile data from other sources such as marketing automation, identifiers such as email addresses or user ids can also optionally be stored. It is solely at Customer's discretion to determine which identifiers they wish to store in Profile Manager, if any. Identifiers can also optionally employ a one-way encryption hash. |br| 
      |acquia-product:lpm| data is stored in the cloud in a NoSQL database and a data warehouse, in order to support the real-time profiling and segmentation, and analytics functions described above. Depending on the Subscription purchased, this data can be viewed using the |acquia-product:lpm| user interface and optionally accessed using APIs and data warehouse connection. |acquia-product:lpm| data is owned by Customer.
   1.2 **Experience Builder** |br| 
      |acquia-product:leb| unifies content and profile data from multiple sources to deliver in-context, personalized experiences on Drupal or non-Drupal websites. It provides a drag-and-drop user interface that overlays on top of any website to allow a user to build rules that define which content to test or target to different segments of users. The content that is available to a user for building personalizations is based on all content published to |acquia-product:ch| from one or more content sources.

      - Testing and targeting of web visitors:
             - |acquia-product:leb| user interface for defining rules and content directly on any webpage
             - A/B testing
             - Content targeting
             - Goals and events management

      - Analytics:
             - Performance reports for A/B tests and targeting.

   1.3 **Content Hub** |br| 
      |acquia-product:ch| is a cloud-based content distribution and discovery service that enables customers to author, search, and share content throughout a complex network of websites and channels. |acquia-product:ch| connects content bi-directionally, enabling global enterprises to discover, reuse, and distribute content throughout their entire organization in a secure cloud environment.

      - |acquia-product:ch| empowers content curators, managers, and creators to take control of their content with a robust set of content discovery and sharing tools, including:
             - A content repository that aggregates and normalizes content and data from any enterprise content source or system.
             - Content discovery tools, including automatic updates and faceted search, to break down content silos and enable enterprise content managers to quickly find relevant content from other enterprise websites, departments, or technologies.
             - Automated subscription updates from content authors to content consumers in near real time, respecting local changes and workflow rules.

      - 99.9% |acquia-product:ch| SLA on the |acquia-product:ch| Service.
      - |acquia-product:ch| Drupal connector modules including ongoing module releases.
      - Publish content into |acquia-product:ch| from an unlimited number of Drupal websites using Acquia-provided connector modules with storage not to exceed 500,000 documents.
      - Subscribe to content into up to five (5) Drupal websites using Acquia-provided connector modules.
      - Access the |acquia-product:ch| API to build custom integrations with non-Drupal applications.

#. **Subscription Packages** |br| 
   |acquia-product:cha| is available in four editions:

   - |acquia-product:lpls|
   - |acquia-product:lplp|
   - |acquia-product:lplpw|
   - |acquia-product:lplpo|

   2.1 **Acquia Lift - Standard** |br| 
      |acquia-product:lpls| includes:

      - |acquia-product:lpm|, as previously described
      - |acquia-product:leb|, as previously described
      - |acquia-product:ch|, as previously described

   2.2 **Acquia Lift - Premium** |br| 
      |acquia-product:lplp| extends the capabilities of |acquia-product:lpls| for omni-channel use cases. It provides all of the functionality of |acquia-product:lpls| plus the following:

      - Real-time profiling and segmentation:
             - Ability to export unlimited amount of data using APIs in addition to the 31 day export that is available in the user interface of the base |acquia-product:lpm|

      - Testing and targeting of web visitors:
             - Decision API for creating rules and retrieving decisions in support of testing and targeting on non-web channels

      - Exchange person data with existing sources such as CRM systems, marketing automation tools, and third party data sources to augment the person profile and share this person data and associated segments with other channels, such as email platforms:
             - File import API
             - File export APIs
             - Push API
             - REST APIs

      - Prebuilt integrations with complementary marketing systems:
             - Marketo
                   - Marketo leads imported to |acquia-product:cha| as People
                   - Marketo activities imported to |acquia-product:cha| as Events
                   - Configurable lead field and activity mappings

      - Dedicated data warehouse
             - Dedicated Redshift database, containing |acquia-product:cha| unified profiles (person, touch, event, rankings, segments, identities).
             - One provisioned user account for connecting to the database, optionally secured with a self-signed certificate.
             - The standard configuration for the database connection provides up to 2 TB of storage in one Region for up to five concurrent queries.

      - Analytics:
             - Utilizes dedicated data warehouse above for faster performance compared to |acquia-product:lpls|.

      - Decision API - Customers can utilize Decision API for creating rules and retrieving decisions in support of testing and targeting on non web-channels
      - |acquia-product:ch|, as previously described.

   2.3 **Acquia Lift Starter - Standard** |br| 
      |acquia-product:lplpw| is a component of |acquia-product:lpls| edition, purchased as a stand-alone subscription. |acquia-product:lplpw| is intended for data collection from the web channel, and includes:

      - Profile Manager element as indicated above.
      - Non-production use of Experience Builder - Customers can utilize testing and targeting functionality for non-production use upon request (for example, development and testing, or evaluation).
      - Non-production use of |acquia-product:ch| as indicated above: Customers can utilize content distribution and discovery functionality for non-production use upon request (for example, development and testing, or evaluation).

   2.4 **Acquia Lift Starter - Premium** |br| 
      |acquia-product:lplpo| is a component of |acquia-product:lplp| edition, purchased as a stand-alone subscription. |acquia-product:lplpo| unifies profile data from any channel or system. It provides all of the functionality of |acquia-product:lplpw| plus the following:

      - Real-time profiling and segmentation:
             - Ability to export unlimited amount of data using APIs in addition to the 31day export that is available in the user interface of the base |acquia-product:lpm|

      - Exchange person data with existing sources such as CRM systems, marketing automation tools, and third party data sources to augment the person profile and share this person data and associated segments with other channels, such as email platforms:
             - File import API
             - File export APIs
             - Push API
             - REST APIs

      - Prebuilt integrations with complementary marketing systems:
             - Marketo
                   - Marketo leads imported to |acquia-product:cha| as People
                   - Marketo activities imported to |acquia-product:cha| as Events
                   - Configurable lead field and activity mappings

      - Dedicated data warehouse
             - Dedicated Redshift database, containing |acquia-product:cha| unified profiles (person, touch, event, rankings, segments, identities).
             - One provisioned user account for connecting to the database, optionally secured with a self-signed certificate.
             - The standard configuration for the database connection provides up to 2 TB of storage in one Region for up to five concurrent queries.

      - Analytics:
             - Utilizes dedicated data warehouse above for faster performance compared to |acquia-product:lplpw| option.

      - Non-production use of Experience Builder - Customers can utilize testing and targeting functionality for non-production use upon request (for example, development and testing, or evaluation).
      - Non-production use of Decision API - Customers can utilize Decision API for creating rules and retrieving decisions in support of testing and targeting on non web-channels for non-production use upon request (for example, development and testing, or evaluation).
      - Non-production use of |acquia-product:ch| as indicated above. Customers can utilize content distribution and discovery functionality for non-production use upon request (for example, development and testing, or evaluation).

   2.5 **Developer Account** |br| 
      Customers who require a separate developer account (|acquia-product:cha| Account and |acquia-product:ch| instance) for development and testing can have one upon request for non-production use. This developer account does not include a dedicated Redshift connection. Objects like rules, slots, events, segments, and content are not synchronized between a customer's production account and the developer account.

#. **Subscription Add-on Packs** |br| 
   All subscriptions of |acquia-product:lpm| and |acquia-product:cha| are licensed based on:

   - The number of total monthly unique people, across all channels and websites, as measured by |acquia-product:cha| analytics, based on the monthly average over the previous 12 months. 100,000 monthly unique people are included with each edition.
   - The number of subscribing websites (and applications if allowed), as measured by the number of websites/applications that content to the |acquia-product:ch| service and register webhooks to update their content. Five (5) subscribing websites are included with edition.

   3.1 **People add-on packs (for Data Collection and Personalization use cases)** |br| 
      Unique people add-on packs are available in the following allotments:

      - add-on 100,000 additional monthly unique people
      - add-on 500,000 additional monthly unique people
      - add-on 1,000,000 additional monthly unique people
      - add-on 5,000,000 additional monthly unique people

   3.2 **Content Subscriber add-on packs (for Content Syndication/Content Hub use cases)** |br| 
      Subscribing website add-on packs are available in the following allotments:

      - add-on 10 subscribing websites/applications. Publish content into |acquia-product:ch| from an unlimited number of Drupal websites using Acquia-provided connector modules with storage limit increased by 500,000 documents.
      - add-on 50 subscribing websites/applications. Publish content into |acquia-product:ch| from an unlimited number of Drupal websites using Acquia-provided connector modules with storage limit increased by 1,000,000 documents.
      - add-on 100 subscribing websites/applications. Publish content into |acquia-product:ch| from an unlimited number of Drupal websites using Acquia-provided connector modules with storage limit increased by 2,000,000 documents.
      - add-on 500 subscribing websites/applications. Publish content into |acquia-product:ch| from an unlimited number of Drupal websites using Acquia-provided connector modules with storage limit increased by 7,500,000 documents.

#. **Support Services** |br| 
   Customer’s subscription to |acquia-product:cha| includes unlimited diagnosis support for |acquia-product:cha| as described in the `Supportability Matrix </support/guide#supportability>`__ in the Support Users' Guide. Customer can contact Acquia Support in accordance with the `Support Users Guide </support/guide>`__ and in accordance with stated `Urgency Levels </support/guide#problem>`__. Initial response times for support requests vary on the urgency level and Customer’s Subscription tier as described in the `Support Users Guide </support/guide>`__.
#. **Service Level Policy for Content Hub** |br| 
   Acquia will use commercially reasonable efforts to make the |acquia-product:ch| infrastructure available for 99.9% during any calendar month during the applicable Subscription Term (“|acquia-product:ch| SLA”). Availability and Unavailability shall be calculated in accordance with the formula set forth in Acquia's `Service Level Policy </guide/service-level>`__. In the event Acquia does not meet the |acquia-product:ch| SLA for a calendar month, the parties shall be entitled to the rights and remedies set forth in the `Service Extensions section </guide/service-level#extend>`__, subject to the following Service Commitment Exclusions.

   5.1 **Service Commitment Exclusions**
      The Service Commitment does not apply to any unavailability, outage, suspension, or termination of any Acquia SaaS performance issues:
      i. due to factors outside Acquia reasonable control
      ii. that resulted from Customer's or third party hardware or
      software
      iii. that resulted from actions or inactions of Customer or third
      parties
      iv. caused by Customer's use of the |acquia-product:ch| Service
      after Acquia advised Customer to modify its use of the Service, if
      Customer did not modify its use as advised
      v. during beta and trial Services (as determined by Acquia)
      vi. attributable to the acts or omissions of Customer or
      Customer's employees, agents, contractors, or vendors, or anyone
      gaining access to Acquia’s Service by means of Customer's
      Authorized Users' accounts or equipment

#. | **Included Enablement Packages** |br| 
   | As part of their subscription, Customers will receive one of the
     following onboarding packages:

   - |acquia-product:lplpw| - Enablement Service
   - |acquia-product:lplpo| - Enablement Service
   - |acquia-product:lepp| - Standard - Enablement Service
   - |acquia-product:lepp| - Premium - Enablement Service
   - |acquia-product:lepc| - Standard - Enablement Service
   - |acquia-product:lepc| - Premium - Enablement Service

   Customers working on a new website build or who do not have initial personalization or data management use cases defined should also purchase an Initiate Workshop.

   6.1 **Acquia Lift Starter - Standard - Enablement Service**
      The |acquia-product:lplpw| - Enablement Service is an onboarding
      package designed for customers whose primary focus is data
      collection from the web channel. It is comprised of remotely
      delivered onboarding services provided by functional and technical
      experts from the Customer Success team. This package performs the
      technical installation of the product, trains the Customer on the
      fundamentals of |acquia-product:cha|, and helps the Customer
      configure the product. Regular check-ins are established to help
      the Customer evolve and adapt their strategy.
      During enablement, Acquia may find that additional code and
      configuration changes to Customer’s Drupal website are necessary
      for 100% |acquia-product:cha| compatibility. Non-Drupal and
      self-hosted customers will be responsible for technical
      installation of the |acquia-product:cha| components on their
      websites, with guidance from Acquia.
      Customers working on a new website build or who do not have
      initial use case defined should purchase an Initiate Workshop.
   6.2 **Acquia Lift Starter - Premium - Enablement Service**
      The |acquia-product:lplpo| - Enablement Service is an onboarding
      package designed for customers whose primary focus is data
      collection from a variety of systems or channels. It is comprised
      of remotely delivered onboarding services provided by functional
      and technical experts from the Customer Success team. This package
      performs the technical installation of the product, trains the
      Customer on the fundamentals of |acquia-product:cha|, and helps
      the Customer configure the product. The package also provides
      consultation on using the |acquia-product:cha| APIs and pre-built
      integrations to integrate |acquia-product:cha| with other systems,
      and using the data warehouse. Regular check-ins are established to
      help the Customer evolve and adapt their strategy.
      During enablement, Acquia may find that additional code and
      configuration changes to Customer’s Drupal website are necessary
      for 100% |acquia-product:cha| compatibility. Non-Drupal and
      self-hosted customers will be responsible for technical
      installation of the |acquia-product:cha| components on their
      websites, with guidance from Acquia.
      Customers working on a new website build or who do not have
      initial use case defined should purchase an Initiate Workshop.
   6.3 **Acquia Lift for Personalization - Standard - Enablement Service**
      The |acquia-product:lepp| - Standard - Enablement Service is an
      onboarding package designed for customers whose primary focus is
      personalization on the web channel. It is comprised of remotely
      delivered onboarding services provided by functional and technical
      experts from the Customer Success team. This package performs the
      technical installation of the product, trains the Customer on the
      fundamentals of |acquia-product:cha|, establishes an initial set
      of personalization use cases, and helps the Customer configure an
      initial set of campaigns and measure their performance. Regular
      check-ins after the initial set of campaigns are established are
      designed to help the Customer implement additional personalization
      use cases and evolve and adapt their strategy.
      During enablement, Acquia may find that additional code and
      configuration changes to Customer’s Drupal website are necessary
      for 100% |acquia-product:cha| compatibility. Non-Drupal and
      self-hosted customers will be responsible for technical
      installation of the |acquia-product:cha| components on their
      websites, with guidance from Acquia.
      Customers working on a new website build or who do not have
      initial use case defined should purchase an Initiate Workshop.
   6.4 **Acquia Lift for Personalization - Premium - Enablement Service**
      The |acquia-product:lepp| - Premium - Enablement Service is an
      onboarding package designed for customers who are focused on
      omni-channel personalization. It is comprised of remotely
      delivered onboarding services provided by functional and technical
      experts from the Customer Success team. This package performs the
      technical installation of the product, trains the Customer on the
      fundamentals of |acquia-product:cha|, establishes an initial set
      of personalization use cases, and helps the Customer configure an
      initial set of campaigns and measure their performance. The
      package also provides consultation on using the
      |acquia-product:cha| APIs and pre-built integrations to integrate
      |acquia-product:cha| with other systems, and using the data
      warehouse. Regular check-ins after the initial set of campaigns
      are established are designed to help the Customer implement
      additional personalization use cases and evolve and adapt their
      strategy.
      During enablement, Acquia may find that additional code and
      configuration changes to Customer’s Drupal website are necessary
      for 100% |acquia-product:cha| compatibility. Non-Drupal and
      self-hosted customers will be responsible for technical
      installation of the |acquia-product:cha| components on their
      websites, with guidance from Acquia.
      Customers working on a new website build or who do not have
      initial use case defined should purchase an Initiate Workshop.
   6.5 **Acquia Lift for Content Syndication - Standard - Enablement Service**
      The |acquia-product:lepc| - Standard - Enablement Service is an
      onboarding package designed for customers whose primary focus is
      content syndication through Drupal websites. It is comprised of
      remotely delivered onboarding services provided by functional and
      technical experts from the Customer Success team. This package
      performs the technical installation of the product, trains the
      Customer on the fundamentals of |acquia-product:cha|, establishes
      an initial content syndication use cases, and helps the Customer
      configure the content discovery interface.
      During enablement, Acquia may find that additional code and
      configuration changes to Customer’s Drupal website are necessary
      for 100% |acquia-product:cha| compatibility. Self-hosted customers
      will be responsible for technical installation of the
      |acquia-product:cha| components on their websites, with guidance
      from Acquia.
      Customers working on a new website build or who do not have
      initial use case defined should purchase an Initiate Workshop.
   6.6 **Acquia Lift for Content Syndication - Premium - Enablement Service**
      The |acquia-product:lepc| - Premium - Enablement Service is an
      onboarding package designed for customers who are focused on
      content syndication across various technologies/platforms. It is
      comprised of remotely delivered onboarding services provided by
      functional and technical experts from the Customer Success team.
      This package performs the technical installation of the product,
      trains the Customer on the fundamentals of |acquia-product:cha|,
      establishes an initial set of Content Syndication use cases, and
      helps the Customer configure the content discovery interface. The
      package also provides consultation on using the
      |acquia-product:cha| APIs and pre-built integrations to integrate
      |acquia-product:cha| with other systems.
      During enablement, Acquia may find that additional code and
      configuration changes to Customer’s Drupal website are necessary
      for 100% |acquia-product:cha| compatibility. Non-Drupal and
      self-hosted customers will be responsible for technical
      installation of the |acquia-product:cha| components on their
      websites, with guidance from Acquia.
      Customers working on a new website build or who do not have
      initial use case defined should purchase an Initiate Workshop.

.. container:: message-status

   Acquia Inc. reserves the right to change the Products and Services Guide based on prevailing market practices and the evolution of our products. Changes will not result in a degradation in the level of services provided during the period for which fees for such services have been paid.

.. |Acquia Lift logo| image:: https://cdn4.webdamdb.com/1280_6hBD2tUaE8E2.png?-62169955200
   :class: no-sb
   :width: 30px

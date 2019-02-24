.. include:: /common/global.rst

|acquia-product:cha| glossary
=============================

|acquia-product:cha| has several terms that have specific definitions
based on their use in the product.

.. list-table::
   :widths: 30 70
   :header-rows: 1 

   * - Term
     - Definition
   * - Binary Files/Assets
     - The content published to |acquia-product:ch|.
   * - Category
     - A group of related fields collected in the `person profile <#profile>`__ which are available for segmentation in the segment builder part of |acquia-product:lpm| used for defining groups of users to target. Examples include ``Current Location`` includes City, Region, Metropolitan Serving Area (MSA), and Country values.
   * - Content Dependency
     - Nodes, taxonomy terms, vocabularies, or other documents that are connected to the primary document being published to |acquia-product:ch|.
   * - |chlink|_
     - Product name for Acquia’s secure, cloud-based distribution and discovery service that enables customers to author, search, and share content throughout a complex network of websites and channels.
   * - |acquia-product:ch| service/subscription
     - Refers to a customer’s specific cloud-based content repository that aggregates and pushes content across a customer’s complex network of websites and channels. Several websites or technologies can be connected to this Hub.
   * - Decision Engine
     - Acquia-developed technology that is used to determine the correct content to display to a user, when provided with a set of rules, available content, and person profile data.
   * - Discovery Interface
     - The interface used to search/import content from |acquia-product:ch| into a subscribing website.
   * - Document
     - The 1:1 mapping in |acquia-product:ch| to a Drupal entity. Examples include nodes, taxonomy terms, vocabularies, and custom product entities.
   * - `Events </lift/profile-mgr/event/category>`__
     - Interesting behavioral activities performed by a `person <#person>`__, and related to a `touch <#touch>`__. Examples include click, add to cart, fill in form, and content view.
   * - |leblink|_
     - Product name for Acquia’s personalization tool that’s integrated with your Drupal website. This tight website integration allows you to track your visitors’ behavior and build content experiences tailored to those visitors’ interests.
   * - Keywords
     - Data collected in the user profile that provides insight into the content that a person has the most affinity towards.
   * - Person
     - A uniquely identified data type of an individual person stored in the |acquia-product:lpm|, along with a set of related attributes such as first time visitor, anonymous visitor, first seen, last seen, and any other customer-defined values (such as account status or customer type).
   * - Person (Visitor) profile
     - A collection of identifiers (including tracking identifiers, email addresses, and account ids), person, touch, event, and rankings information that comprises everything that is known about a person’s interests and behavior in |acquia-product:cha|. `Learn more </lift/profile-mgr/person/profile>`__.
   * - Persona
     - A field at both the `event <#events>`__ level and at the `person <#person>`__ level. Each piece of content can be tagged as being of interest to one or more personas, as captured in an event when a person looks at the content. The persona that is most frequently consumed is assigned at the `person <#person>`__ level. `Learn more </lift/profile-mgr/person/profile>`__.
   * - Publishing website
     - Any website (or application) that publishes content into |acquia-product:ch|. With an |acquia-product:lplp| subscription, customers have access to the API, which they can use to build connections with other technologies, either using their own resources or leveraging the expertise of Acquia’s Professional Services. A prebuilt connector is available for Drupal.
   * - |lpmlink|_
     - Product name for Acquia’s cloud-based application that allows you to search for and categorize data about each of your visitors, based on customizable criteria such as location or the content type the visitor has viewed most frequently.
   * - `Rule </lift/exp-builder/rule>`__
     - A rule defines the content to display to a given person in a given `slot <#slot>`__ for a particular `segment <#segment>`__. Because a person can belong to multiple segments at the same time, rules can be prioritized relative to each other. Types of rules include A/B/n tests and targeted content.
   * - `Segment </lift/profile-mgr/segment>`__
     - A collection of conditions that based on information that is available in the `person profile <#profile>`__ and which defines some audience of people — for example, a segment of people called *Boston visitors* that represents people on the website from Boston.
   * - Segment Criterion
     - A context, an operator, and a value that defines one of the conditions in a `segment <#segment>`__ — for example, **City** matches ``Boston``.
   * - `Slot </lift/exp-builder/slots>`__
     -  An area on a website that you configure to be able to personalize targeted content or display A/B tests.
   * - Subscribing website
     - Any website (or application) that consumes content from |acquia-product:ch|. With an |acquia-product:lplp| subscription, customers have access to the API, which they can use to build connections with other technologies, either using their own resources or leveraging the expertise of Acquia’s Professional Services. A pre-built connector is available for Drupal.
   * - Touch
     - A series of contiguous events (such as content views) with a duration between events of no more than 30 minutes are grouped together under a single touch. Similar to a visit in web analytics, a touch contains information about the referrer, visit source, device, geography, and marketing campaign. `Learn more </lift/profile-mgr/person/activity>`__.



.. |chlink| replace:: \ |acquia-product:ch|\ 
.. _chlink: /content-hub


.. |leblink| replace:: \ |acquia-product:leb|\ 
.. _leblink: /lift/exp-builder

.. |lpmlink| replace:: \ |acquia-product:lpm|\ 
.. _lpmlink: /lift/profile-mgr
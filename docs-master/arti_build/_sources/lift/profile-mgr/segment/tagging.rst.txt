.. include:: /common/global.rst

Content tagging use case examples
=================================

This documentation page provides use cases that are based on how a
fitness website could use content tagging to target content to specific
visitors to the website, and will then provide examples of how websites
from other industries may tag their content. See |mapterms|_ for full instructions for
mapping taxonomies in |acquia-product:cha|.

.. |mapterms| replace:: Mapping taxonomy terms to  \ |acquia-product:cha|\ 
.. _mapterms: /lift/omni

Field mappings
--------------

The following default field mappings are the foundation of content
tagging in |acquia-product:cha|:

-  `Persona <#persona>`__
-  `Content Section <#content-section>`__
-  `Keywords <#keywords>`__

Persona
~~~~~~~

In |acquia-product:cha|, a *persona* is a distinct audience for your
content. For example, a fitness website may have two high-level
personas, with differing motivations:

-  *Active Mom* - Motivated by messaging about nutrition and exercise
   for families and children
-  *Elite Athlete* - Motivated by content about competitions and
   research into new diet and exercise trends

For example, if a visitor to your website engages with *Elite Athlete*
content more than they engage with *Active Mom* content, the visitor
would fall into the *Elite Athlete* persona. Although visitors can only
fall into a single persona at a time, a visitor’s persona can change
over time if their content consumption habits change on your website.

Content should be tagged with a persona only if the content is
exclusively applicable to that persona. If a content item is relevant to
more than one persona, such as an *About Us* page, it should not be
tagged with a persona.


Content section
~~~~~~~~~~~~~~~

The *Content section* field enables you to tag your content by topic,
which allows |acquia-product:cha| to identify the types of content that
a visitor likes, and serve them more of their favored content. Content
should be tagged with only one or (at most) a few terms from the
vocabulary linked to the *Content section* field.

For example, a fitness website contains a Drupal taxonomy called
**Activity** that is linked to the *Content section* field in
|acquia-product:cha| and includes the following terms:

``yoga, running, strength, cycling, swimming``

A particular piece of content on that website can be tagged with any
subset of the terms for **Activity**. Single terms or multiple terms are
acceptable, such as:

-  ``strength`` AND ``cycling``
-  ``yoga`` AND ``running``
-  ``strength``

If a visitor mostly viewed content tagged ``strength``,
|acquia-product:cha| would identify that visitor's favorite Activity
content section as ``strength``.

.. note::  If all terms for a section apply to a piece of content, the content should not receive an *Activity* tag, as selecting all possible tags will not help indicate a user's activity preference.

Acquia recommends that you handle most of your tags as a **Content
section**. The first time that you set up tags in |acquia-product:cha|,
you will be asked to complete a set of field mappings. The first
**Content section** is configured in the existing **Field Mapping**
section, and you can create additional content sections as needed. See
|mapterms|_ for more detail.

Additional content sections are displayed under **User Defined Field Mappings** and **Event Mappings**, starting with **Context to map to the** ``event_udf4`` **field**.

Keywords
~~~~~~~~

*Keywords* provide you with additional flexibility with your content
tagging. Keywords are best used for terms that may change seasonally or
with trends. For example, the fitness website might use the keyword
*Zika Virus* because it is a trending news topic, but not a topic that
will always have much content. Similarly, you can use tags such *Annual
5k*, *Meditation*, and *Business Travel*.

Keywords can also be used for topics that you may want to use for a
persona or content section in the future.

Example: Fitness website taxonomy
---------------------------------

The previous example results in the following taxonomy, which maps the
Drupal entity's *Activity* vocabulary to the **Content Section** field
in |acquia-product:cha|, and maps additional taxonomies from your Drupal
entity to custom fields in |acquia-product:cha|:


.. list-table::
   :widths: 33 33 34
   :header-rows: 1 

   * - Lift client field mapping
     - Lift Profile field
     - Visitor Context
   * - Content Section: Activity
     - `Content Section </lift/omni>`__
     - Yoga, Running, Strength, Cycling, Swimming
   * - Content Section: Location
     - ``event_udf4``
     - NYC, LA, Urban, Suburban
   * - Content Section: Dietary Interests
     - ``event_udf5``
     - Juicing, Gluten Free, Vegetarian, Snacks
   * - Content Section: Beauty Interests
     - ``event_udf6``
     - Athletic wear, Street style, Natural products, DIY, Celebrity
   * - Keywords
     - 
     - Zika virus, Annual 5k, Meditation, Business Travel


Additional mapping examples
---------------------------

The following tables contain additional mapping examples from other
industries, mapping the most important vocabulary from the Drupal entity
to the **Content Section** field in |acquia-product:cha|, and mapping
additional taxonomies to custom fields in |acquia-product:cha|:

Example: Education mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 33 33 34
   :header-rows: 1 

   * - Lift client field mapping
     - Lift Profile field
     - Visitor Context
   * - Persona
     - 
     - Student, Non-Student
   * - Content Section: Status
     - `Content Section </lift/omni>`__
     - Prospective, Admitted, Current, Alumni
   * - Content Section: School Type
     - ``event_udf4``
     - Undergraduate, Graduate, Continuing
   * - Content Section: Location
     - ``event_udf5``
     - New England, USA, International
   * - Content Section: Information Type
     - ``event_udf6``
     - Academic, Admissions, Student Life, Financial
   * - Keywords
     - 
     - Start of term (add or drop classes, housing), End of term (grades, library hours), Visiting campus, Study Abroad, Transfers


Example: Software company mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 33 33 34
   :header-rows: 1 

   * - Lift client field mapping
     - Lift Profile field
     - Visitor Context
   * - Persona
     - 
     - Current customer, Prospect
   * - Content Section: Product Family
     - `Content Section </lift/omni>`__
     - Cloud Hosting, Infrastructure, Professional Services
   * - Content Section: Product Type
     - ``event_udf4``
     - Dedicated Hosting, Network, Storage, Database & Data Analytics, Productivity & Collaboration
   * - Content Section: Industry Type
     - ``event_udf5``
     - Public, Private, Hybrid
   * - Content Section: Industry
     - ``event_udf6``
     - eCommerce, Finance, Health Care
   * - Keywords
     - 
     - Federal, Annual Conference, Open Source, Customer Stories, Certification, Compliance


Example: Financial sector mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 33 33 34
   :header-rows: 1 

   * - Lift client field mapping
     - Lift Profile field
     - Visitor Context
   * - Persona
     - 
     - Customer, Prospect
   * - Content Section: Customer Type
     - `Content Section </lift/omni>`__
     - Business, Personal
   * - Content Section: Product Type
     - ``event_udf4``
     - Checking, Investing, Credit Cards, Loans, Insurance
   * - Content Section: Life Stage
     - ``event_udf5``
     - Teen, Family, Retired
   * - Content Section: Borrower Score
     - ``event_udf5``
     - Building, Average, Excellent
   * - Keywords
     - 
     - Mobile Apps, Customer Stories, Calculator, Events
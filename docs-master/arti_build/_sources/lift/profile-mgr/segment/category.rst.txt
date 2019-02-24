.. include:: /common/global.rst

Default segment criteria
========================

When evaluating the scope of the visitors that you want to connect with,
you can specify criteria to limit a segment to specific visitors. These
segment criteria are defined using *column metadata*.

Column metadata entries are used for several purposes, including:

-  Defining how fields in the core |acquia-product:cha| data model
   should be displayed in the visitor profile
-  Making content available for segmentation
-  Aggregating values in the rankings displayed in the **Insights** tab
   of a visitor's profile in |acquia-product:lpm|
-  Creating new criteria specific to your website's purpose

.. note::  For more information about creating and editing segments, including
   segment examples for ideas to help you build segments for your own use,
   see `Managing your site's segments </lift/profile-mgr/segment>`__.

The segment criteria are made up of `categories <#categories>`__ of
column metadata items, the values you want to compare against, and the
`operators <#operator-types>`__ that control that comparison.

Creating or editing column metadata items
-----------------------------------------

If you want to edit or create new column metadata items, they are
managed in the |acquia-product:lpm| interface at **Admin > Manage
configuration data > Column metadata**, and those items that have a
value of **Y** in the **Is Segmentable** column can be used when
creating segments.

Operator types
--------------

Each category item uses one or more of the following operator types when
determining whether or not the segment criteria matches a visitor:

-  **Equals** – The visitor's information for the category exactly
   matches the configured value.
-  **Contains All** – The visitor's information for the category
   contains all of the comma-delimited configured values.
-  **Contains One** – The visitor's information for the category
   contains one or more of the comma-delimited configured values.
-  **Matches All** – The visitor's information for the category exactly
   matches all of the comma-delimited configured values.
-  **Matches One** – The visitor's information for the category exactly
   matches one or more of the comma-delimited configured values.
-  **Less Than** – The visitor's information for the category is less
   than one or more of the configured values.
-  **Greater Than** – The visitor's information for the category is
   greater than than one or more of the configured values.
-  **Less Than or Equal To** – The visitor's information for the
   category is less than or equal to one or more of the configured
   values.
-  **Greater Than or Equal To** – The visitor's information for the
   category is greater than or equal to one or more of the configured
   values.

Categories
----------

The following categories and segment criteria are available by default
in |acquia-product:lpm|:

-  `Client Time <#client-time>`__
-  `Content History <#content-history>`__
-  `Current Location <#current-location>`__
-  `Current System Info <#current-system-info>`__
-  `Event <#event>`__
-  `External Campaign <#external-campaign>`__
-  `Page Content <#page-content>`__
-  `Person Properties <#person-properties>`__
-  `Person Ranking <#person-ranking>`__
-  `Server Time <#server-time>`__
-  `Touch <#touch>`__
-  `Visit Source <#visit-source>`__

Client Time
~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Segment Criteria      | Operators             | Description           |
+=======================+=======================+=======================+
| Day of Month          | Equals, Greater Than, | Day of the month (as  |
|                       | Less Than, Greater    | reported by the       |
|                       | Than or Equal To,     | visitor's browser)    |
|                       | Less Than or Equal To | when the visitor      |
|                       |                       | performed a specific  |
|                       |                       | action—from the       |
|                       |                       | following values:     |
|                       |                       | ``1`` through ``31``  |
+-----------------------+-----------------------+-----------------------+
| Day of Week           | Equals, Greater Than, | Day of the week code  |
|                       | Less Than, Greater    | (as reported by the   |
|                       | Than or Equal To,     | visitor's browser)    |
|                       | Less Than or Equal To | for when the visitor  |
|                       |                       | performed a specific  |
|                       |                       | action—from the       |
|                       |                       | following values:     |
|                       |                       | ``1`` - Monday \|     |
|                       |                       | ``2`` - Tuesday \|    |
|                       |                       | ``3`` - Wednesday \|  |
|                       |                       | ``4`` - Thursday \|   |
|                       |                       | ``5`` - Friday \|     |
|                       |                       | ``6`` - Saturday \|   |
|                       |                       | ``7`` - Sunday        |
+-----------------------+-----------------------+-----------------------+
| Hour                  | Equals, Greater Than, | Two-digit hour of the |
|                       | Less Than, Greater    | day code (as reported |
|                       | Than or Equal To,     | by the visitor's      |
|                       | Less Than or Equal To | browser) for when the |
|                       |                       | visitor performed a   |
|                       |                       | specific action—from  |
|                       |                       | the following values: |
|                       |                       | ``00`` through ``23`` |
+-----------------------+-----------------------+-----------------------+
| Month                 | Equals, Greater Than, | Two-digit month code  |
|                       | Less Than, Greater    | (as reported by the   |
|                       | Than or Equal To,     | visitor's browser)    |
|                       | Less Than or Equal To | for when the visitor  |
|                       |                       | performed a specific  |
|                       |                       | action—from the       |
|                       |                       | following values:     |
|                       |                       | ``01`` - January \|   |
|                       |                       | ``02`` - February \|  |
|                       |                       | ``03`` - March \|     |
|                       |                       | ``04`` - April \|     |
|                       |                       | ``05`` - May \|       |
|                       |                       | ``06`` - June \|      |
|                       |                       | ``07`` - July \|      |
|                       |                       | ``08`` - August \|    |
|                       |                       | ``09`` - September \| |
|                       |                       | ``10`` - October \|   |
|                       |                       | ``11`` - November \|  |
|                       |                       | ``12`` - December     |
+-----------------------+-----------------------+-----------------------+

Content History
~~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Column Metadata       | Operators             | Description           |
+=======================+=======================+=======================+
| Keyword count         | Equals, Greater Than, | The number of times a |
|                       | Less Than, Greater    | visitor encountered a |
|                       | Than or Equal To,     | specified keyword     |
|                       | Less Than or Equal To | within a selected     |
|                       |                       | duration              |
+-----------------------+-----------------------+-----------------------+
| Section Count         | Equals, Greater Than, | The number of times a |
|                       | Less Than, Greater    | visitor encountered a |
|                       | Than or Equal To,     | specified section     |
|                       | Less Than or Equal To | within a selected     |
|                       |                       | duration              |
+-----------------------+-----------------------+-----------------------+


.. |FIPS| replace:: FIPS
.. _FIPS: https://www.nist.gov/itl/itl-publications/federal-information-processing-standards-fips


.. |ISO 3166| replace:: ISO 3166
.. _ISO 3166: https://en.wikipedia.org/wiki/ISO_3166-2:US


.. |Nielsen| replace:: Nielsen Designated Market Area code
.. _Nielsen: https://developers.google.com/adwords/api/docs/appendix/geotargeting#dma

Current Location
~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 15 15 60
   :header-rows: 1 

   * - Column Metadata
     - Operators
     - Description
   * - City
     - Matches One
     - Visitor's city name (using the 
       `Latin alphabet <https://en.wikipedia.org/wiki/Latin_script>`__)—examples include: ``Boston`` | ``London``
   * - Country
     - Matches One
     - Visitor's location code. In the US and Canada, use the four letter code defined by |ISO 3166|_, for example: ``US-CA``

       Outside of the US and Canada, use the country code (defined by |FIPS|_)—such as UK
   * - DMA Code
     - Matches One
     - The visitor's |Nielsen|_, a region where the population can receive similar TV and radio offerings
   * - Region
     - Matches One
     - Visitor's location code. In the US and Canada, use the four letter code defined by |ISO 3166|_, for example: ``US-CA``
     
       Outside of the US and Canada, use the country code (defined by |FIPS|_)—such as ``UK``

.. note::  The **Country**, **Region**, and **City** column metadata items allow
   you to search for a location to add to your segment, and can
   autocomplete your search term based on the values that you enter. For
   example, entering values for both the **Country** and **Region** fields
   causes |acquia-product:lpm| to display **City** values that are both in
   the selected country and region, and are based on the letters that you
   type.

Current System Info
~~~~~~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Column Metadata       | Operators             | Description           |
+=======================+=======================+=======================+
| Browser               | Matches One           | Visitor's web         |
|                       |                       | browser—from the      |
|                       |                       | following options:    |
|                       |                       | ``Chrome`` \|         |
|                       |                       | ``Firefox`` \|        |
|                       |                       | ``Internet Explorer`` |
|                       |                       | \| ``Opera`` \|       |
|                       |                       | ``Other``             |
+-----------------------+-----------------------+-----------------------+
| Platform              | Matches One           | Visitor'              |
|                       |                       | platform—from the     |
|                       |                       | following options:    |
|                       |                       | ``Desktop`` \|        |
|                       |                       | ``Game Console`` \|   |
|                       |                       | ``Mobile`` \|         |
|                       |                       | ``Other`` \|          |
|                       |                       | ``Tablet``            |
+-----------------------+-----------------------+-----------------------+
| System                | Matches One           | Visitor's operating   |
|                       |                       | system, from the      |
|                       |                       | visitor's browser     |
|                       |                       | user agent—examples   |
|                       |                       | include:              |
|                       |                       | ``Android`` \|        |
|                       |                       | ``BSD`` \|            |
|                       |                       | ``Chrome OS`` \|      |
|                       |                       | ``Debian`` \|         |
|                       |                       | ``Fedora`` \|         |
|                       |                       | ``Firefox OS`` \|     |
|                       |                       | ``FreeBSD`` \|        |
|                       |                       | ``GoogleTV`` \|       |
|                       |                       | ``iOS`` \| ``Kindle`` |
|                       |                       | \| ``Linux`` \|       |
|                       |                       | ``Mac OS`` \|         |
|                       |                       | ``Other`` \|          |
|                       |                       | ``Red Hat`` \|        |
|                       |                       | ``SUSE`` \|           |
|                       |                       | ``Ubuntu`` \|         |
|                       |                       | ``Windows``           |
+-----------------------+-----------------------+-----------------------+

Event
~~~~~

+-----------------------+-----------------------+-----------------------+
| Column Metadata       | Operators             | Description           |
+=======================+=======================+=======================+
| Event Count           | Equals, Greater Than, | The number of times a |
|                       | Less Than, Greater    | specific event        |
|                       | Than or Equal To,     | occurred during a     |
|                       | Less Than or Equal To | time period           |
+-----------------------+-----------------------+-----------------------+
| Customer Site *(only  | Equals, Greater Than, | The website to which  |
| available once*       | Less Than, Greater    | this event criteria   |
| **Event Count** *is   | Than or Equal To,     | applies               |
| selected)*            | Less Than or Equal To |                       |
+-----------------------+-----------------------+-----------------------+
| Event Name *(only     | Equals                | The name of the event |
| available once*       |                       | that must occur a     |
| **Event Count** *is   |                       | certain number of     |
| selected)*            |                       | times within the      |
|                       |                       | specified time period |
+-----------------------+-----------------------+-----------------------+

External Campaign
~~~~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Column Metadata       | Operators             | Description           |
+=======================+=======================+=======================+
| utm_source            | Contains All,         | Google Analytics      |
|                       | Contains One, Matches | parameter indicating  |
|                       | All, Matches One      | the source of website |
|                       |                       | traffic—examples      |
|                       |                       | include:              |
|                       |                       | ``newsletter`` \|     |
|                       |                       | ``google``            |
+-----------------------+-----------------------+-----------------------+
| utm_medium            | Contains All,         | Google Analytics      |
|                       | Contains One, Matches | parameter indicating  |
|                       | All, Matches One      | the medium the link   |
|                       |                       | was used on—examples  |
|                       |                       | include:              |
|                       |                       | ``banner`` \|         |
|                       |                       | ``email``             |
+-----------------------+-----------------------+-----------------------+
| utm_term              | Contains All,         | Google Analytics      |
|                       | Contains One, Matches | parameter identifying |
|                       | All, Matches One      | paid keywords used    |
+-----------------------+-----------------------+-----------------------+
| utm_content           | Contains All,         | Google Analytics      |
|                       | Contains One, Matches | parameter for A/B     |
|                       | All, Matches One      | testing and           |
|                       |                       | content-targeted ads  |
+-----------------------+-----------------------+-----------------------+
| utm_campaign          | Contains All,         | Google Analytics      |
|                       | Contains One, Matches | parameter identifying |
|                       | All, Matches One      | a specific campaign   |
+-----------------------+-----------------------+-----------------------+

Page Content
~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Column Metadata       | Operators             | Description           |
+=======================+=======================+=======================+
| Article Keywords      | Matches One, Matches  | Keywords associated   |
|                       | All                   | with the content on   |
|                       |                       | the webpage the       |
|                       |                       | visitor is currently  |
|                       |                       | viewing               |
+-----------------------+-----------------------+-----------------------+
| Content Section       | Matches One           | Section name of the   |
|                       |                       | content on the        |
|                       |                       | webpage the visitor   |
|                       |                       | is currently          |
|                       |                       | viewing—examples      |
|                       |                       | include:              |
|                       |                       | ``restaurants`` \|    |
|                       |                       | ``bars`` \|           |
|                       |                       | ``coffee shops``      |
+-----------------------+-----------------------+-----------------------+
| Content Title         | Contains One, Matches | Title of the content  |
|                       | One                   | on the webpage that   |
|                       |                       | the visitor is        |
|                       |                       | currently viewing     |
+-----------------------+-----------------------+-----------------------+
| Content Type          | Matches One           | The way in which a    |
|                       |                       | particular kind of    |
|                       |                       | content is collected  |
|                       |                       | and displayed to      |
|                       |                       | visitors—examples     |
|                       |                       | include:              |
|                       |                       | ``article`` \|        |
|                       |                       | ``blog post`` \|      |
|                       |                       | ``poll``              |
+-----------------------+-----------------------+-----------------------+
| Page Type             | Matches One           | The way in which a    |
|                       |                       | particular kind of    |
|                       |                       | static content is     |
|                       |                       | collected and         |
|                       |                       | displayed to          |
|                       |                       | visitors—examples     |
|                       |                       | include:              |
|                       |                       | ``article page`` \|   |
|                       |                       | ``tag page`` \|       |
|                       |                       | ``home page``         |
+-----------------------+-----------------------+-----------------------+
| Page Url              | Contains One, Matches | The address of the    |
|                       | One                   | webpage containing    |
|                       |                       | the content that the  |
|                       |                       | visitor is currently  |
|                       |                       | viewing               |
+-----------------------+-----------------------+-----------------------+
| Persona               | Matches One           | The content tagged    |
|                       |                       | with the ``persona``  |
|                       |                       | taxonomy that is      |
|                       |                       | passed in the event   |
+-----------------------+-----------------------+-----------------------+

Person Properties
~~~~~~~~~~~~~~~~~


.. |notrack| replace:: ``do not track`` settings
.. _notrack: /lift/offers/admin/donottrack

+-----------------------+-----------------------+-----------------------+
| Column Metadata       | Operators             | Description           |
+=======================+=======================+=======================+
| Anonymous Visitor     | Equals                | Visitors without any  |
|                       |                       | `identity             |
|                       |                       | information </lift/ja |
|                       |                       | vascript/identity>`__ |
|                       |                       | (``Yes`` or ``No``)   |
+-----------------------+-----------------------+-----------------------+
| Days Remaining in     | Equals, Greater Than, | The number of days    |
| Subscription          | Less Than, Greater    | before a visitor's    |
|                       | Than or Equal To,     | subscription ends     |
|                       | Less Than or Equal To |                       |
+-----------------------+-----------------------+-----------------------+
| Days Since Last Visit | Equals, Greater Than, | The number of days    |
|                       | Less Than, Greater    | since a visitor last  |
|                       | Than or Equal To,     | accessed the website  |
|                       | Less Than or Equal To |                       |
+-----------------------+-----------------------+-----------------------+
| Do Not Track          | Equals                | Visitors who have     |
|                       |                       | enabled their         |
|                       |                       | |notrack|_            |
|                       |                       | (``Yes`` or ``No``)   |
+-----------------------+-----------------------+-----------------------+
| Engagement Score      | Equals, Greater Than, | The sum of all        |
|                       | Less Than, Greater    | engagement scores for |
|                       | Than or Equal To,     | all events associated |
|                       | Less Than or Equal To | with a visitor within |
|                       |                       | a 90-day period       |
+-----------------------+-----------------------+-----------------------+
| Favorite Content      | Matches One           | User-defined field:   |
| Section               |                       | the content section   |
|                       |                       | in which the visitor  |
|                       |                       | most viewed articles  |
+-----------------------+-----------------------+-----------------------+
| Favorite Content Type | Matches One           | User-defined field:   |
|                       |                       | the content type in   |
|                       |                       | which the visitor     |
|                       |                       | viewed the most       |
|                       |                       | content               |
+-----------------------+-----------------------+-----------------------+
| Favorite Keyword      | Matches One           | User-defined field:   |
|                       |                       | the most common       |
|                       |                       | keyword across all    |
|                       |                       | the content the       |
|                       |                       | visitor viewed        |
+-----------------------+-----------------------+-----------------------+
| First Time Visitor    | Equals                | Denotes whether this  |
|                       |                       | is a first-time       |
|                       |                       | visitor (``Yes`` or   |
|                       |                       | ``No``)               |
+-----------------------+-----------------------+-----------------------+
| Person Identifier     | Equals                | Person's identifier   |
| Type                  |                       | type—from the         |
|                       |                       | following values:     |
|                       |                       | ``Account ID`` \|     |
|                       |                       | ``Email Address`` \|  |
|                       |                       | ``Facebook ID`` \|    |
|                       |                       | ``Name`` \|           |
|                       |                       | ``Purged`` \|         |
|                       |                       | ``Tracking ID`` \|    |
|                       |                       | ``Twitter ID``        |
+-----------------------+-----------------------+-----------------------+
| Persona               | Matches One           | The content tagged    |
|                       |                       | with the ``persona``  |
|                       |                       | taxonomy that the     |
|                       |                       | visitor viewed the    |
|                       |                       | most                  |
+-----------------------+-----------------------+-----------------------+
| Subscriber Status     | Matches One           | The visitor's         |
|                       |                       | subscription          |
|                       |                       | status—examples       |
|                       |                       | include:              |
|                       |                       | ``Unknown`` \|        |
|                       |                       | ``Registered`` \|     |
|                       |                       | ``Subscribed`` \|     |
|                       |                       | ``Lapsed``            |
+-----------------------+-----------------------+-----------------------+

Person Ranking
~~~~~~~~~~~~~~

.. important::  All of the items in the following table are ranked from most to least
   frequent. For example, if the article keyword ``chicken sandwich`` is
   used frequently, it will be ranked highly in a visitor’s top keywords on
   the `Insights tab </lift/profile-mgr/person>`__ in the
   |acquia-product:lpm| interface.


.. |scroll| replace:: ``scroll to bottom of page`` 

+-----------------------+-----------------------+-----------------------+
| Column Metadata       | Operators             | Description           |
+=======================+=======================+=======================+
| Article Keywords      | Matches One           | Search terms from the |
|                       |                       | metadata in the       |
|                       |                       | webpages the visitor  |
|                       |                       | views                 |
+-----------------------+-----------------------+-----------------------+
| Content Section       | Matches One           | The section to which  |
|                       |                       | a piece of            |
|                       |                       | visitor-viewed        |
|                       |                       | content               |
|                       |                       | belongs—examples      |
|                       |                       | include:              |
|                       |                       | ``technology`` \|     |
|                       |                       | ``news`` \|           |
|                       |                       | ``business``          |
+-----------------------+-----------------------+-----------------------+
| Content Type          | Matches One           | The content-type to   |
|                       |                       | which a piece of      |
|                       |                       | visitor-viewed        |
|                       |                       | content belongs       |
+-----------------------+-----------------------+-----------------------+
| Engagement Score      | Equals, Greater Than, | The number chosen by  |
|                       | Less Than, Greater    | the customer to       |
|                       | Than or Equal To,     | signify the           |
|                       | Less Than or Equal To | importance of a       |
|                       |                       | visitor's interest in |
|                       |                       | this event            |
+-----------------------+-----------------------+-----------------------+
| Events                | Matches One           | Visitor's interaction |
|                       |                       | with content, ranked  |
|                       |                       | by frequency in the   |
|                       |                       | **Visitor Insights**  |
|                       |                       | tab—examples include: |
|                       |                       | ``click link`` \|     |
|                       |                       | |scroll|              |
|                       |                       | \|                    |
|                       |                       | ``hover over link``   |
+-----------------------+-----------------------+-----------------------+
| Persona               | Matches One           | The ``persona`` tags  |
|                       |                       | that appear in events |
+-----------------------+-----------------------+-----------------------+
| Platform              | Matches One           | The type of device    |
|                       |                       | the visitor used to   |
|                       |                       | access the            |
|                       |                       | website—examples      |
|                       |                       | include:              |
|                       |                       | ``Desktop`` \|        |
|                       |                       | ``Game console`` \|   |
|                       |                       | ``Tablet`` \|         |
|                       |                       | ``Mobile``            |
+-----------------------+-----------------------+-----------------------+

Server Time
~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Column Metadata       | Operators             | Description           |
+=======================+=======================+=======================+
| Day of Month          | Equals, Greater Than, | Day of the month (as  |
|                       | Less Than, Greater    | reported by the       |
|                       | Than or Equal To,     | |acquia-product:cha|  |
|                       | Less Than or Equal To | service) when the     |
|                       |                       | visitor performed a   |
|                       |                       | specific action—from  |
|                       |                       | the following values: |
|                       |                       | ``1`` through ``31``  |
+-----------------------+-----------------------+-----------------------+
| Day of Week           | Equals, Greater Than, | Day of the week code  |
|                       | Less Than, Greater    | (as reported by the   |
|                       | Than or Equal To,     | |acquia-product:cha|  |
|                       | Less Than or Equal To | service) for when the |
|                       |                       | visitor performed a   |
|                       |                       | specific action—from  |
|                       |                       | the following values: |
|                       |                       | ``1`` - Monday \|     |
|                       |                       | ``2`` - Tuesday \|    |
|                       |                       | ``3`` - Wednesday \|  |
|                       |                       | ``4`` - Thursday \|   |
|                       |                       | ``5`` - Friday \|     |
|                       |                       | ``6`` - Saturday \|   |
|                       |                       | ``7`` - Sunday        |
+-----------------------+-----------------------+-----------------------+
| Hour                  | Equals, Greater Than, | Two-digit hour of the |
|                       | Less Than, Greater    | day code (as reported |
|                       | Than or Equal To,     | by the                |
|                       | Less Than or Equal To | |acquia-product:cha|  |
|                       |                       | service) for when the |
|                       |                       | visitor performed a   |
|                       |                       | specific action—from  |
|                       |                       | the following values: |
|                       |                       | ``00`` through ``23`` |
+-----------------------+-----------------------+-----------------------+
| Month                 | Equals, Greater Than, | Two-digit month code  |
|                       | Less Than, Greater    | (as reported by the   |
|                       | Than or Equal To,     | |acquia-product:cha|  |
|                       | Less Than or Equal To | service) for when the |
|                       |                       | visitor performed a   |
|                       |                       | specific action—from  |
|                       |                       | the following values: |
|                       |                       | ``01`` - January \|   |
|                       |                       | ``02`` - February \|  |
|                       |                       | ``03`` - March \|     |
|                       |                       | ``04`` - April \|     |
|                       |                       | ``05`` - May \|       |
|                       |                       | ``06`` - June \|      |
|                       |                       | ``07`` - July \|      |
|                       |                       | ``08`` - August \|    |
|                       |                       | ``09`` - September \| |
|                       |                       | ``10`` - October \|   |
|                       |                       | ``11`` - November \|  |
|                       |                       | ``12`` - December     |
+-----------------------+-----------------------+-----------------------+

Touch
~~~~~

+-----------------------+-----------------------+-----------------------+
| Column Metadata       | Operators             | Description           |
+=======================+=======================+=======================+
| Engagement Score      | Equals, Greater Than, | Total engagement      |
|                       | Less Than, Greater    | score for the current |
|                       | Than or Equal To,     | touch                 |
|                       | Less Than or Equal To |                       |
+-----------------------+-----------------------+-----------------------+
| Number of Page Views  | Equals, Greater Than, | Number of content     |
|                       | Less Than, Greater    | views in the current  |
|                       | Than or Equal To,     | touch                 |
|                       | Less Than or Equal To |                       |
+-----------------------+-----------------------+-----------------------+
| Touch Duration        | Equals, Greater Than, | Measured as the       |
|                       | Less Than, Greater    | difference between    |
|                       | Than or Equal To,     | the first event and   |
|                       | Less Than or Equal To | the last event in the |
|                       |                       | touch                 |
+-----------------------+-----------------------+-----------------------+
| Touch Duration in     | Equals, Greater Than, | The difference in     |
| Seconds               | Less Than, Greater    | seconds between the   |
|                       | Than or Equal To,     | first event and the   |
|                       | Less Than or Equal To | last event in the     |
|                       |                       | touch                 |
+-----------------------+-----------------------+-----------------------+

Visit Source
~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Column Metadata       | Operators             | Description           |
+=======================+=======================+=======================+
| Domain                | Contains One, Matches | The domain of the     |
|                       | One                   | webpage through which |
|                       |                       | the visitor enters    |
|                       |                       | your website for the  |
|                       |                       | first time            |
+-----------------------+-----------------------+-----------------------+
| Referrer Domain       | Contains One, Matches | The host name of the  |
|                       | One                   | URL that referred the |
|                       |                       | visitor to the first  |
|                       |                       | webpage visited on    |
|                       |                       | the website           |
+-----------------------+-----------------------+-----------------------+
| Search Engine         | Matches One           | Search engine used to |
|                       |                       | find the webpage,     |
|                       |                       | from the visitor's    |
|                       |                       | referrer URL—examples |
|                       |                       | include:              |
|                       |                       | ``About`` \| ``AOL``  |
|                       |                       | \| ``Ask`` \|         |
|                       |                       | ``Baidu`` \| ``Bing`` |
|                       |                       | \| ``CNN`` \|         |
|                       |                       | ``Daum`` \| ``Eniru`` |
|                       |                       | \| ``Lycos`` \|       |
|                       |                       | ``Google`` \|         |
|                       |                       | ``Mamma`` \|          |
|                       |                       | ``Naver`` \|          |
|                       |                       | ``Search`` \|         |
|                       |                       | ``Yahoo`` \|          |
|                       |                       | ``Yandex``            |
+-----------------------+-----------------------+-----------------------+
| Search Terms          | Contains All,         | Organic search terms  |
|                       | Contains One, Matches | used by a visitor to  |
|                       | All, Matches One      | reach this page, when |
|                       |                       | provided in the       |
|                       |                       | referrer URL by the   |
|                       |                       | search engine,        |
|                       |                       | usually passed as the |
|                       |                       | 'q' parameter. Google |
|                       |                       | typically no longer   |
|                       |                       | provides              |
|                       |                       | these—examples        |
|                       |                       | include:              |
|                       |                       | ``rent pig roaster``  |
+-----------------------+-----------------------+-----------------------+
| Url                   | Contains One, Matches | The first webpage     |
|                       | One                   | that the visitor      |
|                       |                       | accessed on the       |
|                       |                       | website               |
+-----------------------+-----------------------+-----------------------+

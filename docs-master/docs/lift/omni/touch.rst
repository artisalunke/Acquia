.. include:: /common/global.rst

|acquia-product:cdw| Touch field types
======================================

.. container:: internal-navigation

   **Acquia Lift data warehouse**

   * :doc:`Intro </lift/omni>`
   * :doc:`Person </lift/omni/person>`
   * :doc:`Person </lift/omni/person>`
   * Touch
   * :doc:`Event </lift/omni/event>`
   * :doc:`Segments </lift/omni/segments>`


The |acquia-product:ldw| uses the *Touch* field layout to describe a
series of contiguous events (such as content views) with a duration
between events of no more than 30 minutes. Each touch has a
`Person </lift/omni/person>`__ record as its parent.


.. list-table::
   :widths: 25 20 10 45
   :header-rows: 1 

   * - Field name
     - `Data type <https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html>`__
     - Sortable
     - Description
   * - browser
     - VARCHAR (50)
     - |no|
     - Browser used for this touch
   * - channel_type
     - VARCHAR (100)
     - |no|
     - Source for this touch (for example, ``Web`` or ``Call Center``)
   * - city
     - VARCHAR (50)
     - |no|
     - City for this touch, based on IP-to-location lookup
   * - country
     - VARCHAR (50)
     - |no|
     - Country for this touch, based on IP-to-location lookup
       
       (`list of country codes <https://en.wikipedia.org/wiki/List_of_FIPS_country_codes>`__)
   * - customer_site_id
     - INT (4 bytes)
     - |yes|
     - Customer site row reference, indicating which website sent the capture
   * - db_last_modified_date
     - TIMESTAMP
     - |no|
     - The UTC time and date when the row was last modified in the database
   * - dma_code
     - INT (4 bytes)
     - |no|
     - `Designated market area code <https://en.wikipedia.org/wiki/Media_market>`__ for this touch (also known as a metro code)
       
       (`searchable list of DMA codes <https://developers.google.com/adwords/api/docs/appendix/geotargeting#dma>`__)

   * - engagement_score
     - INT (4 bytes)
     - |no|
     - Numeric representation (calculated by customer-specific rules) of how this touch describes a person's engagement with the brand
   * - id
     - INT (4 bytes)
     - |yes|
     - Unique touch ID — Profile Manager internal value
   * - identifier
     - VARCHAR (22)
     - |yes|
     - Touch session identifier
   * - java_enabled
     - BOOLEAN
     - |no|
     - Indicates whether the browser has Java enabled or not
   * - last_modified_date
     - TIMESTAMP
     - |no|
     - Time and date that the row was last modified
   * - latitude
     - VARCHAR (50)
     - |no|
     - Latitude for this touch, based on IP-to-location lookup
   * - longitude
     - VARCHAR (50)
     - |no|
     - Latitude for this touch, based on IP-to-location lookup
   * - number_of_page_views
     - INT (4 bytes)
     - |no|
     - Number of page views
   * - operating_system
     - VARCHAR (50)
     - |no|
     - Operating system (OS) used for this touch
   * - person_id
     - INT (4 bytes)
     - |yes|
     - Points to the associated `person's </lift/omni/person>`__ ``person_id`` for this touch
   * - person_identifier_id
     - INT (8 bytes)
     - |no|
     - Internal Profile Manager ID for the ``person_identifier`` that was triggered by this touch
   * - platform
     - VARCHAR (50)
     - |no|
     - Platform used for this touch
   * - postal_code
     - VARCHAR (20)
     - |no|
     - Postal code for this touch, based on IP-to-location lookup
   * - referrer
     - VARCHAR (4000)
     - |no|
     - Referrer URL
   * - referrer_domain
     - VARCHAR (200)
     - |no|
     - Referrer base domain
   * - region
     - VARCHAR (50)
     - |no|
     - State/Province for this touch, based on IP-to-location lookup 
       
       (`list of region codes <https://en.wikipedia.org/wiki/List_of_FIPS_region_codes>`__)

   * - search_engine
     - VARCHAR (100)
     - |no|
     - Search engine used with this touch (for example, ``Google``)
   * - search_terms
     - VARCHAR (1000)
     - |no|
     - Search terms used with this touch (for example, ``rent pig roaster``)
   * - touch_date
     - TIMESTAMP
     - |yes|
     - Touch start-date/time
   * - touch_duration
     - INT (4 bytes)
     - |no|
     - Touch duration in minutes
   * - touch_duration_in_seconds
     - INT (4 bytes)
     - |no|
     - Touch duration in seconds
   * - url
     - VARCHAR (4000)
     - |no|
     - Landing URL
   * - url_domain
     - VARCHAR (200)
     - |no|
     - Landing base domain
   * - user_agent_string
     - VARCHAR (2000)
     - |no|
     - Browser's agent string for this touch
   * - utm_content
     - VARCHAR (2000)
     - |no|
     - Campaign content for paid search, email, or other inbound marketing campaigns — associated with ``utm_content`` UTM parameter
   * - utm_medium
     - VARCHAR (2000)
     - |no|
     - Campaign medium (for example, email) — associated with ``utm_medium`` UTM parameter
   * - utm_name
     - VARCHAR (2000)
     - |no|
     - Campaign name for paid search, email, or other inbound marketing campaigns — associated with ``utm_campaign`` UTM parameter
   * - utm_referrer
     - VARCHAR (2000)
     - |no|
     - Campaign referrer (for example, Newsletters) — associated with ``utm_source`` UTM parameter
   * - utm_terms
     - VARCHAR (2000)
     - |no|
     - Campaign name for paid search, email, or other inbound marketing campaigns — associated with ``utm_term`` UTM parameter
   * - visitor_ip
     - VARCHAR (45)
     - |no|
     - IP address for this touch
   * - custom_field_1
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_2
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_3
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_4
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_5
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_6
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_7
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_8
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_9
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_10
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_11
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_12
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_13
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_14
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_15
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_16
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_17
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_18
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_19
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_20
     - VARCHAR (1000)
     - |no|
     - User-defined field
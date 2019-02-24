.. include:: /common/global.rst

|acquia-product:cdw| Person field types
=======================================

.. container:: internal-navigation

   **|acquia-product:cha| data warehouse**

   * :doc:`Intro </lift/omni>`
   * Person
   * :doc:`Person </lift/omni/person>`
   * :doc:`Touch </lift/omni/touch>`
   * :doc:`Event </lift/omni/event>`
   * :doc:`Segments </lift/omni/segments>`


The |acquia-product:ldw| uses the *Person* field layout to describe
visitors that have been uniquely identified with first-party cookies,
their email addresses, or some other identifier.

The Person field layout uses the following tables to describe your
visitors:

-  `person <#person-table>`__
-  `person_link <#person-link-table>`__
-  `person_identifier <#person-identifier-table>`__
-  `person_ranking_item <#person-ranking-item-table>`__
-  `person_ranking_summary <#person-ranking-summary-table>`__


person table
------------

.. list-table::
   :widths: 25 20 10 45
   :header-rows: 1 

   * - Field name
     - `Data type <https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html>`__
     - Sortable
     - Description
   * - active
     - BOOLEAN
     - |no|
     - The person is a unique entity; ``false`` indicates this person was merged into a|no|ther person during identity resolution (touches and events remain linked to the original person)
   * - anonymous_visitor
     - BOOLEAN
     - |no|
     - Person without any identity information, such as an email address or account ID
   * - articles_remaining
     - INT (4 bytes)
     - |no|
     - Number of articles available for person to access, usable with free previews or limited subscriptions — optional and provided externally
   * - do_not_track
     - BOOLEAN
     - |no|
     - Indicates whether or not the person has opted out of tracking and personalization
   * - engagement_score
     - INT (4 bytes)
     - |no|
     - Numeric representation of this person's engagement with the brand that is calculated by customer-specific rules (for example, a visitor with a newsletter subscription is more engaged than a periodic visitor); calculated here as the sum of all engagement scores at the event level over a 90-day period
   * - external_score
     - INT (4 bytes)
     - |no|
     - Rating value not created or defined by |acquia-product:cha|
   * - first_time_visitor
     - BOOLEAN
     - |no|
     - Indicates whether person is a first-time visitor
   * - first_touch
     - DATE
     - |yes|
     - Time and date of the person's first touch
   * - id
     - INT (4 bytes)
     - |yes|
     - Unique person ID — |acquia-product:cha| internal value; ``person_id`` fields in other tables refer to this value
   * - identifiers_json
     - VARCHAR (65535)
     - |no|
     - A JSON representation of all the identifiers associated with the person
   * - last_modified_date
     - TIMESTAMP
     - |no|
     - Time and date that the row was last modified
   * - last_subscription_plan
     - VARCHAR (50)
     - |no|
     - Immediately previous subscription plan for the person (for example, ``Unlimited``, ``Monthly``, or ``Yearly``) — optional and provided externally
   * - last_touch
     - DATE
     - |yes|
     - Time and date of the person's last touch
   * - persona
     - VARCHAR (100)
     - |no|
     - The top persona of the person, based on their consumed content
   * - primary_identifier
     - VARCHAR (200)
     - |no|
     - Tracking ID assigned to a website visitor and stored in their cookies; if there are multiple identifiers, this field reflects the first assigned identifier
   * - primary_identifier_type_id
     - INT (4 bytes)
     - |no|
     - Person's identifier type — this will always have a value of 2 to reflect the first tracking ID assigned by |acquia-product:cha|
   * - subscriber_status
     - VARCHAR (50)
     - |no|
     - The person's subscription status — optional and provided externally
   * - subscription_end_date
     - DATE
     - |no|
     - Date the person's subscription expires — optional and provided externally
   * - subscription_plan
     - VARCHAR (50)
     - |no|
     - Current person's subscription plan — optional and provided externally
   * - subscription_start_date
     - DATE
     - |no|
     - Date the person's subscription started — optional and provided externally
   * - db_last_modified_date
     - TIMESTAMP
     - |no|
     - The UTC time and date when the row was last modified in the database
   * - custom_field_1
     - VARCHAR (200)
     - |no|
     - User-defined field
     
       *Because this field is also used by Experience Builder, we recommend that you do not use this field for your custom values.*

   * - custom_field_2
     - VARCHAR (200)
     - |no|
     - User-defined field

       *Because this field is also used by Experience Builder, we recommend that you do not use this field for your custom values.*

   * - custom_field_3
     - VARCHAR (200)
     - |no|
     - User-defined field
       
       *Because this field is also used by Experience Builder, we recommend that you do not use this field for your custom values.*

   * - custom_field_4
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_5
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_6
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_7
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_8
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_9
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_10
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_11
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_12
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_13
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_14
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_15
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_16
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_17
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_18
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_19
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_20
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_21
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_22
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_23
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_24
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_25
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_26
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_27
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_28
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_29
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_30
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_31
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_32
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_33
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_34
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_35
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_36
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_37
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_38
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_39
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_40
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_41
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_42
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_43
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_44
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_45
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_46
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_47
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_48
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_49
     - VARCHAR (200)
     - |no|
     - User-defined field
   * - custom_field_50
     - VARCHAR (200)
     - |no|
     - User-defined field


person_link table
-----------------

.. list-table::
   :widths: 25 20 10 45
   :header-rows: 1 

   * - Field name
     - `Data type <https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html>`__
     - Sortable
     - Description
   * - db_last_modified_date
     - TIMESTAMP
     - |no|
     - The UTC time and date when the row was last modified in the database
   * - linked_person_id
     - INT (4 bytes)
     - |no|
     - Points to a person associated with the visitor listed in this record's ``person_id``
   * - person_id
     - INT (4 bytes)
     - |yes|
     - Points to a specific person in |acquia-product:cha| records

.. note::  

   If multiple person records have been joined together as a result of an
   identity merge, only one of the person records in this table will have
   an active flag set to ``Y``. The other linked persons will have the
   active flag set to ``N``.


person_identifier table
-----------------------

.. list-table::
   :widths: 25 20 10 45
   :header-rows: 1 

   * - Field name
     - `Data type <https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html>`__
     - Sortable
     - Description
   * - active
     - BOOLEAN
     - |no|
     - The person is a unique entity; ``False`` indicates this person was merged into another person during identity resolution (touches and events remain linked to the original person)
   * - db_last_modified_date
     - TIMESTAMP
     - |no|
     - The UTC time and date when the row was last modified in the database
   * - identifier
     - VARCHAR (200)	
     - |yes|
     - Person’s identifier information, based on the ``person_identifier_type_id``
   * - last_modified_date
     - TIMESTAMP
     - |no|
     - The timestamp of the last modification of this record
   * - person_id
     - INT (8 bytes)
     - |yes|
     - Points to a specific person in [acquia-product :cha] records
   * - person_identifier_type_id
     - INT (4 bytes)
     - |yes|
     - Person’s identifier type, from the following options:

       1 - email |br|
       2 - tracking identifier |br|
       3 - account id |br|
       4 - Facebook account |br|
       5 - Twitter account |br|
       6 - name

       .. note::  

          If you have 
          `added one or more custom identifiers </lift/profile-mgr/admin/customer>`__ 
          to your customer information, those non-standard identifiers will have values 
          greater than 6. At this time, there is no method to determine a custom 
          identifier’s descriptive name from its ``person_identifier_type_id`` value.


person_ranking_item table
-------------------------

.. list-table::
   :widths: 25 20 10 45
   :header-rows: 1 

   * - Field name
     - `Data type <https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html>`__
     - Sortable
     - Description
   * - db_last_modified_date
     - TIMESTAMP
     - |no|
     - The UTC time and date when the row was last modified in the database
   * - item_date
     - INT (4 bytes)
     - |yes|
     - Date for which the ranking item's value has been accumulated
   * - item_name
     - VARCHAR (200)
     - |yes|
     - Name of the ranking item — for example, ``DESKTOP`` for the device ranking
   * - item_value
     - INT (4 bytes)
     - |no|
     - Value assigned to the ranking item
   * - last_modified_date
     - TIMESTAMP
     - |no|
     - Time and date that the row was last modified
   * - person_id
     - INT (8 bytes)
     - |no|
     - Points to an associated ranking item
   * - person_ranking_id
     - INT (8 bytes)
     - |yes|
     - Points to an associated ranking item

person_ranking_summary table
----------------------------

.. list-table::
   :widths: 25 20 10 45
   :header-rows: 1 

   * - Field name
     - `Data type <https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html>`__
     - Sortable
     - Description
   * - db_last_modified_date
     - TIMESTAMP
     - No
     - The UTC time and date when the row was last modified in the database
   * - column_meta_data_id
     - INT (4 bytes)
     - Yes
     - Points to the column meta data associated with the ranking in |acquia-product:cha| records
   * - column_meta_data_name
     - VARCHAR (50)
     - No
     - Display name of the column meta data
   * - customer_site_id
     - INT (4 bytes)
     - Yes
     - Points to the customer's website in |acquia-product:cha| records
   * - frequency
     - INT (4 bytes)
     - No
     - Value assigned to the ranking summary (for example, the sum of the daily values for the last period)
   * - freq_rank
     - INT (4 bytes)
     - No
     - The rank, by frequency, when compared to other ranking summaries with the same ``person_id``, ``customer_site_id``, and ``column_meta_data_id``
   * - item_name
     - VARCHAR (200)
     - No
     - Name of the ranking summary — for example, ``DESKTOP`` for the device ranking
   * - last_modified_date
     - TIMESTAMP
     - No
     - Time and date that the row was last modified
   * - person_id
     - INT (4 bytes)
     - Yes
     - Points to a specific person in |acquia-product:cha| records
   * - site_external_id
     - VARCHAR (20)
     - No
     - External identifier of the customer's website
   * - site_name
     - VARCHAR (50)
     - No
     - Name of the customer's website

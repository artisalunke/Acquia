.. include:: /common/global.rst

Data warehouse Event field types
======================================

.. container:: internal-navigation

   **Acquia Lift data warehouse**

   * :doc:`Intro </lift/omni>`
   * :doc:`Person </lift/omni/person>`
   * :doc:`Person </lift/omni/person>`
   * :doc:`Touch </lift/omni/touch>`
   * Event
   * :doc:`Segments </lift/omni/segments>`

The |acquia-product:ldw| uses the *Event* field layout to describe
discrete visitor actions, such as a content view of an article or a
click-through on a subscription offer. An event has a
`Touch </lift/omni/touch>`__ record as its parent.

Events also contain information about the specific content that a
visitor is consuming.

.. list-table::
   :widths: 25 20 10 45
   :header-rows: 1 

   * - Field name
     - Data type
     - Sortable
     - Description
   * - campaign_id
     - VARCHAR (200)
     - |no|
     - Campaign ID associated with an |acquia-product:cha| personalized event action
   * - capture_identifier
     - VARCHAR (22)
     - |no|
     - Event identifier
   * - client_date
     - DATE
     - |no|
     - Timestamp as shown in the visitor's device. not translated to UTC, customer timezone, or server time
   * - client_timezone
     - VARCHAR (100)
     - |no|
     - The visitor's timezone
   * - content_id
     - VARCHAR (4000)
     - |no|
     - ID of the content on which the content view or clickthrough event occurred
   * - content_pub_date
     - DATE
     - |no|
     - Date the content was published
   * - content_section
     - VARCHAR (400)
     - |no|
     - Section name of the content (for example, ``restaurants``)
   * - content_title
     - VARCHAR (400)
     - |no|
     - Title of the content
   * - content_type
     - VARCHAR (200)
     - |no|
     - Content type (for example, ``article``)
   * - content_uuid
     - VARCHAR (1000)
     - |no|
     - Unique content ID associated with a content view and a click-through event
   * - customer_site_external_id
     - VARCHAR (20)
     - |no|
     - External identifier for customer site, indicating which website sent the capture
   * - customer_site_id
     - INT (4 bytes)
     - |yes|
     - Customer site row reference, indicating which website sent the capture
   * - db_last_modified_date
     - TIMESTAMP
     - |no|
     - The UTC time and date when the row was last modified in the database
   * - decision_slot_id
     - VARCHAR (1000)
     - |no|
     - Decision slot ID associated with a decision or a goal event
   * - decision_slot_name
     - VARCHAR (1000)
     - |no|
     - Decision slot name associated with a decision or a goal event
   * - decision_rule_id
     - VARCHAR (1000)
     - |no|
     - Decision rule ID associated with a decision or a goal event
   * - decision_rule_name
     - VARCHAR (1000)
     - |no|
     - Decision rule name associated with a decision or a goal event
   * - decision_content_id
     - VARCHAR (1000)
     - |no|
     - Decision content ID associated with a decision or a goal event
   * - decision_content_name
     - VARCHAR (1000)
     - |no|
     - Decision content name associated with a decision or a goal event
   * - decision_goal_id
     - VARCHAR (1000)
     - |no|
     - Decision goal ID associated with a decision or a goal event
   * - decision_goal_name
     - VARCHAR (1000)
     - |no|
     - Decision goal name associated with a decision or a goal event
   * - decision_goal_value
     - VARCHAR (1000)
     - |no|
     - Decision goal value associated with a decision or a goal event
   * - decision_view_mode
     - VARCHAR (1000)
     - |no|
     - Decision view mode associated with a decision or a goal event
   * - decision_policy
     - VARCHAR (1000)
     - |no|
     - Decision policy associated with a decision or a goal event
   * - decision_rule_segment_id
     - VARCHAR (1000)
     - |no|
     - Decision rule segment ID associated with a decision or a goal event
   * - decision_rule_segment_name
     - VARCHAR (1000)
     - |no|
     - Decision rule segment name associated with a decision or a goal event
   * - decision_rule_type
     - VARCHAR (1000)
     - |no|
     - Decision rule type associated with a decision or a goal event
   * - discount_code
     - VARCHAR (200)
     - |no|
     - Campaign's discount code, if applicable
   * - engagement_score
     - INT (4 bytes)
     - |no|
     - Numeric representation of how this event describes a person's engagement with the brand — can be set as explicit value using the |acquia-product:cha| APIs
   * - event_category_id
     - INT (4 bytes)
     - |no|
     - Code for the event (refer to the name field for its human-readable name) — |acquia-product:cha| internal value
   * - event_category_type
     - VARCHAR (200)
     - |no|
     - Event type (examples include ``action``, ``click``, ``conversion``, or ``other``)
   * - event_date
     - TIMESTAMP
     - |yes|
     - Event date-time
   * - id
     - INT (8 bytes)
     - |yes|
     - Unique event ID — |acquia-product:cha| internal value
   * - image_thumb_url
     - VARCHAR (4000)
     - |no|
     - Link to thumbnail image associated with article content
   * - keywords
     - VARCHAR (4000)
     - |no|
     - Keywords associated with the content
   * - last_modified_date
     - TIMESTAMP
     - |no|
     - Time and date that the row was last modified
   * - name
     - VARCHAR (200)
     - |no|
     - Name of the event (for example, ``Content View``)
   * - offer_id
     - VARCHAR (200)
     - |no|
     - Offer ID for |acquia-product:cha| personalized offer
   * - page_type
     - VARCHAR (200)
     - |no|
     - Page type (examples include ``article page``, ``tag page``, and ``home page``)
   * - page_url
     - VARCHAR (4000)
     - |no|
     - Page URL
   * - person_id
     - INT (8 bytes)
     - |yes|
     - Link to an existing ``id`` for a `person </lift/omni/person>`__ — |acquia-product:cha| internal value
   * - referrer
     - VARCHAR (4000)
     - |no|
     - Referrer URL
   * - touch_id
     - INT (8 bytes)
     - |yes|
     - Link to an existing ``id`` for a `touch </lift/omni/touch>`__ — |acquia-product:cha| internal value
   * - custom_field_1
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_2
     - VARCHAR (1000)
     - |no|
     - User-defined field
     
       *Because this field is also used by Experience Builder for personas, we recommend that you do |no|t use this field for your custom values.*

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
   * - custom_field_21
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_22
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_23
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_24
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_25
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_26
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_27
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_28
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_29
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_30
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_31
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_32
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_33
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_34
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_35
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_36
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_37
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_38
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_39
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_40
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_41
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_42
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_43
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_44
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_45
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_46
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_47
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_48
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_49
     - VARCHAR (1000)
     - |no|
     - User-defined field
   * - custom_field_50
     - VARCHAR (1000)
     - |no|
     - User-defined field
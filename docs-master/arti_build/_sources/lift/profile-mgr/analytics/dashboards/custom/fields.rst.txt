.. include:: /common/global.rst

Fields in custom reports
========================

.. container:: message-status

   This feature is available only to |acquia-product:lplpo| or
   |acquia-product:lplp| subscribers. To upgrade your |acquia-product:cha| 
   subscription to this level, contact your Account Manager.

.. container:: internal-navigation

   **Using reports dashboards in Profile Manager**

   * :doc:`Intro </lift/profile-mgr/analytics/dashboards>`
   * :doc:`Overview </lift/profile-mgr/analytics/dashboards/operational>`
   * :doc:`Details </lift/profile-mgr/analytics/dashboards/details>`
   * :doc:`Config </lift/profile-mgr/analytics/dashboards/config>`
   * :doc:`Custom </lift/profile-mgr/analytics/dashboards/custom>`
   * Fields

When building `custom reports </lift/profile-mgr/analytics/dashboards/custom>`__ in
|acquia-product:lpm|,
you can select from the following *dimensions*, or buckets of data, to
search your website's data warehouse in real time and display in your
custom report.

After familiarizing yourself with the fields available in custom
reports, you can `create and
customize </lift/profile-mgr/analytics/dashboards/custom/build>`__ your
first report.

Detailed dimension list
-----------------------

|acquia-product:lpm| groups dimensions by topic, based on the following
list:

|Dimensions grouped by topic|

-  `Content <#content>`__ – Data related to visitors' viewing of content
   on your website
-  `Content UUID <#contentuuid>`__ – UUID (Universal Unique Identifier)
   of content viewed on your website
-  `Customer Site <#customersite>`__ – Identifying information about the
   websites in your |acquia-product:cha| subscription
-  `Decision <#decision>`__ – Identifying information, content returned,
   and goals awarded from decisions
-  `Event <#event>`__ – Visitor events on your website
-  `Event Custom Fields <#eventcustom>`__ – Custom data fields for your
   website's `events </lift/profile-mgr/event/category>`__
-  `Event Date <#eventdate>`__ – Date information related to visitor
   `events </lift/profile-mgr/event/category>`__ on your website
-  `Event Engagement <#eventengagement>`__ – Engagement scores for
   `events </lift/profile-mgr/event/category>`__ on your website
-  `External Campaign <#externalcampaign>`__ – UTM campaigns
-  `Location <#location>`__ – Location lookups of the originating IP
   address
-  `Matched Segment <#matchedsegment>`__ – Data linking
   `segments </lift/profile-mgr/segment>`__ and
   `events </lift/profile-mgr/event/category>`__
-  `Person <#person>`__ – Your website's visitors, including information
   about their locations, identities, and their preferences on your
   website
-  `Person Custom Fields <#personcustom>`__ – Custom data fields for
   your website's visitors
-  `Person Date <#persondate>`__ – Data about your visitors' activities
   on your website
-  `Person Engagement <#personengagement>`__ – Data relating to
   visitors' engagement with your website
-  `Person Identifier <#personidentifier>`__ – Unique identifying
   information about your website's visitors
-  `Person link <#personlink>`__ – Data linking multiple person IDs
-  `Personalization <#personalization>`__ – Data about the
   `personalizations </lift/drupal/creating-personalizations>`__
   developed for your website
-  `Segment <#segment>`__ – Segments matched to
   `events </lift/profile-mgr/event/category>`__ on your website
-  `Source <#source>`__ – Data about the sources of
   `touches </lift/profile-mgr/person/activity>`__
-  `System Info <#systeminfo>`__ – Data about the browser and platform
   associated with `touches </lift/profile-mgr/person/activity>`__
-  `Touch <#touch>`__ – Data about
   `touches </lift/profile-mgr/person/activity>`__
-  `Touch Custom Fields <#touchcustom>`__ – Custom data about
   `touches </lift/profile-mgr/person/activity>`__
-  `Touch date <#touchdate>`__ – Date information for
   `touches </lift/profile-mgr/person/activity>`__
-  `Touch Engagement <#touchengagement>`__ – `Engagement
   scores </lift/profile-mgr/person/activity#activity>`__ associated
   with `touches </lift/profile-mgr/person/activity>`__

Content
~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Content ID**                    | The local Drupal content ID of    |
|                                   | the content displayed, or         |
|                                   | optionally another content ID if  |
|                                   | the content source is non-Drupal  |
+-----------------------------------+-----------------------------------+
| **Content Section**               | The visitor context mapping       |
|                                   | configured in Drupal, typically   |
|                                   | mapped to the category or topic   |
|                                   | that the content relates to, such |
|                                   | as *telecommunications*           |
+-----------------------------------+-----------------------------------+
| **Content Title**                 | The title of the page in a        |
|                                   | content view                      |
+-----------------------------------+-----------------------------------+
| **Content Type**                  | The visitor context mapping       |
|                                   | configured in Drupal, typically   |
|                                   | mapped to the type of content,    |
|                                   | such as *article*                 |
+-----------------------------------+-----------------------------------+
| **Keywords**                      | The visitor context mapping       |
|                                   | configured in Drupal, typically   |
|                                   | mapped to tags associated with    |
|                                   | the content, such as *VendorA,    |
|                                   | VendorB*                          |
+-----------------------------------+-----------------------------------+

.. _contentuuid:

Content UUID
~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Content UUID**                  | The |acquia-product:ch| UUID of   |
|                                   | the content displayed within the  |
|                                   | content view event                |
+-----------------------------------+-----------------------------------+

.. _customersite:

Customer Site
~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Customer ID**                   | A unique integer assigned by      |
|                                   | |acquia-product:cha| representing |
|                                   | the customer website              |
+-----------------------------------+-----------------------------------+
| **Customer Site**                 | The external ID of the customer   |
|                                   | website                           |
+-----------------------------------+-----------------------------------+
| **Customer Site ID**              | A unique integer assigned by      |
|                                   | |acquia-product:cha| representing |
|                                   | the customer website              |
+-----------------------------------+-----------------------------------+
| **Distinct Customer ID**          | A unique integer assigned by      |
|                                   | |acquia-product:cha| representing |
|                                   | the customer website              |
+-----------------------------------+-----------------------------------+

Decision
~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Decision Content Identifier**   | The UUID of the content that was  |
|                                   | displayed in the decision         |
+-----------------------------------+-----------------------------------+
| **Decision Content Name**         | The title of the content that was |
|                                   | displayed                         |
+-----------------------------------+-----------------------------------+
| **Decision Goal Identifier**      | The ID of an awarded goal         |
+-----------------------------------+-----------------------------------+
| **Decision Goal Name**            | The name of an awarded goal       |
+-----------------------------------+-----------------------------------+
| **Decision Goal Value**           | Decision Goal Value               |
+-----------------------------------+-----------------------------------+
| **Decision Policy**               | The decision policy used to make  |
|                                   | the decision, such as *explore*   |
|                                   | and *repeat*                      |
+-----------------------------------+-----------------------------------+
| **Decision Rule Identifier**      | The ID of the rule that was used  |
|                                   | to replace content                |
+-----------------------------------+-----------------------------------+
| **Decision Rule Name**            | The name of the rule that was     |
|                                   | used to replace content           |
+-----------------------------------+-----------------------------------+
| **Decision Rule Type**            | The type of rule that was used,   |
|                                   | such as *ab* for A/B testing and  |
|                                   | *target* for targeting            |
+-----------------------------------+-----------------------------------+
| **Decision Segment Identifier**   | The ID of the segment on which    |
|                                   | the rule triggers                 |
+-----------------------------------+-----------------------------------+
| **Decision Segment Name**         | The name of the segment on which  |
|                                   | the rule triggers                 |
+-----------------------------------+-----------------------------------+
| **Decision Slot Identifier**      | The ID for the slot where content |
|                                   | was replaced                      |
+-----------------------------------+-----------------------------------+
| **Decision Slot Name**            | The name of the slot where        |
|                                   | content was replaced              |
+-----------------------------------+-----------------------------------+
| **Decision View Mode**            | The ID of the layout of the       |
|                                   | content that was displayed        |
+-----------------------------------+-----------------------------------+

Event
~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Event Category Type**           | A value based on the Event Type   |
|                                   | for the event in the event        |
|                                   | configuration page                |
+-----------------------------------+-----------------------------------+
| **Event ID**                      | A unique integer assigned by      |
|                                   | |acquia-product:cha| representing |
|                                   | the event                         |
+-----------------------------------+-----------------------------------+
| **Event Name**                    | The name of the event, such as    |
|                                   | *Content View*                    |
+-----------------------------------+-----------------------------------+
| **Page Type**                     | The visitor context mapping       |
|                                   | configured in Drupal, typically   |
|                                   | mapped to the type of page, such  |
|                                   | as *content page*                 |
+-----------------------------------+-----------------------------------+
| **Page URL**                      | The URL of the page the visitor   |
|                                   | is on, including parameters       |
+-----------------------------------+-----------------------------------+
| **Person ID**                     | The unique ID of the person       |
|                                   | connected to the event            |
+-----------------------------------+-----------------------------------+
| **Referrer**                      | The referring URL to the page the |
|                                   | visitor is on                     |
+-----------------------------------+-----------------------------------+

.. _eventcustom:

Event Custom Fields
~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Custom Field 1**                | Available for customer use        |
+-----------------------------------+-----------------------------------+
| **Custom Field 2**                | Contains the *Persona* visitor    |
|                                   | mapping context configured in     |
|                                   | Drupal                            |
+-----------------------------------+-----------------------------------+
| **Custom Field 3 – 50**           | Available for customer use        |
+-----------------------------------+-----------------------------------+

.. _eventdate:

Event Date
~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Event Date**                    | Date-time the event occured       |
+-----------------------------------+-----------------------------------+
| **Modified Date**                 | Time and date that the row was    |
|                                   | last modified in the data         |
|                                   | warehouse                         |
+-----------------------------------+-----------------------------------+

.. _eventengagement:

Event Engagement
~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Engagement Score**              | The engagement score assigned to  |
|                                   | the event; can be set to other    |
|                                   | desired value via APIs            |
|                                   | *Default value:* ``1``            |
+-----------------------------------+-----------------------------------+

.. _externalcampaign:

External Campaign
~~~~~~~~~~~~~~~~~

+------------------+------------------------------------------------------+
| Name             | Description                                          |
+==================+======================================================+
| **Utm Content**  | The ``utm_content`` parameter assigned to the touch  |
+------------------+------------------------------------------------------+
| **Utm Medium**   | The ``utm_medium`` parameter assigned to the touch   |
+------------------+------------------------------------------------------+
| **Utm Name**     | The ``utm_name`` parameter assigned to the touch     |
+------------------+------------------------------------------------------+
| **Utm Referrer** | The ``utm_referrer`` parameter assigned to the touch |
+------------------+------------------------------------------------------+
| **Utm Terms**    | The ``utm_term`` parameter assigned to the touch     |
+------------------+------------------------------------------------------+

Location
~~~~~~~~

+------------------+----------------------------------------+
| Name             | Description                            |
+==================+========================================+
| **City**         | The city assigned to the touch         |
+------------------+----------------------------------------+
| **Country**      | The country assigned to the touch      |
+------------------+----------------------------------------+
| **Country Code** | The country code assigned to the touch |
+------------------+----------------------------------------+
| **DMA Code**     | The DMA code assigned to the touch     |
+------------------+----------------------------------------+
| **Latitude**     | The latitude assigned to the touch     |
+------------------+----------------------------------------+
| **Longitude**    | The longitude assigned to the touch    |
+------------------+----------------------------------------+
| **Postal Code**  | The postal code assigned to the touch  |
+------------------+----------------------------------------+
| **Region**       | The region assigned to the touch       |
+------------------+----------------------------------------+

.. _matchedsegment:

Matched Segment
~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Segment ID**                    | The |acquia-product:cha|-assigned |
|                                   | integer segment ID(s) that were   |
|                                   | matched to one or more events     |
+-----------------------------------+-----------------------------------+

Person
~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Active (Yes / No)**             | Indicates an active profile       |
|                                   | versus an inactive profile due to |
|                                   | an identity merge                 |
|                                   | *Available values:* ``Yes``,      |
|                                   | ``No``                            |
+-----------------------------------+-----------------------------------+
| **Anonymous Visitor (Yes / No)**  | Anonymous visitor flag            |
|                                   | *Available values:* ``Yes``,      |
|                                   | ``No``                            |
+-----------------------------------+-----------------------------------+
| **Do Not Track (Yes / No)**       | Visitor that has opted out of     |
|                                   | tracking                          |
|                                   | *Available values:* ``Yes``,      |
|                                   | ``No``                            |
+-----------------------------------+-----------------------------------+
| **External Score**                | External Score                    |
+-----------------------------------+-----------------------------------+
| **Favorite Content Section**      | Content Section viewed the most   |
|                                   | in the past 90 days               |
+-----------------------------------+-----------------------------------+
| **Favorite Content Type**         | Content Type viewed the most in   |
|                                   | the past 90 days                  |
+-----------------------------------+-----------------------------------+
| **Favorite Keyword**              | Keyword viewed the most in the    |
|                                   | past 90 days                      |
+-----------------------------------+-----------------------------------+
| **First Time Visitor (Yes / No)** | First time visitor flag           |
|                                   | *Available values:* ``Yes``,      |
|                                   | ``No``                            |
+-----------------------------------+-----------------------------------+
| **Person ID**                     | A unique integer assigned by      |
|                                   | |acquia-product:cha| representing |
|                                   | the person                        |
+-----------------------------------+-----------------------------------+
| **Persona**                       | Persona viewed the most in a      |
|                                   | rolling 90 day window             |
+-----------------------------------+-----------------------------------+

.. _personcustom:

Person Custom Fields
~~~~~~~~~~~~~~~~~~~~

+--------------------------+----------------------------+
| Name                     | Description                |
+==========================+============================+
| **Custom Field 04 - 50** | Available for customer use |
+--------------------------+----------------------------+

.. _persondate:

Person Date
~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **First Touch Date**              | The date-time of the earliest     |
|                                   | touch for the person              |
+-----------------------------------+-----------------------------------+
| **Last Touch Date**               | The date-time of the latest touch |
|                                   | for the person                    |
+-----------------------------------+-----------------------------------+
| **Modified Date**                 | Time and date that the row was    |
|                                   | last modified in the data         |
|                                   | warehouse                         |
+-----------------------------------+-----------------------------------+

.. _personengagement:

Person Engagement
~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Engagement Score**              | The sum of the touch engagement   |
|                                   | scores in the past 90 days        |
+-----------------------------------+-----------------------------------+

.. _personidentifier:

Person Identifier
~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Identifier**                    | The identifier, such as an email  |
|                                   | address                           |
+-----------------------------------+-----------------------------------+
| **Identifier Type**               | The identifier type, such as      |
|                                   | *email*                           |
+-----------------------------------+-----------------------------------+
| **Identifier Type ID**            | The integer ID assigned by        |
|                                   | |acquia-product:cha| representing |
|                                   | the identifier type               |
+-----------------------------------+-----------------------------------+
| **Person ID**                     | The ID of the person              |
+-----------------------------------+-----------------------------------+

.. _personlink:

Person link
~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Linked Person ID**              | For merged records, the linkages  |
|                                   | between profiles, represented by  |
|                                   | a person ID and a second person   |
|                                   | ID                                |
+-----------------------------------+-----------------------------------+
| **Person ID**                     | See **Linked Person ID**          |
+-----------------------------------+-----------------------------------+

Segment
~~~~~~~

+------------------+---------------------------------------------------------+
| Name             | Description                                             |
+==================+=========================================================+
| **Segment Name** | The name of one or more segments that matched to events |
+------------------+---------------------------------------------------------+

Source
~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Channel Type**                  | The channel type associated with  |
|                                   | the touch, such as *Web*          |
+-----------------------------------+-----------------------------------+
| **Referrer**                      | The referring URL associated with |
|                                   | the touch                         |
+-----------------------------------+-----------------------------------+
| **Referrer Domain**               | The referring domain associated   |
|                                   | with the touch                    |
+-----------------------------------+-----------------------------------+
| **Search Engine**                 | The search engine associated with |
|                                   | the touch, if provided            |
+-----------------------------------+-----------------------------------+
| **Search Terms**                  | The search terms associated with  |
|                                   | the touch, if provided            |
+-----------------------------------+-----------------------------------+
| **URL**                           | The landing URL associated with   |
|                                   | the touch                         |
+-----------------------------------+-----------------------------------+
| **URL Domain**                    | The landing URL domain associated |
|                                   | with the touch                    |
+-----------------------------------+-----------------------------------+

.. _systeminfo:

System Info
~~~~~~~~~~~

+---------------------+--------------------------------------------+
| Name                | Description                                |
+=====================+============================================+
| **Browser**         | Browser associated with the touch          |
+---------------------+--------------------------------------------+
| **Operator System** | Operating system associated with the touch |
+---------------------+--------------------------------------------+
| **Platform**        | Platform                                   |
+---------------------+--------------------------------------------+

Touch
~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Number of Page Views**          | Number of *Content Views*         |
|                                   | associated with the touch         |
+-----------------------------------+-----------------------------------+
| **Person ID**                     | The person ID associated with the |
|                                   | touch                             |
+-----------------------------------+-----------------------------------+
| **Touch Duration**                | The duration of the touch in      |
|                                   | minutes                           |
+-----------------------------------+-----------------------------------+
| **The duration of the touch in    | The duration of the touch in      |
| minutes**                         | minutes                           |
+-----------------------------------+-----------------------------------+

.. _touchcustom:

Touch Custom Fields
~~~~~~~~~~~~~~~~~~~

+--------------------------+----------------------------+
| Name                     | Description                |
+==========================+============================+
| **Custom Field 01 – 50** | Available for customer use |
+--------------------------+----------------------------+

.. _touchdate:

Touch date
~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Modified Date**                 | The date-time of the touch        |
+-----------------------------------+-----------------------------------+
| **Touch Date**                    | Time and date that the row was    |
|                                   | last modified in the data         |
|                                   | warehouse                         |
+-----------------------------------+-----------------------------------+

.. _touchengagement:

Touch Engagement
~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| **Engagement Score**              | The sum of all the engagement     |
|                                   | scores in the events associated   |
|                                   | with the touch                    |
+-----------------------------------+-----------------------------------+

.. |Dimensions grouped by topic| image:: https://cdn2.webdamdb.com/1280_omVsUCL15tc4.png?1526475903
   :width: 302px
   :height: 299px

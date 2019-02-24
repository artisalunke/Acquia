.. include:: /common/global.rst

|acquia-product:cha| File Import API reference
==============================================

.. toctree::
   :hidden:
   :glob:

   /lift/api/import/*

.. container:: internal-navigation

   **File import**

   * Create
   * :doc:`Upload </lift/api/import/upload/>`

.. container:: message-status

   This feature is available only to |acquia-product:cha| |acquia-product:ldb| subscribers.

Based on the data that it receives, |acquia-product:cha| can help you to
determine who your visitors are and what they're interested in, and then
allow you to provide your visitors with information about their
interests. Normally, this information is sent to |acquia-product:lpm| as
capture events from websites, either through 
`modules on your Drupal website </lift/exp-builder>`__ or through our 
`JavaScript tracking code </lift/offers/tracker/add>`__. But what if you have data about your
visitors from other sources, such as your CRM system?

When you subscribe to the |acquia-product:ldb|, you can export
information from other data sources and then structure the information
into an upload file that |acquia-product:lpm| can accept. After you do
this, you can import the file into |acquia-product:lpm| for use with
data that you're collecting from your website, enriching your view of
your visitors.

Imports are processed every 15 minutes, at 0, 15, 30, and 45 minutes
after the hour.

File format
-----------

A |acquia-product:lpm| upload file includes two sections to describe its
data: a `header <#header-section>`__ section and a `data <#data-section>`__ section.


Header section
~~~~~~~~~~~~~~

The header for the upload file consists of two lines:

-  *First line* - The version number of the upload file

   .. note::  The current upload file version is ``0.0.1``.

-  *Second line* - A pipe-delimited ( ``|`` ) list of the import element
   fields that you want to use. There are 12 headers (marked as
   **Required** in the following table) that must be on this line. The
   other headers are not mandatory and can be excluded if they are not
   needed.

.. list-table::
   :widths: 30 40 20 10
   :header-rows: 1 

   * - Field name
     - Description
     - Data type
     - Required
   * - event_date
     - Event date and time in UTC ``(Example: 2014-08-27 11:25:00.155)``
     - Date ``(YYYY-MM-DD HH:mm:ss.sss)``
     - Yes
   * - event_name
     - Event name corresponding to the captured information — the event name must be already `created in Profile Manager (see note) </lift/omni/api/file/import#event_name_note>`__ (Example: ``Content View``)
     - String
     - Yes
   * - event_source
     - Source of the event (Example: ``Call Center``)
     - String
     - Yes
   * - identity
     - Visitor's identity information (Example: ``peter@example.com``)
     - String
     - Yes
   * - identity_source
     - `Type </lift/javascript/identity>`__ of visitor's identity information (Example: ``email``)
     - Specific string (``account, email, facebook, name, twitter``), or ``tracking``
     - Yes
   * - ip_address
     - Visitor's IP address (Example: ``76.9.215.214``)
     - IPv4 address
     - Yes
   * - platform
     - Visitor's platform (Example: ``Win32``)
     - String
     - Yes
   * - referral_url
     - Referrer's URL (Example: ``http://www.example.com/homepage``)
     - String
     - Yes
   * - title
     - Page title (Example: ``Some Important News on example.com``)
     - String
     - Yes
   * - touch_id
     - Internal identifier for the touch (Example: ``CALL1920``)
     - String
     - Yes
   * - url
     - Event's URL (Example: ``http://www.example.com/somepage``)
     - String
     - Yes
   * - user_agent
     - Visitor's user agent (Example: ``Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0``)
     - String
     - Yes
   * - engagement_score
     - Number that you have chosen to signify the importance of a visitor's interest in this event (Example: ``100``)
     - Integer
     - No
   * - site
     - Name of a customer site; must match to the external ID of an entry in the Profile Manager customer site table (Example: ``staging``)
     - String
     - No
   * - personalization_goal_name
     - The name of the goal reached
     - String
     - No
   * - personalization_goal_value
     - The value of the goal reached
     - Integer
     - No
   * - personalization_name
     - Name of personalization associated with an event
     - String
     - No
   * - personalization_machine_name
     - Machine name of personalization associated with an event
     - String
     - No
   * - personalization_chosen_variation
     - The variation (decision) chosen for an event
     - String
     - No
   * - personalization_audience_name
     - The name of the audience
     - String
     - No
   * - personalization_decision_policy
     - The decision policy used (Examples: ``explore`` or ``target``)
     - String
     - No


You can also use the import file to enter information into user-defined fields (where ``<i>`` is the user-defined field you want to use, such as ``touch_udf3``):

.. list-table::
   :widths: 30 40 15 15
   :header-rows: 1 

   * - Field name
     - Description
     - Data type
     - Example
   * - person_udf<i>
     - User-defined field for a person — can accept up to 50 values *(Optional)*
     - String
     - ``frequent shopper``
   * - touch_udf<i>
     - User-defined field for a touch — can accept up to 20 values *(Optional)*
     - String
     - ``defect``
   * - event_udf<i>
     - User-defined field for an event — can accept up to 50 values *(Optional)*
     - String
     - ``follow up``

.. note::  You can use any ordering for your user-defined fields in the import file and can also omit unused user-defined fields.

Finally, you can use the file to import information into custom
fields that you have added to the |acquia-product:lpm| service.
Simply add each custom field's name to the end of the pipe-delimited
list.

.. note::  

   -  **event_name** - To import visitor information without associated
      events or touches, enter ``updatePerson`` for this field in the data
      section. When using ``updatePerson``, |acquia-product:cha| imports
      only the following fields for the record: identity, identity_source,
      and person_udf<i>.
   -  If the actual data that you are importing includes pipes, enclose the
      data in double quotes to avoid misinterpretation of column values.
      For example, ``My company | a great company`` is interpreted as two
      column values, and ``"My company | a great company"`` is interpreted
      as a single column value.
      If the data that you are importing already includes double quotes,
      add a second set of double quotes to each double quote. As an
      example, while ``"My company | a "great" company"`` is interpreted as
      two column values, ``"My company | a ""great"" company"`` is
      interpreted as one column value.

Example
^^^^^^^

The following example is the header section of an upload file with the
12 required import element fields and an additional optional field (in
this example, ``engagement_score``):

``0.0.1 event_name|event_date|event_source|identity|identity_source|touch_id|url|referral_url|title|user_agent| platform|ip_address|engagement_score``


Data section
~~~~~~~~~~~~

Enter each event that you want to upload to |acquia-product:lpm| on a
separate line in the file, with each of the event's field separated by a
pipe ( ``|`` ). The ``event_name``, ``identity``, and
``identity_source`` fields are required to be in the data section and
must have associated values. The ``identity_source`` field must be a
specific string as described in the `File format <#format>`__ section.
Even though only three fields are required to be in the data section,
pipes must still be included to indicate that the data is null for
unused core headers.


Upload file examples
~~~~~~~~~~~~~~~~~~~~

The following ``page_example`` upload file is the most basic upload file
template and contains only the required data fields.

.. code::

   0.0.1 event_name|identity|identity_source|event_date|event_source|touch_id|
   url|referral_url|title|user_agent|platform|ip_address Content View|
   exampleIdentity@email.com|email|||||||||

The following is an example of a more complete import file with most of
its fields set. Providing additional information for each field allows
you to analyze events more comprehensively.

.. code::

   0.0.1 event_name|event_date|event_source|identity|identity_source|touch_id|
   url|referral_url|title|user_agent|platform|ip_address|post_id|content_section|
   offerid|campaignid Content View|2014-08-27 11:25:00.155|web|
   exampleEmail@email.com|email|1234|http://www.example.com/page1|
   http://www.example.com/homepage|Page 1 title|Mozilla/5.0 (compatible; MSIE 
   9.0; Windows NT 6.1; WOW64; Trident/5.0)|Win32|90.80.40.225|2693934|
   gallery|| Campaign Action|2014-08-27 11:25:00.162|web|My Name|name|1234|
   http://www.example.com/page1|http://www.example.com/homepage|Page 1 Title|
   Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)|
   Win32|81.255.192.149|||SIDEBAR|RECOFOOD Content View|2014-08-27 11:25:00.381|
   web|1565224|tracking|5566|http://www.example.com/page1|
   http://www.example.com/homepage|Page 1 Title|Mozilla/5.0 (Macintosh; Intel 
   Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 
   Safari/537.36|MacIntel|78.211.126.102|2694516|sports||``


Purging a person from the database
----------------------------------

The File Import API includes a ``purgePerson`` event type that you can
use to remove a person from your database. For more information about
how to use ``purgePerson``, see 
`Purging a person from the database </lift/omni/api/file/import/purge>`__.

Importing goal and decision events
----------------------------------

The File Import API allows you to import goal and decision information
into |acquia-product:lpm|. For more information about how to do this,
see the |event_import|_ documentation.


.. |event_import| replace:: \ |acquia-product:liftapi|\  event_import
.. _event_import: http://docs.lift.acquia.com/profilemanager/#event_import
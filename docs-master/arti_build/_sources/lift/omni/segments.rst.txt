.. include:: /common/global.rst

|acquia-product:cdw| Segment field types
========================================

.. container:: internal-navigation

   **Acquia Lift data warehouse**

   * :doc:`Intro </lift/omni>`
   * :doc:`Person </lift/omni/person>`
   * :doc:`Person </lift/omni/person>`
   * :doc:`Touch </lift/omni/touch>`
   * :doc:`Event </lift/omni/event>`
   * Segments

The |acquia-product:ldw| uses the *Segments* field layout to describe
segments associated with each event for a given person.

The Segments field layout includes the following tables:

-  `segment <#segment-table>`__
-  `matched_segment <#matched-segment-table>`__


segment table
-------------

The Segment table contains a list of the segments in
|acquia-product:cha| and is synchronized with the configuration
database.

.. list-table::
   :widths: 25 20 10 45
   :header-rows: 1 

   * - Field name
     - `Data type <https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html>`__
     - Sortable
     - Description
   * - id
     - INT (4 bytes)
     - |yes|
     - Unique segment ID — Acquia Lift internal value
   * - name
     - VARCHAR (100)
     - |no|
     - Name of the segment (for example, ``All article pages``)
   * - tracking_id
     - VARCHAR (100)
     - |no|
     - Shortened machine name of the segment name, from the |acquia-product:lpm| segment builder



matched_segment table
---------------------

The Matched_Segment table contains a list of the events and segments
that are associated with each segment and links the Segments table to
the Event table.

.. list-table::
   :widths: 25 20 10 45
   :header-rows: 1 

   * - Field name
     - `Data type <https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html>`__
     - Sortable
     - Description
   * - event_id
     - INT (8 bytes)
     - |yes|
     - Link to an existing ID for an `event </lift/omni/event>`__ in the Event table — Acquia Lift internal value
   * - person_id
     - INT (8 bytes)
     - |no|
     - Link to an existing id for a `person </lift/omni/person>`__ — Acquia Lift internal value
   * - segment_id
     - INT (4 bytes)
     - |yes|
     - Link to an existing ID for a segment in the Segments table — Acquia Lift internal value
   * - db_last_modified_date
     - TIMESTAMP
     - |no|
     - The UTC time and date when the row was last modified in the database

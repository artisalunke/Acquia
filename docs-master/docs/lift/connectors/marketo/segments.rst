.. include:: /common/global.rst

Creating segments with Marketo connector data
=============================================

.. container:: internal-navigation

   **Marketo connector**

   * :doc:`Intro </lift/connectors/marketo>`
   * :doc:`Config </lift/connectors/marketo/config>`
   * Segments

After you create and `configure </lift/connectors/marketo/config>`__ a
Marketo connector and begin importing visitor data from Marketo into
|acquia-product:lpm|, you can view this data and use it to create
`segments </lift/profile-mgr/segment>`__.


Viewing imported Marketo data
-----------------------------

|lift-web-marketo-visitor-touch-source.png|

To view imported Marketo data in a visitor profile on
|acquia-product:lpm|, complete the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface, and then click the **People** tab.
#. Click a visitor's tracking ID to view detailed information for that
   visitor.
#. Click the `Activity </lift/profile-mgr/person/activity>`__ tab.
   |acquia-product:lpm| displays the following types of Marketo data:

   -  In the **Touches** table, if a touch was imported from Marketo,
      the **Source** column contains the value ``Marketo``.
   -  When you select a touch that was imported from Marketo, in the
      `Events </lift/profile-mgr/event/category>`__ table,
      |acquia-product:lpm| displays only events corresponding to Marketo
      activities that you have mapped.
   -  Other lead or activity mappings that you have configured in the
      Marketo connector display in a visitor's profile if they have been
      mapped to |acquia-product:cha| `column meta
      data </lift/profile-mgr/admin/column-meta-data>`__ fields. To
      display this data, depending on your needs, you can view the
      following tabs:

      -  To display data mapped to fields in the
         `Person </lift/omni/person>`__ table, in a visitor profile,
         click the **Profile Details** tab.
      -  To display data mapped to fields in the
         `Touch </lift/omni/touch>`__ and `Event </lift/omni/event>`__
         tables, in a visitor profile, click the **Activity** tab, then
         click **Show Properties**.


Configuring column meta data fields for use in segments
-------------------------------------------------------

|lift-web-marketo-column-metadata.png|

Before you can create segments using Marketo activity and lead data, you
need to configure your column meta data fields to be available for use
in segments. For example, when you `created a Marketo
connector </lift/connectors/marketo/config>`__ and added an activity
mapping for **Click Email**, you mapped the activity's primary attribute
``Mailing ID`` to the field ``custom_field_10`` in the Event table. Now
you need to configure ``custom_field_10`` to be segmentable and add
information that allows you to select the field when creating segments.
To customize this field for use in creating segments, complete the
following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface, and then click the
   **Admin** tab.
#. Go to **Manage configuration data > Column meta data**.
#. Click the **Add new column meta data** link.
#. Enter values in the following fields:

   -  **Display Name** - Descriptive name for the column meta data used
      for display in |acquia-product:lpm|. For this example, enter
      ``Mailing ID``.
   -  **Display Order** - The order in which the column meta data
      appears in the Properties section of the Person detail page.
   -  **Table** - Name for the table to which this field belongs in
      |acquia-product:cha|. For this example, click **Event**.
   -  **Accessor** - Method name used to retrieve the value of the
      column meta data. For this example, click
      **custom_field_10(getCustomField10)**.
   -  **Description** - the purpose of this field — for this example,
      enter ``Custom field mapping for Marketo Mailing ID data.``
   -  **Type** - Available data types of the column meta data value
      (based on the selected Table and Accessor), which controls how you
      want the data to be displayed and managed:

      -  **String**
      -  **Boolean**
      -  **Date**
      -  **Integer**
      -  **Float**
      -  **Comma Separated List**

      For this example, click **String**.

   -  **Is Visible In Person Detail** check box - Select the check box
      to display this item in the **Properties** section of the `Person
      detail page </lift/profile-mgr/person>`__ in |acquia-product:lpm|

#. For this example, you want to create a
   `segment </lift/profile-mgr/segment>`__ based on the values stored in
   the column. To do so, click the **Segmentable** check box, and then
   enter values for the following fields:

   -  **Operators** - Defines how an element of a segment can be
      compared to the column value — operators can be numeric values
      (such as **=**) or text values (such as **matches one**),
      depending on the data type you selected above
   -  **Category** - Descriptive grouping that allows you to organize
      your meta data segment criteria into folders in the segment
      builder (examples include **Person Properties** and **Current
      Location**). For this example, enter **Marketo**.
   -  **Units** - Units of measure for the segment based on the data
      type you selected (for example, if you are using the **date** data
      type, **days since** is an available unit of measure)
   -  **Grouping** - A selectable list of groupings to use, based on a
      list predefined by |acquia-product:cha| in the accessor — for
      example, **Current Touch** is one of the items available for
      Keyword Count column meta data)
   -  **Label for Terms Value** - Label to show if additional terms
      criteria are required — for example, this label can be be
      **Keywords** if a list of keywords is part of the criteria for
      **Keyword Count** column meta data)
   -  **Ignore Case When Comparing** check box - Select this check box
      to ignore the case (do not distinguish uppercase characters from
      lowercase characters) when performing a string comparison

#. If you want the values stored in the column to be ranked, select the
   **Rankable** check box, and then enter values for the following
   fields:

   -  **Ranking Eviction Days** - The number of days that the
      |acquia-product:cha| server will rank values; ranking values that
      are older than the number of days you enter in this field will be
      deleted
   -  **Percentage** check box - Selecting this check box displays the
      ranking value as a percentage across all ranking values for that
      column meta data

#. If you want the column meta data to be visible on the **Insights**
   tab of the **Person detail** page, select the **Rankable** check box,
   and then enter values for the following fields:

   -  **Insight Title** - The title as displayed on the **Insights** tab
      of the Person detail page
   -  **Insight Display Order** - Numeric value that determines the
      order displayed on the **Insights** tab of the Person detail page

#. Click **Save**. You have now given **custom_field_10** the name
   **Mailing ID**, enabled its use in segments, and put it into the
   category **Marketo** in the segment builder.

You can now begin creating segments using
`lead </lift/connectors/marketo/lead>`__ and
`activity </lift/connectors/marketo/activity>`__ data.

.. |lift-web-marketo-visitor-touch-source.png| image:: https://cdn3.webdamdb.com/1280_2IfwQl2BWL02.png?1526475836
   :width: 760px
   :height: 255px
.. |lift-web-marketo-column-metadata.png| image:: https://cdn4.webdamdb.com/1280_UeC0p37wDR14.png?1526475576
   :width: 590px
   :height: 408px

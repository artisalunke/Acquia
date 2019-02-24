.. include:: /common/global.rst

Creating segments with Eloqua
=============================

.. container:: message-status

   Eloqua connector integration is currently in a private beta. Contact your account manager if you wish to participate*.

.. container:: internal-navigation

   **Eloqua connector for Acquia Lift**

   * :doc:`Intro </lift/connectors/eloqua>`
   * :doc:`Config </lift/connectors/eloqua/configure>`
   * Segments

After you create and configure an Eloqua connector and begin importing
visitor data into |acquia-product:leb|, you can view this data and use
it to create `segments </lift/profile-mgr/segment>`__.


Viewing imported Eloqua data
----------------------------

To view imported Eloqua data in a visitor profile on
|acquia-product:lpm|, complete the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface, and then click the **People** tab.
#. Click a visitor's tracking ID to view detailed information for that
   visitor.
#. Click the `Activity </lift/profile-mgr/person/activity>`__ tab.

|acquia-product:lpm| displays the following types of Eloqua data:

-  In the **Touches** table, if a touch was imported from Eloqua, the
   **Source** column contains the value ``Eloqua``.
-  When you select a touch that was imported from Eloqua, in the
   `Events </lift/profile-mgr/event/category>`__ table,
   |acquia-product:lpm| displays only events corresponding to Eloqua
   activities that you have mapped.
-  Other contact or activity mappings that you have configured in the
   Eloqua connector display in a visitor's profile if they have been
   mapped to |acquia-product:cha| `column meta
   data </lift/profile-mgr/admin/column-meta-data>`__ fields. To display
   this data, depending on your needs, you can view the following tabs:

   -  To display data mapped to fields in the
      `Person </lift/omni/person>`__ table, in a visitor profile, click
      the **Profile Details** tab.
   -  To display data mapped to fields in the
      `Touch </lift/omni/touch>`__ and `Event </lift/omni/event>`__
      tables, in a visitor profile, click the **Activity** tab, then
      click **Show Properties**.


Configuring column meta data fields for use in segments
-------------------------------------------------------

Before you can create segments using Eloqua activity and lead data, you
will need to configure your column meta data fields to be available for
use in segments.

As an example (based on the sample values on the `Configuring the Eloqua
connector </lift/connectors/eloqua/configure>`__ page), creating an
Eloqua connector and adding an activity mapping for **Subscribe** maps
the activity's primary attribute ``CampaignId`` to the field
``event_udf5`` in the Event table. Next, you will need to configure
``event_udf5`` to be segmentable and add information that allows you to
select the field when creating segments. To customize this field for use
in creating segments, complete the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface, and then click the
   **Admin** tab.
#. Go to **Manage configuration data > Column meta data**.
#. Click the **Add new column meta data** link.
#. Enter values in the following fields:

   -  **Display Name** - Descriptive name for the column meta data used
      for display in |acquia-product:lpm| (for this example, enter
      ``CampaignID``)
   -  **Display Order** - The order in which the column meta data
      appears in the Properties section of the Person detail page
   -  **Table** - Name for the table to which this field belongs in
      |acquia-product:cha| (for this example, click **Event**)
   -  **Accessor** - Method name used to retrieve the value of the
      column meta data (for this example, click **custom_field_5**)
   -  **Description** - The purpose of this field (for this example,
      enter
      ``Campaign ID associated with an Acquia Lift Profile Manager personalized event action``)
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
      Location**) (for this example, enter **Eloqua**)
   -  **Units** - Units of measure for the segment based on the data
      type you selected (for example, if you are using the **date** data
      type, **days since** is an available unit of measure)
   -  **Grouping** - A selectable list of groupings to use, based on a
      list predefined by |acquia-product:cha| in the accessor (for
      example, **Current Touch** is one of the items available for
      Keyword Count column meta data)
   -  **Label for Terms Value** - Label to show if additional terms
      criteria are required (for example, this label can be be
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

#. Click **Save**. You have now assigned **custom_field_5** the name
   **CampaignID**, enabled its use in segments, and put it into the
   category **Eloqua** in the segment builder.

You can now begin creating segments using contact and activity data.

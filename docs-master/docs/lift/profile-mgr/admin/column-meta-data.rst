.. include:: /common/global.rst

Using column meta data
======================

The |acquia-product:cha| service stores information about visitors by
using a *person profile*. The profile is structured to collect data
about persons (information specifically about the visitor), events
(captured visitor actions from a website or other location), and touches
(a group of associated events that occur no more than 30 minutes apart
from one another).

Although some of the fields in the person profile are required by
|acquia-product:cha| for its operation (for example, geographic and
device-related information stored in the touch), you can use certain
fields to store additional data that you may want to use for
personalization — for example, information about gender for your
visitors. The |acquia-product:cha| service includes a certain number of
custom fields for each type of this information:

-  `Person table </lift/omni/person>`__ – 50 custom fields
-  `Touch table </lift/omni/touch>`__ – 20 custom fields
-  `Event table </lift/omni/event>`__ – 50 custom fields

The method by which |acquia-product:lpm| does this is to create an alias
(also known as a *column name*) for your custom data to an existing data
structure element, which you are reassigning to collect and store the
data that you require. For example, ``custom field 10`` in the Person
table might have the alias of ``gender``. |acquia-product:lpm| displays
``gender`` as the field name in the person profile and in the segment
builder.

Viewing your site's column names
--------------------------------

To view the custom field aliases that have already been configured for
your |acquia-product:lpm| environment, complete the following steps:

#. Sign in to the |acquia-product:lpm| `admin
   interface </lift/profile-mgr#signing>`__, and then click the
   **Admin** tab.
#. Click the **Manage configuration data** link.
#. Click the **Column meta data** link.

|acquia-product:lpm| displays a list of the current aliases for your
environment. To search for specific meta data items, complete the
following steps:

#. Enter the name of the meta data item in the **Find Meta Data** field.
#. In **Table**, click on the name of a table to limit your search
   results to meta data items belonging to that table:

   -  **Blank** – Select this option if you do not want to narrow your
      search results.
   -  **Person** – Narrows your search results to meta data items from
      the Person table.
   -  **Touch** – Limits search results to the Touch table's meta data
      items.

#. If you selected a table in **Table**, **Accessor** displays a list of
   column names for the selected table. Select a column name from this
   list to search for its associated column meta data item.
#. Click **Find**.

The list of aliases displayed by |acquia-product:lpm| contains several
pieces of information:

+-----------------------------------+-----------------------------------+
| Column                            | Description                       |
+===================================+===================================+
| **Display name**                  | The name of the column meta data  |
|                                   | item                              |
+-----------------------------------+-----------------------------------+
| **Table**                         | The table to which this column    |
|                                   | meta data item belongs            |
+-----------------------------------+-----------------------------------+
| **Display order**                 | The order in which this column    |
|                                   | meta data item appears in the     |
|                                   | **Properties** section of the     |
|                                   | **Person Detail** page            |
+-----------------------------------+-----------------------------------+
| **Is visible in person detail**   | Whether this particular column    |
|                                   | meta data item is listed in the   |
|                                   | **Person Detail** section of Lift |
|                                   | Web. For more information about   |
|                                   | the meta data items that are      |
|                                   | visible in this section of        |
|                                   | |acquia-product:lpm|, see         |
|                                   | `Examining visitor                |
|                                   | information </lift/profile-mgr/pe |
|                                   | rson>`__                          |
+-----------------------------------+-----------------------------------+
| **Is segmentable**                | Whether this column meta data     |
|                                   | item can be used as criteria in a |
|                                   | segment to track website          |
|                                   | visitors' behavior                |
+-----------------------------------+-----------------------------------+
| **Is rankable**                   | Whether this column meta data     |
|                                   | item can be used to track the     |
|                                   | number of times that every        |
|                                   | permutation of values in this     |
|                                   | column has occurred, such as how  |
|                                   | many times a visitor has accessed |
|                                   | your website, ranked by the type  |
|                                   | of platform on which the visitor  |
|                                   | accessed your website             |
+-----------------------------------+-----------------------------------+
| **Description**                   | An explanation of the column meta |
|                                   | data item's properties, purpose,  |
|                                   | and possible uses                 |
+-----------------------------------+-----------------------------------+
| **Actions**                       | Additional steps you can take     |
|                                   | regarding this column meta data   |
|                                   | item, including deleting it       |
+-----------------------------------+-----------------------------------+

Managing your site's column names
---------------------------------

Using the column names page, you can add new column names and edit or
remove already existing column names.

.. important:: 

   Do not modify the values for the following custom fields and their
   corresponding **Accessors** column. These fields are used by
   |acquia-product:leb| for internal data collection.

-  `Person </lift/omni/person>`__ table – custom_field_1,
   custom_field_2, custom_field_3
-  `Event </lift/omni/event>`__ table – custom_field_2

Adding a column name
~~~~~~~~~~~~~~~~~~~~

To add a new column name, complete the following steps:


.. |signinlpm| replace:: Sign in to the  \ |acquia-product:lpm|\  interface
.. _signinlpm: /lift/profile-mgr#signing

#. |signinlpm|_, and then click the **Admin** tab.
#. Click the **Manage configuration data** link.
#. Click the **Column meta data** link.
#. Click the **Add new column meta data** link.
#. Enter values in the following fields:

   -  **Display Name** – Descriptive name for the column meta data used
      for display in |acquia-product:lpm|
   -  **Display Order** – The order in which the column meta data
      appears in the Properties section of the Person detail page
   -  **Table** – Name for the table in |acquia-product:ldb|
   -  **Accessor** – Method name used to retrieve the value of the
      column meta data
   -  **Type** – Available data types of the column meta data value
      (based on the selected Table and Accessor), which controls how you
      want the data to be displayed and managed:

      -  **String**
      -  **Boolean**
      -  **Date** (Format: *YYYY-MM-DD HH:mm:ss:SSS TIMEZONE* )
      -  **Integer**
      -  **Float**
      -  **Comma Separated List**

   -  **Is Visible In Person Detail** check box – Select the check box
      to display a visitor's value for the column meta data item in the
      **Properties** section of the `Person detail page</lift/offers/person>`__ in
      |acquia-product:lpm|.

#. If you want to create `segments </lift/profile-mgr/segment>`__ based
   on the values stored in the column, click the **Segmentable** check
   box, and then enter values for the following fields:

   -  **Operators** – Defines how an element of a segment can be
      compared to the column value — operators can be numeric values
      (such as **=** or **<=**) or text values (such as **matches
      one**), depending on the data type you selected above
   -  **Category** – Descriptive grouping that allows you to organize
      your meta data segment criteria into folders in the segment
      builder (examples include **Person Properties** and **Current
      Location**)
   -  **Units** – Units of measure for the segment based on the data
      type you selected (for example, if you are using the **date** data
      type, **days since** is an available unit of measure)
   -  **Grouping** – A selectable list of groupings to use, based on a
      list predefined by |acquia-product:cha| in the accessor — for
      example, **Current Touch** is one of the items available for
      Keyword Count column meta data)
   -  **Label for Terms Value** – Label to show if additional terms
      criteria are required — for example, this label can be be
      **Keywords** if a list of keywords is part of the criteria for
      **Keyword Count** column meta data)
   -  **Ignore Case When Comparing** check box – Select this check box
      to ignore the case (do not distinguish uppercase characters from
      lowercase characters) when performing a string comparison

#. If you want the values stored in the column to be ranked, select the
   **Rankable** check box, and then enter values for the following
   fields:

   -  **Ranking Eviction Days** – The number of days that the
      |acquia-product:cha| server will rank values; ranking values that
      are older than the number of days you enter in this field will be
      deleted
   -  **Percentage** check box – Selecting this check box displays the
      ranking value as a percentage across all ranking values for that
      column meta data

#. If you want the column meta data to be visible on the **Insights**
   tab of the **Person detail** page, select the **Rankable** check box,
   and then enter values for the following fields:

   -  **Insight Title** – The title as displayed on the **Insights** tab
      of the Person detail page
   -  **Insight Display Order** – Numeric value that determines the
      order displayed on the **Insights** tab of the Person detail page

#. Click **Save**.

Editing a column name
~~~~~~~~~~~~~~~~~~~~~

To edit a column name, complete the following steps:

#. `Sign in </lift/profile-mgr>`__ to the |acquia-product:lpm|
   interface , and then click the **Admin** tab.
#. Click the **Manage configuration data** link.
#. Click the **Column meta data** link.
#. Click the column name that you want to edit and then modify its
   values as required.
#. Click **Save** to save your changes.

Deleting a column name
~~~~~~~~~~~~~~~~~~~~~~

To remove a column name, complete the following steps:

#. `Sign in </lift/profile-mgr#signing>`__ to the |acquia-product:lpm|
   interface, and then click the **Admin** tab.
#. Click the **Manage configuration data** link.
#. Click the **Column meta data** link.
#. Find the column name that you want to remove and then click its
   **Delete** link.

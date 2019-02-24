.. include:: /common/global.rst

2D Table node
=============

|2D Table node|

The 2D Table node takes exactly two input values, referred to as the
X-Value and the Y-Value, and produces a single output. The output can be
any valid JavaScript value. The 2D Table node is very useful for
applying simple segmentation to data.

The input values for the 2D Table node are set when the node is used
within a graph. Within the node itself there are simple controls for
adding rows and columns to the decision table. Each row and column is
headed by a JavaScript expression and the table cell for which the row
and column expressions are both true will give the return value. The
X-Value expressions are evaluated left-to-right and the Y-Value
expressions are evaluated top-to-bottom.

The 'Add Column' and 'Add Row' buttons are used to add columns and rows
to the table respectively. Each column or row is headed by a box which
expects an expression to be entered in the 'Edit Operator' panel on the
right hand side of the window. All JavaScript expressions are passed the
|acquia-product:aj| internal variable 'VAL' which can be used in any
valid JavaScript expression.

For example the screenshot below shows a 2D Table which expects to
receive an Age and a Gender value as the X-Value and Y-Value inputs
respectively and will return a segment identifier. The segment
identifier (an integer literal) ranges between 1 and 4.

|2d Table Node|

The Operator for the middle column of the X-Value is shown in detail
below demonstrating the use of the JavaScript VAL variable.

|Javascript VAL example|

The Operator can also be given a display description which has been used
to create a more understandable label for the column or row. For example
to cater for the end conditions where the JavaScript operator expression
is ``TRUE`` and to display that as 'Else' in the table, the Edit
Operator panel would look like this:

|Operator Expression|

Creating a conditional node
---------------------------

To create a conditional node, perform the following actions:

#. Sign in to your |acquia-product:aj| interface.
#. Identify the project you wish to modify.
#. Click the **Project Editor** |Project Editor icon| icon.
#. In the top left-hand corner of the screen, click the **Action Menu**
   |Action Menu icon| icon.
#. Select **+ Create New** from the list.
#. Enter the name of your new 2D Table node in the **Name** field.
#. Scroll through the list of node types to find the **Logic** section,
   and click **2D Table**:

   |Logic node type listing|

#. Click **Create New Item**.
#. Use the **Add Column** and **Add Row** buttons to construct your data
   matrix.
#. Click **Save**.

2D Table return values
----------------------

The 2D Table will return the value at the intersection of the X-Value
and Y-Value row and column or it will return an 'error' in the Testing
Console. The 2D Table can return any valid JavaScript literal value, a
schema location or a public variable. For example, to return a more
complex segmentation object from the table above a literal such as this
could be used for the cell return value:

``{   "label" : "youngMan",   "offer" : 1 }``

This allows complex two dimensional segmentations to be applied.

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Each table cell must have a     | One or more table cells do not    |
| valid (non-empty) data            | have a data reference (literal,   |
| reference**                       | schema or public variable) set.   |
+-----------------------------------+-----------------------------------+
| **Each column must have a         | No expression has been given for  |
| condition**                       | the column or row.                |
+-----------------------------------+-----------------------------------+

Errors
------

-  ``Unable to find value for (x or y) parameter`` - One of the X or Y
   values has not been provided in the schema.

.. |2D Table node| image:: https://cdn4.webdamdb.com/1280_AexGBJKU0J65.png?1526475646
   :class: no-sb float-left logo-sm-lift
   :width: 51px
.. |2d Table Node| image:: https://cdn3.webdamdb.com/1280_MYOIzBS5Ji51.png?1526475726
   :width: 554px
   :height: 279px
.. |Javascript VAL example| image:: https://cdn3.webdamdb.com/1280_QdPEjFuxhh61.png?1526475659
   :width: 325px
   :height: 175px
.. |Operator Expression| image:: https://cdn3.webdamdb.com/1280_IxJptAe5j4g0.png?1526476048
   :width: 321px
   :height: 166px
.. |Project Editor icon| image:: https://cdn4.webdamdb.com/100th_sm_YcVG2zY8pZL5.png?1526475783
   :width: 33px
   :height: 29px
.. |Action Menu icon| image:: https://cdn3.webdamdb.com/100th_sm_Aa8wvVef08x7.png?1526475662
   :width: 26px
   :height: 22px
.. |Logic node type listing| image:: https://cdn3.webdamdb.com/1280_kfNiX7lNWL28.png?1526475881
   :width: 377px
   :height: 116px

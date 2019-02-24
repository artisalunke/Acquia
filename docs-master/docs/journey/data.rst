.. include:: /common/global.rst

|acquia-product:aj| data structure
==================================

|acquia-product:aj| maintains an internal data store during graph
execution. Every `graph node </journey/node>`__ has at least one input
or output location that refers to a data store property. As the graph
executes, each node may alter the data store. The data in
|acquia-product:aj| falls into one of following distinct types:

-  **Data Schema** - A JavaScript object that lasts for the execution of
   a single graph. It can be read from and altered by any node within
   the graph.
-  **Literal** - A constant value which is used as an input to a node or
   the return value from a `Return Node </journey/node/return>`__.
-  **Public Variable** - A JavaScript object that exists outside of the
   schema. A public variable can be read from and written to from any
   node in the graph. Public variables have two modes: transactional and
   persistent. Persistent public variables last throughout the
   deployment of a graph and across all `graph listener
   events </journey/getting-started/graph#listening>`__.

When `building a graph </journey/getting-started/graph>`__ and choosing
the data location for a node, the three options for choosing data are
shown in the top right panel of the window. This panel can be toggled
through the **Data Schema**, **Literals** and **Public Variables** views
by using the navigation buttons |Navigation arrows| on the right-hand
side of the screen.

Data schema
-----------

The **Data Schema** is a single JavaScript object that can contain
fields and other objects in a hierarchical layout. Elements containing
child elements can be displayed and hidden using the plus and minus
buttons next to an item; elements without children will display ``>`` to
the left of the element name.

Graphs can read and write individual fields or whole records from the
schema during execution. It is not necessary to declare fields in the
schema prior to graph execution, but it is necessary if they are to be
chosen as an input or output location for a node.

Searching the schema
~~~~~~~~~~~~~~~~~~~~

You can filter the **Data Schema** by field name. As you type,
|acquia-product:aj| updates the schema to display only fields that are a
partial or exact match for the text entered in the search field. The
filter is not case sensitive, so ``uid`` and ``UID`` are considered the
same field. If you have an existing field selected in the schema, it
will remain visible and selected, even if it does not match your query.

To filter the schema, complete the following steps:

#. Sign in to |acquia-product:aj|.
#. On the **Home Screen**, find the project tile for the project that
   you want to customize, and then click its **Project Editor** |Project
   Editor icon| icon.
#. Click the name of the item that you want to open, and then at the
   bottom of the page click **Open**.
#. In the right-hand side of the page, click the **navigation**
   |Navigation arrows| icons until **Data Schema** is displayed.
#. In the search box, enter a keyword to filter on. If you enter more
   than one word, |acquia-product:aj| will search for each keyword and
   display fields that match any of the entered keywords.

   |data schema search|

In the following example, the data schema is filtered for the keywords
``tweet created``, returning 6 matching results:

|data schema filter example|

Adding a single field to the schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add a field to the schema, perform the following actions:

#. In the right-hand side of the page, click the navigation icons
   |Navigation arrows| until **Data Schema** is displayed.
#. Expand the Data Schema and click the field you want to add a child
   field to.
#. Click the plus sign:
   |Add schema field|
#. The **Add Field** dialogue will be displayed. Enter a name for the
   new field.
#. Click **Save**.

Adding a child record to the schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add a child record to an existing record, perform the following
actions:

#. In the right-hand side of the page, click the navigation icons
   |Navigation arrows| until **Data Schema** is displayed.
#. Click the record you want to add a child to.
#. In the **Data Schema** icon list, click the **Add Child Record to
   Entities** |Add Child Record| icon.
#. In the **Add Child Record** dialog that appears, paste in any valid
   JavaScript Object Notation (JSON) record definition. Each property in
   the JSON record will become a field. Any other values are ignored.
#. Click **Save**.

.. note:: You can use websites like `JSON Lint <http://jsonlint.com/>`__ to
          confirm you have valid JSON syntax. Your JSON must be a valid standalone
          object and must begin and end with curly brace (``{``, ``}``)
          characters.

Renaming a field in the schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To rename a field in the **Data Schema**, complete the following steps:

#. In the right-hand side of the page, click the navigation icons
   |Navigation arrows| until **Data Schema** is displayed.
#. Click the field you want to edit.
#. Click the **Pencil** icon.
#. In the **Edit Field** dialog, enter the new field name.
#. Click **Save**.

Deleting a field or record from the schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To delete a field (and all of its children) from the **Data Schema**,
complete the following steps:

#. In the right-hand side of the page, click the navigation icons
   |Navigation arrows| until **Data Schema** is displayed.
#. Click the field you want to delete.
#. Click the **Trashcan** icon.

.. important::
  -  Deleting fields cannot be undone.
  -  If you delete a schema field currently in use by one or more nodes,
     the field reference will be removed from each node, and your graph
     will no longer be valid until you update the affected nodes.

Literal values
--------------

A Literal value is any valid `JavaScript ES5 (ECMAScript 5) primitive or
object <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures>`__.
Examples include:

-  *Values*

   -  String - ``Hello World``
   -  Numeric - ``3``, ``4.5``

-  *Objects* -
   ``{ "car" : { "make" : "Ford", "model" : "Mondeo", "engine" : "diesel" } }``

Assigning a literal value
~~~~~~~~~~~~~~~~~~~~~~~~~

In |acquia-product:aj|, a literal value may be assigned directly to a
graph node. To assign or edit a literal value for a node, complete the
following steps:

#. Click the node in your graph you want to associate with a literal
   value.
#. In the right-hand side of the page, click the navigation icons
   |Navigation arrows| until **Literals** is displayed.
#. In the **Literals** text field, enter a literal value.
#. In the **Edit** panel for the node, click the **left arrow** |left
   arrow| icon to associate your literal value with the node. An example
   of a `Set Node </journey/node/set>`__ with an object literal
   associated with is shown in the following example:
   |Set Node|

Public variables
----------------

Public variables are used to hold data that is necessary, but not
related to, the entity being processed. Public variables can hold any
valid JavaScript object or primitive value, such as a temporary value or
an access key. If the data should be part of the transaction and
discarded at the end of the graph execution, then it should be included
with the schema, instead of a public variable. Public variables can be
initialized with values, unlike schema elements.

Creating a public variable
~~~~~~~~~~~~~~~~~~~~~~~~~~

Public variables have a scope which can be persistent or transactional.
*Persistent* variables exist across all executions of a graph, including
all of the executions of a graph from a listener, while *transactional*
variables are reset on each graph execution.

Public variables are empty by default, but they can have any valid
JavaScript Object Notation (JSON) or primitive as an initial value. For
example, a public variable could be initialized with the number ``120``,
the string ``journey``, or the JSON literal
``{"count":90, "label":"How many?"}``.

To create a public variable, perform the following actions:

#. In the right-hand side of the page, click the **navigation**
   |Navigation arrows| icons until **Public Variables** is displayed.
#. Click the **Plus** sign to display the **Add Public Variables**
   dialog: |br|
   |Add Variables screen|
#. Enter a name for the variable.
#. Click to select whether the variable is *Persistent* or
   *Transactional*.
#. If you want to specify a default value, click **Specify** and provide
   a value in the **Initial Value** field.
#. Click **Save**.

Editing a public variable
~~~~~~~~~~~~~~~~~~~~~~~~~

To edit a public variable, complete the following steps:

#. In the right-hand side of the page, click the navigation icons
   |Navigation arrows| until **Public Variables** is displayed.
#. Click the **pencil** icon to display the **Edit Public Variables**
   dialog.
#. Make any necessary changes.
#. Click **Save**.

Deleting a public variable
~~~~~~~~~~~~~~~~~~~~~~~~~~

To delete a public variable, complete the following steps:

#. In the right-hand side of the page, click the navigation icons
   |Navigation arrows| until **Public Variables** is displayed.
#. Click the **trash can** icon to delete the highlighted public
   variable name. **You cannot undo this action**.

.. important::
  If you delete a public variable currently in use by one or more nodes,
  the public variable reference will be removed from each. Your graph will
  no longer be valid until you update the effected nodes.

.. |Navigation arrows| image:: https://cdn4.webdamdb.com/1280_snhN2b7Bd5h4.png?1526475819
   :width: 69px
   :height: 34px
.. |Project Editor icon| image:: https://cdn3.webdamdb.com/1280_Qx24aCvtr211.png?-62169955200
   :class: no-sb
   :width: 30px
   :height: 30px
.. |data schema search| image:: https://cdn2.webdamdb.com/1280_cNQpPhpaHfy8.png?1527199132
   :width: 300px
.. |data schema filter example| image:: https://cdn3.webdamdb.com/1280_g6QUAM68svj1.png?1527199222
   :width: 300px
.. |Add schema field| image:: https://cdn4.webdamdb.com/1280_sTYiLrqakxm0.png?1526475665
   :width: 338px
   :height: 103px
.. |Add Child Record| image:: https://cdn4.webdamdb.com/1280_2uZfLwE2RR31.png?-62169955200
   :width: 40px
   :height: 42px
.. |left arrow| image:: https://cdn2.webdamdb.com/100th_sm_kR0cgUi72rf3.png?1527199363
   :width: 24px
.. |Set Node| image:: https://cdn3.webdamdb.com/1280_oBU38rfKy1d7.png?1527199430
   :width: 400px
.. |Add Variables screen| image:: https://cdn2.webdamdb.com/1280_k4LG6hnRcfC3.png?1526475673
   :width: 206px
   :height: 250px

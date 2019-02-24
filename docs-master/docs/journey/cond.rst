.. include:: /common/global.rst

Conditions and expressions
==========================

|acquia-product:aj| uses expressions extensively in business logic and
for conditional branches in graphs. Each expression can be defined in
one of two ways: *Basic* or *Advanced*. Both of these techniques
generate a JavaScript expression that is evaluated for truthfulness.

Basic expressions
-----------------

Basic expressions provide a list of common expressions which are
available to be used.

+-----------------+-----------------+-----------------+-----------------+
| Basic           | Arguments       | Equivalent      | Note            |
| Expression      |                 | JavaScript      |                 |
+=================+=================+=================+=================+
| **Is True**     | None            | ``VAL === true` |                 |
|                 |                 | `               |                 |
+-----------------+-----------------+-----------------+-----------------+
| **Is False**    | None            | ``VAL === false |                 |
|                 |                 | ``              |                 |
+-----------------+-----------------+-----------------+-----------------+
| **Less Than or  | Constant Value  | ``VAL <= 12.3`` |                 |
| Equal To**      | - numeric or    |                 |                 |
|                 | string          |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| **Greater       | Constant Value  | ``VAL > 12.3``  |                 |
| Than**          | - numeric or    |                 |                 |
|                 | string          |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| **Greater Than  | Constant Value  | ``VAL >= 12.3`` |                 |
| or Equal To**   | - numeric or    |                 |                 |
|                 | string          |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| **Equals**      | Constant Value  | ``VAL == {...}` |                 |
|                 | - number,       | `               |                 |
|                 | string, or      |                 |                 |
|                 | boolean         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| **Not Equal     | Constant Value  | ``VAL != {...}` |                 |
| To**            | - number,       | `               |                 |
|                 | string, or      |                 |                 |
|                 | boolean         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| **Contains**    | Constant String | ``VAL.indexOf(' | Case-sensitive  |
|                 |                 | abc') > -1``    | — see           |
|                 |                 |                 | `Case-insensiti |
|                 |                 |                 | ve              |
|                 |                 |                 | expressions <#c |
|                 |                 |                 | ase-insensitive |
|                 |                 |                 | >`__            |
+-----------------+-----------------+-----------------+-----------------+
| **Starts With** | Constant String | ``VAL.indexOf(" | Case-sensitive  |
|                 |                 | abc") === 0``   | — see           |
|                 |                 |                 | `Case-insensiti |
|                 |                 |                 | ve              |
|                 |                 |                 | expressions <#c |
|                 |                 |                 | ase-insensitive |
|                 |                 |                 | >`__            |
+-----------------+-----------------+-----------------+-----------------+
| **Ends With**   | Constant String | ``VAL.lastIndex | Case-sensitive  |
|                 |                 | Of("abc") === V | — see           |
|                 |                 | AL.length - "ab | `Case-insensiti |
|                 |                 | c".length``     | ve              |
|                 |                 |                 | expressions <#c |
|                 |                 |                 | ase-insensitive |
|                 |                 |                 | >`__            |
+-----------------+-----------------+-----------------+-----------------+

Advanced expressions
--------------------

Advanced expressions are any valid boolean JavaScript (ECMAScript 5)
expressions. The JavaScript variable ``VAL`` is available and is set to
the value of the previous node when used as an expression on a
conditional branch.

If the basic expressions do not have the type of operator that you
require, the advanced mode should allow you to program your own
condition. To access the advanced mode, in the **Type** list, click
**Conditional**, select **Advanced**.

The following examples are available for your use:

+-----------------------------------+-----------------------------------+
| Description                       | JavaScript                        |
+===================================+===================================+
| Membership of a list. Test to see | ``['worda', 'wordb', 'wordc'].ind |
| if the returned value is in a     | exOf(VAL) >= 0``                  |
| list of values.                   |                                   |
+-----------------------------------+-----------------------------------+
| Determine whether or not a        | ``Object.keys(obj).length === 0 & |
| javascript object is empty        | & obj.constructor === Object``    |
+-----------------------------------+-----------------------------------+

.. note::   JavaScript has the following outcomes when comparing against ``null``:

            -  Evaluates as TRUE - ``null >= 0``
            -  Evaluates as TRUE - ``null <= 0``
            -  Evaluates as FALSE - ``null == 0``
            -  Evaluates as TRUE - ``+null == 0``

Case-insensitive expressions
----------------------------

The basic conditions ``Contains``, ``StartsWith``, and ``EndsWith`` are
case-sensitive. For example, the string ``dog`` would not match the
string ``DOG``.

To create a case-insensitive condition `in an existing
graph </journey/getting-started/graph>`__, create an Advanced Expression
on the branch, and use the JavaScript ``toLowerCase()`` function using
these steps:

|Example graph|

#. *Create your **Set** node*

   #. Right-click in the background of your graph, and then click **Add
      Node to Graph**.
   #. Scroll to the **Basic Nodes** section, and then double-click
      **Set** to add it to your graph.
   #. Click the **Set** node to select it.
   #. In the sidebar, scroll to the **Edit Set Node** panel, and then
      define the node's value as a child value in your schema.

#. *Create your **Get** node*

   #. Right-click in the background of your graph, and then click **Add
      Node to Graph**.
   #. Scroll to the **Basic Nodes** section, and then double-click
      **Get** to add it to your graph.
   #. Link the **Set** and **Get** nodes together with a **Goto**.
   #. Click the **Get** node to select it.
   #. In the sidebar, scroll to the **Edit Get Node** panel, and then
      define the value to ``GET`` that value from your schema.

#. *Create your **Return False** node*

   #. Right-click in the background of your graph, and then click **Add
      Node to Graph**.
   #. Scroll to the **Basic Nodes** section, and then double-click
      **Return** to add it to your graph.
   #. Link the **Get** and **Return False** nodes together with a
      **Goto**.

#. *Create your **Return True** node*

   #. Right-click in the background of your graph, and then click **Add
      Node to Graph**.
   #. Scroll to the **Basic Nodes** section, and then double-click
      **Return** to add it to your graph.
   #. Link the **Get** and **Return True** nodes together.
   #. Click the link between your **Get** and **Return True** nodes
      (currently **Goto**). In the sidebar, scroll to the **Edit Link**
      panel.
   #. In the **Type** section, click **Conditional**.
   #. For **Link Operation**, click **Advanced**, and then paste the
      following code into the code evaluation window, altering the code
      to match your variable's name:

      ``VAL.toLowerCase().indexOf("dog") > -1``

The code in the **Return True** node converts ``VAL`` to lower case, and
then looks for the starting position in the search string ``dog``. If it
finds ``dog`` anywhere in that ``VAL``, it will return true.

.. |Example graph| image:: https://cdn3.webdamdb.com/1280_Is7pZ0Dyu9F6.png?-62169955200
   :width: 550px
   :height: 296px

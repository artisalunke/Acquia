.. include:: /common/global.rst

Creating a graph
================

.. toctree::
   :hidden:
   :glob:

   /journey/getting-started/graph/*

A graph is a series of nodes, connected by links, that execute their
steps in a predictable fashion. Each node in the graph is an
`adaptor </journey/adaptors>`__, which is a either piece of business
logic or another graph. A graph will always have a start node and must
finish with a `return node </journey/node/return>`__; otherwise, the
graph `will not be valid <#validation>`__.

|acquia-product:aj| describes the executable pieces as *graphs* because
they are `Directed Acyclic
Graphs <https://en.wikipedia.org/wiki/Directed_acyclic_graph>`__, which
are executed by the proprietary |acquia-product:aj| graph engine. Each
graph contains `nodes </journey/node>`__, including temporary
placeholder nodes called `ghost nodes <#ghost>`__, connected by
`links <#links>`__. A graph may have a `listener <#listening>`__
attached or receive `parameters <#parameters>`__ when called from
another graph.

The following example graph has three nodes: a `Columnar
Table </journey/node/columnar-table>`__ and two `Return
Nodes </journey/node/return>`__.

|Journey Graph|

The graph also has two `links <#links>`__: a Goto link and an Error
link. The first node in the graph has an attachment on its left-hand
side; this attachment can be moved to any node in the graph to make it
the first node.

To learn more about working with graphs in |acquia-product:aj|, refer to
the following sections:

-  `Creating a graph <#create>`__
-  `Managing a listener adaptor <#managelisten>`__
-  `Managing parameters <#manageparam>`__
-  `Editing a link <#link>`__

.. note::
  Although |acquia-product:aj| supports `versioning for your entire
  project </journey/admin/version>`__, there is no versioning support at
  the graph level.

Parameters and listeners
------------------------

A graph may optionally receive parameters or listen with an adaptor, but
not both.

Listening adaptors
~~~~~~~~~~~~~~~~~~

Graphs can have special starting nodes, called *listening adaptors*,
which denote where and how data will be picked up to be put into the
graph. Listeners are always displayed in the top left-hand part of the
graph window. The following listener types are supported:

-  `Database </journey/adaptors/database/listen>`__ - Process a queue of
   items from a database table
-  `Queue </journey/adaptors/message/listen>`__ - Process messages
   arriving in a message queue
-  `Twitter </journey/adaptors/twitter/listen>`__ - Process Twitter
   stream items, such as hashtags, keywords, or direct messages
-  `Graph API </journey/adaptors/graph-api>`__ - Allow other systems to
   interact with your graph

Parameters
~~~~~~~~~~

When called from another graph, a graph may receive parameters, which
allow you to reuse business logic with different input values. When the
graph is executed, the schema location for each parameter is populated
by the graph that called it. Because the value is copied to the schema
location, modifications of the value from the called graph will not
modify the value known to the calling graph.

Links
-----

The graph is traversed by executing each node in order and following the
appropriate link, based on the result, to the next node. The links
between nodes denote how the data flows, and are traversed in the
following order of priority:

-  *Error* - Executed if the node does not execute correctly
-  *Conditional* - Executed if a conditional expression returns ``True``
-  *Goto* - Executed if none of the error or confitional conditions are
   met

Ghost nodes

|Ghost node icon|\ Nodes with no information, known as `ghost
nodes </journey/node/ghost>`__, are displayed with grey boxes in your
graph. For your graph to validate, all ghost nodes must be replaced with
nodes containing valid information.

Graph validation
----------------

A graph will execute only if all of the following conditions are true:

-  No ghost nodes
-  No ghost links
-  All nodes have their inputs and outputs mapped to data sources
-  At least one return node exists

With all of the previous conditions satisfied, the Graph Editor window
will display the **Valid Graph** indicator.

|Valid graph|

Graphs with validation warnings will display a validation warning icon.

|Validation warning icon|

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Note                              |
+===================================+===================================+
| **Graph does not have a return    | Every graph must have at least    |
| node**                            | one return node.                  |
+-----------------------------------+-----------------------------------+
| **Graph contains ghost nodes**    | Before a graph can be executed    |
|                                   | all ghost nodes (displayed in     |
|                                   | grey) need to be replaced with    |
|                                   | executable node types. The number |
|                                   | in parentheses indicates how many |
|                                   | ghost nodes there are.            |
+-----------------------------------+-----------------------------------+
| **Graph contains ghost links**    | Before a graph can be executed    |
|                                   | all links must be one of          |
|                                   | Conditional, Error or Goto. Click |
|                                   | the highlighted links to set the  |
|                                   | type of the link. The number in   |
|                                   | parentheses indicates how many    |
|                                   | ghost links there are.            |
+-----------------------------------+-----------------------------------+

.. _creating-a-graph-1:

Creating a graph
----------------

To create a blank graph in `an existing
project </journey/getting-started/project>`__, perform the following
actions:

#. Sign in to |acquia-product:aj|.
#. On the **Home Screen**, identify the project you want to customize.
#. Find the project's tile, and then click its Project Editor icon
   |Project Editor icon|.
#. In the top left of the page, click the action menu icon |Action
   menu|.
#. Click **Create New**.
#. In the **Graphs** box, click **Blank** to select a blank graph.
#. In the **Name** text field, enter a name for your graph.
#. At the bottom of the page, click **Create New Item**.

.. note::
  For information about creating a graph from a template, see `Using a
  graph template </journey/getting-started/graph/template>`__.

Adding a new node to your graph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add a new node to the graph you are currently editing, use one of the
following methods:

-  *From an existing node:*

   #. Point to an existing node (except a `return
      node </journey/node/return>`__) to display a grab arrow.
   #. Drag and drop the grab arrow to an empty area of the window to
      create a new ghost node with a *goto* link to the previous node.

      |Add another node|

-  Right-click anywhere in the graph, and then click **Add Node to
   Graph** to create a new node.

Deleting a node from a graph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To delete a node from the graph you are editing, right click the node,
and then click **Delete Node**. |acquia-product:aj| will also remove any
links associated with the node. Links can be moved separately by
selecting the connection point of the link, and then moving the link to
a new node.

Moving nodes in a graph
~~~~~~~~~~~~~~~~~~~~~~~

Nodes will generally snap to a grid if moved individually. Many nodes
can be moved at once by creating a rubber-band selection around the
nodes, and then selecting the grey background to move all of the nodes
simultaneously:

|Move a group of nodes|

Replacing ghost nodes

To replace a ghost node with a valid node, perform the following
actions:

#. Use one of the following methods to select the node:

   -  Double-click the ghost node.
   -  Right-click the node, and then click **Replace Node**.

   |acquia-product:aj| will display a **Replace Node** dialog box.
#. Select a replacement node.

For more information about the different node types, read about `Nodes
in |acquia-product:aj| </journey/node>`__.

Managing a listener adaptor
---------------------------

You can add or remove a listener adaptor from your graph.

Adding a listener adaptor
~~~~~~~~~~~~~~~~~~~~~~~~~

To add a listener adaptor to your graph, complete the following steps:

#. At the top of the graph, click **Add Listener**.
#. In the **Listener Type** list, click the type of listener that you
   want to add.
#. Complete the configuration for your chosen `listener adaptor
   type <#listening>`__.
#. Click **Save**.

Removing a listener adaptor
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To remove a listener adaptor from your graph, complete the following
steps:

#. At the top of the page, click the **Remove** icon.
   |acquia-product:aj| will display a **Remove Listener** dialog box.
#. Click **Yes, Remove Listener**.

Managing parameters
-------------------

You can add, modify, and delete individual parameters from your graph or
remove all parameters.

Adding parameters
~~~~~~~~~~~~~~~~~

To add parameters, when editing a graph complete the following steps:

#. Click **Add Parameters** at the top of the graph window to display
   the **Parameters** dialog box.
#. For each parameter that you want to add, click **Add Parameter**, and
   then enter a name for your new parameter.
#. Click the arrow icon |Left arrow| to the right of your parameter, and
   then select the schema location to obtain the parameter from when the
   graph is called.
#. When you are finished, click the close icon |Close dialog box icon|
   for the dialog box.

Modifying or deleting a parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To modify or delete a parameter, when editing a graph complete the
following steps:

#. Click **Edit** at the top of the page.
#. Make any necessary changes:

   -  To delete a parameter, click the trashcan icon |Trashcan icon| to
      the left of the parameter name.
   -  To modify a parameter's schema location, click the arrow icon
      |Left arrow| to the right of the parameter name, and then choose a
      new schema location.

#. When you are finished, click the close icon |Close dialog box icon|
   for the dialog box.

Removing all parameters
~~~~~~~~~~~~~~~~~~~~~~~

To remove all parameters from your graph, complete the following steps:

#. Click **Remove** at the top of the page.
   |acquia-product:aj| will display a **Delete Item** dialog box.
#. Click **Yes, Delete Item** to remove all parameters from your graph.

Editing a link
--------------

To edit a link between nodes, click the arrow between the nodes. The
**Edit Link** panel will appear on the right side of the page. In the
**Edit Link** panel, you can set the type of link (*Error, Conditional,*
or *Goto*), and if your link needs more explanation, provide an
alternative **Description**.

Using a *Conditional* link, you must specify an expression under the
**Link Operation** section of the **Edit Link** panel. The condition
expression is any valid JavaScript expression. The value of the
preceding node is automatically populated into the variable ``VAL``.
Common expressions include:

-  *String equality* - ``VAL === "My String Value"``
-  *Numeric equality* - ``VAL == 6``

For additional examples, see the reference section of `Conditions and
expressions </journey/cond>`__.

.. |Journey Graph| image:: https://cdn4.webdamdb.com/1280_Xl0ylAgSt79.png?1526475559
   :width: 321px
   :height: 281px
.. |Ghost node icon| image:: https://cdn2.webdamdb.com/1280_trDxMb5gLp16.png?1526475851
   :class: logo-pp no-sb
   :width: 64px
   :height: 78px
.. |Valid graph| image:: https://cdn4.webdamdb.com/1280_c5UQQAvyKW75.png?1526475653
   :class: no-sb
   :width: 185px
   :height: 40px
.. |Validation warning icon| image:: https://cdn4.webdamdb.com/1280_gkXv6WOP9J10.png?1526475606
   :class: no-sb
   :width: 188px
   :height: 41px
.. |Project Editor icon| image:: https://cdn3.webdamdb.com/1280_Qx24aCvtr211.png?1526475782
   :class: no-sb
   :width: 30px
   :height: 30px
.. |Action menu| image:: https://cdn3.webdamdb.com/1280_ksdoaWdShDr2.png?1526476127
   :class: no-sb
   :width: 30px
   :height: 30px
.. |Add another node| image:: https://cdn2.webdamdb.com/1280_AHsGmkAtM912.jpg?1526475799
   :width: 392px
   :height: 112px
.. |Move a group of nodes| image:: https://cdn3.webdamdb.com/1280_I2F0W7I3vwt0.png?1526476043
   :width: 500px
   :height: 257px
.. |Left arrow| image:: https://cdn2.webdamdb.com/1280_UyxLBHlcGQ68.png?1526475469
   :class: no-sb
   :width: 27px
   :height: 26px
.. |Close dialog box icon| image:: https://cdn2.webdamdb.com/1280_rtaumdfmL28.png?1526475455
   :width: 26px
   :height: 26px
.. |Trashcan icon| image:: https://cdn2.webdamdb.com/1280_Qrx3lTnyDqi4.png?1526475511
   :class: no-sb
   :width: 26px
   :height: 26px

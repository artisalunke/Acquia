.. include:: /common/global.rst

Loop node
=========

|Loop node|

The Loop node allows a sub-graph to be executed many times from the same
position in a graph.

To use a loop node you will need a schema location that typically
contains a JavaScript array and a graph to process each element in the
array.

|Loop Node example|

The loop node will call the graph once for each entry in the array
sequentially. If the data provided to the loop node is not a JavaScript
array it will be converted into an array of length one. Arrays can often
be returned by web services or database end points.

Creating a Loop Node
--------------------

Unlike other node types, Loop Nodes can only be added directly `from an
existing graph </journey/getting-started/graph>`__, and not through the
**New** menu option. To add a Loop Node to a graph:

#. On the **Home Screen**, identify the project you want to customize.
#. In the project's tile, click the **Project Editor** |Project Editor
   icon| icon.
#. Double-click the graph you want to edit.
#. In the white background of the Graph, right-click and choose **Add
   Node to Graph**.
#. Scroll down to the **Basic Nodes** section, and click **Loop**.
#. Click **Add Loop**.
#. In the right-hand sidebar, scroll to the **Edit Loop Node** panel and
   click the **Expand** |Expand| icon.
#. In the fields provided, define your sources.
#. Click **Replace Node**.

In this example graph the schema location ``loopData`` is being used,
and the ``loopData`` location is set to this value in the Set Node
below:

``[{"val":"a"},{"val":"b"},{"val":"c"}]``

|Loop Node example|

The sub-graph just returns the 'val' attribute of the object:

|Return value icon|

The graph shows one transaction executing but the testing console will
show the iterations of the loop node and the Display JSON button will
show the state of the data store at the end of that iteration. The
output of the subgraph can be seen in each transaction as the loop node
iterates over the array.

Notes
-----

-  A loop node graph can not call itself and the graph will not appear
   on the Using Graph dropdown
-  The loop node processes the array sequentially and the graph state is
   global so that changes to the schema or a public variable in one
   sub-graph will be available to the next sub-graph

Another Example
---------------

This example will loop through an array of words and concatenate them
together into one sentence. Each time the loop runs it will concatenate
the next word onto the previous words slowly building the sentence. It
will return 'true' each loop and at the end the entire sentence will be
in one schema location.

This is the array of words:

``["The","quick","brown","fox","jumps","over","the","lazy","dog."]``

The set node below sets a schema location with this array of words which
is then used in the loop node.

|Loop Node location|

These are the two graphs. The upper picture is the main graph and the
bottom picture is the graph the loop runs with. The JavaScript node's
output is stored in a separate schema location compared to where the
words are stored, the code is shown below along with the testing console
output.

|Loop Node code example|

The following screenshot shows each loop returning 'true' instead of any
value.

|Loop Node returns true|

The following screenshot shows the final result of the graphs.

|Loop Node final result|

The array of words is stored in the ``data`` portion of the schema while
the built sentence is stored in the ``result`` part of the schema, both
under the ``aLoopExample`` section.

.. |Loop node| image:: https://cdn3.webdamdb.com/1280_UUrX7RLK6y73.png?1526475471
   :class: no-sb float-left logo-sm-lift
.. |Loop Node example| image:: https://cdn3.webdamdb.com/1280_otbT3Zjrcw52.png?1526475981
   :width: 638px
   :height: 218px
.. |Project Editor icon| image:: https://cdn4.webdamdb.com/100th_sm_YcVG2zY8pZL5.png?1526475783
   :width: 33px
   :height: 29px
.. |Expand| image:: https://cdn4.webdamdb.com/1280_2JkCGJsHGM10.png?1526475741
   :width: 34px
   :height: 32px
.. |Return value icon| image:: https://cdn4.webdamdb.com/1280_plE5ZHhaEj34.png?1526475896
   :width: 205px
   :height: 167px
.. |Loop Node location| image:: https://cdn3.webdamdb.com/1280_EUYZ1O6Ia0g4.png?1526476094
   :width: 381px
   :height: 273px
.. |Loop Node code example| image:: https://cdn4.webdamdb.com/1280_2vv1r6uNdlK3.png?1526475766
   :width: 304px
   :height: 134px
.. |Loop Node returns true| image:: https://cdn4.webdamdb.com/1280_g3OJtir8oDu8.png?1526475816
   :width: 650px
   :height: 320px
.. |Loop Node final result| image:: https://cdn4.webdamdb.com/1280_LBnDSp29ej71.png?1526476144
   :width: 550px
   :height: 281px

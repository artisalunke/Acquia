.. include:: /common/global.rst

Testing a graph
===============

|acquia-product:aj| allows you to test graphs and
`nodes </journey/node>`__ interactively prior to deployment. This allows
you to test a graph with defined test cases. The **Project Editor** with
the testing console expanded is displayed below:

|Journey testing console|

Only a valid graph can be tested. You can validate a graph by clicking
the **Validate** link at the top right of the graph canvas. If the graph
is valid, the **Valid Graph** icon is displayed. If the graph is not
valid, you must fix the validation error before the testing console can
be used. For more information on troubleshooting errors, read the
|troubleshooting|_.

.. |troubleshooting| replace:: \ |acquia-product:aj| \ troubleshooting guide
.. _troubleshooting: /journey/troubleshooting

Testing console
---------------

The testing console is available at the bottom of the graph window. It
is displayed below, collapsed:

|Testing console|

The testing console provides insight into both the execution of each
step in the graph, as well as the state of the `data store and public
variables </journey/data>`__ at the end of the graph's execution. To
access the testing console for your graph, complete the following steps:

#. Sign in to |acquia-product:aj|.
#. On the main project page (accessible by clicking the
   |acquia-product:aj| logo in the top menu), find the project that you
   want to modify, and click its **Project Editor** |Project Editor
   icon| icon.
#. Select the graph you want to test, and then click **Open** at the
   bottom of the panel.
#. Click the **Arrow** |Maximize| icon to expand the testing console.

The testing console provides the following controls:

+-----------------------------------+-----------------------------------+
| Control                           | Description                       |
+===================================+===================================+
| |Start|                           | Starts the graph engine and       |
|                                   | displays the **Testing Settings** |
|                                   | dialog. The control is disabled   |
|                                   | when the graph is executing, and  |
|                                   | is available only for valid       |
|                                   | graphs.                           |
+-----------------------------------+-----------------------------------+
| |Stop|                            | Stops the execution of the        |
|                                   | current graph. When the graph is  |
|                                   | executing, this control is green; |
|                                   | when not executing, it is gray.   |
+-----------------------------------+-----------------------------------+
| |Clear Logs|                      | Clears the testing console and    |
|                                   | removes information from all      |
|                                   | previous runs.                    |
+-----------------------------------+-----------------------------------+
| |Maximize| |Minimize|             | Maximizes or minimizes the        |
|                                   | testing console. The console can  |
|                                   | also be enlarged or shrunk by     |
|                                   | grabbing the bar between the      |
|                                   | graph window and the console and  |
|                                   | moving it up or down.             |
+-----------------------------------+-----------------------------------+

Testing settings
----------------

To configure your test settings, click **Start**. The test configuration
varies based on whether your graph has a listener attached or not:

-  *If your graph does not have a listener attached,* you will see the
   **Test Settings** dialog below:

   |Standard graph test|

-  *If your graph has a listener attached,* you will see the **Test
   Settings** dialog below:

   |Graph with listener test dialog|

In the **Data (JSON)** section, you can include a valid JSON payload,
such as from the execution of another graph.

If the graph `has a
listener </journey/getting-started/graph#listening>`__, the **Testing
Settings** dialog box includes three mutually exclusive modes of testing
the graph:

-  **Iterations** - Graph executes until the specified number of
   iterations has occurred.
-  **Duration** - Graph executes until the number of seconds has
   elapsed.
-  **Data** - Graph executes a single time with the specified data
   payload.

|Graph with listener test|

During visual testing, graph execution is limited to prevent interactive
graphs from locking up engines unnecessarily:

-  **Maximum number of iterations** - 1,000
-  **Duration** - Maximum runtime of any graph is 30 minutes

Testing console output
----------------------

The testing console will display **Running** if the graph is a listener,
and then display **Finished** if the graph is not a listener.

To view the console output, you must click the **expand**
|journey-console-expand-node.png| icon in the **Test Console**. For each
transaction, click the **expand** |journey-console-expand-node.png| icon
to display the execution details for that transaction. Each transaction
displays a row for every graph node. The final two rows display **Total
Elapsed Time** and **Data Store Values**, respectively. The most recent
execution of the graph will always be appended to the end of the
**Testing Console** log. An example of the **Testing Console** output is
displayed below:

|Testing console output|

The testing console displays the following information for every node
executed in a transaction:

-  Name of the node and, if it is an adaptor, its
   `type </journey/node>`__
-  Execution time (usually in milliseconds)
-  Return value of the node

In addition, after a transaction completes, the **Total Elapsed Time**
is reported.

You can examine the **Data Store Values** after a transaction completes
by clicking the **expand** |journey-console-expand-node.png| icon next
to each value you want to display. You can examine the entire data
schema by clicking **Expand All**. If you want to copy some or all of
the data schema, click **Display JSON** to open a dialog with the schema
in JSON format.

If an error occurs with one of your nodes during execution of a
transaction, the row of the offending node is displayed highlighted in
orange in the **Testing Console**. An example with detail of the error
message from the engine is displayed below:

|Testing console error output|

If the graph is a `listener </journey/adaptors/graph-api>`__ and there
are multiple iterations, pointing to a transaction will indicate its
path on the graph by highlighting the path with an orange highlight.

.. |Journey testing console| image:: https://cdn2.webdamdb.com/1280_E8kT6aeogCH6.png?1526475982
   :width: 923px
   :height: 625px
.. |Testing console| image:: https://cdn4.webdamdb.com/1280_kNZrCXdHFG20.png?1526475945
   :width: 933px
   :height: 37px
.. |Project Editor icon| image:: https://cdn4.webdamdb.com/100th_sm_YcVG2zY8pZL5.png?1526475783
   :width: 33px
   :height: 29px
.. |Maximize| image:: https://cdn4.webdamdb.com/1280_gj1Ff2rk2K12.png?1526476041
   :width: 32px
   :height: 22px
.. |Start| image:: https://cdn2.webdamdb.com/1280_EAAFLrRF8RQ1.png?1526476024
   :width: 73px
   :height: 22px
.. |Stop| image:: https://cdn3.webdamdb.com/1280_AJGZtTpTAu55.png?1526476085
   :width: 71px
   :height: 22px
.. |Clear Logs| image:: https://cdn3.webdamdb.com/1280_ouZQLPnzbTz5.png?1526475624
   :width: 109px
   :height: 22px
.. |Minimize| image:: https://cdn2.webdamdb.com/1280_6Tfnl6bst211.png?1526475625
   :width: 32px
   :height: 22px
.. |Standard graph test| image:: https://cdn4.webdamdb.com/1280_Qj2fYYMQKl61.png?1526475581
   :width: 598px
   :height: 379px
.. |Graph with listener test dialog| image:: https://cdn4.webdamdb.com/1280_UnBavduqlfX2.png?1526475519
   :width: 528px
   :height: 250px
.. |Graph with listener test| image:: https://cdn2.webdamdb.com/1280_UjKlxjyCSIB5.png?1526475608
   :width: 545px
   :height: 250px
.. |journey-console-expand-node.png| image:: https://cdn3.webdamdb.com/1280_AnozUjdM4k72.png?1526475997
   :width: 24px
   :height: 24px
.. |Testing console output| image:: https://cdn3.webdamdb.com/1280_Yk3jSb3a48e1.png?1526476087
   :width: 798px
   :height: 250px
.. |Testing console error output| image:: https://cdn2.webdamdb.com/1280_EP6A6tQ3S3E0.png?1526475932
   :width: 893px
   :height: 233px

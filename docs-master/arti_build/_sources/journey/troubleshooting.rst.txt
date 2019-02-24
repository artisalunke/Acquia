.. include:: /common/global.rst

|acquia-product:aj| troubleshooting guide
=========================================

There are many methods for debugging business logic and adaptors
throughout |acquia-product:aj| Hub. While most error messages are very
self explanatory, some issues are not as obvious. As a general rule, one
should have a test-driven development plan for building graphs in
|acquia-product:aj| Hub. Implementing such a plan means that every
adaptor and every graph should have a unit test case and every process
should utilize a tool such as Postman to send test data to test end
points and processes. By having this plan from the start, it will make
any troubleshooting and debugging much simpler to do, as you can quickly
refer to already written test cases to test your graph as you develop
the logic and integrations.

.. note:: |acquia-product:aj| does not provide log files for graph executions.

On this page, you will find a general guideline of how to move from the
high-level to the granular-level in identifying the issue, debugging it,
and then testing it. To do so, we will start with running tests in the
admin page and gradually move towards running tests in the graph.

Testing adaptors in the Admin page
----------------------------------

One of the first things to determine is whether or not the service you
are integrating with is still successfully connected. To do so, go to
the Admin page, select the connection that you want to test, and then
click **Test Connection**. This will cause |acquia-product:aj| to
indicate if the adaptor was tested successfully, or not. If the test
runs successfully, it may not be an issue with the connection, in which
case one would proceed to look at the graph instead.

If the connector fails to run a test for a database adaptor, more often
than not, it is due to a change in the password. If the connector fails
on a queue adaptor, it may be an issue with a name mismatch of the queue
assigned or an incorrect password.

Debugging in the graph
----------------------

If the admin page tests successfully, the next thing to look at is
running the graph and looking at the JSON as the record progresses
through the graph. To test the graph, there are generally two ways to go
about it:

-  Using test data that will get picked up by the listener
-  Using mock JSON data to send into the graph.

As a rule of thumb, one could start testing the graph using test data
picked up by the listener, and then use that resulting JSON to test
particular sections of the graph or individual nodes after identifying
the incriminating node.

+-----------------------+-----------------------+-----------------------+
| Method                | Pro                   | Con                   |
+=======================+=======================+=======================+
| Using test data that  | -  Enables end-to-end | -  Cannot test the    |
| will get picked up by |    testing to send    |    output of an       |
| the listener          |    data from one end  |    individual node    |
|                       |    of the process to  | -  Forced to test the |
|                       |    the other          |    entire graph from  |
|                       | -  Can test multiple  |    the start node to  |
|                       |    nodes in one go to |    the point of error |
|                       |    pin-point which    |                       |
|                       |    general area of    |                       |
|                       |    nodes is           |                       |
|                       |    performing the     |                       |
|                       |    incorrect action   |                       |
|                       | -  Can display the    |                       |
|                       |    json at the end of |                       |
|                       |    each subgraph to   |                       |
|                       |    see if the JSON is |                       |
|                       |    what's expected    |                       |
+-----------------------+-----------------------+-----------------------+
| Using mock data to    | -  Can see if the     | -  More tedious as it |
| test an individual    |    output of each     |    requires a lot of  |
| node                  |    node one at a time |    manual changing in |
|                       |    before it gets     |    the JSON data      |
|                       |    passed to the next | -  Does not           |
|                       |    node or subgraph,  |    constitute as end  |
|                       |    providing a more   |    to end testing     |
|                       |    granular view of   |                       |
|                       |    the record         |                       |
|                       | -  Good for quickly   |                       |
|                       |    testing a single   |                       |
|                       |    node, debugging    |                       |
|                       |    and retesting      |                       |
|                       |    until the node     |                       |
|                       |    works as expected  |                       |
|                       | -  Gives you the      |                       |
|                       |    flexibility to     |                       |
|                       |    test the graph     |                       |
|                       |    from any starting  |                       |
|                       |    point              |                       |
+-----------------------+-----------------------+-----------------------+

After the faulting node has been discovered, depending on the type of
node it is, there are different ways to debug the problem and resolve
the issue. If the node is having a validation error, check that it is
pointing to the correct connection string in the right environment. If
that is correct, visit that node's wiki page to see its common error
messages and possible solutions.

.. important::
  After debugging the issue, remember to do regression testing on the
  entire graph to ensure that no new issues were introduced.

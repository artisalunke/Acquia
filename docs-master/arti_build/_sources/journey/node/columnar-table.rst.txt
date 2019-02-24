.. include:: /common/global.rst

Columnar Table node
===================

|Columnar Table node|

The Columnar Table node allows complex decisions with multiple inputs
and outputs to be created easily. Essentially, it is a visual interface
that can hold many if-then-else statements in one place to evaluate
rules and make decisions.

The columnar table is commonly used across processes that are used to
filter records through exclusion logic or decide what kind of content a
person is going to receive in a tweet, email, or personalized web
experience. As the columnar table is a generic piece of logic, it has a
wide range of uses and applications.

General Usage
-------------

-  In the columnar table, each column is called a *decision*, each row
   is called a rule (for example, **input**), and each row after the
   results row is called a *result* (for example, **output**).
-  Columnar tables are particularly good for the circumstances where you
   may have a large number of input fields, but the combination of
   decisions is quite sparse compared to the number of combinations. It
   is good practice to have a catch-all rule where all rules are blank
   (and hence true) to ensure that a result is always generated.
-  All decisions are evaluated left-to-right and the rules in a decision
   are evaluated from top-to-bottom.
-  A blank rule will accept any input and will always return true.
-  Each decision if evaluated to true can be used to set multiple output
   results.
-  The first rule where all rules are true is the decision and any
   decision that is placed after will not be evaluated. Hence, it is
   always best to have your strictest decisions on the left.

|Columnar table example|

Creating a columnar table
-------------------------

To create a columnar table, perform the following actions:

#. Sign in to your |acquia-product:aj| interface.
#. Identify the project you wish to modify.
#. Click the **Project Editor** |Project Editor icon| icon.
#. In the top left-hand corner of the screen, click the **Action Menu**
   |Action Menu icon| icon.
#. Select **+ Create New** from the list.
#. Enter the name of your new Columnar Table node in the **Name** field.
#. Scroll through the list of node types to find the **Logic** section,
   and click **Columnar Table**:
   |Logic node type listing|
#. Click **Create New Item**.
#. Use the **Add Column** and **Add Row** buttons to construct your data
   matrix.
#. Click **Save**.

The columnar table starts out blank:

|Blank columnar table example|

Adding decisions
~~~~~~~~~~~~~~~~

New decisions can be added by clicking **Add Decision**, which will
prompt you for the column name to display at the top of the table. After
assigning a name to the decision, the name will appear in the first
empty column to the right of **Add Decision**:

|First decision added|

Adding rules for evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

After adding a decision, you can add rules to be evaluated by performing
the following steps:

#. Click the **Plus** |Plus icon| icon next to **Rules**.
#. In the pop-up window, provide a **Rule Name** and click **Add**.
#. Point your mouse to the white, open intersection between your
   decision and your rule, and click in the empty space, turning it
   blue:
   |Select the intersection|
#. In the right-hand side of the page, scroll to the **Edit Rule** pane
   and click the **Expand** |Expand icon| icon.
#. Optionally, provide a description for your rule.
#. Click to select **Basic** or **Advanced** for your rule operation.
#. Add in the conditions for your rule (examples below) and click **Save
   Changes To Rule**.

Two examples of using rules evaluating whether or not a customer has
opted-in for email communications, one using the **Basic** operation and
one using the **Advanced** operation:

|Example of Basic operation| |Example of Advanced operation|

Adding results
~~~~~~~~~~~~~~

After a decision, a rule, and evaluation logic have been created, add
the results to generate the desired outputs if a decision evaluates to
``TRUE``:

#. Click the **Plus** |Plus icon| icon next to **Results**.
#. Provide a **Result Name** and click **Add**.
#. Point your mouse to the white, open intersection between your
   decision and your result, and click in the empty space, turning it
   blue.
#. In the right-hand side of the page, scroll to the **Edit Result
   Value** pane and click the **Expand** |Expand icon| icon.
#. The value for the result can be a literal value, a schema location or
   a public variable.
#. Clicking in the result box for that decision will show the current
   value in the Edit Result Value and Schema, Literal or Public Variable
   chooser.

For each characteristic created, a data source must be added in the list
of parameters outside of the node at the graph level.

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **A columnar table must have at   | No decision columns have been     |
| least one column**                | created. Use **Add Decision** to  |
|                                   | add a decision column.            |
+-----------------------------------+-----------------------------------+
| **A columnar table must have at   | A decision column has been        |
| least one rule**                  | created but no rule has been      |
|                                   | added to the table.               |
+-----------------------------------+-----------------------------------+

Errors
------

-  ``ColumnarTable unable to find value for rule with this data source``
   - the incoming data did not contain the expected value in the schema
   or public variable.

.. |Columnar Table node| image:: https://cdn4.webdamdb.com/1280_QAhUZIYTapX2.png?1526475710
   :class: no-sb float-left logo-sm-lift
   :width: 51px
.. |Columnar table example| image:: https://cdn2.webdamdb.com/1280_233ZrrLHsrp0.png?1526475958
   :width: 550px
   :height: 345px
.. |Project Editor icon| image:: https://cdn4.webdamdb.com/100th_sm_YcVG2zY8pZL5.png?1526475783
   :width: 33px
   :height: 29px
.. |Action Menu icon| image:: https://cdn3.webdamdb.com/100th_sm_Aa8wvVef08x7.png?1526475662
   :width: 26px
   :height: 22px
.. |Logic node type listing| image:: https://cdn3.webdamdb.com/1280_kfNiX7lNWL28.png?1526475881
   :width: 377px
   :height: 116px
.. |Blank columnar table example| image:: https://cdn3.webdamdb.com/1280_QqKDaHBQOWa0.png?1526475768
   :width: 163px
   :height: 158px
.. |First decision added| image:: https://cdn2.webdamdb.com/1280_YGsVjAlr2qp2.png?1526476142
   :width: 318px
   :height: 163px
.. |Plus icon| image:: https://cdn4.webdamdb.com/1280_kbmc0O5OMt91.png?1526475736
   :width: 25px
   :height: 22px
.. |Select the intersection| image:: https://cdn4.webdamdb.com/1280_ABUScaMZmf12.jpg?1526476088
   :width: 310px
   :height: 179px
.. |Expand icon| image:: https://cdn4.webdamdb.com/1280_2JkCGJsHGM10.png?1526475741
   :width: 34px
   :height: 32px
.. |Example of Basic operation| image:: https://cdn3.webdamdb.com/1280_UIhBNlB0Jpf8.png?1526476093
   :width: 337px
   :height: 243px
.. |Example of Advanced operation| image:: https://cdn4.webdamdb.com/1280_oPrvz0DKus51.png?1526475742
   :width: 339px
   :height: 208px

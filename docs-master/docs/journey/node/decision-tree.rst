.. include:: /common/global.rst

Decision Tree node
==================

|Decision Tree node|

The Decision Tree Node is commonly used across processes that are used
to filter records through exclusion logic, apply a dynamic segmentation,
or decide what kind of content a person is going to receive in a tweet,
email, or personalized web experience. As the decision tree node is a
generic piece of logic, it has a wide range of uses and applications.

A decision tree consists of columns, each referred to as a
*characteristic*, and rows, each referred to as a
`condition </journey/cond>`__. You can define as many characteristics
as you need. The decision tree executes beginning from the top left
condition, testing each condition in turn until either a **True** value
is found or the **Else** condition is reached.

The value of each characteristic comes from your graph's Data schema,
Public variables, and Literals. When you create a new characteristic, it
has two conditions, or branches. You can add more conditions as needed.
Each characteristic always has an *Else* branch that executes if no
other branch evaluates to **True**. As |acquia-product:aj| executes
along a decision tree branch, it will return the value in the Result
column once it fully executes a branch.

|Decision tree node example|

In the preceding example decision tree node, Gender, Age, and Shoe Size
are characteristics. Each characteristic column has several conditions.
For the decision tree to return the "young woman" result, the decision
tree will execute in the following sequence:

#. *Gender* - The condition "Female" evaluates as **True**
#. *Age* The condition ``VAL < 25`` evaluates as **True**
#. *Shoe Size* The characteristic evaluates its conditions:

   #. ``VAL < 4`` The condition evaluates as **False**
   #. The *Else* branch executes as all other possibilities are
      exhausted

#. After all characteristics are evaluated, the result "young woman" is
   returned.

Creating a decision tree node
-----------------------------

To create a decision tree node, perform the following actions:

#. Sign in to your |acquia-product:aj| interface.
#. Find the tile for the project that you want to modify, and then click
   its **Project Editor** |Project Editor icon| icon .
#. In the top left of the page, click the **Action Menu** |Action menu|
   icon.
#. Click **Create New**.
#. In the **Name** field, enter the name of your new decision tree node.
#. In the **Type** section of the **Create a New Item** view, scroll
   through the list of node types to find its **Logic** section, and
   then click **Decision Tree**.

   |Logic node type listing|

#. Click **Create New Item**.

Next, you must configure your new decision tree node.

Configuring a decision tree node
--------------------------------

A decision tree characteristic always includes an **Else** conditional
branch and at least one user defined conditional branch. To configure a
decision tree note, perform the following steps:

#. `Create a decision tree node <#create>`__ with one characteristic and
   one branch:

   |Default decision tree image|

#. To add additional characteristics, click the **Plus** |Plus icon|
   icon at the top left and provide the name for the new characteristic.
#. To add more conditions to evaluate for a characteristic, click the
   Plus |Plus icon| icon to the left of the item you want to expand:

   |Decision tree expansion|

|acquia-product:aj| saves your changes as you configure your decision
tree.

Editing characteristics or conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After creating a characteristic or condition, edit it by performing the
following steps:

#. Click the condition that you want to edit.
#. In the right pane, scroll to the **Edit Rule** panel, and then click
   the expand icon to display its entire contents.
#. Optionally, provide a description for your condition.
#. Click to select **Basic** or **Advanced** operations. (Learn more
   about how `Conditions and expressions </journey/cond>`__ work in
   |acquia-product:aj|.)
#. For **Advanced** conditions, supply the logic for your condition; for
   **Basic** conditions, click the **Select** box to select your
   condition, and if required, provide the values needed to complete
   your conditional.
#. Click **Save Changes to Condition**.

Providing results for each conditional
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After creating your characteristics and their conditionals, supply the
results for each conditional. Results can be in the form of literals
(hard-coded, static variables), a section of your schema, or a dynamic
field in your schema.

#. Sign in to your |acquia-product:aj| interface.
#. Find the tile for the project that you want to modify, and then click
   its **Project Editor** |Project Editor icon| icon.
#. In the top left of the page, click the **Action Menu** |Action menu|
   icon .
#. Click **Open**.
#. Find the name of the decision tree you want to edit and click its
   name, then click **Open**.
#. In the **Results** column, select the result you want to edit, select
   a value from either the **Data schema** or **Public variables**
   panels or enter a specific value in the **Literals** panel. In the
   **Edit Result Value** panel, click the **left arrow** icon |left
   arrow| to set the **Result** value for this decision tree node.

Mapping characteristics to data sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each created characteristic, you must add a data source in the list
of parameters outside of the node at the graph level. To add data
sources, perform the following steps:

#. Sign in to your |acquia-product:aj| interface.
#. Find the tile for the project that you want to modify, and then click
   its **Project Editor** |Project Editor icon| icon.
#. In the **Graphs** section of the project editing page, double-click
   the graph that you want to edit.
#. In your graph, click the icon for the decision tree node that you
   want to configure.
#. In the right sidebar, scroll to the **Edit** panel.
#. For each **Characteristic**, provide a source for the data. Select a
   value from either the **Data schema** or **Public variables** panels
   or enter a specific value in the **Literals** panel. In the **Edit**
   panel, click the left arrow icon |left arrow| for the characteristic.
   Repeat for each remaining characteristic.
#. Save your changes.

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **All decision tree result        | The results returned can either   |
| destination must be valid data    | be strings or JSON objects and    |
| reference formats**               | cannot be blank.                  |
+-----------------------------------+-----------------------------------+
| **All decision tree condition     | A condition node needs to have    |
| nodes must be valid JavaScript or | valid JavaScript in order to      |
| 'else'**                          | evaluate if a condition is true   |
|                                   | or not. If no conditions are      |
|                                   | needed, simply delete the branch  |
|                                   | so that it will evaluate true.    |
+-----------------------------------+-----------------------------------+

.. |Decision Tree node| image:: https://cdn2.webdamdb.com/1280_IgAlLvz4LFV9.png?1526475666
   :class: no-sb float-left logo-sm-lift
   :width: 51px
.. |Decision tree node example| image:: https://cdn3.webdamdb.com/1280_wUjw8SmQwxg3.png?1526475984
   :width: 550px
   :height: 238px
.. |Project Editor icon| image:: https://cdn2.webdamdb.com/1280_Qx24aCvtr211.png?1527098007
   :class: no-sb
   :width: 30px
   :height: 30px
.. |Action menu| image:: https://cdn4.webdamdb.com/1280_ksdoaWdShDr2.png?1526476127
   :class: no-sb
   :width: 30px
   :height: 30px
.. |Logic node type listing| image:: https://cdn3.webdamdb.com/1280_kfNiX7lNWL28.png?1526475881
   :width: 377px
   :height: 116px
.. |Default decision tree image| image:: https://cdn2.webdamdb.com/1280_25Hi9UpRe4v1.png?1526476141
   :width: 618px
   :height: 183px
.. |Plus icon| image:: https://cdn3.webdamdb.com/1280_kbmc0O5OMt91.png?1526475736
   :width: 25px
   :height: 22px
.. |Decision tree expansion| image:: https://cdn2.webdamdb.com/1280_U7fViS6fVC61.jpg?1526475445
   :width: 860px
   :height: 383px
.. |left arrow| image:: https://cdn4.webdamdb.com/100th_sm_kR0cgUi72rf3.png?1526475474
   :class: no-sb
   :width: 24px

.. include:: /common/global.rst

Conditional node
================

|Conditional node|

The Conditional Table node allows you to evaluate a set of conditions
using ``if-then-else`` statements, and will return ``true`` or
``false``. The expression can be one of the following:

-  ``AND`` - All of the following statements are true
-  ``OR`` - Any of the following statements are true

Recommended usage
-----------------

The conditional node is commonly used across processes that are used to
filter records through exclusion logic, check if someone is opted-in to
receive a certain type of communication, and many other uses. As the
conditional node is a generic piece of logic, it has a wide range of
uses and applications.

|Example of a conditional node|

The following evaluation methods are available:

-  Less Than
-  Less Than or Equal
-  Greater Than
-  Greater Than or Equal
-  Equals
-  Not Equal To
-  Contains
-  Starts With
-  Ends With

For more information about evaluation methods, see `Conditions and
Expressions </journey/cond>`__.

Creating a conditional node
---------------------------

To create a conditional node, complete the following actions:

#. Sign in to your |acquia-product:aj| interface.
#. Identify the project that you want to modify, and then click the
   project editor icon |Project Editor icon|.
#. In the top left of the page, click the action menu icon |Action Menu
   icon|, and then click **Create New**.
#. In the **Name** field, enter the name of your new conditional node.
#. Scroll through the list of node types to find the **Logic** section,
   and then click **Conditional**.

   |Logic node type listing|

#. Click **Create New Item**.
#. Enter your conditional data into the **Conditional Editor**, select
   an evaluation method, and the comparison value.
#. Click **Save**.

.. note::
  If a condition no longer needs to be evaluated, click the trashcan
  placed to the right of each rule to remove it.

After creating a condition, ensure that the correct parameters are
passed into the node at the graph level.

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **All conditional data names must | All values on the left hand side  |
| be non-empty**                    | of each expression must be        |
|                                   | non-empty.                        |
+-----------------------------------+-----------------------------------+
| **All conditional comparison      | All values on the right hand side |
| values must be non-empty**        | of the expression must be         |
|                                   | non-empty.                        |
+-----------------------------------+-----------------------------------+

.. |Conditional node| image:: https://cdn4.webdamdb.com/1280_k11NE17xQaq3.png?1526475708
   :class: no-sb float-left logo-sm-lift
.. |Example of a conditional node| image:: https://cdn4.webdamdb.com/1280_6tKJqqpALH65.png?1526475634
   :width: 550px
   :height: 190px
.. |Project Editor icon| image:: https://cdn4.webdamdb.com/100th_sm_YcVG2zY8pZL5.png?1526475783
   :width: 33px
   :height: 29px
.. |Action Menu icon| image:: https://cdn3.webdamdb.com/100th_sm_Aa8wvVef08x7.png?1526475662
   :width: 26px
   :height: 22px
.. |Logic node type listing| image:: https://cdn3.webdamdb.com/1280_kfNiX7lNWL28.png?1526475881
   :width: 377px
   :height: 116px

.. include:: /common/global.rst

About metrics and goals
=======================

Metrics allow |acquia-product:aj| to perform closed-loop journey
analytics, helping you identify the marketing efforts and content that
contributed to a user selecting your product or brand. Metrics are
defined and associated with steps in the\ `Journey
Mapper </journey/getting-started/map>`__, and they are incremented by a
graph when certain nodes are executed. (Read `Creating a Journey
Map </journey/getting-started/map>`__ to learn how to create a new map.)

Metrics are associated with steps in journey maps, where you will
develop the customer journey, but they are updated by nodes in graphs,
where the customer journey logic is executed. Metrics can be created and
associated with any step in the **Journey Map** editor or **graph**.
|acquia-product:aj| supports the following types of metrics:

-  `Basic <#basic>`__ - Increments a counter whenever a
   `node </journey/node>`__ has been executed
-  `Compound <#compound>`__ - Performs a calculation that returns a
   percentage or decimal based on your defined numerator and denominator
-  `Default <#default>`__ - Increments counters on a graph with a
   listener for each start and completion of the graph respectively

Types of Metrics
----------------

There are three types of metrics: *default*, *basic*, and *compound*.

Default metrics
~~~~~~~~~~~~~~~

*Default* metrics are displayed unless you configure another metric
instead. Each metric has a name, a type, an optional goal and
description. Whenever a graph is deployed, |acquia-product:aj| creates
two metrics for that graph: one to record the number of times the graph
is started, and another to record successful completions of the graph.
These metrics are useful for finding the number of times that a graph
has been run, how many times it ran successfully, and how many times it
incurred an error.

|Default metrics|

Basic metrics
~~~~~~~~~~~~~

A *basic* metric is a simple tally that increases by one each time a
specific node in a graph has been run, or a deployable graph has started
and ended. You define these metrics in the graph, and they can be of two
types: *numeric* or *monetary*. Monetary metrics allow the selection of
the currency — Dollar ($), Pound (£) and Euro (€) — and the increment
value.

|Basic metric 1| |Basic metric 2|

Compound metrics
~~~~~~~~~~~~~~~~

A *compound* metric will calculate a percentage, ratio, or rate between
two metrics, usually between a numerator and a denominator. Compound
metrics use a qualified metric, displayed on the left side, and a total
metric, displayed on the right side, to support four types of methods
for calculations: *percentage*, *rate*, *weighted index*, and
*advanced*.

|Compound metrics|

With the exception of the percentage method, the outputs of all methods
will result in a decimal that ranges from 0.0 to 1.0, while the
percentage method will return a value between 0% to 100%. The four
methods for calculating compound metrics are described as follows:

.. list-table::
  :header-rows: 1

  * - Method
    - Formula
    - Example
  * - Percentage
    - **Qualified Metrics** (QM) divided by **Total Metrics** (TM)
    - Calculating the percentage of customers that received Offer A (QM) out
      of all possible offers (TM) |br|
      ``QM / TM = X%``
  * - Rate
    - **Qualified Metrics** divided by **Total Metrics**
    - Calculating the rate at which customers received Offer A (QM) out of
      all possible offers (TM) |br|
      ``QM / TM = 0.X``
  * - Weighted Index
    - **Qualified Metrics** multiplied by their weight and then divided by
      **Total Metrics** multiplied by their weight
    - Calculating the rate after assigning a weighted value to each of the
      metrics to evaluate price of marketing spend on customers |br|
      ``((QM1 * 0.3) + (QM2 * 0.4)) / (TM * 1)``
  * - Advanced
    - A freeform formula that you can use to write your own formulas that
      utilize basic math symbols and various basic functions such as random,
      max, and min. |acquia-product:aj| uses the `JavaScript Expression
      Evaluator <https://github.com/silentmatt/expr-eval>`__ ``npm`` module.
      For information on the expression syntax, view that project's
      `documentation <https://github.com/silentmatt/expr-eval#expression-syntax>`__.
    -

After creating a metric, |acquia-product:aj| will display the metric as
a tile in the **Associated Metrics** list. Up to four favorite metrics
will be displayed on a project's tile on the |acquia-product:aj| project
page, but all metrics are displayed by clicking the metrics button on
the project's tile.

|Metric detail|

A metric's tile has two active areas:

-  *Top left* - clicking the star will mark this metric as a favorite
-  *Bottom right* - clicking this link will disassociate this metric
   from the selected project's tile

If a metric is defined with a goal, a percentage of the goal achieved is
displayed, and the metric tile will be colored in red, orange or green
depending on its completion level.

Accessing metrics
-----------------

To access metrics for a project from the |acquia-product:aj| home
screen, perform the following actions:

#. Sign in to your |acquia-product:aj| admin interface.
#. On the **Home Screen**, identify the project you want to customize.
#. In the project's tile, click the **View All Metrics** icon ( |View
   All Metrics| ).

From this screen, you can add a new metric by clicking the plus icon (
|Plus icon| ), and selecting whether you want to create a *Basic* or
*Compound* metric.

.. |Default metrics| image:: https://cdn3.webdamdb.com/1280_UbzGngvEbbZ0.png?1526475667
   :width: 422px
   :height: 250px
.. |Basic metric 1| image:: https://cdn2.webdamdb.com/1280_cftiisxtE21.png?-62169955200
   :width: 345px
   :height: 250px
.. |Basic metric 2| image:: https://cdn2.webdamdb.com/1280_saspBEzr2KX6.png?1526475670
   :width: 297px
   :height: 249px
.. |Compound metrics| image:: https://cdn2.webdamdb.com/1280_6Xnyoy1i1jk4.png?-62169955200
   :width: 447px
   :height: 400px
.. |Metric detail| image:: https://cdn4.webdamdb.com/1280_UwBFeVmP3Ia0.png?1526475711
   :width: 160px
   :height: 71px
.. |View All Metrics| image:: https://cdn3.webdamdb.com/1280_wXNkJEa2l6z1.png?-62169955200
   :width: 19px
   :height: 19px
.. |Plus icon| image:: https://cdn2.webdamdb.com/1280_kbmc0O5OMt91.png?-62169955200
   :width: 25px
   :height: 22px

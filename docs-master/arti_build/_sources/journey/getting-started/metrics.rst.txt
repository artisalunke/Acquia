.. include:: /common/global.rst

Creating metrics and goals
==========================

`Metrics </journey/metrics>`__ enable the user to add counters,
monetary value, and analytics to |acquia-product:aj| customer Journeys.
Metrics are either automatically created for listener graphs or manually
defined and associated on individual nodes in the Journey Mapper and
Graph.

Creating metrics
----------------

To define and associate a metric to a certain node, perform the
following actions:

#. In the top right of the page, click **Execution** to switch to
   Execution mode:

   |Click to select Execute|

   The **Edit Step**, **Associated Graphs**, and **Associated Metrics**
   panels will appear on the right side of the page.

#. Click the icon of the node to which you want to associate a metric.
#. In the **Associated Metrics** panel, click **Create New Metric**.
   The **Create Metric** menu will appear.
#. Add your desired metrics, and then click **Create**.

Each metric has a name, a type, a description, and an optional goal.
Basic metrics can be either *Numeric* or *Monetary*, which allow the
selection of the currency (Dollar ($), Pound (£), or Euro (€)) and the
increment value.

|Create numeric metric| |Create currency metric|

After creating a metric, |acquia-product:aj| will display the metric as
a tile in the right sidebar in the **Associated Metrics** panel. The
tile has two active areas that are revealed when pointing to the tile: a
**Favorite Metric** thumbtack in the top right corner, and a
**Disassociate Metric** icon (represented by a broken chain link) in the
bottom right corner.

|Metric tile in sidebar|

Up to four favorite metrics can be displayed for the project's tile on
the |acquia-product:aj| Project page.

Metrics that contain goals will display the percentage of the
goal-achieved in red, orange, or green text, depending on the metric
completion level.

Additional information
----------------------

For more information about metrics and graphs, including the different
types of metrics, see `About metrics and graphs </journey/metrics>`__.

.. |Click to select Execute| image:: https://cdn4.webdamdb.com/1280_kv7dj15x5211.png?1527094217
   :width: 444px
   :height: 102px
.. |Create numeric metric| image:: https://cdn4.webdamdb.com/1280_wjCDB91sNsb3.png?1527094227
   :width: 323px
   :height: 225px
.. |Create currency metric| image:: https://cdn3.webdamdb.com/1280_QzlEsaqb4T26.png?1527094235
   :width: 267px
   :height: 225px
.. |Metric tile in sidebar| image:: https://cdn4.webdamdb.com/1280_26KApLahF008.jpg?1527094240
   :width: 168px
   :height: 86px

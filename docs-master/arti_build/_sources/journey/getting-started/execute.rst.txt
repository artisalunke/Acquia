.. include:: /common/global.rst

Executing a journey
===================

When you execute a journey in |acquia-product:aj|, your graphs are run
in *headless mode*. In this mode, your graph execution will persist
until you explicitly stop it. The |acquia-product:aj| **Journey
Execution** panel displays the current state of all valid, deployable
graphs linked to journey steps in a journey map.

Before you can execute a journey through the Journey Mapper, you must
`create a journey map </journey/getting-started/map>`__, `create a
graph </journey/getting-started/graph>`__, and associate that graph with
your journey map.

Associating a graph with a journey step
---------------------------------------

For a journey to execute, you must have one or more
`graphs </journey/getting-started/graph>`__ associated with a journey
step. To associate a graph with a journey step, complete the following
instructions:

#. Sign in to |acquia-product:aj|.
#. On the main project page (accessible by clicking the
   |acquia-product:aj| logo in the top menu), find the project that you
   want to modify, and click its **Journey Mapper** icon.
#. In the **Journeys** section, click the name of the journey map you
   want to work with.
#. Click **Open**.
#. In the canvas, click the step you want to associate a graph with.
#. Above the **Edit Step** panel, click **Execution** to display the
   **Associated Graphs** panel.
#. Click **Associate Graph**.
#. In the **Associate Graph** dialog, select one or more graphs to
   associate with the journey step by clicking the graph name.
#. Click **Associate**.

After associating graphs with your journey steps, you can deploy your
journey.

Deploying a customer journey
----------------------------

You can deploy a customer journey, and all of its associated graphs, by
completing the following actions:

#. Sign in to |acquia-product:aj|.
#. On the main project page (accessible by clicking the
   |acquia-product:aj| logo in the top menu), find the project that you
   want to modify, and click its **Journey Mapper** icon.
#. In the **Journeys** section, click the name of the journey map you
   want to work with.
#. Click **Open**.
#. Click the **Execution** tab.
#. Under **Journey Execution**, find the |acquia-product:aj| environment
   associated with the graphs you want to deploy, then click **Deploy**.
   If you want to deploy graphs individually, open the list of
   deployable graphs by clicking the plus ( |Plus icon| ) icon to
   display each graph.

Deploying graphs from this location is equivalent to `deploying graphs
from the Admin page </journey/admin/graph>`__. If you have more than one
|acquia-product:aj| `environment </journey/admin/env>`__,
|acquia-product:aj| will display the state of the graphs in each
environment.

|Execution mode|

When the journey begins executing, any `metrics </journey/metrics>`__
associated with your journey's steps will update in the **All Metrics
for Journey** panel. If you have more than one |acquia-product:aj|
environment, |acquia-product:aj| will both display a list in the metrics
panel to the right of the journey map.

.. |Plus icon| image:: https://cdn2.webdamdb.com/1280_o8jtxxpFQK07.png?1526476168
   :width: 18px
   :height: 18px
.. |Execution mode| image:: https://cdn2.webdamdb.com/1280_I4Vmgx6SLzs3.png?1526475508
   :width: 346px
   :height: 449px

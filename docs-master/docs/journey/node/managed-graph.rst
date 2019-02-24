.. include:: /common/global.rst

Managed Graph node
==================

|Managed Graph icon|

A Managed Graph provided by Acquia offers pre-built business logic you
can use when `creating a project </journey/getting-started/project>`__.
It is useful when you want to use functionality created and managed by
Acquia on your behalf.

You cannot make any changes to the behavior of a managed graph.

.. _create:

Creating a managed graph node
-----------------------------

To use a managed graph in your project, complete the following steps:

#. Sign in to your Acquia Journey interface.
#. On the **Home Screen**, identify the project you want to customize.
#. In the project's tile, click the **Project Editor** |Project Editor
   icon| icon.
#. To open a graph, double-click it, or from the **Open Item** tab,
   select the graph you want to open in the **Project Editor** from the
   **Graphs** section, then click **Open** at the bottom of the tab
   panel.
#. From within the **Project Editor**, perform one of the following
   actions:

   -  Right-click on the canvas and click **Add Node to Graph**.
   -  Click on an existing node, then in the Edit panel click **Replace
      Node**.

#. Scroll to the **Managed Graphs** section, and identify the managed
   graph you want to use in your project:
   |Add node to graph|
#. Click on the managed graph you want to use in your project, then
   click **Add**.

   .. note::
    Pointing your mouse to icon for a managed graph will display
    information about its inputs and outputs, as well as any recent
    changes to it.

   |Managed graph description|

#. If the managed graph has any connection dependencies, then you will
   be asked to provide the required information. For example, in the
   following screenshot, the managed graph requires a REST Web Service
   connection: |Managed graph connection|
#. Click **Finalize** when you are finished.

.. _update:

Updating a managed graph
------------------------

If your managed graph is updated by Acquia, then its icon will show an
alert bubble in the upper right corner to indicate it is out of date:
|Managed graph update bubble|

To update your managed graph, complete the following steps:

#. Hover over your managed graph node, then click the **Change Log**
   tab. Review the changes before deciding whether to apply the update.
#. Click the **managed graph** icon to update the Managed Graph.

|Managed graph warning|

.. note::
  It is recommended that you perform regression testing to ensure
  your graph works as expected before `deploying a new
  version </journey/admin/graph>`__.

.. |Managed Graph icon| image:: https://cdn2.webdamdb.com/100th_sm_6nHkHpOGxAQ5.png?1527871061
   :class: no-sb float-left logo-sm-lift
   :width: 51px
.. |Project Editor icon| image:: https://cdn4.webdamdb.com/100th_sm_YcVG2zY8pZL5.png?1526475783
.. |Add node to graph| image:: https://cdn3.webdamdb.com/1280_MtnT6JUIogd9.png?1526475833
   :width: 447px
   :height: 429px
.. |Managed graph description| image:: https://cdn2.webdamdb.com/1280_oH7P7Sz1q13.png?1526475480
   :width: 449px
   :height: 350px
.. |Managed graph connection| image:: https://cdn2.webdamdb.com/1280_EmAKofRKqfC3.png?1526476146
   :width: 403px
   :height: 613px
.. |Managed graph update bubble| image:: https://cdn3.webdamdb.com/1280_o81mWZxoetl1.png?1526475863
   :width: 300px
   :height: 268px
.. |Managed graph warning| image:: https://cdn4.webdamdb.com/1280_w2FzsrQ9iGv1.png?1526475637
   :width: 792px
   :height: 338px

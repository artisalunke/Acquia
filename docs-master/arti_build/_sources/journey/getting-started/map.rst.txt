.. include:: /common/global.rst

Creating a journey map
======================

|acquia-product:aj| uses *journey maps* to allow you to plan your
integrations at a high level, and model data flows from inputs, decision
processing, and outputs. Each decision point is represented by a node in
the journey map. You can associate one or more `metrics or
goals </journey/metrics>`__ with each node in your customer journey map.

|Journey map example|

You can build journey maps from scratch, or you can use a predefined
*Jumpstart* template provided by your system administrator.

Creating a new journey
----------------------

To create a customer journey for your project, perform the following
steps:

#. Sign in to your |acquia-product:aj| account.
#. Click the **Journey Mapper** icon on the card for the project that
   you want to modify.

   |Click the Journey Mapper icon|

#. Depending on if you have already created a journey for the project,
   complete the appropriate procedure:

   -  *If this is your first journey for this project*, the **Add New
      Journey** tab opens.
   -  *If a journey already exists for this project*, click the
      **Options** menu in the upper left corner. and choose **Create
      New** to open the **Add New Journey** tab.

#. Provide a name and description for your journey, and then click
   **Create New Item**.

   |Create a new journey|

The Journey Mapper user interface
---------------------------------

The **Journey Mapper** interface allows you to create and annotate
customer journeys in a free-form manner. The **Journey Mapper** also
allows metrics to be created and associated with journey elements, and
for journey elements to be associated with graphs.

|Journey Mapper interface|

The Journey Mapper displays a canvas in the left side of the window, and
a panel with tabs for **Design** and **Execution** modes on the right.
To select a mode, click **Design** or **Execution**.

|Select a mode|

The panel contains several panes, which can each be expanded to fill the
full right-hand column by clicking on the **Expand** icon |Expand icon|
in the top right of a pane. To collapse the pane, click the **Collapse**
|Collapse icon| icon.

Design Mode
~~~~~~~~~~~

In **Design** mode, the panel on the right contains the following panes:

|Add Step pane|

-  **Edit Map** - For editing the journey's name and description
-  **Step** - Contains possible steps to assist with the journey

Execution Mode
~~~~~~~~~~~~~~

In **Execution** mode, the panel on the right contains the following
panes:

-  The **Journey Name** and **Description** pane
-  The **Journey Execution** pane
-  The **Metrics** pane

Drawing and annotating journeys
-------------------------------

Adding a journey step
~~~~~~~~~~~~~~~~~~~~~

In **Design** mode, add a new journey step by performing the following
steps:

-  *Clicking and dragging*

   #. Point to the default **Pencil** icon.
   #. When the grab arrow appears, click and drag it away from the
      **Pencil** icon.

      |Click and drag|

-  *Right-clicking the canvas*

   #. Right-click inside the white **Journey Mapper** canvas, and select
      **Add Step to Journey**.

Adding a style to a journey step
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A style is a visual representation of a step in a journey, and enhance
the readability of your journey. Styles include:

-  Channels
-  Social Media
-  Sales
-  Miscellaneous
-  Custom

To add a style journey step, perform the following steps:

#. Right-click the step's icon, and then click **Apply New Style to
   Step**.
#. In the **Apply Style** dialog box, click the icon of the desired
   style.
#. Click **Apply**.

Connecting steps in a journey
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After creating a new step and adding an action to it, connect it to
existing steps in the journey by performing the following actions:

#. Click the existing step in your canvas you want to connect to your
   new step. A grab arrow will appear to the right of the step icon.
#. Click and drag the grab arrow to the new step.
#. Release the mouse button when your mouse pointer is inside the new
   step's icon.
#. An arrow will appear, connecting the steps together.

|Join steps together|

To delete the connection between two steps, right-click the arrow, and
then click **Delete Link**.

Deleting a journey step
~~~~~~~~~~~~~~~~~~~~~~~

To delete a step, right-click the step's icon, and then click **Delete
Step**.

Customizing a step's appearance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To customize a step's icon or colors, perform the following actions
while in **Design** mode:

#. Click the icon you wish to change.
#. The **Customize Journey Step** pane will appear in the right-hand
   panel.
#. In the **Customize Journey Step** pane, click the **Pencil** |Pencil|
   icon next to the attribute you wish to customize.
#. Perform the desired changes.
#. Click the **Save Changes to Step** |Save Changes to Step| icon before
   de-selecting the step in the Journey Mapper.

   .. important::
      If you do not save your changes, they will be lost when you click the
      canvas or another step.

To customize the **Step Name** or **Description** of a step, perform the
following actions:

#. Click the icon you wish to change.
#. The **Edit Step** pane will appear in the right-hand panel.
#. In the **Edit Step** pane, make your desired changes.
#. Click the **Save Changes to Step** button before de-selecting the
   step in the Journey Mapper.

Displaying icon names

The Journey Map can display only the journey icons, or icons and the
name of each step. To display step names in addition to icons, click the
**Show Step Names** icon at the top right of the canvas.

|Display step names|

Click the icon again to hide step names.

Customizing links between steps

To make connections between steps easier to understand, you can add
custom text, colors, and icons to the arrows connecting journey steps
together:

|Customized link between steps|

To add explanatory text on the arrows between each step, perform the
following actions:

#. Click the arrow you want to customize.
#. The **Edit Journey Link** pane will appear in the right-hand panel.
#. Edit the **Link Name** and **Link Description**.
#. Click **Save Changes to Link**.

To change the color of an arrow, or add a small icon on the arrow
itself, perform the following actions:

#. Click the arrow that you want to customize.
#. The **Customize Journey Link** pane will appear in the right-hand
   panel.
#. Click the pencil icon |Pencil icon| next to the attribute that you
   want to change, and then make your desired changes.
#. To save your changes, click the save icon |Save icon|.

.. |Journey map example| image:: https://cdn2.webdamdb.com/1280_kBleRZe9it71.png?1526476038
   :width: 1280px
   :height: 735px
.. |Click the Journey Mapper icon| image:: https://cdn4.webdamdb.com/1280_In7huR3rrme1.png?1526475750
   :width: 333px
   :height: 126px
.. |Create a new journey| image:: https://cdn3.webdamdb.com/1280_PGbE0Cglqa41.png?1526475721
   :width: 600px
   :height: 284px
.. |Journey Mapper interface| image:: https://cdn2.webdamdb.com/1280_IhBEWsNdoA19.png?1526476181
   :width: 450px
   :height: 271px
.. |Select a mode| image:: https://cdn2.webdamdb.com/1280_oROoJMOaiEh5.png?1526475821
   :width: 336px
   :height: 44px
.. |Expand icon| image:: https://cdn3.webdamdb.com/1280_2JkCGJsHGM10.png?1526475741
   :width: 34px
   :height: 32px
.. |Collapse icon| image:: https://cdn4.webdamdb.com/1280_wYozuNFLTd88.png?1526475714
   :width: 33px
   :height: 33px
.. |Add Step pane| image:: https://cdn2.webdamdb.com/1280_oAkByd7KJzl4.png?1526475537
   :width: 250px
   :height: 221px
.. |Click and drag| image:: https://cdn3.webdamdb.com/1280_AmE8IfxaKy56.jpg?1526476053
   :width: 305px
   :height: 113px
.. |Join steps together| image:: https://cdn2.webdamdb.com/1280_s4Hm0I14XHx8.jpg?1526475729
   :width: 294px
   :height: 140px
.. |Pencil| image:: https://cdn3.webdamdb.com/1280_shNNBVPixWv1.png?1526476001
   :width: 25px
   :height: 25px
.. |Save Changes to Step| image:: https://cdn4.webdamdb.com/1280_spViT5Asgp74.png?1526476072
   :width: 16px
   :height: 16px
.. |Display step names| image:: https://cdn4.webdamdb.com/1280_AcbHCWQfvn91.jpg?1526475813
   :width: 330px
   :height: 185px
.. |Customized link between steps| image:: https://cdn4.webdamdb.com/1280_cCzjMNI6cYb4.png?1526475849
   :width: 465px
   :height: 119px
.. |Pencil icon| image:: https://cdn3.webdamdb.com/1280_shNNBVPixWv1.png?1526476001
   :width: 25px
   :height: 25px
.. |Save icon| image:: https://cdn4.webdamdb.com/1280_spViT5Asgp74.png?1526476072
   :width: 16px
   :height: 16px

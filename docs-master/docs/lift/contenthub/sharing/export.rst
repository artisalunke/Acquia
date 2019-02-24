.. include:: /common/global.rst

Exporting multiple entities at once
===================================

As a content creator, you may need to export many of your publishing
website's entities to your |acquia-product:ch| at the same time. To help
you with your content management, |acquia-product:ch| makes it possible
to handle many entities at once through the use of an optional *export
queue*. Each item in the export queue contains entities to be exported
to |acquia-product:ch|.

You can export entities from the queue using either the user interface
or Drush.

.. note::  

   For information about batch imports (instead of exports) of entities,
   see `Importing multiple entities at
   once </content-hub/sharing/import>`__.

Enabling the export queue
-------------------------

The **Export Queue** configuration page allows you to enable the export
queue, and modify its behavior. To enable the queue, perform the
following steps:

#. Sign in to your website as an administrator.
#. Go to **Configuration > Web Services > Acquia Content Hub**.
#. Click the **Export Queue** tab.
#. Select the **Export via queue** check box.
   |acquia-product:ch| will display additional configuration options.
#. Click **Save Configuration**.

Configuring the export queue
----------------------------

The export queue is a Drupal batch process, and each item in the batch
process contains entities to be exported. To alter these queue
configuration values, navigate to the **Export Queue** page (as
previously described) to display the **Queue Behavior Configuration**
section. The section includes the following settings:

.. important:: 

   Increasing any of these values will place additional load on your
   publishing and subscribing sites, and should be done with caution.

-  **Queue Batch Size** - Number of queue items that will be processed
   in the same batch queue process. Processing more batch items
   simultaneously will add load to the exporting website. *Default
   value: ``1``*
-  **Entities Per Queue Item** - Maximum number of entities sent through
   an entity hook to be included in a queue item. These entities *and
   all of their dependencies* (including vocabulary items and node
   references) will be sent to |acquia-product:ch| in the same HTTP
   request. Increasing this value increases the size and complexity of
   each queue item, which also increases the load on websites that
   import this data. *Default value: ``1``*
-  **Queue Waiting Time Between Items** - Waiting time in seconds
   between processed queue items. Decreasing this value causes your
   subscribing websites to have less time to finish processing queue
   items before more items are sent. *Default value: ``3`` seconds*

If you make any modifications to the entered values on this page, be
sure to click **Save Configuration** to save your changes.

Processing the export queue
---------------------------

To process all items in the export queue, use one of the following
methods:

-  *User interface*

   #. Sign in to your website as an administrator.
   #. Go to **Configuration > Web Services > Acquia Content Hub**.
   #. Click the **Export Queue** tab.
   #. In the **Run Export Queue** section, select the number of queue
      items that you want to process.
   #. Click **Submit**.

-  *Drush* - Open a command prompt window, and then execute the
   following Drush command:

   .. code-block:: none
   
      queue-run acquia_contenthub_export_queue
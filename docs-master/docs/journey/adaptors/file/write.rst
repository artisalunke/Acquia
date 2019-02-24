.. include:: /common/global.rst

File: Write adaptor
===================

The **File write adaptor** allows you to store information about a
customer journey as a file object in your cloud provider's storage
service, enabling you to keep persistent information about a journey for
use in other graphs.

.. important::
  The file write adaptor overwrites existing content. We recommend that
  you use a `unique filename <#unique>`__ when using the file write
  adaptor to prevent unintentional data loss.

Creating the adaptor
--------------------

To use the file write adaptor, complete the following steps:

#. `Sign in to |acquia-product:aj| </journey/access>`__.
#. `Create an adaptor </journey/adaptors#add>`__ of the type **File**.
#. In the configuration panel, configure the following settings for the
   adaptor:

   |file write adaptor|

   -  Under **Adaptor Action**, click the select box, and select
      **Write**.
   -  Under **File Name**, click the **Data Schema** panel. Identify the
      schema location that maps to the filename, click its name, and
      then click the **left arrow** |left arrow| icon. The filename
      should include any necessary path component.
   -  Under **File Contents To Write**, click the select box. In the
      **Data Schema** panel, identify the schema location that contains
      the content of the file to upload to your cloud provider, click
      its name, and then click the **left arrow** |left arrow| icon.

#. |acquia-product:aj| saves each configuration change as you complete
   it. To close the adaptor configuration page, click the **X** next to
   the title of the file adaptor in the tab bar:

   |Close file adaptor box|

Generating a unique filename
----------------------------

To create a unique filename and save it to your data schema for use with
the file write adaptor, we recommend the following approach using a
`JavaScript node </journey/node/javascript>`__ within your graph.

#. Sign in to |acquia-product:aj|.
#. On the main project page (accessible by clicking the
   |acquia-product:aj| logo in the top menu), find the project that you
   want to modify, and click its **Project Editor** |Project Editor
   icon| icon.
#. In the upper left of the page, click the **action menu** ( |Action
   menu| ) , and then click **Create new**.
#. Enter a **Name** for the JavaScript node.
#. In the **Logic** section, click JavaScript.
#. At the bottom of the page, click **Create New Item**.
   |acquia-product:aj| will display the JavaScript editor.
#. Click **Add Argument**, and then enter *basename*. Repeat for *ext*
   and *prefix*.
#. In the **JavaScript Editor**, enter the following code:

   ::

       const uuid = require('uuid/v4');
       const date = new Date();

       return prefix + '/' + basename + '_' + date.getTime() + '_' + uuid() + '.' + ext;

#. In the upper right corner of the editor, click **Save Script**.

When you use the JavaScript node you just created within your graph, it
will save a unique filename to the schema location assigned to **Script
Return Value**. You can assign that schema location as the source for
the file write adaptor **File Name** parameter.

.. |file write adaptor| image:: https://cdn3.webdamdb.com/1280_E6xBb6PZ6512.png?1526476120
   :width: 600px
.. |left arrow| image:: https://cdn4.webdamdb.com/100th_sm_kR0cgUi72rf3.png?1526475474
   :class: no-sb
   :width: 24px
.. |Close file adaptor box| image:: https://cdn3.webdamdb.com/1280_YJx6xqUVcJF7.jpg?1526475651
   :width: 352px
   :height: 198px
.. |Project Editor icon| image:: https://cdn4.webdamdb.com/100th_sm_YcVG2zY8pZL5.png?1526475783
   :width: 33px
   :height: 29px
.. |Action menu| image:: https://cdn4.webdamdb.com/1280_kpCePUhKSlg0.png?1526475518
   :width: 69px
   :height: 35px

.. include:: /common/global.rst

File: Read adaptor
==================

The **File read adaptor** allows you to download data from your cloud
provider's storage service for incorporation into a customer journey.
The data is saved to your schema location depending on its type:

-  *If the file is a single JSON object,* it is parsed and saved as a
   child record at the schema location you specify.
-  *If the file contains multiple JSON objects or non-JSON data,* it is
   saved as a text string to the schema location.

Creating the adaptor
--------------------

To create a **File read adaptor**, complete the following steps:

#. `Sign in to |acquia-product:aj| </journey/access>`__.
#. `Create an adaptor </journey/adaptors#add>`__ of the type **File**.
#. In the configuration panel, configure the following settings for the
   adaptor: |file read adaptor|

   -  Under **Adaptor Action**, click the select box, and select
      **Read**.
   -  Under **File Name**, click the **Data Schema** panel. Identify the
      schema location that maps to the filename, click its name, and
      then click the **left arrow** |left arrow| icon. The filename
      should include any necessary path component.
   -  Under **File Contents Destination**, click the select box. In the
      **Data Schema** panel, identify the schema location that will
      store the contents of the file, click its name, and then click the
      **left arrow** |left arrow| icon.

#. |acquia-product:aj| saves each configuration change as you complete
   it. To close the adaptor configuration page, click the **X** next to
   the title of the file adaptor in the tab bar:

   |Close file adaptor box|

.. |file read adaptor| image:: https://cdn4.webdamdb.com/1280_gf5hyJnKXWo4.png?1526475909
   :width: 600px
.. |left arrow| image:: https://cdn4.webdamdb.com/100th_sm_kR0cgUi72rf3.png?1526475474
   :class: no-sb
   :width: 24px
.. |Close file adaptor box| image:: https://cdn3.webdamdb.com/1280_YJx6xqUVcJF7.jpg?1526475651
   :width: 352px
   :height: 198px

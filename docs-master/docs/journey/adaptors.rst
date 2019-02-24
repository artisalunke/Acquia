.. include:: /common/global.rst

|acquia-product:aj| adaptors
============================

.. toctree::
   :hidden:
   :glob:

   /journey/adaptors/*

|acquia-product:aj| provides a wide variety of adaptors, enabling you to
interact with external systems from within your graphs. This allows you
to drive your customer next best action based on specific information
about a user.

Adaptors are `created in the project editor <#add>`__, and each adaptor
uses a pre-defined `connection </journey/connect>`__ to do its work.
Based on your connection type, the following adaptor types and methods
can be created:

.. list-table::
  :header-rows: 1

  * - Connection
    - Image
    - Action / Method
    -
    -
    -
  * - |Lift conn|
    - |Lift adaptor|
    - `Capture </journey/adaptors/lift/capture>`__
    - `Decide </journey/adaptors/lift/decide>`__
    - `Visitor </journey/adaptors/lift/visitor>`__
    - `Content </journey/adaptors/lift/content>`__
  * - `Database </journey/connect/database>`__
    - |Database adaptor|
    - `Read </journey/adaptors/database/read>`__
    - `Write </journey/adaptors/database/write>`__
    - `Listen </journey/adaptors/database/listen>`__
    - `Delete </journey/adaptors/database/delete>`__
  * - `Email </journey/connect/email>`__
    - |Email adaptor|
    -
    - `Write </journey/adaptors/email/write>`__
    -
    -
  * - `File </journey/connect/file>`__
    - |File adaptor|
    - `Read </journey/adaptors/file/read>`__
    - `Write </journey/adaptors/file/write>`__
    -
    -
  * - `Graph API </journey/adaptors/graph-api>`__
    - |Graph API listener|
    -
    -
    - `Listen </journey/adaptors/graph-api>`__
    -
  * - `Message Queue </journey/connect/message>`__
    - |Message adaptor|
    - `Read </journey/adaptors/message/read>`__
    - `Write </journey/adaptors/message/write>`__
    - `Listen </journey/adaptors/message/listen>`__
    -
  * - `REST Web Service </journey/connect/rest>`__
    - |REST web service adaptor|
    - `GET </journey/adaptors/rest/get>`__
    - `POST </journey/adaptors/rest/post>`__
    - `PUT </journey/adaptors/rest/put>`__
    - `DELETE </journey/adaptors/rest/delete>`__
  * - `SOAP Web Service </journey/connect/soap>`__
    - |SOAP web service adaptor|
    - Web service-dependent
    -
    -
    -
  * - `Twitter </journey/connect/twitter>`__
    - |Twitter adaptor|
    - `Read </journey/adaptors/twitter/read>`__
    - `Write </journey/adaptors/twitter/write>`__
    - `Listen </journey/adaptors/twitter/listen>`__
    -

.. _add:

Adding an adaptor
-----------------

To add an adaptor to your project, complete the following actions:

.. note:: Most adaptors require that you first create the
          `connection </journey/connect>`__ that is required for the adaptor type
          that you want to create.

#. In the **Projects** page, click the **Project Editor** icon on your
   project's card.
   |acquia-product:aj| will display the Project Editor for your project.
#. Click the **action menu** ( |Action menu| ) in the upper left of the
   page, and then click **Create new**.
#. Enter a **Name** for the adaptor that describes its purpose.
#. In the **Adaptors** section, click the adaptor type that you want to
   use.
#. At the bottom of the page, click **Create New Item**.
   |acquia-product:aj| will display the configuration page for your new
   adaptor.
#. In the **Adaptor Connection** list, click the
   `connection </journey/connect>`__ that you want to use for this
   adaptor.
#. Continue to configure the adaptor based on its specific configuration
   instructions.

.. _delete:

Deleting an adaptor
-------------------

To delete an adaptor from |acquia-product:aj| that you no longer
require, complete the following actions:

#. In the **Projects** page, click the **Project Editor** icon on your
   project's card.
   |acquia-product:aj| will display the Project Editor for your project.
#. In the **Open Item** tab, find the adaptor that you want to remove,
   and then click the adaptor.
#. At the bottom of the page, click **Open '[adaptor]'**, where
   *[adaptor]* is the name of your adaptor. |acquia-product:aj| will
   display the configuration page for your adaptor.
#. Click the **trash can** |Delete icon| icon to permanently delete the
   adaptor from |acquia-product:aj|.

   |Delete icon location|

.. |Lift conn| replace:: \ |acquia-product:cha| \ 
.. _Lift conn: /journey/connect/lift

.. |Lift adaptor| image:: https://cdn3.webdamdb.com/100th_sm_gWT0ClJBKXP4.png?1527198335
   :class: no-sb
   :width: 53px
.. |Database adaptor| image:: https://cdn3.webdamdb.com/1280_MPQTqoZzw6F6.png?-62169955200
   :class: no-sb
   :width: 53px
.. |Email adaptor| image:: https://cdn3.webdamdb.com/1280_woXxAkJDu671.png?-62169955200
   :class: no-sb
   :width: 53px
.. |File adaptor| image:: https://cdn2.webdamdb.com/100th_sm_clRHYs4T8RF5.png?1527197848
   :class: no-sb
   :width: 53px
.. |Graph API listener| image:: https://cdn2.webdamdb.com/1280_I0gRWmw332Z6.png?-62169955200
   :class: no-sb
   :width: 53px
.. |Message adaptor| image:: https://cdn3.webdamdb.com/1280_gOFtcaVv9K59.png?1526475659
   :class: no-sb
   :width: 53px
.. |REST web service adaptor| image:: https://cdn4.webdamdb.com/1280_6g6C8mrAZ0E8.png?1526475822
   :class: no-sb
   :width: 53px
.. |SOAP web service adaptor| image:: https://cdn2.webdamdb.com/1280_AyEHsvy16411.png?1526475800
   :class: no-sb
   :width: 53px
.. |Twitter adaptor| image:: https://cdn3.webdamdb.com/1280_2iWN4x4ZRb54.png?1526475788
   :class: no-sb
   :width: 53px
.. |Action menu| image:: https://cdn3.webdamdb.com/1280_kpCePUhKSlg0.png?-62169955200
   :width: 69px
   :height: 35px
.. |Delete icon| image:: https://cdn3.webdamdb.com/1280_o5LnBf2eT12.png?-62169955200
   :width: 22px
   :height: 22px
.. |Delete icon location| image:: https://cdn3.webdamdb.com/1280_2OeweDfnK7m5.png?-62169955200
   :width: 926px
   :height: 68px

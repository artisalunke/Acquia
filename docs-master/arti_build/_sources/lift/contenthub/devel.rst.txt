.. include:: /common/global.rst

Using Devel with Content Hub
====================================

|acquia-product:ch| includes an extension of the
`Devel <https://www.drupal.org/project/devel>`__ module for
troubleshooting |acquia-product:ch|-specific issues.

Enabling Content Hub Devel
----------------------------------

The Devel extension for |acquia-product:ch| can be enabled like any
other Drupal module. As an administrator:

#. Navigate to the **Modules** or **Extend** page.
#. Select the check box next to |acquia-product:ch| Development.
#. Click **Save configuration**.

Using Devel
-----------

Once the module is enabled, a new **Content Hub Devel** tab will appear
on content nodes to users with the **Access developer information**
permission.

|content-hub-devel-tab.png|

Accessing this tab enables you to view the `CDF </content-hub/cdf>`__
(common data format) information for that node. Subtabs are available
for additional information:

-  **Local**: displays the array format of CDF for that node.
-  **Local JSON**: displays the JSON format of CDF for that node.
-  **Remote**: displays the response from the hub in the array format of
   CDF.
-  **Remote JSON**: displays the response, from the hub, in the JSON
   format of CDF for that node.

.. note::  

   If the **Remote** tab displays the message ``The Content Hub does not 
   have an entity with UUID = xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`` instead 
   of displaying the CDF, it means content is not being pushed to the Hub. 
   This information helps the developer to debug.

You can expand each of the values by clicking on their bar, so you can
see the exact value of the variable.

|ch-devel-expanded.png|

.. |content-hub-devel-tab.png| image:: https://cdn2.webdamdb.com/1280_sNtXOEjAc911.png?-62169955200
   :width: 453px
   :height: 274px
.. |ch-devel-expanded.png| image:: https://cdn3.webdamdb.com/1280_AaIrysvkwno6.png?-62169955200
   :width: 706px
   :height: 604px

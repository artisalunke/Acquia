.. include:: /common/global.rst

Creating custom fields and forms
================================

.. container:: message-status

  This feature is available only to |acquia-product:dam| Professional
  subscribers.

Admins can create custom fields for the registration and download
request forms, allowing you to gather important information from users
during the registration process — such as their department, title, or
how they will be using the asset.

.. _create:

Create a custom field
---------------------

#. Sign in to |acquia-product:dam|.
#. Click the settings icon |Settings|, and then click **System
   Preferences**.
#. Click **Custom Fields** in the left-hand navigation.
#. Click the ``(+)`` in the actions toolbar.

   |Adding a custom field|

#. Select the **Field Type** from the drop down menu.
#. If you choose **Picklist**, enter the picklist values in the Options
   section. You can also set the default value that displays to your
   users.
#. You can also alphabetize your picklist, by selecting the box next to
   **Sort Alphabetically**. Any time you add a new value, you'll need to
   sort the list again to alphabetize it. If desired, after sorting you
   can reorder values to keep more common inputs at the top of your
   list.

   |Picklist sorted|

#. Enter the label and name. The label will display to your users, while
   the name is only seen by the admin.
#. Click **Save**.

.. _edit:

Edit or delete a custom field
-----------------------------

#. Click the wrench icon |Wrench icon| for the field that you want to
   edit.
#. Click **Edit** to modify the field or **Delete** to remove the custom
   field.

   |Select a custom field|

.. _configure:

Configure the registration or download request form
---------------------------------------------------

#. Sign in to |acquia-product:dam|.
#. Click the settings icon |Settings|, and then click **System
   Preferences**.
#. Click **Configure Forms** in the menu to the left.
#. Click the wrench icon |Wrench icon| for the form that you want to
   configure, and then click **Edit**.

.. _fields:

Field management
----------------

To add a field, complete the following steps:

#. In the actions toolbar, click **Add field**.
#. Select a previously created custom field from the list, or click
   create a new field.
#. Click **Add**.

Other actions:

-  *Remove a field* - Click the subtract icon |Subtract| in the
   **Actions** column for the field you want to remove.
-  *Reorder fields* - Click and hold the reorder icon |Reorder|, drag
   and drop to the desired location, and then click **Save Changes**.
-  *Require a field* - Select the check box in the required column for
   the field that you want users be required to complete, and then click
   **Save Changes**.

.. _info:

Helpful information
-------------------

-  You can create registration rules based on responses to custom fields
   to automatically add users to certain groups and/or automatically
   have them approved. (Read more about `registration
   rules </dam/admin/system/users>`__.)
-  Some fields of the registration and download request form cannot be
   edited, removed or rearranged.
-  The same custom field can be added to both the registration and
   download request forms.

.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 30px
.. |Adding a custom field| image:: https://cdn2.webdamdb.com/md_cRVGu86Fcn31.png?1527121380
   :width: 421px
   :height: 221px
.. |Picklist sorted| image:: https://cdn3.webdamdb.com/md_kW8vnjSswW85.png?1527121376
   :width: 350px
   :height: 541px
.. |Wrench icon| image:: https://cdn2.webdamdb.com/100th_sm_24n8wRX5SH32.png?1526475691
   :width: 24px
   :height: 21px
.. |Select a custom field| image:: https://cdn4.webdamdb.com/md_YIi1iJbaYMM9.png?1527121368
   :width: 550px
   :height: 172px
.. |Subtract| image:: https://cdn3.webdamdb.com/100th_sm_gUmFYCc6cec8.png?1527118348
   :width: 23px
   :height: 23px
.. |Reorder| image:: https://cdn3.webdamdb.com/100th_sm_EcsnczhpsAv4.png?1527121377
   :width: 29px
   :height: 29px

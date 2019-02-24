.. include:: /common/global.rst

Creating metadata templates
===========================

Metadata Templates can be used to apply a set of metadata values to a
group of assets upon upload or as a batch edit. This set of metadata can
include specific values for active fields as well as keywords.

.. _create:

Create a metadata template
--------------------------

#. Sign in to |acquia-product:dam|, click the |Settings| **Settings**
   icon, and select **Metadata Schema**.
#. Click **Metadata Templates** in the left-hand navigation.
#. Click the ``(+)`` **Plus** icon in the actions toolbar.
#. Enter a template name and populate the values for any or all active
   metadata fields. (Read more about `configuring the metadata
   schema </dam/admin/metadata>`__.)
#. Click **Save**.

.. _folder:

Apply a metadata template to a folder
-------------------------------------

When a metadata template is applied to a folder, any assets uploaded
into that folder will automatically adopt the metadata from the
template. However, the metadata template will not be applied to the
assets already residing in or moved to the folder.

There are two ways to apply metadata templates to a folder:

Option 1:

#. Log into |acquia-product:dam|, click the |Settings| **Settings**
   icon, and select **Metadata Schema**.
#. Click **Metadata Templates** in the left-hand navigation.
#. Click the number under the **Number of folders** applied column. You
   can also click the |Wrench| **Wrench** icon, and choose **Select
   folders**.
#. Click the box next to the folder(s) you want the metadata template
   applied to.
#. To apply the metadata template to nested folders, switch the **Apply
   to Nested** toggle for the parent folder to **Yes**. (Note: The
   toggle will always default to No. The toggle can be updated when
   changing the metadata templates for a specific folder.)
#. Click **Save**.

Option 2:

#. Log into |acquia-product:dam|.
#. Click the downward-pointing triangle |Downward arrow| next to the
   appropriate folder in the folder tree and select **Edit**.
#. At the bottom of the dialogue window, choose a template from the
   **Apply metadata template** dropdown. You can also choose to **Apply
   settings to all nested folders** with the checkbox.
   |Metadata for folder|
#. Click **Save**.

.. _asset:

Apply a metadata template to an asset
-------------------------------------

Admins and contributors can apply a metadata template to assets.

#. Log into |acquia-product:dam|.
#. Select the asset you want to edit.
#. In the actions toolbar, click the |Edit| **Edit** or |Batch edit|
   **Batch Edit** icons, and select **Edit metadata**.
#. Select a metadata template in the dropdown menu.
#. You can then make changes to the values as needed.
#. If the metadata should apply (will be added to any pre-existing
   metadata) to only one asset in the set, use the dropdown to **Apply
   to this Asset Only**.
#. If the metadata should be apply to all assets in the set, use the
   dropdown to **Append to all**.
#. If the metadata is replacing all existing metadata (overwrites any
   pre-existing metadata), select **Replace All**:
   |Replacing metadata|
#. Click **Save**.

.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 30px
.. |Wrench| image:: https://cdn2.webdamdb.com/100th_sm_24n8wRX5SH32.png?1526475691
   :width: 24px
   :height: 21px
.. |Downward arrow| image:: https://cdn4.webdamdb.com/100th_sm_w5hXi5f4ij44.png?1526475856
   :width: 21px
   :height: 20px
.. |Metadata for folder| image:: https://cdn2.webdamdb.com/1280_Q2kwr9HE6AL4.png?1526475657
   :width: 550px
   :height: 398px
.. |Edit| image:: https://cdn2.webdamdb.com/100th_sm_2xhR0XmxWk21.png?1526475528
   :width: 21px
   :height: 21px
.. |Batch edit| image:: https://cdn2.webdamdb.com/100th_sm_wuqdHlA6cO38.png?1526475845
   :width: 23px
   :height: 23px
.. |Replacing metadata| image:: https://cdn2.webdamdb.com/1280_YGsIXkQBN31.png?1526475494
   :width: 550px
   :height: 111px

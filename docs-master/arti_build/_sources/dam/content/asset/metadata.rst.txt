.. include:: /common/global.rst

Managing assets' metadata
=========================

*Metadata* is the information used to describe an asset. Metadata not
only enhances searchability, but also tracks key pieces of information
such as copyright, location, image source, and more.

Admins and contributors with `Edit asset
permission </dam/admin/users#role>`__ for a folder can edit metadata.
Metadata fields `must be active </dam/admin/metadata>`__ to display in
|acquia-product:dam|. It is important that your metadata is consistent
for it to be useful. Tools such as keyword taxonomies, and presenting
your users select lists of approved terms instead of freeform text input
fields, can assist with keeping your metadata consistent. We recommend
that you follow `Metadata best practices </dam/admin/metadata/best>`__
for your metadata.

In |acquia-product:dam|, you can manage your metadata in multiple ways:

-  Editing metadata for a `single asset <#single>`__ and
   `multiple <#multiple>`__ assets
-  `Enabling suggested keywords <#enable>`__
-  `Using suggested keywords <#use>`__

.. note::
  Writing metadata to video is supported for most file formats except MPG,
  MPEG, and M2V.

.. _single:

Editing metadata for a single asset
-----------------------------------

To edit metadata for a single asset, complete the following steps:

#. Sign in to |acquia-product:dam|.
#. In the folder hierarchy on the left side of the page, browse to find
   the asset that you want to edit and select it by clicking on it. (You
   can also enter keywords in the **Search** box on the upper left side
   of the page, then click the **magnifying glass** icon.) The asset
   metadata will display in the **Details** panel on the right side of
   the page.
#. Click **View fields** to display all active metadata fields.
#. Click in the space to the right of the metadata field to begin
   editing.

   |Editing metadata|

#. To save, click the **check mark** |Check mark| icon or click to
   another field.

.. _multiple:

Editing metadata for multiple assets
------------------------------------

To edit metadata for multiple assets, complete the following steps:

#. Sign in to |acquia-product:dam| and select the assets you want to
   edit (for multiple assets, hold down the ``Control`` key on a PC or
   the ``Command`` key on a Mac).
#. Click **Edit** |Edit|. (You can also click the **Pencil** |Pencil
   icon| icon, then select **Edit metadata**.) The selected images will
   open in the **Edit metadata** modal dialog with the metadata for the
   first image in the selection set displayed:

   -  To view and edit the metadata for a different asset in the set,
      click the asset.
   -  To update a metadata field, enter data into the field.

#. Click the dropdown next to the new value you entered and select one
   of the following:

   -  **Apply to this Asset Only** - Apply the metadata only to the
      current asset. This is the default.
   -  **Append to All** - Add the new metadata to any existing metadata
      for the asset selection set.
   -  **Replace All** - Overwrite any pre-existing metadata for the
      asset selection set.

#. Click **Save**.

You can also add or update metadata to your assets in bulk using
`Acquia's metadata mapping service </dam/services/metadata>`__, where we
map your desired metadata to the assets you have stored in
|acquia-product:dam|.

.. _keywords:

Suggested keywords
------------------

The **Suggested keywords** feature scans your images and uses machine
learning to return a set of recommended words for tagging those images.
It can help expedite tagging in |acquia-product:dam|, and help
standardize the keywords used across your organization. Suggested
keywords can be used for image files that are 256px or larger; video
files are not supported. See `Supported file
formats </dam/admin/system/files>`__ for a full list of supported file
types.

.. _enable:

Enabling suggested keywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Admins can enable or disable suggested keywords. To manage suggested
keywords, complete the following steps:

#. Sign in to |acquia-product:dam|.
#. Click the **Settings** |Settings icon| icon, and then click **System
   preferences**.
#. In the **Assets** section, select the **Allow suggested keywords**
   check box.
#. De-select **Enforce keyword taxonomy** for suggested keywords to
   display.

   |Save metadata|

#. Click **Save**.

.. _use:

Using suggested keywords
~~~~~~~~~~~~~~~~~~~~~~~~

To use suggested keywords, complete the following steps:

#. Sign in to |acquia-product:dam|.
#. Select the `single asset <#single>`__ or `multiple
   assets <#multiple>`__ you'd like to tag.
#. Under **Suggestions**, click the **plus sign ( + )** next to the
   keyword that you want to add to the asset, or click **ADD ALL** to
   add all suggestions.

   .. note::
      You can still manually add keywords by typing them into the **Add a
      keyword** field, separating keywords with a comma, or by clicking
      **View Keyword List** to add from your keyword taxonomy.

#. Click the dropdown next to the new value you entered and select one
   of the following options:

   -  **Apply to this Asset Only** - Apply the metadata only to the
      current asset. This is the default.
   -  **Append to All** - Add the new metadata to any existing metadata
      for the asset selection set.
   -  **Replace All** - Overwrite any pre-existing metadata for the
      asset selection set.

#. Use the arrows on the asset preview to scroll through your other
   assets, and repeat the process of selecting your desired keywords if
   your assets require different tags.
#. Click **Save**.
#. After you have tagged all assets, click **Close**.

|Keyword selections|

.. |Editing metadata| image:: https://cdn3.webdamdb.com/md_2tUQ6nRhVRZ3.png?1526476068
   :width: 450px
   :height: 523px
.. |Check mark| image:: https://cdn2.webdamdb.com/100th_sm_UovxmkK2g4L8.png?1526475856
   :width: 30px
   :height: 30px
.. |Edit| image:: https://cdn4.webdamdb.com/100th_sm_MV9ttWvwLeG1.png?1526475897
   :width: 30px
   :height: 29px
.. |Pencil icon| image:: https://cdn4.webdamdb.com/100th_sm_K79Fu3YB0P61.png?1526475582
   :width: 30px
   :height: 30px
.. |Settings icon| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 31px
.. |Save metadata| image:: https://cdn3.webdamdb.com/md_pklQeHTFy961.png?1526475671
   :width: 550px
   :height: 275px
.. |Keyword selections| image:: https://cdn4.webdamdb.com/md_ISxLvhxKiex7.png?1526475705
   :width: 512px
   :height: 248px

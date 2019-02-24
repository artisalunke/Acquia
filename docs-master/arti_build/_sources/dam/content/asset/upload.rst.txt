.. include:: /common/global.rst

Uploading or editing assets
===========================

.. toctree::
   :hidden:
   :glob:

   /dam/content/asset/upload/*

Admins and contributors with upload permission for a folder can upload
assets.

After signing in to |acquia-product:dam| and clicking the folder you
want to upload assets to, you can upload assets using the following
methods:

-  Drag assets from your computer and drop them into
   |acquia-product:dam|, in the thumbnail view.
-  Click **Upload** on the actions toolbar and either drag and drop
   assets from your computer into the uploader or click **Select files
   to upload** to browse and select files on your computer to upload.
-  By using `Box </dam/integrate/box>`__ or
   `Dropbox </dam/integrate/dropbox>`__.

You can minimize the upload window to continue working in
|acquia-product:dam| while assets are uploading.

|Upload window|

After the assets are uploaded, they may appear with an **Asset
processing** thumbnail. While assets are processing, preview thumbnails
are being generated and metadata is being indexed. This may take a few
minutes.

.. note::
  Assets that are still processing are inactive. For more information
  about asset statuses, see `Changing an asset's
  status </dam/content/asset/status>`__.

.. _options:

Additional asset edit options
-----------------------------

#. Sign in to |acquia-product:dam| and select the asset.
#. Click the pencil icon |Pencil| on the actions toolbar or the asset
   thumbnail.
#. Select the edit option:

   -  You can also rename the asset by clicking the filename in the
      asset details panel. Click the check mark |Check mark| to save.
   -  The duplicate asset will display in the folder with “Copy of”
      preceding the name. The duplicate asset will include the metadata
      of the original.
   -  Admins and contributors with delete asset permission for a folder
      can delete assets. If an asset was accidentally deleted, `contact
      Acquia Support </support#contact>`__.
   -  You can recreate the thumbnail of an asset that displays Asset
      processing for an extended period of time.
   -  If you apply a watermark to a folder after assets have been
      uploaded, you must recreate the thumbnail in order for the
      watermark to display. This same process applies if you remove a
      watermark from a folder. (`Read more about applying a
      watermark </dam/admin/system#setting>`__.)
   -  Select the file from your computer that you would like to replace
      the asset with. Click **Upload**.

-  **Rename** - Renames an asset.
-  **Duplicate** - Duplicates an asset.
-  **Delete** - Deletes an asset.
-  **Edit expiration** - Allows users to set an `expiration
   date </dam/content/asset/status>`__ for the asset.
-  **Recreate thumbnail** - Reprocesses the asset.
-  **Replace asset file** - Replaces the existing asset and does not
   keep a version history.
-  **Upload new version** - Allows the user to upload a new
   `version </dam/content/asset/version>`__ and review version history.
-  **Set as folder favorite** - Allows users to set the folder favorite
   (the image that displays on the folder thumbnail). Only one asset can
   be set as the folder favorite at a time.
-  **Rotate clockwise and counterclockwise** - Rotates the asset
   thumbnail. After selecting this option, it can take a few minutes for
   the rotated asset to display in |acquia-product:dam|.
-  **Activate and Deactivate** - Updates the `status of the
   asset </dam/brand-connect/publish>`__.
-  **Publish/Unpublish** - Allows users to `publish or unpublish
   assets </dam/brand-connect/publish>`__ to Brand Connect.
-  **Edit Metadata** - Allows users to edit the metadata for assets.
   (Read more about `editing the metadata for
   assets </dam/content/asset/metadata>`__.)

.. |Upload window| image:: https://cdn2.webdamdb.com/1280_AXO0cQS9kL31.png?1526476073
   :width: 550px
   :height: 346px
.. |Pencil| image:: https://cdn2.webdamdb.com/100th_sm_K79Fu3YB0P61.png?1526475582
   :width: 30px
   :height: 30px
.. |Check mark| image:: https://cdn4.webdamdb.com/100th_sm_UovxmkK2g4L8.png?1526475856
   :width: 30px
   :height: 30px

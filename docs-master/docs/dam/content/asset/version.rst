.. include:: /common/global.rst

Asset version control
=====================

.. container:: message-status

  *This feature is available only to |acquia-product:dam| Professional
  subscribers.*

You can view and manage current and previous versions of assets in
|acquia-product:dam|.

.. _view:

Viewing versioned assets
------------------------

In |acquia-product:dam|, versioned assets will display a version number
next to the file name on the asset thumbnail and in the asset details
panel.

In |acquia-product:bc|, users will only see the latest version — they
won’t be able to view version history or an indication of versioning.

|Versioning example|

.. _history:

Version history
---------------

You can view thumbnails of all previous versions of an asset along with
upload dates and comments.

#. Sign in to |acquia-product:dam|, and then select the asset.
#. From the asset details page, click **Versions** on the actions
   toolbar.
#. The current and previous versions of the asset will display. You can
   comment on the current or previous version and view, download,
   restore and delete previous versions.

   |Versioning list|

#. When finished, click **Done**.

.. _automatic:

Automatic versioning
--------------------

When an asset is uploaded with the same filename as a previously
uploaded asset, automatic versioning adds the asset as a new version of
the previous one. Both files remain in |acquia-product:dam|.

#. Sign in to |acquia-product:dam|.
#. Click on the top navigation and select System Preferences.
#. In the **Assets** section, configure the setting:

   -  Version uploaded assets with the same name: When enabled, an asset
      uploaded to a folder where its filename already exists will be
      added as a new version of that asset.

      -  When the setting is disabled, the newly uploaded asset’s
         filename will append with “_1” when uploaded to a folder where
         its filename already exists.

#. You also have the option to apply metadata from the new version or
   the current version:

   -  If you want to retain the metadata from the original asset, choose
      the **Apply metadata from current version** option.
   -  If you want to save the metadata from the newly uploaded version,
      choose the **Apply metadata from new version** option.

#. Click **Save**.

|Versioning preferences|

.. _manual:

Manual versioning
-----------------

Admins and contributors with upload permission for a folder can manually
version assets.

#. Sign in to |acquia-product:dam| and select the asset.
#. From the asset details page, click in the actions toolbar and select
   **Add version**.

   |Versioning toolbar|

#. Click **Choose file** and enter a comment (optional).

   |Upload version|

#. Click **Upload**.

.. |Versioning example| image:: https://cdn4.webdamdb.com/md_guvTjEImA81.png?1526475977
   :width: 400px
   :height: 448px
.. |Versioning list| image:: https://cdn3.webdamdb.com/md_2MlTyoRjnpS9.png?1526475812
   :width: 500px
   :height: 375px
.. |Versioning preferences| image:: https://cdn3.webdamdb.com/md_gcElinWcHKu6.jpg?1526475674
   :width: 500px
   :height: 341px
.. |Versioning toolbar| image:: https://cdn2.webdamdb.com/md_MAjTgVEKkm81.jpg?1526476048
   :width: 550px
   :height: 96px
.. |Upload version| image:: https://cdn4.webdamdb.com/md_cE80KNcIDXh8.png?1526475761
   :width: 550px
   :height: 299px

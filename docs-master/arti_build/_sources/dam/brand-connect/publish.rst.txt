.. include:: /common/global.rst

Publishing folders and assets
=============================

To display folders and assets in |acquia-product:bc|, they first need to
be published by an admin or contributor with publish permission. For
more information about permissions, see `Managing users and
groups </dam/admin/users>`__.

This documentation page covers:

-  `Manually publishing folders and assets <#publish>`__
-  `Unpublish folders and assets <#unpublish>`__
-  `Publishing folders and assets upon activation <#auto>`__
-  `Publish folders and assets by date <#date>`__
-  `Publish rules <#rules>`__

.. _publish:

Manually publish folders and assets to |acquia-product:bc|
----------------------------------------------------------

To manually publish folders and assets, perform the following steps:

#. Sign in to |acquia-product:dam|, and then navigate to the folder or
   asset you want to publish.
#. Click the **Publish** |Publish icon| icon. You can also click the
   **Pencil** icon |dam-icon-pencil-blue.png| and select **Publish /
   Unpublish**. Light gray **Publish** icons indicate that the folder or
   asset is not published, while a dark gray **Publish** icon indicates
   that the folder or asset is published.
#. Select the |acquia-product:bc| portal that you would like to publish
   to, and whether you would like to also publish subfolders.
#. Click **Save**.

.. _unpublish:

Unpublish folders and assets
----------------------------

If you no longer need an asset, you can remove it from display.

#. Sign in to |acquia-product:dam|, and then navigate to the folders or
   assets that you want to unpublish.
#. Click the **Publish** icon |publish/unpublish icon|. You can also
   click the **Pencil** icon |dam-icon-pencil-blue.png|, and then click
   **Publish / Unpublish**. Light gray **Publish** icons indicate that
   the folder or asset is not published, while a dark gray **Publish**
   icon indicates that the folder or asset is published.
#. Select the **X** next to the |acquia-product:bc| portal that you
   would like to unpublish to and whether you would like to also
   unpublish subfolders.
#. Click **Save**.

.. _auto:

Publishing folders and assets upon activation
---------------------------------------------

Admins may set their folders and assets to publish to
|acquia-product:bc| upon activation.

.. container:: message-status

  This feature is available only to |acquia-product:bc| subscribers who
  are also |acquia-product:dam| Professional subscribers.

#. Sign in to |acquia-product:dam|, then click **Brands** in the top
   navigation.
#. Click the brand you want to configure.
#. In the top navigation, select **Settings**.
#. Check the box to publish folders and assets upon activation.

Now when you activate an asset or folder, it is published. In order for
folders and assets to be published upon upload, ensure that the default
status of folders and assets is **Active** under the System Preferences.

.. _date:

Publishing folders and assets by date
-------------------------------------

.. container:: message-status

  This feature is available only to |acquia-product:bc| subscribers, and
  not to users of the version of |acquia-product:bc| included with
  |acquia-product:dam| Standard or Professional subscriptions.

This feature gives admins and contributors with publish permissions the
ability to schedule a day and time to publish an asset or folder to
|acquia-product:bc|. As an example, you’re launching a new product. The
campaign materials and product photos are uploaded, but they cannot be
launched to the broader audience until a specific date.

#. Sign in to |acquia-product:dam| and navigate to the folder(s) or
   asset(s) you’d like to schedule.
#. Click the **Publish** |Publish icon| icon. You can also click the
   **Pencil** |dam-icon-pencil-blue.png| icon and select **Publish /
   Unpublish**.
#. Select the |acquia-product:bc| portal that you’d like to publish to
   and whether you’d like to also publish subfolders.
#. The folders/assets will default to publishing immediately. Click
   **Change**.
#. Enter the day and time that you’d like to have the folder(s) or
   asset(s) published. The time zone used is based on your computer’s
   time zone settings.
#. Click **Schedule**.
#. Click **Edit** to update the publish day and time, or click
   **Cancel** to delete.

.. _rules:

Publish rules
-------------

Published folders and assets follow specific rules.

-  Newly uploaded, created or moved assets and folders inherit publish
   status from its parent folder. Exceptions can occur in
   |acquia-product:bc| Basic accounts when the asset publish limit has
   been reached.
-  You can manually publish an asset or nested folder residing in an
   unpublished folder. This action will display only the selected asset
   (or nested folder) and its parent folder(s) in |acquia-product:bc|.
-  Individual assets in a published folder cannot be manually
   unpublished.
-  Inactive assets and folders won’t be published in
   |acquia-product:bc|. If you deactivate a published folder or asset,
   it will be unpublished.

.. |Publish icon| image:: https://cdn4.webdamdb.com/100th_sm_wSpfnfnfBvT5.png?1526475704
   :width: 25px
   :height: 25px
.. |dam-icon-pencil-blue.png| image:: https://cdn3.webdamdb.com/100th_sm_k9G4c1INbMi5.png?1526476066
   :width: 21px
   :height: 21px
.. |publish/unpublish icon| image:: https://cdn4.webdamdb.com/100th_sm_wSpfnfnfBvT5.png?1526475704
   :width: 25px
   :height: 25px

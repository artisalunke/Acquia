.. include:: /common/global.rst

Obtaining notifications and alerts
==================================

You can obtain notifications for asset-related activities — such as new
assets uploaded, new versions added, and assets expiring — by using the
watch and notifications functions in |acquia-product:dam|. This ensures
that you are always aware of and using the latest approved assets.

Each user can configure the types of notifications they want to receive
and how they want to receive them.

.. _types:

Types of notifications and alerts
---------------------------------

You can choose to receive notifications for the following actions:

-  Asset is created
-  Asset is moved
-  Asset is deleted
-  A new version is created
-  An asset expires
-  An asset is modified
-  A comment is added
-  A Lightbox is updated

.. _watch:

Managing your asset watch settings
----------------------------------

To enable or disable a watch on particular assets, folders, or
lightboxes, complete the following steps:

#. Sign in to |acquia-product:dam|.
#. Select the asset(s), folder(s), or lightbox.
#. In the asset details panel, click the watch icon |Watch| to toggle
   its watch status.

   -  |Watch| - Asset is being watched
   -  |Unwatched| - Asset is not being watched

To watch certain assets, refer to the following section.

.. _configure:

Configuring notifications and alerts
------------------------------------

To configure the notifications and alerts that |acquia-product:dam|
generates based on asset or lightbox events, complete the following
steps:

#. Sign in to |acquia-product:dam|.
#. Click the bell icon |Bell icon| in the bottom-right toolbar, and then
   click **View all**.
#. Click **Change Settings**.
#. Select the check box in the corresponding column for each action to
   receive an in-system alert, email, or both. Alerts display both on
   the |acquia-product:dam| homepage and in the notification panel,
   which can be found by clicking the bell icon |Bell icon|.
#. To watch groups of assets, in the **Watch assets if** section, select
   from the following options:

   -  **I uploaded them** - Assets that you upload
   -  **I downloaded them** - Assets that you download
   -  **All assets**

#. Click **Save**.

|Notification settings|

To watch individual assets or folders, click the watch icon.

|Notification watch|

.. _admin:

Setting admin-specific alerts
-----------------------------

In addition to the above notifications, admins can choose to receive
additional alerts — such as when a new user registers or when someone
downloads an asset. For more information about these alerts, see
|config prefs|_

.. |config prefs| replace::
  Configuring your \ |acquia-product:dam|\  system preferences
.. _config prefs: /dam/admin/system

.. |Watch| image:: https://cdn4.webdamdb.com/100th_sm_cAZygugBoO70.png?1526475935
   :width: 25px
   :height: 20px
.. |Unwatched| image:: https://cdn2.webdamdb.com/100th_sm_UQVrh3uNMQ02.png?1526475990
   :width: 24px
   :height: 22px
.. |Bell icon| image:: https://cdn4.webdamdb.com/100th_sm_s8drB3U8m6w0.png?1526475706
   :width: 23px
   :height: 23px
.. |Notification settings| image:: https://cdn3.webdamdb.com/100th_sm_c95YGVNszl43.png?1526476073
   :width: 450px
   :height: 470px
.. |Notification watch| image:: https://cdn4.webdamdb.com/1280_GNzxfjn7QI88.jpg?1526476094
   :width: 416px
   :height: 255px

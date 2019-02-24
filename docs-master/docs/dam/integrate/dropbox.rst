.. include:: /common/global.rst

Integration: Dropbox
====================

The Dropbox Integration makes it easy to move files under 5GB back and
forth between |acquia-product:dam| and Dropbox. You can use this
integration to quickly centralize assets stored in various personal
Dropbox accounts, and distribute files to people who don’t have access
to your DAM. Acquia recommends you `upload files larger than 5GB using
FTP </dam/content/asset/upload/ftp>`__ (File Transfer Protocol).

This integration is available to Enterprise and Professional users with
download and/or upload access in |acquia-product:dam| core, but first
must be enabled by your admin.

.. _enable:

Enable the Dropbox integration (admins)
---------------------------------------

#. Click the |Settings| **Settings** icon in the top navigation and
   select System Preferences.
#. In the **Cloud Sharing Settings** section, click the **Cloud sharing
   channels** box and choose **Dropbox**.
   |Cloud sharing settings|
#. Click **Save**.

.. _todropbox:

Sending assets to Dropbox
-------------------------

Regular users and contributors with download access can start sending
assets to Dropbox once the admin has enabled the integration.

#. Log in to |acquia-product:dam|.
#. Click an asset to get to the asset details page, then click the
   |Share| **Share** icon in the actions toolbar.
#. Choose **Dropbox** from the dropdown menu.
   |Select Dropbox|
#. The first time you choose to send an asset to Dropbox, you'll need to
   click **Add Integration**.
#. Log in with your Dropbox credentials.
#. In the pop-up, create a new Dropbox folder or choose an existing one.
#. Click **Send** – the file will go to the selected folder.
   |Send to Dropbox|

You can use a lightbox to send multiple assets to Dropbox at once:

#. Add the assets you would like to send to a lightbox. (Learn more
   about `lightboxes here </dam/content/lightbox>`__.)
#. Click the |Share| **Share** icon in the actions toolbar.
#. Choose **Dropbox** from the dropdown menu.
#. In the pop-up, create a new Dropbox folder or choose an existing one.
#. Click **Send** – the files will go to the selected folder.

.. _fromdropbox:

Uploading assets to |acquia-product:dam|
----------------------------------------

To send assets from Dropbox to |acquia-product:dam|, you'll need to have
upload permission in |acquia-product:dam|.

#. Select the folder where the assets will be uploaded to.
#. Click **Upload** in the actions toolbar. Note: If you do not see the
   **Upload** option, you may not have the appropriate permissions to
   upload (ask your |acquia-product:dam| admin to change this setting)
   or you have not selected a folder.
#. Select the **Dropbox** tab and click the **Choose from Dropbox**
   button.
   |Choose from Dropbox|
#. Select the asset(s) you wish to upload to |acquia-product:dam| and
   click **Choose**.
#. Click **Minimize** to continue working in the system while your
   upload is processing.
#. The newly uploaded files will appear in the folder as **Asset
   Processing** while the preview thumbnail is being generated.

.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 30px
.. |Cloud sharing settings| image:: https://cdn2.webdamdb.com/md_Y21X0DBnr2H7.jpg?1526475726
   :width: 474px
   :height: 218px
.. |Share| image:: https://cdn2.webdamdb.com/100th_sm_UuE2e2Ggqx91.png?1526475526
   :width: 23px
   :height: 20px
.. |Select Dropbox| image:: https://cdn4.webdamdb.com/md_2a9MeAMad9M8.png?1526475508
   :width: 528px
   :height: 194px
.. |Send to Dropbox| image:: https://cdn2.webdamdb.com/md_kTp6joQzVmi9.png?1526476042
   :width: 450px
   :height: 346px
.. |Choose from Dropbox| image:: https://cdn4.webdamdb.com/md_YoojdJpLm851.jpg?1526476101
   :width: 450px
   :height: 282px

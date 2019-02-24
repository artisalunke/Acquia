.. include:: /common/global.rst

Using FTP to upload assets
==========================

You can use FTP (File Transfer Protocol) to upload both assets and
folders to your |acquia-product:dam| account. (`Read more about
uploading assets via drag and drop </dam/content/mobile/manage>`__.) FTP
is the only way to upload assets greater than 5 GB in size.

To upload assets using FTP, you’ll need to use a third-party FTP client
such as FileZilla, Cyberduck or SmartFTP.

.. note::
  The FTP server is limited to processing a maximum of 250 GB at a time.
  If you’re importing more than 250 GB, you will need to break it up into
  separate imports. FTP imports may take up to 24 hours to fully load into
  |acquia-product:dam|.

.. _ftp:

Upload assets/folders with FTP
------------------------------

Using the FTP credentials you received from your Account Manager, upload
the assets or folders to your FTP server:

#. Open the FTP client and create a new site, if necessary.
#. Enter the following credentials:

   -  *Host* - ``ftp.acquiadam.com``
   -  *Username* - Your FTP username, which is not the same as your
      |acquia-product:dam| username
   -  *Password* - Your FTP password, which is not the same as your
      |acquia-product:dam| password
   -  *Port* - 21

#. Once connected, add the assets or folders into the FTP queue.
#. Once the FTP queue is finished processing, you can `upload assets and
   folders to |acquia-product:dam| <#upload>`__.

.. _upload:

Upload assets/folders to |acquia-product:dam|
---------------------------------------------

After the assets are uploaded to the FTP server, admins and contributors
with upload permissions to a folder can upload the assets and folders to
|acquia-product:dam|.

#. Log in to |acquia-product:dam| and navigate to the folder you want to
   upload assets or folders to. (If uploading folders, you can also
   click the **Home** folder to import the folders as top-level parent
   folder.)
#. Click **Upload** on the actions toolbar then select the **FTP
   import** tab.
#. There will be a dropdown for folders and assets with the number in
   each displayed. Check the box next to the assets and folders you want
   to import or click the box next to the dropdown to select all.
#. Click the **Import** button.
#. An email and in-system notification will be sent once the FTP import
   is complete.

|FTP import window|

.. |FTP import window| image:: https://cdn2.webdamdb.com/1280_sJzxeF53ysi3.png?1526476067
   :width: 550px
   :height: 345px

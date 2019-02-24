.. include:: /common/global.rst

Integration: Box
================

The Box integration makes it easy to move files back and forth between
|acquia-product:dam| and Box. You can use it to quickly centralize
assets stored in various personal or professional Box accounts, and to
distribute files to people who do not have access to
|acquia-product:dam|.

This integration is available to *Admin*, *Contributor*, and regular
users with download or upload permissions. You can transfer assets
smaller than 5GB — assets greater than 5GB must use FTP.

.. _enable:

Enabling the integration
------------------------

*The information in this section applies only to users that have
`*Admin* <#role>`__ role type permissions.*

#. Sign in to |acquia-product:dam|.
#. Click the **Settings** icon |Settings| in the top navigation, and
   then click **System Preferences**.
#. In the **Cloud Sharing Settings** section, click the **Cloud sharing
   channels** field, and then click **Box**.
#. Click **Save**.

|Sharing|

.. _tobox:

Sending assets to Box
---------------------

Users with download access can start sending assets to Box once the
administrator has enabled the integration:

#. Sign in to |acquia-product:dam|.
#. Click an asset to get to the asset details page.
#. Click |Sharing| **Show Sharing Options** in the actions toolbar and
   select **Box** from the dropdown menu.

   |Select 'Box'|

#. The first time you send an asset to Box, you will need to click **Add
   Integration**.
#. Sign in with your Box credentials.
#. In the dialog box, create a new Box folder or choose an existing one.
#. Click **Send**. The will file go to the selected folder.

You can use a a lightbox to send multiple assets to Box at once:

#. Add the assets that you want to send to a lightbox.
#. Click the **Share** icon |Share icon| in the actions toolbar, and
   then click **Box**.
#. In the dialog box, create a new Box folder or choose an existing one.
#. Click **Send**. The will file go to the selected folder.

.. _frombox:

Sending Box assets to |acquia-product:dam|
------------------------------------------

To send assets or folders from Box to |acquia-product:dam|, you will
need to have upload permission in |acquia-product:dam|.

#. Sign in to your Box account.
#. Go to https://app.box.com/apps and search for Webdam.
#. Select the Webdam app and add it to your account.
#. From the main page of your Box account, click the **more actions**
   icon |More actions| next to the folder or asset that you want to
   send, and then click **More Actions > Send file to Webdam**.
#. You will initially need to enter your |acquia-product:dam|
   credentials.
#. Choose the folder to send to. The asset will be queued for import.

The newly uploaded files will appear in the folder as *Asset Processing*
while the preview thumbnail is generating.

.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :width: 30px
   :height: 30px
.. |Sharing| image:: https://cdn4.webdamdb.com/md_YEJu2wZg8678.png?1526475505
   :width: 550px
   :height: 200px
.. |Sharing| image:: https://cdn4.webdamdb.com/100th_sm_EiLNr1SJUlN8.png?1526475843
   :width: 23px
   :height: 20px
.. |Select 'Box'| image:: https://cdn2.webdamdb.com/md_EugFGvjNau71.png?1526475832
   :width: 528px
   :height: 168px
.. |Share icon| image:: https://cdn4.webdamdb.com/100th_sm_UuE2e2Ggqx91.png?1526475526
   :width: 23px
   :height: 20px
.. |More actions| image:: https://cdn3.webdamdb.com/100th_sm_YinNFBrBKHj5.png?1526475648
   :width: 26px
   :height: 18px

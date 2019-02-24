.. include:: /common/global.rst

Configuring your |acquia-product:dam| system preferences
========================================================

.. toctree::
   :hidden:
   :glob:

   /dam/admin/system/*

To configure the preferences for your |acquia-product:dam|
implementation, complete the following steps:

#. Sign in to |acquia-product:dam| with administrative privileges.
#. In the top right of the page, click the settings icon |Settings|.
#. Clicking **System Preferences**.

|acquia-product:dam| will display the system preferences page that you
can use to configure your image and user handling options.

.. _avail:

Available settings
------------------

The |acquia-product:dam| system preferences page provides access to the
following functions, by section:

-  `General Settings <#general>`__
-  `Users and Groups <#users>`__
-  `Assets <#assets>`__
-  `Supported File Extensions <#extensions>`__
-  `Folders <#folders>`__
-  `Downloads <#downloads>`__
-  `Search <#search>`__
-  `Image Download Presets <#imagepresets>`__
-  `Video Download Presets <#videopresets>`__
-  `Cloud Sharing Settings <#cloud>`__
-  `Asset Approval <#approval>`__

.. _general:

General Settings
~~~~~~~~~~~~~~~~

-  **Admin email notification address** – Email notifications listed in
   the system preferences (such as when new users register, email
   notification of upload and download, etc.) will be sent to this email
   address.
   If you will have multiple account administrators who will need to
   receive these notifications, we recommend creating an email
   distribution list—such as ``dam@example.com``—that includes all
   admins.
-  **Enable Early Access for product features on this account** check
   box – Early Access is a great way to stay on the cutting edge of new
   |acquia-product:dam| features and capabilities. When enabled, Early
   Access features will automatically be enabled for the account.
-  **I would like to learn about participating in Beta programs for
   product features** check box – Participating in |acquia-product:dam|
   Beta programs allows you to have a voice in the evolution of
   |acquia-product:dam| products. By selecting this check box, you agree
   to be contacted by the |acquia-product:dam| Product team to
   participate in upcoming Beta tests. As a participant, you’ll gain
   early access to new features while also agreeing to provide feedback
   on performance.

.. _users:

Users and Groups
~~~~~~~~~~~~~~~~

-  **Allow users to self-register** check box – When enabled, a
   registration link will display on the sign in page. This will allow
   new users to register for an account.
-  **Notify when new user registers** check box – When enabled, an email
   notification with the registrant’s information will be sent to the
   admin email notification address.
-  **New users must be approved after registering** check box – When
   enabled, users registering for an account will be added as
   **inactive**. This means they will not be able to sign in to
   |acquia-product:dam| until after an admin activates them. For more
   information, see `Managing users and groups </dam/admin/users>`__.
   You can also use this setting for customers with authentication
   integration. When enabled, users accessing |acquia-product:dam| for
   the first time through the company’s authentication system will be
   added to |acquia-product:dam| as inactive.
-  **Automatically expire passwords after 90 days** check box – When
   enabled, users will need to reset their password every 90 days.
-  **Display the following click-on agreement on registration** – Click
   the **edit** link to enter terms and conditions that users must agree
   to when registering for an account. (Read more about `terms and
   conditions sample language </dam/admin/tos>`__.)
-  **Session expiration time** list – Click the value for the duration
   of inactivity that can occur before the system requires the user to
   sign in again.

Assets
------

-  **Activate assets upon creation** – Set the
   `status </dam/content/asset/status>`__ of newly uploaded assets to
   active or inactive.
   In most instances, the status will be active. Contact your customer
   success manager for best practices.
-  **Default asset name on upload** – Set the displayed asset name to
   match the file name or pull from the headline metadata field.
-  **Auto rotate assets on upload** check box – When enabled, assets
   will automatically be rotated to the correct orientation during the
   upload process.
-  **Receive email notification of uploads** check box – When enabled,
   an email will be sent to the admin email notification address when
   new assets are uploaded to |acquia-product:dam|.
-  **Version uploaded assets with same name** check box – For
   information about this option, see `Asset version
   control </dam/content/asset/version>`__.
-  **Apply metadata from** – Select from the **New version** or
   **Current version** options. For information about this option, see
   `Asset version control </dam/content/asset/version>`__.
-  **Allow suggested keywords** check box – For information about this
   option, see `Configuring the metadata
   schema </dam/admin/metadata>`__.
-  **Enable keyword taxonomy** check box – For information about this
   option, see `Configuring the metadata
   schema </dam/admin/metadata>`__.
-  **Enforce keyword taxonomy** check box – For information about this
   option, see `Configuring the metadata
   schema </dam/admin/metadata>`__.
-  **Deactivate asset upon expiration** check box – When enabled, assets
   will automatically become inactive on their expiration date. If not
   enabled, assets will remain active after expiration but will not be
   downloadable by any non-admin user.
-  **Receive email upon asset expiration** check box – If this option is
   enabled, an email will be sent to the admin email notification
   address when the asset expires.
-  **Receive email reminders before asset expires** - Enable this option
   if you want to be notified of an asset’s upcoming expiration. Then,
   enter the number of days prior to expiration that you’d like to be
   notified.
-  **Source of video thumbnail** – In the list, click the value to use
   for which second of the video you want displayed as the thumbnail.

.. _extensions:

Supported File Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~

Read more about this setting in the documentation on `Supported File
Formats </dam/admin/system/files>`__.

Folders
~~~~~~~

-  **Default status of folders on create** - Set whether you want the
   status of newly created folders to be active or inactive. (Read more
   about `the folder statuses </dam/content/asset/status>`__.)
-  **Keep folders upon FTP import** - When enabled, the folders will
   remain in the FTP client after import. (Read more about `uploading
   assets using FTP </dam/content/asset/upload/ftp>`__.)

Downloads
~~~~~~~~~

-  | **Comp (watermarked) downloads**:

   -  Set to **Allow download for all users** to have the ability to
      download watermarked versions of assets.
   -  Set to **Allow download for logged in users only** for signed-in
      users (therefore not guest users) to have the ability to download
      a watermarked version of the asset.
   -  Set to **DO NOT allow download** if you don’t want any users to
      download a watermarked version of the asset.

   .. note::

      Add a watermark to an asset by ensuring that **Watermark assets in
      this folder** is enabled for the asset's folder. After doing so,
      click the |Edit| **Edit** icon on the asset thumbnail and choose
      **Recreate Thumbnail**.

-  Click-on agreement for downloads:

   -  **Enable click-on agreement** - When enabled, users must agree to
      terms and conditions before downloading assets.
   -  **Require user to agree**:

      -  When set to **Upon first download only**, users must agree to
         the download terms and conditions the first time they download
         an asset.
      -  When set to **For every download**, users must agree to the
         download terms and conditions every time they download an
         asset.

   -  **Click-on agreement text** - Click edit to add the terms and
      conditions language. (Read more about `Terms and Conditions sample
      language </dam/admin/tos>`__.)

-  **Receive email notification of downloads** - When enabled, an email
   will be sent to the admin email notification address when assets are
   downloaded.

   -  This setting is global and will apply to new folders created in
      |acquia-product:dam|. If you change the settings, you will also
      need to change it at the folder level for it to apply to
      previously created folders.

-  **Enable download requests** - When this feature is enabled and a
   group’s download permissions are set to **Do not allow**, users can
   request access to download assets. (Read more about `editing the
   permissions of a group </dam/admin/users>`__.)

   -  This setting is global and will apply to new folders created in
      |acquia-product:dam|. If you change the settings, you will also
      need to change it at the folder level for it to apply to
      previously created folders.

Search
~~~~~~

Read more about this preference in the documentation on `Shutterstock
Search </dam/integrate/shutterstock>`__.

.. _imagepresets:

Image Download Presets
~~~~~~~~~~~~~~~~~~~~~~

Users can convert images to a different file format, resolution, size
and/or color space upon download. Download presets allow you to create
predefined options for your users to choose from when downloading the
assets.

Create:

#. Click **Create New Image Preset**.
#. Enter a preset name.
#. Set the file format, resolution, dimensions and/or color space.
#. Click **Save**.

Additional Information
^^^^^^^^^^^^^^^^^^^^^^

-  **Edit a preset** - Click the edit icon |Edit|.
-  **Delete** - Click the trashcan icon |Trashcan|.
-  If an option is left blank, the file will retain its original setting
   when it is downloaded.
-  **Best practices**:

   -  **Resolution** - The recommended values are 72 dpi for web and 300
      dpi for print.
   -  **Color Space** - RGB is recommended for web use and CMYK is
      recommended for print.

.. _videopresets:

Video Download Presets
~~~~~~~~~~~~~~~~~~~~~~

Users can transcode videos upon download. Download presets allow you to
create predefined options for your users to choose from when downloading
the assets.

#. Click **Create new video preset**.
#. Enter a preset name.
#. Click the dropdown next to **Load preset** to work off a preformatted
   preset. Once selected, the configurations will automatically update.
#. Select the **Format** from the dropdown.
#. Configure the video and audio settings as needed.
#. Click **Save**.

.. _additional-information-1:

Additional Information
^^^^^^^^^^^^^^^^^^^^^^

-  **Edit a preset** - Click the edit icon |Edit|.
-  **Delete** - Click the trashcan icon |Trashcan|.
-  If an option is left blank, the file will retain its original setting
   when it is downloaded.

.. _cloud:

Cloud Sharing Settings
~~~~~~~~~~~~~~~~~~~~~~

Refer to the following documentation for more information:

-  `Social Publishing: Facebook, Twitter and
   YouTube </dam/integrate/social>`__
-  `Box </dam/integrate/box>`__
-  `Dropbox </dam/integrate/dropbox>`__
-  `Wistia </dam/integrate/wistia>`__

.. _approval:

Asset Approval
~~~~~~~~~~~~~~

For information about the options in this section, see `Handling
approval requests </dam/admin/approve>`__.

.. |Settings| image:: https://cdn3.webdamdb.com/100th_sm_QQ4APRDmdze4.png?1526476135
   :class: no-sb
   :width: 30px
   :height: 30px
.. |Edit| image:: https://cdn2.webdamdb.com/100th_sm_2xhR0XmxWk21.png?1526475528
   :width: 21px
   :height: 21px
.. |Trashcan| image:: https://cdn2.webdamdb.com/100th_sm_UBHYDcodQJ12.png?1526475715
   :width: 23px
   :height: 23px

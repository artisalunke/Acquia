.. include:: /common/global.rst

Managing folders
================

Use the procedures on this page to manage the folders that you use in
|acquia-product:dam|.

.. _create:

Creating a folder
-----------------

Admins and contributors with **create folder** permission can create
folders. (If you are unsure of your permissions, ask your
|acquia-product:dam| administrator.)

#. Sign in to |acquia-product:dam|.
#. Click **Home** to add a top-level (parent) folder or click a folder
   to add a nested (child) folder. Folders nested under a parent folder
   must all have unique names.
#. Click the **Add Folder** icon |Add Folder| on the actions toolbar.
#. Enter the folder name.
#. Configure the folder settings, from the following options:

   -  **Watermark assets in this folder** - When enabled, assets in this
      folder will display a watermark in |acquia-product:dam|. If assets
      already exist in the folder, you will need to recreate the
      thumbnail for them to display. (`Read more about recreating
      thumbnails </dam/content/asset/upload>`__.)
   -  **Receive notification of downloads** - When enabled, the admin
      email notification address configured in the `System
      Preferences </dam/admin/system>`__ will receive a notification of
      asset downloads. This setting can also be enabled at the global
      level in the `System Preferences </dam/admin/system>`__.
   -  **Enable download requests** - When enabled and a group’s download
      permissions for this folder are set to *Do not allow*, users can
      request access to download assets. This setting can also be
      enabled at the global level in the `System
      Preferences </dam/admin/system>`__.
   -  **Send download requests to** - The email address where download
      requests should be routed. We recommend that the recipient be an
      admin or contributor.
   -  **Apply Metadata Template** - Click the list to apply a metadata
      template to this folder. (`Read more about metadata
      templates. </dam/content/asset/metadata>`__)
   -  **Apply settings to all nested folders** - Select this check box
      to apply any edited options to nested (children) folders.

#. Click **Save**.

.. _rename:

Renaming or editing a folder
----------------------------

Admins and contributors with *edit folder* access can edit folders. (If
you are unsure of your permissions, ask your |acquia-product:dam|
administrator.)

#. Sign in to |acquia-product:dam|, and then click the folder that you
   want to edit.
#. Click the **Edit** icon |Edit pencil| in the actions toolbar or
   folder details panel, and then click **Edit**.
#. Rename or edit the folder settings. (For more information, see the
   `previous procedure <#create>`__.)
#. Click **Save**.

.. _move:

Moving a folder
---------------

Admins and contributors with *move* permission can move folders. (If you
are unsure of your permissions, ask your |acquia-product:dam|
administrator.)

#. Sign in to |acquia-product:dam|, and then select one or more folders
   that you want to move.
#. Drag the folder to its new parent folder in the folder tree to the
   left of the page. |acquia-product:dam| will display one of the
   following icons for the folder:

   -  |Can Move|  **Can Move** icon - Displayed if the folder can be
      moved into the folder
   -  |Can't Move|  **Can't Move** icon - Displayed if the folder cannot
      be moved

After the move is complete, |acquia-product:dam| will display a message
that states ``You successfully moved a folder``.

If you do not have the appropriate permissions to move the folder, an
error message (``Unable to move assets``) will be displayed. Contact
your |acquia-product:dam| administrator regarding your permission
questions.

.. _delete:

Deleting a folder
-----------------

Admins and contributors with *edit folder* access can delete folders.
(If you are unsure of your permissions, ask your |acquia-product:dam|
administrator.)

#. Sign in to |acquia-product:dam|, and then select one or more folders
   that you want to delete.
#. Click the **Edit** icon |Edit pencil| in the actions toolbar or
   folder details panel, and then click **Delete**.
#. Click **Delete** to confirm.

.. important::
  If you delete a folder that contains nested folders, the nested folders
  will also be deleted.

.. |Add Folder| image:: https://cdn4.webdamdb.com/100th_sm_MSS53YlHD2p7.png?1526475918
   :width: 35px
   :height: 27px
.. |Edit pencil| image:: https://cdn2.webdamdb.com/100th_sm_2xhR0XmxWk21.png?1526475528
   :width: 21px
   :height: 21px
.. |Can Move| image:: https://cdn3.webdamdb.com/100th_sm_c6MN37yaEJf7.png?1526476193
   :width: 25px
   :height: 24px
.. |Can't Move| image:: https://cdn4.webdamdb.com/100th_sm_UKohQ6MWtbv9.png?1526475472
   :width: 23px
   :height: 20px

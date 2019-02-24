.. include:: /common/global.rst

Uninstalling the Adobe Creative Cloud connector
===============================================

..  container:: message-status

  This is an add-on feature. Contact your Account Manager to add this
  feature to your subscription.

.. container:: internal-navigation

  **Connector for Adobe Creative Cloud**

  * :doc:`Intro </dam/services/cc>`
  * :doc:`2018 </dam/services/cc/2018>`
  * :doc:`2017 </dam/services/cc/2017>`
  * :doc:`2015 </dam/services/cc/2015>`
  * :doc:`Use </dam/services/cc/use>`
  * Uninstall

Only one version of the |acquia-product:dam| Connector can be active at
a time. Because of this, you must remove any existing
|acquia-product:dam| Connector plug-ins from your InDesign Plug-Ins
folder before installing a ZXP package that contains
|acquia-product:dam| Connector plug-ins.

After the uninstall is complete, you can install the most-recent version
of |acquia-product:dam| Connector for Adobe Creative Cloud.

.. note::
  Because Adobe no longer supports CS6, users with the
  |acquia-product:dam| Connector with CS6 may experience limited
  connectivity and support options.

.. _mac:

macOS users
-----------

#. Quit InDesign, Photoshop and/or Illustrator if it’s open.
#. Open a Finder window.
#. Open your **Library** folder.

   #. Click **Go** on the top navigation and choose **Go to Folder**.
   #. Enter ``~/Library``

#. Navigate through the folder path to
   ``/Library/ApplicationSupport/Adobe/CEP/extensions`` and move the
   ``|acquia-product:dam|CCConnector`` file to the trash.
#. Open your **Applications** folder.
#. Navigate through the folder path to
   ``/Applications/Adobe InDesign CC 201#/Plug-Ins`` and move the
   ``SiliconConnector|acquia-product:dam|`` file to the trash.

.. _windows:

Windows users
-------------

#. Quit InDesign if it’s open.
#. Navigate to ``Control Panel > Programs > Uninstall a Program``.
#. Uninstall |acquia-product:dam|CCConnector 1.0.
#. If you want to retain existing InDesign plug-ins, do not use the
   uninstaller, but go to
   ``\C:\Program Files (x86)\Common Files\Adobe\CEP\extensions\|acquia-product:dam|CCConnector``
   and delete the folder.

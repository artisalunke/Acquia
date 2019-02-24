.. include:: /common/global.rst

Upgrading Acquia Dev Desktop
============================

Use the information on this page to help you upgrade your installed
version of |acquia-product:add|. This includes instructions on
`upgrading your version 2 installation <#upgrade2>`__, `upgrading from
version 1 to version 2 <#upgrade1>`__, or `restoring a previous
version <#restore>`__ if required.

.. _upgrade2:

Upgrading |acquia-product:add| 2
--------------------------------

Starting |acquia-product:add| 2 causes it to check whether an updated
version is available. Click **Yes** to download the new version.

|Update available|

You can check whether an updated version of |acquia-product:add| 2 is
available and upgrade to the new version from within the application. In
the menu, select **Acquia Dev Desktop > Check for Update**.

You do not have to upgrade your installed version of
|acquia-product:add| 2 if a new version of Drupal is released. Each time
you create a new website using |acquia-product:add|, you download and
install the latest version of the Drupal distribution you choose. For
more information, see `Starting from
scratch </dev-desktop/start/new>`__.

.. _upgrade1:

Upgrading from |acquia-product:add| version 1
---------------------------------------------

If you have been using |acquia-product:add| 1 and want to upgrade to
|acquia-product:add| 2:

#. Install |acquia-product:add| 2, following the procedure described in
   `Installing |acquia-product:add| </dev-desktop/install>`__. Make sure
   you install |acquia-product:add| 2 in a different directory from your
   existing |acquia-product:add| 1 installation directory.
#. Start |acquia-product:add| 1 and export any websites you want to use
   with |acquia-product:add| 2. To do this, in the Acquia Dev Desktop 1
   Control Panel, click **Settings > Sites > Export**.
#. Import the websites that you exported from |acquia-product:add| 1,
   following the procedure described in `Starting with an existing local
   site </dev-desktop/start/local>`__.

Restoring a previous installation
---------------------------------

The upgrade process preserves all website databases and configuration
data (including paths and ports numbers). Your previous installation is
backed up in the ``C:\Users\[username]\.acquia\backup`` (Windows) or
``~/.acquia/backup`` (Mac OS) directory. If you need to restore a
previous version of |acquia-product:add| 2, copy the files from the
``backup`` directory over the files in your newest installation.

Note

On Mac OS, the ``/.acquia`` directory is hidden. To locate the
directory, complete the following steps:

#. Open Finder.
#. In the menu bar, select **Go > Go to folder**.
#. Enter the path of the directory and click **Go**.

.. |Update available| image:: https://cdn4.webdamdb.com/1280_gAZFNjZe31.png?1526475695
   :width: 415px
   :height: 161px

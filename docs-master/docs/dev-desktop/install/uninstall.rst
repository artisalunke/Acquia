.. include:: /common/global.rst

Uninstalling |acquia-product:add|
=================================

Important

Before you uninstall |acquia-product:add|, be sure to `back up your
websites </dev-desktop/sites/backup>`__ using **More > Export to Drupal
archive**. This is important because uninstalling |acquia-product:add|
deletes the websites contained by |acquia-product:add|, including your
websites' files and databases.

To uninstall |acquia-product:add|, complete the following steps:

#. In |acquia-product:add|, click **Stop**, and then close
   |acquia-product:add|.
#. Run the uninstallation application. To do this, use the method based
   on your operating system:

   -  *Mac* - Run the uninstall application at
      ``/Applications/DevDesktop/uninstall.app``.
   -  *Windows* - From the Start menu, select **All Programs > Acquia
      Dev Desktop > Uninstall Acquia Dev Desktop**.

#. Follow the provided instructions to uninstall |acquia-product:add|.

The uninstallation process removes the following components installed by
|acquia-product:add|:

-  MySQL server and database, including all website content
-  Drupal codebase and files
-  Apache HTTP server
-  **Windows-only:** XMail server (if installed as part of
   |acquia-product:add|)

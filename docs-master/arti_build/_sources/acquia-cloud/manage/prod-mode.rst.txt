.. include:: /common/global.rst

Using Production mode to protect your live application
======================================================

When you first create an application, the Production environment is in
Pre-launch mode. When you are ready to publish the application, you
should change it to Production mode. In Pre-launch mode, you can freely
drag your files or database to the Production environment. In Production
mode, you cannot copy your files or database to the Production
environment. This protects you from possibly destroying your live
application by overwriting your Production files and databases.

Generally, you copy databases and files up to the Production environment
only until you first launch your application. After that, you push code
to Production, but you pull databases and files backwards from
Production to the Staging and Development environments for testing and
development.

.. _enable:

Enabling Production mode
------------------------

To change your Production environment's mode, complete the following
steps:

#. Sign in to the |acquia-product:ui|, and then select your application.
#. Select the Production environment, and then click the **Production
   mode** icon.
   |Select production mode|
   A dialog box will appear.
#. Click **Enable** to enable production mode.

After you enable production mode, the **Production mode** icon becomes a
closed lock.

.. _disable:

Disabling Production mode
-------------------------

To disable production mode, complete the same procedure `listed
previously <#enable>`__, but click **Disable** in the final step.

.. |Select production mode| image:: https://cdn3.webdamdb.com/md_EJNjJdcPBqL5.png?1526476051
   :width: 309px
   :height: 145px

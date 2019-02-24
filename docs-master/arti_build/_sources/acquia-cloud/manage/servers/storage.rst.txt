.. include:: /common/global.rst

Managing disk storage space
===========================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/manage/servers/storage/*

.. container:: internal-navigation

   **Disk storage in Acquia Cloud**

   * :doc:`About </acquia-cloud/manage/servers/storage/cli>`
   * Manage

If your |acquia-product:ac| application uses its set quantity of
allocated disk storage, your application's database will stop working,
which will cause your application to stop working. You can `check your
disk storage availability from the command
line </acquia-cloud/manage/servers/storage/cli>`__.

.. note::  

   -  |acquia-product:ace| subscribers
       Acquia manages your servers for you, including your disk storage 
       allocation, or you can manage the servers yourself if you have a 
       `Cloud Service Management plan </acquia-cloud/csm>`__.
   -  |acquia-product:acfs| subscribers
       Your disk storage allocation cannot be changed. If you need additional 
       disk storage, you will need to upgrade your subscription. For more 
       information, see `Managing disk storage for |acquia-product:acfs| </acquia-cloud/free/storage>`__.
   -  |acquia-product:acs| subscribers
       Use the procedure following this note.

If you are approaching your storage limit, you should increase the
amount of storage available. Additional disk storage has an additional
cost; for details, see |billing|_. In addition, increasing your disk
storage allocation will make all sites on your server unavailable for 30
minutes or even longer (depending on the size of the disk, how many
files and how much data you have) while the larger disk volume is
provisioned and your data is transferred from the old disk to the new
one. As a rough estimate, the process may take approximately one second
for each 10MB on your existing disk, plus approximately five minutes of
additional setup time.

.. |billing| replace:: About \ |acquia-product:ac|\  Billing: Disk storage
.. _billing: /support/billing

To increase your application's storage allocation, complete the
following steps:

#. `Sign in <https://cloud.acquia.com>`__ to the |acquia-product:ui|,
   select your application and environment, and then click **Servers**
   in the left menu.
#. Click **Resize Disk**.
#. Select the amount of storage you want, check the box to confirm that
   all sites on the server will be down during the upsizing, and click
   **Upgrade**.

   |Upgrade storage|

.. note::  

   You can only increase your storage allocation on the **Servers** page,
   and cannot decrease it.

.. _related:

Related topics
--------------

-  `Managing your servers </acquia-cloud/manage/servers>`__
-  `Improving application performance </acquia-cloud/performance>`__
-  `Managing disk storage for
   |acquia-product:acfs| </acquia-cloud/free/storage>`__

.. |Upgrade storage| image:: https://cdn2.webdamdb.com/1280_A7n3qVimegS4.png?1526475523
   :width: 750px
   :height: 457px

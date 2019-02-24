.. include:: /common/global.rst

Managing disk storage for |acquia-product:acfs| applications
============================================================

|acquia-product:acfs| applications are limited to 1 GB of disk storage
for databases, 1 GB for files, and 1 GB for the codebase. Applications
that exceed the storage limit will have significantly limited
functionality and may stop working. This page describes how to manage
your disk storage so you don't exceed the storage limit and can recover
if you do.

.. _about:

About disk storage on |acquia-product:acfs|
-------------------------------------------

Disk storage on |acquia-product:acfs| includes these persistent elements
of your application, each of which has a separate 1 GB disk storage
limit:

-  Databases
-  Files, including user-uploaded files and backups
-  Codebase

Consequences of exceeding the disk storage limits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  If your databases exceed their disk storage limit, your application
   will no longer be able to make insertions into the database.
-  If your files exceed their disk storage limit, you will no longer be
   able to add files or create backups.
-  If your codebase exceeds its disk storage limit, you will no longer
   be able to commit code.

.. _reducing:

Reducing disk storage usage
---------------------------

If you need more disk storage space, you can `upgrade to a paid
|acquia-product:ac|
subscription <https://www.acquia.com/cloud-pricing>`__. If you want to
remain with an |acquia-product:acfs| subscription, here are some steps
you can take to reduce the amount of disk storage your site uses:

-  **Clear Drupal caches**
-  **Delete unneeded backups**
   |acquia-product:ac| maintains three automatic backups that it creates
   and that you cannot delete, but you can also create your own
   on-demand backups. You can delete any unneeded backups using the
   **Databases** page. `Learn more </acquia-cloud/manage/back-up#db>`__.
-  **Delete or compress user-uploaded files**
   You may have some very large videos or pictures, for example. You can
   delete them from within your Drupal website, or by accessing the file
   system on |acquia-product:ac| using SSH. For more information, see
   `Accessing system files </acquia-cloud/files/system-files>`__.
-  **Reduce image file sizes**
   You may have images that are much larger or much higher quality than
   you need for your website. You can replace them with images that are
   smaller, lower resolution, or flattened to remove data that isn't
   needed for display.

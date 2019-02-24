.. include:: /common/global.rst

Working with files
==================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/manage/files/*

Your application's files are kept separately from your codebase and
databases in |acquia-product:ac|. Files consist of the content that you
upload (for example, PDF files).

The **Files** section of the **Environments > Overview** page is a user
interface for copying your application's files between your
application's environments. When you first create or import an
application, the Prod environment is in **Pre-launch mode**. You can
copy files freely between your Dev, Stage, and Prod environments while
your application is in the **Pre-launch mode**.

After you switch to **Production mode**, you cannot copy files (or
databases) to your Production environment. The typical workflow is from
right to left, where you copy files from Production to either Staging or
Development. `Learn more about Production
mode </acquia-cloud/manage/prod-mode>`__.

If you change the mode to **Pre-launch mode**, any file copy task
between environments will be non-destructive. For example, if you drag
your Staging environment to Production, the files present in both your
Staging and Production environments are overwritten, but files present
only in the target (Production) environment — but not the source
environment — are preserved. |acquia-product:ac| writes any new files,
overwrites any pre-existing files, and ignores any files that are
already in place. This prevents accidental deletion of files.

Note

Files in your application's file storage are not executable by
|acquia-product:ac| PHP processes.

.. _copy:

Copying files between environments
----------------------------------

You can copy files from one environment to another environment in the
|acquia-product:ui|, using either the **Application > Environments**
page or the **Application > [Environment] > Overview** page for a
particular environment.

To copy files from one environment to another environment using the
**Application > Environments** page, complete the following steps:

#. Drag a **Files** node from the source environment to the target
   environment.
#. In the confirmation dialog box, click **Copy**.

To copy files from one environment to another environment using the
**Application > [Environment] > Overview** page for a particular
environment, complete the following steps:

#. Under **Files**, click **Copy**.
#. In the **Copy files** dialog box, select the target environment that
   you want to copy files to, and then click **Continue**.

   |Copy files to a different environment|

#. In the confirmation dialog box, click **Copy**.

|acquia-product:ac| copies the files between the environments and
updates the web servers with your changes. You can track the status of
the file copy process in the Activity panel.

For information about how to copy some but not all files from one
environment to another, see `Copying files to a different
environment </acquia-cloud/manage/transfer-files>`__.

.. _backup:

Backing up your files
---------------------

For information about backing up your files, see `Backing up your
application </acquia-cloud/manage/back-up#file>`__. The `Backup and
Migrate <https://www.drupal.org/project/backup_migrate>`__ module is not
supported on |acquia-product:ac|.

.. _related:

Related topics
--------------

-  `Importing your files </acquia-cloud/create/import/manual-files>`__
-  `Understanding files </acquia-cloud/manage/files/about>`__
-  `Backing up your application </acquia-cloud/manage/back-up#file>`__

.. |Copy files to a different environment| image:: https://cdn3.webdamdb.com/1280_wf9Q9eXrMb67.png?1526475709
   :width: 720px
   :height: 474px

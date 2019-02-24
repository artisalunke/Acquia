.. include:: /common/global.rst

Using Live Development mode to change code on your server
=========================================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/develop/livedev/*

Live Development is a feature that enables you to make changes to code
on your |acquia-product:ac| Dev and Stage environments directly, without
needing to first make the changes locally, and then commit them using a
version control system.

.. _use:

Using Live Development to edit code on your server
--------------------------------------------------

After Live Development is enabled for an environment, you can `sign in
to your environment with SSH </acquia-cloud/ssh/enable#access>`__ and
directly edit code. You can also either upload code with Secure FTP or
rsync, or configure an IDE on your local computer to upload code
directly to your |acquia-product:ac| server. When you are ready, you can
commit changes in your Live Development directory to Git.

Your application's code repository is located on the environment at
``~/[env]/livedev``. In the Dev environment, that would be
``~/dev/livedev`` and in the Staging environment, that would be
``~/test/livedev``. When you enable Live Development, this directory is
initialized to contain the currently deployed branch of your Git
repository. Use the code editor of your choice to make changes to your
files. You'll be able to see the effects of your changes immediately in
the environment you are working in. When you are done making changes,
remember to commit and push your changes to your Git repository. For
information about committing changes, see `Live Development
workflow </acquia-cloud/develop/livedev-workflow>`__ and `Sending
updates to your code repository </acquia-cloud/develop/update>`__.

Whenever Live Development is enabled for an environment, you cannot
complete the following tasks:

-  Deploy code from or push code to that environment using a
   drag-and-drop operation in the |acquia-product:ui|.
-  Install a new Drupal distribution in that environment in the
   |acquia-product:ui|.
-  Import an existing application in that environment in the
   |acquia-product:ui|.

`Disable Live Development <#disable>`__ to restore the ability to take
these actions.

Enabling Live Development on an environment can slow the response times
of your Drupal application. Live Development uses the
|acquia-product:ac| platform file system to ensure that your code is
reachable from all web servers. Since a network file system is not
well-suited for code execution, the performance of your application may
be adversely impacted while using Live Development. Because of this, we
recommend that you `disable Live Development <#disable>`__ when you are
finished with your changes.

.. _enable:

Enabling Live Development
-------------------------

To enable Live Development:

#. From the `Overview page of a non-production
   environment </acquia-cloud/manage/environments>`__, click **Live
   Development**.
#. A dialog box will open to confirm that you want to enable live
   development. Click **Enable**.
#. Wait for the `activity log </acquia-cloud/notify>`__ to show that the
   task is complete.

You can enable Live Development for your Development or Staging
environments. You cannot enable Live Development for your Production
environment.

If you have an |acquia-product:acfs| subscription, your codebase has a
limited amount of disk storage available. When you enable Live
Development, |acquia-product:ac| creates a copy of your codebase. If
your codebase is already using a large portion of your codebase disk
quota, then enabling Live Development may fail. For more information,
see `Managing disk storage for |acquia-product:acfs|
subscriptions </acquia-cloud/free/storage>`__.

.. _disable:

Disabling Live Development
--------------------------

You can disable Live Development at any time. When you disable Live
Development, |acquia-product:ac| deploys whatever branch the environment
was set to deploy before you enabled Live Development for it. Therefore,
you need either to commit and push all changes on your Live Development
directory (``~/[env]/livedev``), or discard them.

To disable Live Development, complete the following steps:

#. From the `Overview page of a non-production
   environment </acquia-cloud/manage/environments>`__, click **Live
   Development**.
#. A dialog box will open to confirm that you want to disable live
   development. If you have uncommitted changes that you do not want to
   keep, select the check box for **Discard all uncommitted or unpushed
   changes** in the dialog box.
#. Click **Disable**.
#. Wait for the `activity log </acquia-cloud/notify>`__ to show that the
   task is complete.

.. _related:

Related topics
--------------

-  `Working with code </acquia-cloud/develop/code>`__
-  `About your code repository </acquia-cloud/develop/repository>`__

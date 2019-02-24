.. include:: /common/global.rst

Resolving codebase update errors
================================

When you run updates in either your development, staging, or production
environments with code from the Acquia repository, you can encounter
errors during the process with one or more websites in their multisite
docroots.

Important

Because the code workflow is based on the concept of failing forward,
the best practice is to test your codebase changes across a
representative set of websites in your staging environment before
deploying those changes to your production environment. For more
information, see `Staging a Factory to a non-production
environment </site-factory/workflow/staging>`__.

|acquia-product:edg| reports any multisite docroot or website update
errors it encounters on the Site update progress page.

To view this page, complete the following steps:

#. `Sign in to the |acquia-product:edg|
   environment </site-factory/manage/login>`__ that you are updating
   using an account with either the *`release
   engineer </site-factory/users/admin/release-engineer>`__* or
   *`developer </site-factory/users/admin/developer>`__* role.
#. In the admin menu, click **Administration**, and then click the
   **Site update status** link.

Notes

Users with the *platform admin* role can view the Site update status
page but cannot restart update processes.

Accounts with the *developer* role can restart updates for multisite
docroots and websites on the staging server, and *release engineer*
accounts can restart updates on the staging and production servers.

The **At a glance** section provides the following information about the
website update process:

-  **Not Started** – Number of websites still to be updated
-  **In Progress** – Number of websites being updated by
   |acquia-product:edg|
-  **Error** – Number of websites that did not update due to an error
   (click the number to view a detailed list of website errors)
-  **Warning** – Number of websites that finished updating, but
   completed with errors (click the number to view a detailed list of
   warnings)
-  **Completed** – Number of websites that updated with no issues

After the site update process completes, your multisite docroots will
display either a checkmark or an error image, depending on if all of the
websites that use the multisite docroot completed successfully or if
some websites had errors.

Until all of your multisite docroots display a checkmark, you have not
yet completed the site update process.

.. _errors:

Examining multisite docroot errors
----------------------------------

For each multisite docroot on the Site update status page that displays
an error image, in the actions menu for the multisite docroot, click the
**View sub-tasks** link.

Examine the list of websites that use the multisite docroot, and select
from the following diagnosis options, based on the number of websites
that display an error message:

-  `One (or a few) websites with errors <#few>`__
-  `All (or most) displayed websites <#most>`__

.. _few:

One (or a few) websites with errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If only one or a few websites failed to update successfully, click the
**Restart** link in the actions menu for each failed website update.

The restarted websites’ images change to a working image. Refresh the
page until the working image changes to either a checkmark (success) or
error (fail) image.

If the update process fails again for a website, click the **View logs**
action menu link. Examine the logs, especially the entries whose level
is Error.

-  If you see *PHP fatal* in the message column for an error entry, you
   probably have a code error that you’ll need to resolve on your
   website. After you resolve the error, you’ll need to send a new code
   update.
-  If |acquia-product:edg| displays any other error messages, click the
   **Export logs** action menu link for the process, and then `contact
   Acquia Support </support#contact>`__ with the exported logs to help
   you diagnose the error.

After you’ve successfully updated all of the multisite docroot’s
websites, you’ll have to restart the update process for the multisite
docroot itself. To do this:

#. In the admin menu, click **Administration**, and then click the
   **Site update status** link.
#. Find the multisite docroot that you want to restart, and then click
   the **View logs link** in its actions menu.
#. Click the **Work Pool** tab.
#. Find the multisite docroot to restart, and then click the **Restart**
   link in its actions menu.

You can track the results of the multisite docroot restart process on
the Site update status page.

.. _most:

All (or most) websites with errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If most or all of the websites associated with the multisite docroot did
not update and display an error image, there's probably an issue with
the code in the update.

Select one of the websites that failed, and then click the **View logs**
link on its actions menu. Examine the logs, especially the entries whose
level is Error.

If you see *PHP fatal* in the message column for an error entry, you
probably have a code error that you’ll need to resolve on your website.
After you resolve the error, you’ll need to send a new code update.

After you’ve pushed the new code to |acquia-product:edg|, restart the
site update process for your websites (as described in `Hotfixing an
|acquia-product:edg| deployment </site-factory/workflow/hotfix>`__).

If |acquia-product:edg| displays any other error messages, click the
**Export logs** action menu link for the process, and then `contact
Acquia Support </support#contact>`__ with the exported logs to help you
diagnose the error.

.. _filtering:

Filtering log messages
----------------------

To reduce the number of displayed messages and to be able to better
identify issues reported in the logs, you can set a default error level
for displayed logs.

For information about filtering log messages, see `Configuring task log
settings </site-factory/monitor/tasklog/settings>`__.

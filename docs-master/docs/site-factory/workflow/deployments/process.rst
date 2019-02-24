.. include:: /common/global.rst

Deploying code in |acquia-product:edg|
======================================

Code deployments are a consecutive—not concurrent—process.
|acquia-product:edg| manages the entire process for you, to ensure that
your code is deployed to all of your websites in as efficient a method
as possible, without you having to intervene. You can, however, `track
the progress of the process <#track>`__ to determine the status of the
process.

To minimize possible problems during deployment, certain website
functions are disabled at the beginning of a deployment, and are
re-enabled only after the platform has been safely updated.

.. _steps:

Code deployment overview
------------------------

Whenever you start a code deployment, |acquia-product:edg| performs the
following steps:

Note

If during the code deployment process, you determine that your code
contains an error that affects your websites, you can pause the code
update process, and then upload revised code to attempt to resolve the
issue. For information about this process, see `Hotfixes during a paused
code update </site-factory/workflow/hotfix>`__.

#. Record the deployment's starting time.
#. Disable website installation and cloning tasks to prevent data
   inconsistency. For information about tasks, see `Task logs in
   |acquia-product:edg| </site-factory/monitor/tasklog>`__.
#. `Soft-pause any currently-executing
   tasks </site-factory/monitor/tasklog#softpause>`__, and block new
   tasks from executing.
#. Wait for all tasks that are blocking the update to complete.
#. Perform the following deployment tasks on each cluster in your
   subscription, sequentially:

   #. Verify that the deployment does not contain a major version
      upgrade to Drupal, and that the ``acsf-init`` command has been
      executed.
   #. Ensure that the code deployed on the ``update`` environment
      matches what is currently deployed on the production environment.
   #. Repoint all domain names in use on the production environment to
      the ``update`` environment.
   #. Deploy the new code on the production environment.
   #. Clear caches.
   #. Perform the `per-website deployment tasks <#website>`__
      sequentially on each website in this cluster.
   #. Wait until all update tasks for this cluster have completed.
   #. Deploy the new code to the ``update`` environment, so it matches
      the production environment.

#. Resume paused tasks.
#. Re-enable website installation and cloning tasks
#. Record the deployment's completion time.

The code deployment process should be complete.

If there were any update error messages reported on the Site update
status page, for information about resolving these issues, see
`Resolving codebase update
errors </site-factory/workflow/deployments/errors>`__.

.. _website:

Deployment tasks per website
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:edg| completes the following deployment tasks for each
website:

#. Perform a health check to verify that the website can be updated.
#. Place the website into maintenance mode.
#. Repoint all domain names for the website from the ``update``
   environment to the production environment.
#. Verify that the domains respond to requests.
#. Perform any needed database updates.
   For information about modifying these updates with a hook script, see
   `Overriding drush updatedb </site-factory/extend/hooks/dbupdate>`__.
#. Disable maintenance mode for the website, which returns the website
   to online status.
#. Rebuild the website's caches to improve performance.

.. _track:

Tracking the progress of a deployment
-------------------------------------

You can track the status of the deployment on the **At a glance**
section on the **Site update status** page. To view this page, complete
the following steps:

#. Sign in to the |acquia-product:edg| environment that you are updating
   using an account with either the *`release
   engineer </site-factory/manage/website/manage/roles/release-engineer>`__*
   or
   *`developer </site-factory/manage/website/manage/roles/developer>`__*
   role.
#. In the admin menu, click **Administration**, and then click the
   **Site update status** link.

Note

To verify your platform version number or to determine if maintenance
has completed for your subscription, see `Determining your platform
version </site-factory/workflow/version>`__.

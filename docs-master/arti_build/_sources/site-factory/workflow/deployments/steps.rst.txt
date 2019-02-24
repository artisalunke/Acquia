.. include:: /common/global.rst

Performing a production deployment
==================================

After you have finished `testing the release
branch </site-factory/workflow/staging>`__ across a representative set
of websites in your staging environment, you can deploy the completed
features to your production websites.

.. _prepare:

Preparing for the code deployment
---------------------------------

Use the commands in the following steps to prepare your code to be
deployed to your production websites.

#. Ensure that you're using the release branch that you tested with your
   staged websites, replacing ``[RC]`` with the name of your release
   branch:

   ``git checkout [RC]``

#. Merge the release branch back into the master branch.

   #. Create a ``RELEASE.txt`` file in the ``sites/all`` folder (or edit
      the file if it already exists) and note the feature branches that
      you’ve merged into the release branch.

      If you have not yet created the ``RELEASE.txt`` file, use the
      following command to do so:

      ``git add docroot/sites/all/RELEASE.txt``

   #. Commit the changes to the ``RELEASE.txt`` file, replacing
      ``[version]`` with version-specific information:

      ``git commit -m "Updated RELEASE.txt for [version]"``

   #. Switch to the master branch.

      ``git checkout master git pull origin master``

   #. Merge the release branch into the master branch, replacing
      ``[RC]`` with the name of your branch:

      ``git merge --no-ff [RC]``

#. Create a tag on the master branch that references the release branch
   merge (replacing ``[version]`` with your version number, and
   ``[message]`` with an explanatory message), and then push the changes
   to the code repository.

   ``git tag -a [version] -m [message] git push origin master git push origin --tags``

   Important

   Always deploy a tag—not master or a different branch. Code changes
   made to a deployed branch are deployed into production within
   minutes. Using a deployed branch as a method to quickly deploy new
   code into production is discouraged, as errors with code check-ins
   will immediately impact production, and perhaps cause downtime or
   data loss for your production websites.

   When creating tags, be sure to use version numbers that describe the
   contents of the release branch, when it was released, or both. For
   example, the following naming scheme: ``2.71.20170918.distro``

   where ``2.71`` is the |acquia-product:edg| version and ``20170918``
   is the release date information (a release on September 18, 2017).

.. _deploy:

Deploying your code
-------------------

After you create a new tag in your master branch, update your production
websites to use the tag by using the following steps:

#. Visit the **Site update** page on your *Prod* environment's Factory
   server. Complete the following steps based on your current signed-in
   location:

   -  **|acquia-product:ac|**

      a. Sign in to the |acquia-product:ui| at https://cloud.acquia.com.
      b. Select your application and the *Prod* environment, and then
         click the **Update code** link.

         If you're not already signed in to your |acquia-product:edg|
         *Prod* environment, you will be redirected to a sign-in page.
         Sign in using an account with the *`release
         engineer </site-factory/users/admin/release-engineer>`__* role.

   -  **|acquia-product:edg|**

      a. Sign in to your *Prod* environment’s
         `|acquia-product:sfi| </site-factory/manage/login>`__ using an
         account with the *`release
         engineer </site-factory/users/admin/release-engineer>`__* role.
      b. In the admin menu, click **Administration**, and then click the
         **Update code** link.

#. In the **Start time** section, select from the following options to
   control when |acquia-product:edg| will start the code update process:

   -  **Immediately** - Starts the code update process when you click
      **Update**.
   -  **At a specific time** - Starts the code update process at a
      specific time, based on the GMT time zone. In the **Time** field
      that appears, enter a time using the
      `strtotime <http://us1.php.net/strtotime>`__ format, which can
      include specific or relative values that include the following
      examples:

      -  *Date and time:* ``Mon Feb 24 13:28:38 2018`` - 13:28:38 GMT on
         February 24, 2018
      -  *Unix timestamp:* ``@1519478918`` - 13:28:38 GMT on February
         24, 2018
      -  *Relative time:* ``5 hours`` - Five hours from the current time

#. In the **Stack** section, select the Site Factory stack whose code
   you are updating.
#. In the **Site update action** section, in the **Choose a path to
   deploy** list, click the tag that you created in the `Preparing for
   the code deployment <#prepare>`__ section.
#. After you select your tag, select the same option that you selected
   during the `staging deployment
   process </site-factory/workflow/staging#options>`__.
#. After you select the appropriate check box to confirm that you are
   aware that you are updating your production environment, click
   **Update**.

|acquia-product:edg| begins the update process. All production websites
are updated with the code from the specified tag.

You can track the status of the update on the **At a glance** section on
the Site update status page.

If you determine that your code update contains an error that affects
your websites, you can pause the code update process and upload revised
code in an effort to resolve the issue. For more information about this
process, see `Hotfixes during a paused code
update </site-factory/workflow/hotfix>`__.

For more information about resolving update errors reported on the Site
update status page, see `Resolving codebase update
errors </site-factory/workflow/deployments/errors>`__.

.. _clean:

Cleaning up your environment
----------------------------

After you complete a release, you should perform the following cleanup
tasks on your environment:

-  `Clear caches <#caches>`__
-  `Remove unneeded branches from version control <#branches>`__

.. _caches:

Clearing caches after a release
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A final step of the deployment process should include clearing caches,
by using the |acquia-product:sfa| instead of Drush commands or the
|acquia-product:ui| interface—this is because the |acquia-product:sfa|
provides failsafe logic to prevent concurrent execution of
cache-rebuilding tasks. For information about this process, see the
documentation for the ```cache-clear`` |acquia-product:sfa|
endpoint <https://www.demo.acquia-cc.com/api/v1#Clear-a-site's-caches>`__.

.. _branches:

Removing unneeded branches from version control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To reduce the size of your code repository, it is a best practice to
remove branches no longer needed after a release. To do so, run the
following command for each feature branch that you merged into the
release, replacing ``[feature_branch]`` with the name of the branch:

``git branch -d [feature_branch]``

Run the following command to remove the now unneeded release branch,
replacing ``[RC]`` with the name of your release branch.

``git branch -d [RC]``

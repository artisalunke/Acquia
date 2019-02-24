.. include:: /common/global.rst

Staging a Factory to a non-production environment
=================================================

As part of maintaining your |acquia-product:edg| platform, you will
develop new features and functionality that you want to test against a
representative sample of your websites. To test your feature branches
before making them available to your website visitors, you should
*stage* your factory, which copies your websites from your production
environment to the non-production environment that you select. The
staging process also sends the multisite management information that is
required by |acquia-product:edg| to those non-production environments.

The Factory staging process copies both the multisite management
information and the selected websites from the production environment,
deleting everything previously in the non-production environment. After
completing the copy process, |acquia-product:edg|
`scrubs </site-factory/workflow/scrub>`__ user account and configuration
information from any staged websites.

Important

In |acquia-product:edg|, new websites should first be created in your
production environment, and then staged to your non-production
environments for thorough testing before deploying them to production.

.. _deploy:

Steps in staging a factory
--------------------------

To stage your Factory, you must complete the following steps in the
overall process:

#. `Sign in to your |acquia-product:sfi| </site-factory/manage/login>`__
   using an account with either the
   `*developer* </site-factory/manage/website/manage/roles/developer>`__
   or `*release
   engineer* </site-factory/manage/website/manage/roles/release-engineer>`__
   role
#. `Copy production data to non-production environments <#data>`__
#. `Verify the status of a staging deployment <#verify>`__
#. `Deploy code to the non-production environment <#deploy_code>`__
#. `Verify execution of ``post-staging-update`` hook scripts <#hooks>`__

After copying your data, verifying it, and deploying code, review the
instructions for `signing in to a staged and scrubbed
website <#login>`__.

.. _data:

Copy production data to non-production environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*You can use the following, alternate process instead of the standard
method to copy production data for individual websites to non-production
environments. To use this alternate method, contact your Account Manager
for access to the feature.*

Because the website copy process can take a long time to complete, when
copying websites to a non-production environment, you should not select
all of your websites for testing. Instead, stage a representative sample
of your production websites to ensure that the updated code functions
correctly. To do so, complete the following steps after signing in to
your |acquia-product:sfi|:

#. In the admin menu, click **Administration**, and then click the
   **Deploy staging environment** link.
#. *If your subscription contains multiple non-production environments,*
   select the non-production environment to which you want to stage
   websites.

   |Select an environment|

#. Select one or more websites that you want to copy to your
   non-production environment. To do this, in the **Choose sites to
   deploy** field, start entering a site name, and then click the
   correct website from the displayed list.

   |Enter website name|

   Note

   If you select a primary or secondary website contained in a site
   collection, the copy process will stage all of the websites in the
   site collection.

#. Select one or more of the following check boxes to customize your
   staging deployment:

   -  **Stage all users** check box – Copy all user accounts (without
      `scrubbing the user account
      list </site-factory/workflow/scrub%20>`__) to the non-production
      environment. All existing user accounts in the non-production
      environment will be updated.
   -  **Wipe target environment** check box – Delete all existing
      websites in the non-production environment, and replace them with
      new copies.
   -  **Send a status email for each site** check box – Receive a status
      email with the success or failure of each website as it is staged.

#. Click **Deploy**.

After beginning the deployment, you should `monitor the progress of the
deployment <#verify>`__ to monitor for errors, and to determine when
your staging environment is ready for use.

To use the standard method of copying production data to a
non-production environment, complete the following steps after signing
in to your |acquia-product:sfi|:

#. In the admin menu, click **Administration**, and then click the
   **Deploy staging environment** link.
#. Select the non-production environment to which you want to stage
   websites.

   |Select your non-production environment|

#. Select one or more websites that you want to copy to your
   non-production environment. To do this, in the **Choose sites to
   deploy** field, start typing the name of a website in the field, and
   then select the website name.

   |Select the websites to deploy|

   Notes

   Because the website copy process can take a long time to complete,
   when copying websites to a non-production environment, you should not
   select all of your websites for testing. Instead, stage a
   representative sample of your production websites to ensure that the
   updated code functions correctly.

   If you select a primary or secondary website contained in a site
   collection, the copy process will stage all of the websites in the
   site collection.

#. Optionally, select the **Send a status email for each site** check
   box to receive a status email with the success or failure of each
   website as it is staged.
#. Click **Deploy**.

After beginning the deployment, you should `monitor the progress of the
deployment <#verify>`__ to monitor for errors, and to determine when
your staging environment is ready for use.

Verify the status of a staging deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To verify the status of a staging deployment, complete the following
steps:

#. `Sign in </site-factory/manage/login>`__ to your production
   environment’s |acquia-product:sfi| using an account with either the
   `*developer* </site-factory/manage/website/manage/roles/developer>`__
   or `*release
   engineer* </site-factory/manage/website/manage/roles/release-engineer>`__
   role.
#. In the admin menu, click **Administration**, and then click the
   **Staging deployment status** link.
#. Under **Filter tasks**, review the staging progress bar to determine
   if your deployment completed successfully or contained failures.

After verifying that data copied successfully to your non-production
environment, you should `deploy code to the
environment <#deploy_code>`__.

.. _deploy_code:

Deploy new code to the non-production environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To deploy your release branch to the websites you staged to the
non-production environment to ensure that there are not any errors or
branch integration issues, complete the following steps:

#. Visit the **Site update** page on your non-production environment's
   Factory server. Complete the following steps, depending on where you
   are currently signed in:

   -  **|acquia-product:ac|**

      #. Sign in to |acquia-product:ac|.
      #. Go to **Cloud > Workflow**, and then click the **Update code**
         link for the *Dev* or *Stage* environment.
         If you are not already signed in, you will be redirected to a
         sign-in page. Sign in using an account that has been assigned
         the `*release
         engineer* </site-factory/manage/website/manage/roles/release-engineer>`__
         role.

   -  **|acquia-product:edg|**

      #. Sign in to your non-production environment’s
         |acquia-product:sfi| using an account with the `*release
         engineer* </site-factory/manage/website/manage/roles/release-engineer>`__
         role.
      #. In the admin menu, click **Administration**, and then click the
         **Update code** link.

#. In the **Start time** section, select from the following options to
   control when |acquia-product:edg| will start the code update process:

   -  **Immediately** – Starts the code update process when you click
      **Update**.
   -  **At a specific time** – Starts the code update process at a
      specific time. In the **Time** field that appears, enter a time
      using the `strtotime <http://us1.php.net/strtotime>`__ format,
      which can include specific or relative values that include the
      following examples:

      -  *Date and time* – ``Mon Feb 24 13:28:38 2014`` (13:28:38 GMT on
         24 February 2014)
      -  *Unix timestamp* – ``@1393248518`` (13:28:38 GMT on 24 February
         2014)

#. In the **Site update action** section, in the **Choose a path to
   deploy** list, click the release branch that you want to test.
#. After you select your release branch, select the action that
   describes the type of code update you want to deploy from the
   following options:

   -  **Code only** – Causes the update to set only the version control
      system (VCS) code path, which it does for all of the websites at
      the same time. This can reduce the time required to complete the
      process.

      Select this option only if you meet both of the following
      conditions:

      -  The release branch does not contain any update hooks.
      -  Your code does not require a cache clear or a registry rebuild.

   -  **Code and databases** *(normal usage)* – Causes the update to
      sync the environment's VCS path names, manage the websites' custom
      domain names, and complete the following steps for each website,
      from one to the next:

      #. Inspects the website to ensure that it does not have any known
         issues
      #. Enables maintenance mode for the website
      #. Puts the code on the website
      #. Runs updates
      #. Clears the website's cache
      #. Disables maintenance mode

   -  **Code and databases, and rebuild registries** – Causes the update
      to complete all of the actions from the Code and databases option,
      while also rebuilding the registries.

      Note

      To use this option, you must add `Registry
      Rebuild <https://drupal.org/project/registry_rebuild>`__ to the
      ``docroot/sites/all/drush`` folder in your code repository. If you
      have not added Registry Rebuild to this folder (even if you have
      added it to a folder in specific websites' repositories), the code
      update will use the **Code and databases** option and add a
      warning to the logs.

      Select this option if you have moved files around in your code
      repository since the last time you sent code to the environment
      (for example, moving an installed module from
      ``/sites/all/modules`` to ``/sites/all/modules/custom``).

#. Click **Update**.

|acquia-product:edg| begins the update process for the staged websites.
If you encounter errors during the update, examine the **At a glance**
section on the **Site update status** page. For more information about
resolving update errors, see `Resolving codebase update
errors </site-factory/workflow/deployments/errors>`__.

After you have successfully deployed the release branch on your
non-production environment, you can test your updated, staged websites
that contain your changes to the codebase.

If you need to deploy an updated release branch, use the previous steps
for deployment and testing.

Signing in to a staged and scrubbed website
-------------------------------------------

|acquia-product:edg| starts the staging process by copying the selected
websites and the |acquia-product:sfi| to the environment you selected.
Although the staging process copies the files and databases associated
with each selected website, it scrubs the websites of personal data,
including the email addresses of user accounts, for all users without
either the `*developer* </site-factory/users/admin/developer>`__ or
`*release engineer* </site-factory/users/admin/release-engineer>`__
roles.

As a result, to `sign in </site-factory/manage/login>`__ to either a
staged website or the |acquia-product:sfi| on the *Dev* or *Test*
environment, you may not be able to use your usual email address. By
default, the scrubbing script replaces your email address username with
userXXXXX (where XXXXX is your user account number). You can either sign
in using this scrubbed username, or you can follow the procedures
described in `Protecting Site Factory accounts during
staging </site-factory/workflow/scrub#protectsf>`__ or `Protecting
hosted website accounts during
staging </site-factory/workflow/scrub#protecthosted>`__ to keep your
email address from being scrubbed.

For both a list of information scrubbed by default from staged websites
and instructions for creating a separate scrub script to remove custom
website information that you do not want to copy to staging, see
`Scrubbing sensitive data from staged
sites </site-factory/workflow/scrub>`__.

.. _hooks:

Verify execution of ``post-staging-update`` hook scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|acquia-product:edg| offers `a ``post-staging-update``
hook </site-factory/extend/hooks/post-staging-update>`__ to synchronize
data structure changes and module changes from your production
environment to your newly-staged non-production environment. If you have
created any ``post-staging-update`` hooks, you should verify the hook
script executed successfully on all newly-staged websites.

Next step
---------

After you have completed your testing on your staged websites, you can
`deploy your code changes to your production
websites </site-factory/workflow/deployments>`__.

.. |Select an environment| image:: https://cdn4.webdamdb.com/1280_AQoZTTewC0W0.jpg?1526475565
   :width: 750px
   :height: 151px
.. |Enter website name| image:: https://cdn4.webdamdb.com/1280_Mp1ukrYEW98.jpg?1526475532
   :width: 750px
   :height: 74px
.. |Select your non-production environment| image:: https://cdn3.webdamdb.com/1280_sZXb3iAyVTS5.jpg?1526475761
   :width: 710px
   :height: 306px
.. |Select the websites to deploy| image:: https://cdn3.webdamdb.com/1280_2bo3HuE2n241.jpg?1526475596
   :width: 672px
   :height: 146px

.. include:: /common/global.rst

Hotfixing an |acquia-product:edg| deployment
============================================

Sometimes, code updates that are `deployed to your production
|acquia-product:edg| websites </site-factory/workflow/deployments>`__
may contain one or more problems. Instead of waiting for the code update
to complete across all websites in your platform — and potentially cause
multiple websites to become nonfunctional — you can pause the code
update process and send a hotfix to immediately address the issue.

Notes

The hotfix process supports *only* the **Code only** update option. If
you selected **Code and databases**, the hotfix process will update the
previously updated websites and the code update itself, and then
continue with the code and database update.

*If you realize that you need to immediately address a problem in a code
update by deploying a hotfix*, complete the following steps:

#. Pause the code update deployment process.
#. Develop a hotfix that resolves the issue (or issues) you discovered
   in your previously running code update.

   Note

   If your hotfix uses Drush commands that affect a single website, be
   sure to use the ``--uri=site.host.com`` parameter for the commands,
   where ``site.host.com`` is your website's complete site and domain
   name.

#. Sign in to the |acquia-product:sfi| using an account with the
   `*release engineer* </site-factory/users/admin/release-engineer>`__
   role.
#. In the admin menu, click **Administration**, and then click the
   **Update code** link to open the Site update page.
#. In the **Update in progress** section, click **Pause**.
#. Create a tag for your updated hotfix code using the procedures in the
   `Preparing for the code
   deployment </site-factory/workflow/deployments/steps#prepare>`__
   section of `Deploying your code to
   production </site-factory/workflow/deployments/steps>`__.
#. On the Site update page, in the **Scheduled start time** section,
   select from the following options to control when
   |acquia-product:edg| will start the hotfix process:

   -  **Immediately** - Starts the code update process when you click
      **Update**.
   -  Date string field - Starts the code update process at a specific
      time. Enter a time using the
      `strtotime <http://php.net/manual/en/datetime.formats.php>`__
      format, which can include specific or relative values. Here are
      some examples:

      -  **Date and time:** ``Mon Feb 24 13:28:38 2016`` - 13:28:38 GMT
         on 24 February 2016
      -  **Unix timestamp:** ``@1456321108`` - 13:38:28 GMT on 24
         February 2016
      -  **Relative time:** ``5 hours`` - Five hours from the current
         time

#. In the **Sites: VCS tag** list, click the tag for the hotfix.
#. Click **Update**.

The hotfix update is applied to the websites that were already updated
by the code update process, and is then applied to the code update
itself.

After the hotfix is complete, the previously started code update process
resumes, deploying the hotfixed code update to the remaining websites.

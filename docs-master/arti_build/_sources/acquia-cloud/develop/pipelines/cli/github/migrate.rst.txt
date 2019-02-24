.. include:: /common/global.rst

Migrating a repo to GitHub from the command line
================================================

.. container:: internal-navigation

  **Acquia Cloud pipelines client**

  * :doc:`Intro </acquia-cloud/develop/pipelines/cli>`
  * :doc:`Install </acquia-cloud/develop/pipelines/cli/install>`
  * :doc:`Connect </acquia-cloud/develop/pipelines/cli/github>`
  * :doc:`Require </acquia-cloud/develop/pipelines/cli/github/reqs>`
  * :doc:`Commands </acquia-cloud/develop/pipelines/cli/commands>`
  * Migrate
  * :doc:`Workflows </acquia-cloud/develop/pipelines/cli/workflows>`

If you have a Git repository which is cloned from an |acquia-product:ac|
repository and you want to use the |acquia-product:ac| pipelines
command-line client to switch to using GitHub as the source repository
for the associated application, complete the following steps:

#. Ensure you have all the latest commits from the |acquia-product:ac|
   repository with the following command:

   ``git fetch``

#. Rename the |acquia-product:ac| remote from ``origin`` to ``cloud``:

   ``git remote rename origin cloud``

#. Add a new remote named ``origin`` for the GitHub repository that you
   want to use:

   ``git remote add origin git@github.com:user/repo.git``

#. Push all branches from the repository to GitHub:

   ``git push origin --all --force``

#. Run the ``pipelines github-connect`` `command 
   </acquia-cloud/develop/pipelines/cli/commands>`__ to associate this 
   repository with your |acquia-product:ac| application.

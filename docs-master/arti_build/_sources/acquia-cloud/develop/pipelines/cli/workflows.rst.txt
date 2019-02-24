.. include:: /common/global.rst

Workflows with the pipelines client
===================================

.. container:: internal-navigation

  **Acquia Cloud pipelines client**

  * :doc:`Intro </acquia-cloud/develop/pipelines/cli>`
  * :doc:`Install </acquia-cloud/develop/pipelines/cli/install>`
  * :doc:`Connect </acquia-cloud/develop/pipelines/cli/github>`
  * :doc:`Require </acquia-cloud/develop/pipelines/cli/github/reqs>`
  * :doc:`Commands </acquia-cloud/develop/pipelines/cli/commands>`
  * :doc:`Migrate </acquia-cloud/develop/pipelines/cli/github/migrate>`
  * Workflows

After you have installed and configured the pipelines client (which is
required only if you want to manage pipelines from the command prompt),
complete the following steps to create an application with the
command-line client:

#. Create a `build definition
   file </acquia-cloud/develop/pipelines/yaml>`__ that describes how to
   build your application and add it to the root of your workspace.

#. Build your application using the ``start`` command.

   .. admonition:: Note for GitHub users

    As an alternative, you can use the `|acquia-product:ac| pipelines
    integration </acquia-cloud/develop/pipelines/connect>`__ in the user
    interface, in which case creating a pull request or pushing a branch
    in GitHub triggers a pipelines build.

    When you run the ``pipelines start`` command in a Git repository that
    has an |acquia-product:ac| repository as a remote, the ``start``
    command determines the correct application ID. However, if your local
    Git repository has only GitHub as a remote, the ``start`` command
    cannot determine the correct application ID on its own. You can set
    the correct application ID for a specific repository using the
    ``pipelines set-application-id`` command.

    To determine the correct application ID, run the
    ``pipelines list-applications`` command, and then find the
    application ID associated with the application that you want. Then,
    from the Git repository that you want to configure, run the following
    command:

    ``pipelines set-application-id --application-id=[application ID]``

#. Use the ``status`` command to verify if the build has completed and
   whether it was successful. If you use the |acquia-product:ac|
   pipelines GitHub integration, you can see job completion and success
   information on the GitHub pull request. You still need to use the
   ``status`` command for information about commits that are not part of
   a pull request.

#. If desired, `deploy your build artifact <#deploy>`__.

.. _artifact:

The build artifact
------------------

After the build is complete, the build artifact is committed to your
|acquia-product:ac| repository in a build branch, which by default is
given the name of the branch that you built, with ``pipelines-build``
prepended. The path of the build branch in the repository is reported in
the output of the ``start`` command. The build branch is then available
to be deployed into one of your |acquia-product:ac| environments.

Why is the build artifact created in the repository?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Storing the build artifact in your |acquia-product:ac| repository
provides the following advantages over alternatives such as creating a
tarball:

-  You can easily deploy the build artifact to your |acquia-product:ac|
   environments, using the |acquia-product:ui| or the Cloud API.
-  You can easily view the build artifact using Git.
-  You can more easily debug your build process, comparing the build
   artifact against what you may have expected, as well as compare build
   artifacts over time, using a tool like ``git diff``.
-  You can control how long your build artifacts are retained, since you
   control the contents of your own repository. You may, for example,
   have compliance requirements that mandate keeping them for a
   specified time, or security concerns that require you to be able to
   delete them promptly.
-  You can easily copy a build artifact to other systems for such
   purposes as static code analysis or license compliance.

.. _deploy:

Deploying the build artifact
----------------------------

After you have successfully completed a build, you can deploy the
resulting build artifact in any |acquia-product:ac| environment. You can
do this by selecting the build branch for deployment, using either of
the following methods:

-  Directly in the |acquia-product:ui|
-  By using the `Cloud API </acquia-cloud/develop/api/>`__ or `Drush Cloud
   commands </acquia-cloud/develop/api/drush-reference/>`__

After you set the deployed branch of an environment to a build branch,
each build artifact committed to that branch is deployed immediately,
without requiring any intervention. For example, if you build the master
branch, and your |acquia-product:ac| development environment is set to
the ``pipelines-build-master`` branch, the build artifact is deployed
immediately to that development environment when the pipeline job
completes successfully.

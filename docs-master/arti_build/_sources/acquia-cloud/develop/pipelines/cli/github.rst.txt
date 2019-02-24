.. include:: /common/global.rst

Using GitHub with the pipelines client
======================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/develop/pipelines/cli/github/*

.. container:: internal-navigation

  **Acquia Cloud pipelines client**

  * :doc:`Intro </acquia-cloud/develop/pipelines/cli>`
  * :doc:`Install </acquia-cloud/develop/pipelines/cli/install>`
  * Connect
  * :doc:`Require </acquia-cloud/develop/pipelines/cli/github/reqs>`
  * :doc:`Commands </acquia-cloud/develop/pipelines/cli/commands>`
  * :doc:`Migrate </acquia-cloud/develop/pipelines/cli/github/migrate>`
  * :doc:`Workflows </acquia-cloud/develop/pipelines/cli/workflows>`

By default, the pipelines client uses your |acquia-product:ac| code
repository as the source repository for build jobs. As an alternative,
however, you can configure the client to use a GitHub repository as the
source, so the command-line client runs a build job and commits the
build artifact to your |acquia-product:ac| target repository when
commits are pushed, or pull requests are created.

You can start with an |acquia-product:ac| code repository and clone it
into GitHub, or you can start with a GitHub repository and push it into
the |acquia-product:ac| code repository.

.. note::

    Installing the pipelines command-line client is optional, and is not
    required for pipelines to function with your application. To connect
    through the user interface, see `Connecting an application to an
    external Git repo </acquia-cloud/develop/pipelines/connect>`__.

Getting started
---------------

Use the following pages to help you use your GitHub repositories with
the pipelines client:

-  `Configuring the GitHub connection to the pipelines
   client </acquia-cloud/develop/pipelines/cli/github/connect>`__
-  `Obtaining required GitHub
   information </acquia-cloud/develop/pipelines/cli/github/reqs>`__
-  `Migrating a repo from |acquia-product:ac| to
   GitHub </acquia-cloud/develop/pipelines/cli/github/migrate>`__

If you prefer to connect to GitHub from the user interface, see
`Connecting an application to an external Git
repo </acquia-cloud/develop/pipelines/connect>`__.

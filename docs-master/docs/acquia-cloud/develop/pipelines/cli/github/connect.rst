.. include:: /common/global.rst

Configuring the GitHub to pipelines client connection
=====================================================

Use the procedures on this page to control the connection between your
GitHub repository and the optional pipelines command-line client. If you
prefer to use your web browser to connect |acquia-product:ac| to GitHub,
see `Connecting an application to an external Git
repo </acquia-cloud/develop/pipelines/connect>`__.

.. _prereq:

Requirements
------------

To configure the pipelines client integration with GitHub (both to
connect and disconnect), you must have the following items:

-  `GitHub
   permissions </acquia-cloud/develop/pipelines/cli/github/reqs#permissions>`__
   for the GitHub repository
-  A `GitHub personal access
   token </acquia-cloud/develop/pipelines/cli/github/reqs#token>`__

For information about obtaining these items from GitHub, see `Obtaining
required Github
information </acquia-cloud/develop/pipelines/cli/github/reqs>`__.

.. _init:

Connecting to GitHub
--------------------

To configure the pipelines client to use a GitHub repository as the
source, run the ``pipelines github-connect`` command as a user with the
necessary `GitHub
permission </acquia-cloud/develop/pipelines/cli/github/reqs#permissions>`__
for the GitHub repository.

Use the following command to connect the pipelines client to GitHub:

``pipelines github-connect --application-id=[Acquia app ID] [GitHub user/GitHub repo-name] [GitHub token]``

where

-  ``[Acquia app ID]`` is your |acquia-product:ac| `application
   ID </acquia-cloud/develop/pipelines/cli/commands#appids>`__.
-  ``[GitHub user/GitHub repo-name]`` is your GitHub user name and the
   name of the GitHub repository that will be the source repository for
   build jobs. You can find this in GitHub by selecting the repository
   and looking in the URL bar or on the repository's main page.

   |Finding your GitHub user name and repository name|

-  ``[GitHub token]`` is a `GitHub personal access
   token </acquia-cloud/develop/pipelines/cli/github/reqs#token>`__ that
   you generate.

After you have run ``pipelines github-connect``, the GitHub repository
that you specify in ``pipelines github-connect`` becomes the default
source repository for pipelines build jobs.

Each time that you use GitHub to create or reopen a pull request or push
a commit, |acquia-product:ac| runs the ``pipelines start`` command using
the build definition file in the GitHub repository and commits the build
artifact to your |acquia-product:ac| repository.

.. _webhook:

GitHub webhooks and deploy keys
-------------------------------

When you run ``pipelines github-connect``, the pipelines client adds a
webhook to your GitHub repository.

To view the webhook in GitHub, complete the following steps:

#. Go to your repository, and then click **Settings**.
#. In the menu on the left side, click **Webhooks**.

The pipelines client also creates a deploy key in your GitHub
repository, which gives the client permission to interact with your
repository.

To see the deploy key in GitHub, complete the following steps:

#. Go to your repository, and then click **Settings**.
#. In the menu on the left side, click **Deploy keys**.

.. _disconnect:

Disconnecting from GitHub
-------------------------

To disconnect the pipelines client from a GitHub repository, run the
following command:

``pipelines github-disconnect --application-id=[Acquia app ID] [GitHub user/GitHub repo-name] [GitHub token]``

where

-  ``[Acquia app ID]`` is your |acquia-product:ac| `application
   ID </acquia-cloud/develop/pipelines/cli/commands#appids>`__.
-  ``[GitHub user/GitHub repo-name]`` is your GitHub user name and the
   name of the GitHub repository that is the source repository for build
   jobs. You can find this in GitHub by selecting the repository and
   looking in the URL bar or on the repository's main page.
-  ``[GitHub token]`` is a `GitHub personal access
   token </acquia-cloud/develop/pipelines/cli/github/reqs#token>`__ that
   you generate.

Disconnecting your GitHub repository from the pipelines client also
removes the webhook and deploy key added by the connection of the two
services.

.. |Finding your GitHub user name and repository name| image:: https://cdn2.webdamdb.com/1280_gdq2AZQrGai2.png?1526475783
   :width: 750px
   :height: 144px

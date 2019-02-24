.. include:: /common/global.rst

Using pipelines for site development and testing
================================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/develop/pipelines/*

The |acquia-product:ac| pipelines feature is a tool for developing,
testing, and deploying websites or other applications to
|acquia-product:ac|, and the feature enables you to complete the
following actions:

-  Manage your application's source code on third-party Git servers, and
   seamlessly deploy to |acquia-product:ac|.
-  Use tools like Composer or Drush Make to assemble your application's
   components and dependencies automatically.
-  Use technologies such as Sass and Typescript to compile application
   source code.
-  Control which developers or teams have access to change different
   parts of your application code base.

How the pipelines feature works
-------------------------------

Pipelines in |acquia-product:ac| execute instructions that you provide
to transform application source code into a build artifact which can
then be tested and deployed. Specifically:

-  Pipelines jobs are triggered by a commit or pull request to your
   connected code repository or, optionally, when you run the command
   line client's ``pipelines start`` command.
-  The pipelines feature clones the Git source repository and checks out
   the specified branch. Initially, the source repository for your
   application is its |acquia-product:ac| Git repository, but you can
   choose to use GitHub or Bitbucket repositories as the source.
-  Pipelines looks for a file named ``/acquia-pipelines.yml`` in YAML
   format in the selected Git branch and executes the instructions it
   finds there. These instructions can assemble your application from
   multiple code bases, transform source files into compiled files ready
   to deploy, and run tests. For more information, see `Using a build
   definition file </acquia-cloud/develop/pipelines/yaml>`__.
-  If all of the instructions in the YAML build definition file succeed,
   |acquia-product:ac| commits all of the files and directories created
   by the instructions as a build artifact to a build branch in the
   target repository. Currently, the target repository is always the
   application's |acquia-product:ac| Git repository. Other repositories
   cannot be targets.
-  You can view the results of each job with the pipelines user
   interface in |acquia-product:ac|, the status posted to your pull
   request on your third-party code repository, and the
   ``pipelines status`` and ``logs`` commands.

For a list of software available in your container, and resource limits
on pipelines jobs, see `Container
resources </acquia-cloud/container/resources>`__.

Getting started
---------------

Use the following general steps to start using the|acquia-product:ac|
pipelines feature for your website development and testing:

#. Confirm that your `Acquia Cloud account's
   role </acquia-cloud/teams/roles>`__ has the `Execute Pipelines
   permission </acquia-cloud/teams/permissions>`__.
   You may also need to be assigned the `Add an environment
   permission </acquia-cloud/teams/permissions>`__.
#. *Optional:* `Connect your application to an external Git
   repository </acquia-cloud/develop/pipelines/connect>`__.
#. `Create a build definition
   file </acquia-cloud/develop/pipelines/yaml>`__.
#. `Start a build job </acquia-cloud/develop/pipelines/ui>`__.

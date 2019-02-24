.. include:: /common/global.rst

Connecting an application to an external Git repo
=================================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/develop/pipelines/connect/*

If you want to use an external Git repository with the
|acquia-product:ac| pipelines feature, you must first connect to your
external Git repository. Acquia supports integration with Bitbucket and
GitHub.

Note

If you want to use the internal Git repository included with
|acquia-product:ac|, you do not have to complete this step to use
pipelines with your application, and can go ahead and `create your build
definition file </acquia-cloud/develop/pipelines/yaml>`__.

Follow these steps to connect your |acquia-product:ac| subscription with
your external Git repository, depending on what you use to store your
repository:

-  `Connecting pipelines to your Bitbucket
   repo </acquia-cloud/develop/pipelines/connect/bitbucket>`__
-  `Connecting pipelines to your Github
   repo </acquia-cloud/develop/pipelines/connect/github>`__

For a more detailed technical explanation of how the pipelines feature
works and its benefits, see `Using pipelines for site development and
testing </acquia-cloud/develop/pipelines>`__.

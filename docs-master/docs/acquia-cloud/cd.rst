.. include:: /common/global.rst

|acquia-product:ccd|
====================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/cd/*

.. container:: message-status

   Available only to |acquia-product:ace| subscribers

Developers thrive on a continuous delivery process in which time is invested in creating, and not waiting for tools, environments, or delays due to bottlenecks in processing pull requests from multiple developers. To assist with this need, |acquia-product:ccd| provides developer and tester teams a continuous delivery cloud service, allowing them to quickly create customer value by accelerating integration and delivery of production ready features.

|acquia-product:ccd| is developer-ready, automating the process of building and testing versions of code and applications with the `Acquia Cloud pipelines feature's </acquia-cloud/develop/pipelines>`__ orchestration and production-like environments, all seamlessly integrated with the |acquia-product:ac| platform.

.. _feature:

Features
--------

Developer teams can use |acquia-product:ccd| to help them increase their productivity, code quality, and the performance of the development-to-staging process by providing access to a consistent set of continuous code building, testing, and integration tools. Available features include the following:

-  **Self-service, production-like environments** |--| Eliminates the need to move code and testing between multiple cloud platforms saving time and reducing the risk of errors, by allowing you to provision and deprovision production-like environments in |acquia-product:ac| on your own.
-  **Seamless Acquia Cloud integration** |--| Provides a single environment for continuous integration and delivery orchestration with self-service production-like environments.
-  **Automated development governance** |--| When used with the `Acquia Cloud pipelines feature </acquia-cloud/develop/pipelines>`__, brings speed and velocity to developers while lowering risks in quality, stability, and intellectual property. The automation benefits of ready to use building and testing orchestration and self-service environments greatly reduces code and versioning inconsistencies.

.. _intro:

Why use |acquia-product:ccd|?
-----------------------------

Code that is built frequently needs consistency to achieve continuous integration. However, it can be challenging for individual developers on a team to achieve consistency.

In traditional deployment workflows, you need to do all of the work of assembling a website's deployment image in your code repository. For example, if a module is updated, you have to copy the new version of that module into your repository. Also, for deployment workflows based on local builds, each developer needs to ensure that they have available all the correct prerequisites in their correct versions (such as PHP, Git, or |acquia-product:ac| repository access), and all developers must be able to consistently replicate this development environment locally.

Working together, |acquia-product:ccd| and the |acquia-product:ac| pipelines feature can contain only your website's version-controlled build instructions and private resources. You can keep the canonical version of external resources outside of your repository, and pull in the latest or other required version as you build your website for deployment. |acquia-product:ccd| also provides a consistent build and testing environment to all developers in a cloud-based container, which has access to production-like environments that you can create or remove as needed.

.. _about:

Getting started with |acquia-product:ccd|
-----------------------------------------

To get started with creating and using CD environments for your continuous development and delivery, see `Managing on-demand CD environments </acquia-cloud/cd/env>`__.

.. include:: /common/global.rst

Containers in |acquia-product:ac|
=================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/container/*

Containers are a virtualization technology with many advantages over
traditional approaches, including virtual machines. These advantages
include being lightweight (making them faster), being more secure, and
the use of packaging (images that contain all of an application’s
dependencies, ensuring no dependencies are outdated or missing).

A container can run any application, together with its dependencies, in
isolation from all other applications on the same hardware.

|acquia-product:ac| uses containers for several of its features,
including the following:

-  |ccd|_
-  |ac|_ - The pipelines feature uses containers to execute builds prior to 
   their deployment on |acquia-product:ac|.

.. _info:

Additional |acquia-product:ac| container information
----------------------------------------------------

For a list of the tools and PHP extensions provided in an
|acquia-product:ac|-provided container, see `Container
resources </acquia-cloud/container/resources>`__.

For instructions about using Drush in containers, see `Using different
Drush versions in containers </acquia-cloud/container/drush>`__.


.. |ccd| replace:: \ |acquia-product:ccd|\  environments
.. _ccd: </acquia-cloud/cd/env>

.. |ac| replace:: \ |acquia-product:ac|\ pipelines feature
.. _ac: /acquia-cloud/develop/pipelines
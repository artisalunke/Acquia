.. include:: /common/global.rst

Acquia BLT
==========

|acquia-product:blt|, `available on GitHub <https://github.com/acquia/blt>`__, generates new Drupal projects using a standardized template that is based on Acquia Professional Services' best practices.

To improve efficiency and collaboration across Drupal projects, |acquia-product:blt| provides both a common set of tools and standardized structure, hopefully helping developers reduce incidents of duplicated work, speed up project set up time, and get new developers onboarded more quickly.

Using |acquia-product:blt| for your Drupal projects will help you meet the following goals during your development cycles:

-  Provide a standard project template for Drupal based projects
-  Provide tools that automate much of the setup and maintenance work for projects
-  Document and enforce Drupal standards and best practices through default configuration, automated testing, and continuous integration

Features
--------

|acquia-product:blt| offers the following features for your
organization's use:

-  `Local Git hooks <https://blt.readthedocs.io/en/latest/scripts/git-hooks>`__ |--| Validate formatting, syntax, and compliance with Drupal coding standards
-  `Testing frameworks <https://blt.readthedocs.io/en/latest/template/tests>`__ |--| Provides default configurations for Behat and PHPUnit
-  `Project automation tasks <https://blt.readthedocs.io/en/latest/readme/project-tasks/>`__ |--| Includes commands for syncing environments, compiling front-end assets, and executing tests
-  `Deployment artifact generation <https://blt.readthedocs.io/en/latest/readme/deploy/>`__ |--| Includes building production-only dependencies and sanitizing production-environment code
-  `Continuous integration and deployment tools <https://blt.readthedocs.io/en/latest/readme/ci/>`__ |--| Supports both the |pipefeature|_ and TravisCI


.. |pipefeature| replace:: \ |acquia-product:ac|\  pipelines feature
.. _pipefeature: /acquia-cloud/develop/pipelines

Getting started
---------------

Use the following steps to help you get started using |acquia-product:blt|:

#. Review the |minimumskills|_ to determine if |acquia-product:blt| is a good fit for your organization.
#. |reviewdocs|_ to determine which version of |acquia-product:blt| to install.
#. `Review the system requirements <http://blt.readthedocs.io/en/latest/INSTALL/>`__, and then perform the installation steps appropriate for your operating system.
#. `Review the repository architecture <http://blt.readthedocs.io/en/latest/readme/repo-architecture/>`__ to familiarize yourself with code organization practices in |acquia-product:blt|


.. |minimumskills| replace:: minimum skillset for using  \ |acquia-product:blt|\ 
.. _minimumskills: http://blt.readthedocs.io/en/latest/readme/skills/

.. |reviewdocs| replace:: Review the  \ |acquia-product:blt|\  documentation
.. _reviewdocs: http://blt.readthedocs.io/en/latest/


Developing with Acquia BLT
------------------------------------

|acquia-product:blt| offers commands that can simplify many of the `everyday tasks required in development <http://blt.readthedocs.io/en/latest/readme/project-tasks/>`__, including the following:

-  `Configure continuous integration (CI) <http://blt.readthedocs.io/en/latest/readme/ci/>`__ - |usepipelines|_ or TravisCI
-  `Generate build artifacts <http://blt.readthedocs.io/en/latest/readme/release-process/>`__ - As a part of the release process
-  |deployto|_ -  |usepipelines|_ or TravisCI

.. |deployto| replace:: Deploy code to  \ |acquia-product:ac|\ 
.. _deployto: http://blt.readthedocs.io/en/latest/readme/deploy/

.. |usepipelines| replace:: Using  \ |acquia-product:ac|\  pipelines
.. _usepipelines: /acquia-cloud/develop/pipelines


Acquia BLT and Remote Administration
----------------------------------------------

|acquia-product:blt| is compatible with Acquia's `Remote Administration </ra>`__ service only if all vendor and Drupal code is committed to the main development or build branch. Although the Remote Administration service cannot update |acquia-product:blt| itself, Drupal core and contributed modules can be updated.

If your website's deployment process builds your production codebase using continuous integration and your ``composer.json`` and ``composer.lock`` files are committed to the codebase, Remote Administration cannot perform updates on your website.

Additional information
----------------------

For more information about |acquia-product:blt|, including installation instructions and how to use its available hooks, see the
|bltdocs|_.

.. |bltdocs| replace:: \ |acquia-product:blt|\  documentation
.. _bltdocs: https://blt.readthedocs.io/en/stable/README/
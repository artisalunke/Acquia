.. include:: /common/global.rst

Working with code
=================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/develop/code/*

The |acquia-product:ui| gives you powerful and easy-to-use tools for
managing your application's code in its version control system.

.. _directories:

Repository directory structure
------------------------------

For each application, |acquia-product:ac| creates a master branch with
the following three folders:

-  ``/acquia-utils`` - Contains the application code and files for your
   development area. In the initial configuration, |acquia-product:ac|
   deploys code from this directory to both your production and staging
   servers.
-  ``/docroot`` - Stores the development copy of your Drupal codebase,
   from which |acquia-product:ac| executes on your web servers if you
   select ``master`` as the deployment branch.
-  ``/library`` - Contains the PHP libraries for your application. This
   directory is in your PHP include path, so you can add PHP extensions
   here if needed.

.. _recommended:

Code management recommendations
-------------------------------

Develop your code management workflow on the following best practices
and requirements to manage code in your version control system and
environments:

-  **Master is always a stable, up-to-date codebase.**
   This means that the master is immediately able to be deployed to
   production unless updates are in process. The master is deployed to
   the Dev environment unless testing is in process.
-  **Branches are used for developing and testing new code and
   updates.**
   Branches will be taken from the production tag. Acquia labels
   branches according to the function, the date and time started.
-  **Development can happen in parallel on different branches.**
   Acquia recommends keeping track of changes that are eventually merged
   into master and regularly updating the branch with master to ensure
   that the working branch is up-to-date. This may or may not be
   possible depending on the type of development on the branch.
-  **All tested and approved branches should be merged back into
   master.**
   Once they are fully tested, you should merge development branches
   into master. This ensures that master always includes updated code.
-  **Tags from tested and approved branches (including the master) are
   used for production.**
   Tags are similar to snapshots of the code, frozen in time. The
   |acquia-product:ui| doesn't allow you to make commits on a tag. By
   not modifying tags, you can easily go back to a previous tag if an
   error is discovered on the most recent tag.
-  **Deployed branches cannot be deleted.**
   Be sure that your workflow accounts for |acquia-product:ac| not
   allowing you to delete branches that are deployed to an environment.

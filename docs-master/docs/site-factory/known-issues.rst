.. include:: /common/global.rst

Known issues in |acquia-product:edg|
====================================

This page describes any known issues with |acquia-product:edg|.

-  **Acquia Cloud Site Factory is incompatible with Drush 9**

   Although |acquia-product:edg| is compatible with Drupal 8.4, the
   ``drush acsf-init`` command is incompatible with Drush 9.
   |acquia-product:edg| websites should not use either of the following
   configurations:

   -  An installation with a vendored dependency for Drush 9
   -  An |acquia-product:blt| version that includes Drush 9

-  **Drush 8.1.16 requires Acquia Cloud Site Factory Connector version 1.44 or greater**

   To use Drush 8.1.16 or greater with your websites, you must use version 1.44 or greater of the `Acquia Cloud Site Factory Connector <https://www.drupal.org/project/acsf>`__ module for your
   version of Drupal.
-  **PHP 7.1 requires Acquia Cloud Site Factory Connector version 1.40 or greater**

   To use PHP 7.1 with your websites, you must use version 1.40 or
   greater of the `Acquia Cloud Site Factory Connector <https://www.drupal.org/project/acsf>`__ module for your
   version of Drupal.
-  **Unicode characters and emoji are not supported in branch names**
   
   If a branch name contains a Unicode character, such as an emoji,
   |acquia-product:edg| will display a
   ``Failure due to fatal system error`` message when users attempt to
   switch to that branch. This error affects all
   |acquia-product:ac|-related products.
-  **Adding a path-based domain completes with an error message**
   
   Adding `path-based domains to a
   website </site-factory/manage/website/domains/path>`__ will succeed,
   but the domain name server (DNS) lookup failure will display an
   error.
-  **Incorrect concurrency values are displayed for task logs**
   
   The `Task log </site-factory/monitor/tasklog>`__ webpage
   displays incorrect values for **Concurrency** when users attempt to
   view detailed task information.
-  | **Git checkouts fail after reporting non-existent changes to binary
     files**
   | Git checkouts fail with the following error when non-text files
     contain a specific byte sequence and are not explicitly defined as
     binary files:
     ``Your local changes to the following files would be overwritten by checkout. Please, commit your changes or stash them.``
   | *Workaround* - Edit the following section of your ``.gitattributes`` file:

   .. code::
      
      # Auto-detect text files, ensure they use LF. 
      *         text=auto eol=lf``

   and then make one of the following changes:

   -  Remove the line beginning with ``*``
   -  Remove the ``eol=lf`` text
   -  Ensure that a specification line is added for every binary file
      extension used in your repository

-  **Acquia Dev Desktop overwrites settings.php**
   
   The ``acsf-init`` command in |acquia-product:edg| removes lines in
   ``settings.php`` inserted by |acquia-product:add|.
   *Workaround* - Remove the changes made by |acquia-product:add| to
   your ``settings.php`` file with ``git stash`` before executing the
   ``acsf-init`` command, unstashing the changes afterward.
-  **Local development using Microsoft Windows is unsupported**
   
   The |connector|_ module is
   incompatible with local filesystem paths in Microsoft Windows.
   *Workaround* - Either develop your website locally using a different
   operating system, or set up a Linux-based virtual machine for local
   development.
-  **Customizations to php.ini unavailable to command-line applications**
   
   |unlikecloud|_, |acquia-product:edg| does not allow you to bypass the inclusion of
   your environment's ``php.ini`` by clearing the PHPRC environment
   variable.
-  **Update the code distribution provided in your repository before beginning development**
   
   The code distribution provided when a new |acquia-product:edg|
   account is provisioned should be replaced with the distribution of
   your choice before development begins.

If you encounter any difficulties with your |acquia-product:edg|
subscription, `contact Acquia Support </support#contact>`__ for
assistance.

.. |connector| replace:: \ |acquia-product:edg|\  Connector
.. _connector: https://www.drupal.org/project/acsf


.. |unlikecloud| replace:: Unlike other  \ |acquia-product:ac|\ -hosted websites
.. _unlikecloud: /platform-improvement/ssh-and-cloud-hooks-will-have-phprc-environment-variable-set-site-phpini-path
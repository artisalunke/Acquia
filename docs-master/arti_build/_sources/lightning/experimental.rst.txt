.. include:: /common/global.rst

Lightning experimental modules
==============================

.. important::

   Acquia strongly recommends that you *do not* enable experimental modules on production websites.

|acquia-product:ld| includes one or more *experimental modules* for
testing with your non-production websites. Experimental modules are
provided for testing purposes, but are not yet fully supported.

For more information about experimental modules and their use in Drupal
8, see `Experimental modules in Drupal
8 <https://www.drupal.org/core/experimental>`__ on Drupal.org.

Installing experimental modules
-------------------------------

Although these not-fully-supported modules are included with
|acquia-product:ld|, you must specifically select them *during* the
distribution installation process, as follows:

#. During the **Choose extensions** portion of the installation process,
   in the **Experimental** section, select the **I understand the
   potential risks of experimental modules** check box.
   The |acquia-product:ld| installation application displays the
   available experimental modules.
#. Select the check boxes for the experimental modules that you want to
   include for use with your |acquia-product:ld| website.
#. Click **Continue**.

The installation process will continue, and will copy the experimental
modules you selected to your website.

Enabling experimental modules
-----------------------------

To enable one or more |acquia-product:ld| experimental modules on your
website, complete the following steps:

#. Sign in as an administrator, and then click **Extend** in the admin
   toolbar.
#. Find the **Lightning (Experimental)** section, and then select the
   check boxes for the experimental modules that you want to use.
#. Click **Install**.

Current experimental modules
----------------------------

The current version of |acquia-product:ld| contains the following
experimental module:

-  **Lightning Preview**

   |acquia-product:ld| Preview (also referred to as the Workspace
   Preview System or WPS) was marked as experimental for the following
   reasons:

   -  It relies on the
      `Multiversion <https://www.drupal.org/project/multiversion>`__
      module, which has the following issues:

      -  The module does not have a stable release.
      -  The module modifies data structures.
      -  After being uninstalled, the module leaves permanent changes in
         the database.
      -  The module introduces the concept of a trash bin for deleted
         content, but deleted content is not actually removed from the
         database.
         Deleted content must also be purged to be completely wiped from
         the database, but the user interface to purge content (provided
         by the `Trash <https://www.drupal.org/project/trash>`__ module)
         is still under development, making it impossible to completely
         delete content using the user interface.

   -  There are several scenarios where URL aliases can produce
      unexpected results, including the following:

      -  Pathauto is enabled, but rules are not configured for all
         content types
      -  Overriding pathauto generated aliases
      -  Aliases for all entities other than nodes

   -  In certain circumstances, blocks on block listing pages are not
      properly filtered by the Workspace module.
   -  The Workspace listing page displays a PHP warning caused by the
      Workspace module. Although this warning does not signify a real
      problem, it can be alarming to some users.
   -  The Author user-reference relationship that is implicit with all
      node entities is lost when replicating from workspace to
      workspace. This means that if User A creates Node B on the Live
      workspace, and that node is pulled to the Stage workspace, the
      Stage workspace will be unaware of the author, and will set the
      author to Anonymous. Furthermore, if an edit is then made to Node
      B on the Stage workspace, and that edit is pushed back to Live,
      Node B on the Live workspace will also lose its author. For more
      information, see `Issue
      #2817231 <https://www.drupal.org/node/2817231>`__ on Drupal.org.
   -  There is no way to properly resolve conflicts. Users can delete
      the conflicting entity from one of the two workspaces to remove
      conflicts, but there is no interface for picking the winner and
      then keeping both versions.

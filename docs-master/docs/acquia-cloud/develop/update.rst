.. include:: /common/global.rst

Sending updates to your code repository
=======================================

When you make changes to your Drupal
```[docroot]`` <%5Bacquia-product:kb%5Darticles/docroot-definition>`__
that you want to save and deploy to your site, commit the changes from
your local workspace directory. Remember that you can commit only to a
branch, not to an existing tag. You can find these and other useful VCS
commands in the |acquia-product:ac| `**Application
info** </acquia-cloud/develop/repository/git#basic>`__ panel.

.. _git:

Committing with Git
-------------------

In the following Git ``commit``, note that the ``-a`` option sends all
of the changes that you made to the workspace. To commit only a specific
file or directory, replace ``-a`` with the name of the folder or
directory.

``git commit -a -m "Added Foo module."``

After you use the ``commit`` command to send your changes to your local
clone of the repository, you must use the ``git push`` command to push
the changes to the appropriate branch of your code on
|acquia-product:ac|. For example, if you are deploying from a branch
named ``master``, use the following command:

``git push origin master``

.. _related:

Related topics
--------------

-  `About your code repository </acquia-cloud/develop/repository>`__
-  `Checking out a local copy of your
   code </acquia-cloud/develop/checkout>`__
-  `Reset a Git repository on
   |acquia-product:ac| <%5Bacquia-product:kb%5Darticles/reset-git-repository-acquia-cloud>`__

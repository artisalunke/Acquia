.. include:: /common/global.rst

Using Git
=========

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/develop/repository/git/*

Git is the version control system available for use with
|acquia-product:ac|. Use the following information to help you use Git
to manage your |acquia-product:ac| code repository.

Note

Acquia does not provide support for third-party version control
management tools.

.. _download:

Downloading a Git client
------------------------

You will need a Git client installed on your local system in order to
interact with the code repository using Git.

To download a Git client, use the method based on your operating system:

-  *macOS* – Use the `Git OS X
   Installer <https://sourceforge.net/projects/git-osx-installer/>`__.
   If you use the `Homebrew package manager <https://brew.sh/>`__, run
   ``brew install git``.
-  *Windows* – Use `Git for Windows
   (msysgit) <https://gitforwindows.org/>`__ (command line) or
   `TortoiseGit <https://tortoisegit.org/>`__ (GUI).
-  *Ubuntu* – Use the command ``sudo apt-get install git-core`` to
   install Git using the command line. Follow the installation options
   on the `official Git website <https://git-scm.com/download>`__.

Note

Be sure to `enable SSH access </acquia-cloud/ssh/enable>`__ to your
|acquia-product:ac| environments.

.. _basic:

Basic Git commands
------------------

You can find several basic Git commands, customized for your
|acquia-product:ac| application, in the |acquia-product:ui|:

#. Sign in to the `|acquia-product:ui| <https://cloud.acquia.com>`__,
   and then select your application.
#. Click **Application info**.

   |Application Info icon|

The **Application Information** panel displays basic Git commands for
your application that you can use to clone a repository, stage modified
files, commit changes, and push local commits to a remote repository.
You can click the copy icon |Copy icon| to copy a command to your
clipboard and then paste it into an SSH session.

You can also find procedures to help you get started with Git in
`Checking out a local copy of your
code </acquia-cloud/develop/checkout>`__ and `Sending updates to your
code repository </acquia-cloud/develop/update>`__.

.. _help:

Git best practices
------------------

The following best practices apply to any application hosted in
|acquia-product:ac|, and can assist you in developing with Git:

-  `Creating a feature branch <#create>`__
-  `Committing branch changes <#commit>`__
-  `Merging your feature branches <#merge>`__
-  `Code placement in Drupal <#where>`__

.. _create:

Creating a feature branch
~~~~~~~~~~~~~~~~~~~~~~~~~

To create a branch for development work, complete the following steps:

#. Open a command prompt window, and then change the directory to the
   location that contains the `clone of your code
   repository </site-factory/workflow/git#clone>`__.
#. Switch to the master branch.

   ``git checkout master git pull origin master``

#. Create the feature branch with a descriptive name that relates to the
   code that it contains, and then switch to the new branch using the
   following commands, replacing ``[feature_id]`` with the name of your
   feature branch:

   ``git checkout -b [feature_id] git push origin [feature_id]``

Create and use as many feature branches as needed to keep your
development efforts separate from one another.

.. _commit:

Committing branch changes
~~~~~~~~~~~~~~~~~~~~~~~~~

Whenever you want to commit your changes back to the code repository for
the branch that you're working on, run the following command to commit
the change locally:

``git commit -a -m "Comment"``

After you commit the change, send the change to the code repository
(where ``[feature_id]`` is the name of your feature branch):

``git pull origin [feature_id] git push origin [feature_id]``

When working with your code, if you need to run a
`Drush <https://www.drupal.org/project/drush>`__ command that only
affects one of your websites, be sure to use the ``--uri=site.host.com``
parameter, where ``site.host.com`` is your website's complete site and
domain name.

.. _merge:

Merging your feature branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To merge your feature branches into a single release branch for testing,
complete the following steps:

#. Create a release branch from your master branch. You will use this
   branch for feature integration and testing. Use the following steps
   to create the branch:

   #. Switch to the master branch.

      ``git checkout master git pull origin master``

   #. Create the release branch (in this example, the release branch is
      named RC), and then switch to the new branch.

      ``git checkout -b RC``

#. Run the following command to ensure that you have the most recent
   feature branch versions:

   ``git fetch all``

#. Merge each of the completed feature branches into your new release
   branch, using a command similar to the following:

   ``git merge [feature_id] --no-ff``

#. Push your release branch to the remote repository for testing.

   ``git push origin RC``

.. _where:

Code placement in Drupal
~~~~~~~~~~~~~~~~~~~~~~~~

As you develop each code branch, place code changes and additions in the
folders appropriate for your version of Drupal. Placing your changes in
other folders can cause serious problems for your repository, including
merge conflicts that Acquia will not be able to help you resolve.

.. _drupal8:

Drupal 8
^^^^^^^^

Drupal 8 expects code changes in the following directories:

+-----------------------------------+-----------------------------------+
| Directory                         | Suggested contents                |
+===================================+===================================+
| ``docroot/libraries``             | Third-party libraries, such as    |
|                                   | WYSIWYG editors                   |
+-----------------------------------+-----------------------------------+
| ``docroot/modules/custom``        | Custom modules                    |
+-----------------------------------+-----------------------------------+
| ``docroot/modules/contrib``       | Modules from                      |
|                                   | `Drupal.org <https://www.drupal.o |
|                                   | rg/>`__                           |
+-----------------------------------+-----------------------------------+
| ``docroot/profile``               | Custom profiles                   |
+-----------------------------------+-----------------------------------+
| ``docroot/themes``                |                                   |
+-----------------------------------+-----------------------------------+

.. _drupal7:

Drupal 7
^^^^^^^^

Drupal 7 expects code changes in the following directories:

+-----------------------------------+-----------------------------------+
| Directory                         | Suggested contents                |
+===================================+===================================+
| ``docroot/sites/all/modules``     |                                   |
+-----------------------------------+-----------------------------------+
| ``docroot/sites/all/modules/custo | Custom modules                    |
| m``                               |                                   |
+-----------------------------------+-----------------------------------+
| ``docroot/sites/all/modules/contr | Modules from                      |
| ib``                              | `Drupal.org <https://www.drupal.o |
|                                   | rg/>`__                           |
+-----------------------------------+-----------------------------------+
| ``docroot/sites/all/libraries``   | Third-party libraries, such as    |
|                                   | WYSIWYG editors                   |
+-----------------------------------+-----------------------------------+
| ``docroot/sites/all/themes``      |                                   |
+-----------------------------------+-----------------------------------+
| ``docroot/profiles``              | Custom profiles                   |
+-----------------------------------+-----------------------------------+

.. _resource:

Additional resources
--------------------

For more information about how to use Git, see the following online
resources:

-  `Git basics <%5Bacquia-product:kb%5Darticles/git-basics>`__, Acquia's
   article on the basics of using Git.
-  `Resources for learning
   Git <%5Bacquia-product:kb%5Darticles/resources-learning-git>`__, an
   Acquia Knowledge Base article with a list of valuable tutorials and
   references.
-  `How to apply and test a patch from drupal.org using Git on
   |acquia-product:ac| <%5Bacquia-product:kb%5Darticles/how-apply-and-test-patch-drupalorg-using-git-acquia-cloud>`__.

.. |Application Info icon| image:: https://cdn2.webdamdb.com/md_s50ELlOsbIh7.png?1527195520
   :width: 453px
   :height: 151px
.. |Copy icon| image:: https://cdn4.webdamdb.com/100th_sm_QWl4Yj11ry94.png?1527195523
   :width: 20px
   :height: 21px

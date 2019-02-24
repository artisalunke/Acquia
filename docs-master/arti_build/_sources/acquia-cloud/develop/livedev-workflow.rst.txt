.. include:: /common/global.rst

Live Development workflow
=========================

With Live Development mode, you can make changes locally and see the
results right away in your |acquia-product:ac| development environment.
This document describes how to take the changes you have made locally
and eventually deploy them on your production application.

Note

For information about how to enable or disable Live Development mode,
see `Using Live Development mode to change code on your
server </acquia-cloud/develop/livedev>`__.

When you first enable Live Development mode for an |acquia-product:ac|
Development environment, |acquia-product:ac| checks out the code branch
that is currently deployed on your Dev environment into your
``~/dev/livedev`` directory, making it a local version of whatever
branch was deployed in that environment. All requests for your
application's development environment now refer to these files as long
as you leave Live Development enabled. While you can enable Live
Development for other non-production environments, the best practice is
to use it only on Development environments.

Before you enable Live Development mode, make sure that your environment
has a branch (ideally, the master branch) and not a tag deployed. You
cannot commit your changes to a tag.

Enabling Live Development on an environment can slow the response times
of your Drupal application. Live Development uses the
|acquia-product:ac| network file system to ensure your code is reachable
from all web servers. Because a network file system is not well-suited
for code execution, using Live Development can affect the performance of
your application. Therefore, we recommend disabling Live Development
when you are done with your changes.

Consider a typical use case where you have installed or imported a
Drupal application into the Development environment of an
|acquia-product:ac| application. The master branch is deployed in
Development, so that you can see commits to the master branch quickly.
Your Environments page looks something like this, displaying the master
branch deployed in the Dev environment:

|Master branch deployed|

#. Enable Live Development for the Development environment.

   Your Environments page now displays the Live Development branch
   deployed in the Development environment.

#. Sign in to your server, as described in `Accessing your server using
   SSH </acquia-cloud/ssh/enable#access>`__.
#. Navigate to the live development directory:

   ``cd ~/dev/livedev/docroot``

Suppose that you make a change to some files. For example, you might
update a module or make various CSS file changes. You have made these
changes in your local code repository, and you can see them immediately
in your |acquia-product:ac| application, but you then need to get these
changes back into your |acquia-product:ac| code repository so that they
can be incorporated into future production releases of your code. To do
this, you need to commit the changes to your |acquia-product:ac|
application's repository. You will accomplish these steps:

#. Identify the uncommitted changes.
#. Commit the desired changes.
#. Disable Live Development mode.
#. Test your code and deploy it on your Staging or Production
   environments.

.. _git-commit:

Committing your changes in Git
------------------------------

The first step is to ask your version control system to show you all the
changes since your last commit. You may not even remember all of the
changes, so it is important to review what they all were, before
proceeding. Enter the following command:

``git status --short --untracked-files=all --ignored``

Now review the feedback you get from this command as to what the
uncommitted new and changed files are. Uncommitted new files look like
this:

``?? docroot/kb1.txt``

You can commit the new file with commands similar to the following:

``git add kb1.txt git commit -m "New file 'docroot/kb1.txt'" kb1.txt``

Uncommitted changed files look like this:

``M docroot/.htaccess``

You can commit the changed file with the following command:

``git commit -m "Added redirect for legacy URL http://example.com/about-us" .htaccess``

Note

Be sure to set up your identity as a Git user before committing code
changes the first time, or you will not be able to commit your changes.
Use one of the following methods to do this:

-  Use the ``--author`` option with your ``git commit`` command:

   ``git commit --author="Ephraim Symbolist " -m "New file 'docroot/kb1.txt'" kb1.txt``

-  Use the ``git config`` command to set your email and name before you
   run ``git commit``:

   ``git config --global user.email "esymbolist@example.com" git config --global user.name "Ephraim Symbolist"``

Then push the changes to the master branch of your |acquia-product:ac|
repository with the following:

``git push origin master``

.. _live:

Making your changes live
------------------------

After you have committed your changes in your Development environment to
your application's code repository, you need to `disable Live
Development mode </acquia-cloud/develop/livedev#disable>`__ to make your
changes go live on your Staging or Production environments.

Note

Until you disable Live Development mode for the Development environment,
you cannot drag your code from Dev to either Stage or Prod.

After you leave Live Development mode, you can drag your code to the
Stage environment, test it, and eventually drag it to the Prod
environment when you are ready to deploy it on your live, production
application.

This completes one cycle of using Live Development mode in the
Development environment.

.. |Master branch deployed| image:: https://cdn3.webdamdb.com/1280_6RZ5Rs0wpu49.png?1526476014
   :width: 768px
   :height: 321px

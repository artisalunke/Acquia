.. include:: /common/global.rst

Correcting detached head problems with Git
==========================================

When working in `Live Development
mode </acquia-cloud/develop/livedev>`__, attempting to push your changes
using ``git push`` can occasionally fail with a message similar to the
following:

``You are in 'detached HEAD' state. You can look around, make experimental changes and commit them, and you can discard any commits you make in this state without impacting any branches by performing another checkout.``

This *detached head state* occurs when a specific commit is checked out
instead of a branch. You cannot commit to a commit—only to a branch. To
correct this, use the following steps to create a branch for your
commits:

#. From a command prompt window, create a branch by using a command
   similar to the following:

   ``git checkout -b [branchname]``

#. Commit your changes to the branch.
#. Push the branch that you created into the origin Git repository:

   ``git push origin [branchname]``

Your Environment webpage will display the branch for
`deployment </acquia-cloud/develop/code#deploy>`__ to each of your
environments.

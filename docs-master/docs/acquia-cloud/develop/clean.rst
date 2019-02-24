.. include:: /common/global.rst

Copying your code to a new Git repository
=========================================

Occasionally you may need to remove and replace your current code
repository, while keeping the existing code intact. Use the following
procedure to copy your code from an existing |acquia-product:ac|
repository to a new repository.

#. `Clone the code from the existing
   repository </acquia-cloud/develop/checkout>`__ to ensure you have a
   recent, accurate version of your codebase.
#. Open a command prompt window, and then run the following command to
   ensure you have the most up to date code commits:

   ``git log``

#. Use the following command to add the new code repository as a remote,
   which will enable you to push code to the new repository using the
   same method as the origin:

   ``git remote add new-origin``

#. Validate that the new remote origin has been added properly by using
   the following command:
#. Push the mirrored code to the new origin:

   ``git push --mirror new-origin  git push --all new-origin  git push --tags new-origin``

#. With the following commands, rename the origin to be the new
   repository:

   ``git remote rename origin old-origin  git remote rename new-origin origin``

Your code repository should now have a clean, working copy of the
previous code.

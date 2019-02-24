.. include:: /common/global.rst

Importing your codebase
=======================

.. container:: internal-navigation

  **Importing manually**

  * :doc:`Intro </acquia-cloud/create/import/manual>`
  * Code
  * :doc:`Database </acquia-cloud/create/import/manual-db>`
  * :doc:`Files </acquia-cloud/create/import/manual-files>`

This page describes manually importing the codebase of an existing
Drupal application into |acquia-product:ac| using Git, as part of the
process of `manually importing the entire
application </acquia-cloud/create/import/manual>`__. For information
about other methods of importing an application, see `Importing an
existing application </acquia-cloud/create/import>`__.

To prepare and import your application's codebase into an
|acquia-product:ac| code repository, complete the following steps:

#. Ensure that your existing application's most current Drupal code
   `[docroot] <%5Bacquia-product:kb%5Darticles/docroot-definition>`__
   (the directory containing files and directories including Drupal's
   ``index.php``, ``/includes`` directory, and ``/modules`` directory)
   is on your local computer.
#. Move any user-uploaded files directories (such as ``/files``,
   ``/sites/default/files``, or ``/sites/[sitename]/files``) out of your
   ``[docroot]`` directory. There are separate `instructions for
   importing your user-uploaded files
   directories </acquia-cloud/create/import/manual-files>`__. This is
   necessary because, on |acquia-product:ac|, files are stored outside
   of your ``[docroot]`` to simplify management of your repository and
   to guarantee their availability across multiple, redundant web nodes.
#. Determine where you want your code repository to be located on your
   local computer. The local code repository will contain the new
   ``[docroot]`` for your application that is connected to the
   repository on |acquia-product:ac|.
#. The remote |acquia-product:ac| code repository comes with a default
   ``[docroot]`` directory that contains a placeholder file called
   ``index.html``. To remove it and commit the change back to your
   repository, complete the following steps:

   a. Go to the directory for the new local code repository for
      ``[docroot]``, and then check out the current default application
      code repository contents to your computer.

      ``cd [local_repository_dir] git clone [code_repository] cd [sitename] git checkout master``

      where:

      -  ``[local_repository_dir]`` is the directory for the new local
         code repository for your application's ``[docroot]``.
      -  ``[code_repository]`` is the URL of the |acquia-product:ac|
         code repository. To obtain the repository URL, select your
         application in the |acquia-product:ui| and click **Application
         Info**.
      -  ``[sitename]`` is the name of your site on |acquia-product:ac|.

   b. In the new local code repository for the ``[docroot]`` directory,
      remove the default website and send the changes to
      |acquia-product:ac|.

      ``git rm -r docroot git commit -m "Remove default docroot." git push origin master``

#. From the new local code repository directory, make a copy of your
   application's most current ``[docroot]`` directory using the
   following command:

   ``$ cp -R [current_docroot] docroot``

   where ``[current_docroot]`` is the complete path to the local
   location for the current ``[docroot]`` for your Drupal application.

#. Commit the prepared Drupal ``[docroot]`` (without any ``/files``
   directories) into your |acquia-product:ac| repository:

   ``git add docroot git commit -m "Import my docroot." git push origin master``

.. _next:

Next step
---------

After your codebase is ready, `import your
database </acquia-cloud/create/import/manual-db>`__ and configure its
website connection.

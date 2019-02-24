.. include:: /common/global.rst

Importing your files
====================

.. container:: internal-navigation

  **Importing manually**

  * :doc:`Intro </acquia-cloud/create/import/manual>`
  * :doc:`Code </acquia-cloud/create/import/manual-code>`
  * :doc:`Database </acquia-cloud/create/import/manual-db>`
  * Files

This page describes manually importing the files of an existing Drupal
application into |acquia-product:ac|, as part of the process of
`manually importing the entire
application </acquia-cloud/create/import/manual>`__. For information
about other methods of importing an application, see `Importing an
existing application </acquia-cloud/create/import>`__.

|acquia-product:ac| stores user-uploaded files of a Drupal application
(the ``/files`` directory) on a network filesystem so that it can be
shared across multiple web nodes. The network filesystem for your
application is accessible as ``/mnt/gfs/[site].[env]`` (also accessible
as ``/mnt/files/[site].[env]``), where ``[site]`` is the name of your
application on |acquia-product:ac| and ``[env]`` is the
|acquia-product:ac| environment (one of ``prod``, ``test``, or ``dev``).
The files directories themselves are subdirectories of this network
filesystem, such as ``/mnt/files/[site].[env]/sites/[subsite]/files``.

In your deployed Drupal ``docroot``, which is on the local disk for performance,
|acquia-product:ac| creates a symbolic link from the files directory to the 
actual files directory in the network filesystem; in this way, Drupal is able
to access the files in the location it expects. For example,
``[docroot]/sites/default/files`` is set up to be a symbolic link to
``/mnt/files/[site].[env]/sites/default/files``. |acquia-product:ac|
creates this symbolic link in any subdirectory of ``docroot/sites`` that
contains a file named ``settings.php``. As an example, if you have a
multisite setup with the file ``docroot/sites/foo.com/settings.php``,
|acquia-product:ac| creates ``docroot/sites/foo.com/files`` as a
symbolic link to ``/mnt/files/[site].[env]/sites/foo.com/files``.

To import your user-uploaded files to your |acquia-product:ac|
application, complete the following steps:

#. `Enable SSH access to your server </acquia-cloud/ssh/enable>`__.
#. Upload your files to the user-uploaded files directory using the
   ``sftp``, ``scp``, or ``rsync`` command. This directory is
   ``/mnt/files/[site].[env]/sites/default/files`` or, for multisite
   installations, ``/mnt/files/[site].[env]/sites/[sitedir]/files``.
   For more information, see `Understanding
   files </acquia-cloud/manage/files/about>`__. For examples regarding
   how to use ``rsync``, see `rsyncing files on
   </acquia-cloud/develop/rsync>`__ |acquia-product:ac|.

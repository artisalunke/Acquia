.. include:: /common/global.rst

rsyncing files on |acquia-product:ac|
=====================================

.. toctree::
   :hidden:
   :glob:

   /acquia-cloud/develop/rsync/*


.. container:: internal-navigation

   **Rsync**

   * Unix
   * :doc:`Windows </acquia-cloud/develop/rsync/windows>`

To copy a large number of files from one place to another, one of the
better options is to use `rsync <http://rsync.samba.org/>`__, which
provides either an interactive or non-interactive way to copy files from
one location to another on a single server, or from one server to
another.

.. note::  

   -  We recommend that you run rsync on your production server, because it 
      requires you to put a private key on the server.
   -  We recommend testing your rsync commands by adding the ``-n`` option 
      with each rsync command, which gives you an output of the changes 
      without committing them. You will need to add the ``-n`` option to the 
      commands in the following steps.
   -  You should download your `Drush aliases </acquia-cloud/drush-aliases>`__.

To rsync files on |acquia-product:ac|, do the following:

#. Ensure that the user, group, and mode of the files and folders you
   intend to rsync are set to permit the web server to have read-only
   access, and to explicitly block any other user from reading your
   content. Doing so prevents file locks or changes while you're copying
   data.
#. Create a new SSH key or use an existing SSH key, and then add the
   public key to your Acquia account on your account page. See `Enabling
   SSH access </acquia-cloud/ssh/enable>`__.
#. Place your private SSH key somewhere on the production server. For
   this example, suppose that you placed the key in the
   ``/mnt/files/[site]/files-private/private_key`` directory, where
   ``[site]`` is the website's name on |acquia-product:ac|. For more
   information about placement, see `Storing private information in the
   file system </acquia-cloud/files/system-files/private>`__.
#. To allow access to the key, give it the proper permissions by using a
   command similar to the following:

   ::

       chmod 600 /mnt/files/[site]/files-private/private_key

#. Execute the rsync from either of the production servers, as in this
   example:

   ::

       rsync -rltDvPh -e "ssh -i [path to private key]" [source] [destination]

   If you are using Drush and aliases to download files, you can use a
   command like this:

   ::

       drush rsync @mysite.dev:%files sites/default

#. Transfer the files folder from staging to production:

   ::

       rsync -rltDvPh -e "ssh -i /mnt/files/[site]/files-private/private_key" [user].[env]@[stage_server]:/mnt/files/[stage_name]/sites/default/files/ /mnt/files/[site]/sites/default/files

   In this example, ``[stage_name]`` is the name of the staging
   website's name on |acquia-product:ac|, and the ``[stage_server]`` is
   the name of the staging server on |acquia-product:ac|.

These rsync flags ensure that all the files are copied recursively, and
preserve both modification times and symlinks. For more information on
the rsync options used here, see the `rsync man
page <http://linux.die.net/man/1/rsync>`__.

.. _more:

Additional examples
-------------------

The following examples provide information on how you can extend or
modify rsync commands to meet your needs.

.. _stages:

Transferring files between environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To transfer the files folder from your production environment to your
staging environment, execute a command similar to the following:

::

    rsync -rltDvPh -e "ssh -i /mnt/files/[site]/files-private/private_key" /mnt/files/[site]/sites/default/files/ [user].[env]@[stage_server]:/mnt/files/[stage_name]/sites/default/files/

.. _remove:

Removing and replacing files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To completely remove and replace files with a new copy, execute a
command similar to the following:

::

    rsync -rltDvPh /mnt/files/[site]/sites/default/files/ /mnt/files/[site]/sites/default/files --delete

.. _local:

Transferring files across two servers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also use SCP over rsync from a local machine to transfer files
between two remote servers. You may need to set up SSH keys between the
two servers:

::

    scp -r -P22 [user].[env]@[svr].hosting.acquia.com:/mnt/files/[site]/sites/default/files/ [user].[env]@[svr].hosting.acquia.com:/mnt/files/[site]/sites/default/files

In this example, ``[user]`` is your username, and ``[svr]`` is the name
of the particular server you're moving data to or from.

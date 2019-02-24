.. include:: /common/global.rst

Transferring files to a different docroot
=========================================

In many circumstances, users will want to `copy files to a different
environment </acquia-cloud/manage/transfer-files>`__. Other applications
may share a single server in standalone or multisite configurations,
which can require multiple
`docroots <%5Bacquia-product:kb%5Darticle/docroot-definition>`__ on the
same server. You can use the ``rsync`` command to accomplish file
transfers in this situation as well.

To transfer files to a different, local docroot, complete the following
steps:

#. `Create a private key </acquia-cloud/ssh/generate>`__ on your local
   computer.
#. `Add the public key </acquia-cloud/ssh/enable/add-key>`__ to an
   account that has team lead permissions on the source server.
#. Copy the private key to the ``.ssh`` directory in the destination
   directory.
#. Set the ``.ssh`` directory permissions by using the following
   command:

   ``chmod 700 .ssh``

#. Use the following command to set the private key file permissions:

   ``chmod 400``

#. | Run your rsync command.
   | For example, the following is an rsync command between docroots on
     the same server:

   .. code-block:: none

      rsync -avz -e "ssh -i /home/sourcedocroot/.ssh/id_rsa_rsync"  destinationuser.dev@staging-1234.prod.hosting.acquia.com:/mnt/gfs/sourceenv.dev/files /mnt/gfs/destinationenv.dev/files/

.. _tunnel:

Tunneling
---------

Setting up the SSH keys between docroots is also a method to help enable
SSH tunneling between servers, or between your server and an external
application. For more information, see `SSH tunneling for server-side
applications <%5Bacquia-product:kb%5Darticles/ssh-tunneling-server-side-applications>`__.

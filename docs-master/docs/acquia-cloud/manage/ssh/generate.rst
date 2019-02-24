.. include:: /common/global.rst

Generating an SSH public key
============================

Before you are able to SSH to sign in to your web server or to connect
to your Git code repository, you must have an SSH private/public key
pair.

.. _requirements:

Key requirements
----------------

|acquia-product:ac| requires that your SSH public key must be at least
4096 bits.

All websites that require Payment Card Industry Data Security Standard
(PCI DSS) compliance must be in an Acquia PCI DSS-compliant product
offering. To meet PCI DSS requirements, all users must use multifactor
authentication for remote access to their PCI DSS environment. When you
connect to an |acquia-product:ac| environment using SSH, you use your
SSH key as one authentication factor. To comply with PCI DSS, you must
use a passphrase with your SSH key to provide a second authentication
factor. You can add a passphrase when you create your key pair. For more
information about PCI compliance on |acquia-product:ac|, see the
`Compliance with standards and
regulations </acquia-cloud/arch/compliance-standards-and-regulations#pci-dss>`__.

.. _methods:

Methods for generating a key pair
---------------------------------

To generate an SSH private/public key pair for your use, you can use one
of the following methods: |add| or `ssh-keygen <#ssh-keygen>`__.

.. _dev-desktop:

|acquia-product:add|
--------------------

|image0|

Using |add| (`free
download <https://dev.acquia.com/downloads>`__) for your local
application development provides you with an additional advantage —
creation of an SSH private/public key pair for your application by
clicking a button.

After you `install </dev-desktop/install>`__, |acquia-product:add| see
the `Generating an SSH key </dev-desktop/keygen>`__ documentation page
to learn how to create an SSH key and then register it with
|acquia-product:ac|.

ssh-keygen
----------

You can also use the ``ssh-keygen`` command from the command line to
generate an SSH private/public key pair.

.. note:: 
   If you are using Windows, you may not have access to the ``ssh-keygen`` 
   command. To use this command, you can download and install 
   `Git for Windows <https://git-for-windows.github.io/>`__, and then use the 
   Bash shell to follow the remaining instructions in this section.

To generate an SSH private/public key pair using the ``ssh-keygen``
command, complete the following steps:

#. Open a shell or command-line window on your computer.
#. Ensure that you do not already have a public key saved to your
   computer. To do this, run the following command:

   ``cd ~/.ssh ls -l``

   If the directory and key file exists, run the following commands to
   back up the key ``id_rsa``, as this procedure overwrites your current
   key if it is named ``id_rsa``.

   ``mkdir key_backup mv id_rsa* key_backup``

#. Generate a new public/private key pair using the ``keygen`` command:

   ``ssh-keygen -b 4096``

   The ``keygen`` command prompts you for the directory to contain the
   key.

   .. code-block:: none
   
      Generating public/private rsa key pair. Enter file in which to save the 
      key (/Users/[user_dir]/.ssh/id_rsa):

   Press the Enter key to accept the default location of
   ``/.ssh/id_rsa`` in your user directory.

   .. code-block:: none

      Enter passphrase (empty for no passphrase): [passphrase] Enter same 
      passphrase again: [passphrase]

   Substitute ``[passphrase]`` with your own text. This is for
   encrypting the private key on your computer. It is possible to use a
   blank passphrase, but if you do this, another user can impersonate
   you with a copy of the key file.

   .. note:: 
      Be sure to keep track of the passphrase because you will need to enter 
      it when you use the key.

   The ``keygen`` command displays the following output:

   .. code-block:: none
   
      Generating public/private rsa key pair. Your identification has been saved
      in /Users/[user_dir]/.ssh/id_rsa. Your public key has been saved in 
      /Users/[user_dir]/.ssh/id_rsa.pub. The key fingerprint is: 
      52:96:e9:c8:06:c2:57:26:6d:ef:2f:0c:d9:81:f4:1c username@hostname

#. Copy the key to your clipboard. To simplify the process, you can
   execute the following command to copy the key from the ``id_rsa.pub``
   file to your clipboard:

   ``pbcopy < ~/.ssh/id_rsa.pub``

   Alternatively, using your favorite text editor, you can open the
   ``~/.ssh/id_rsa.pub`` file, and then copy the contents of the file
   manually.

   .. important:: Copy the key exactly without adding newlines or whitespace.

After you create and obtain the key, you can `add the public key to your
Acquia user profile </acquia-cloud/ssh/enable/add-key>`__ in
|acquia-product:ac|.

.. _related:

Related topics
--------------

-  `Enabling SSH access </acquia-cloud/ssh/enable>`__

.. |image0| image:: https://www.acquia.com/sites/default/files/product/header/aquiadrupal_icon_80.png
   :class: no-sb

.. |add| replace:: \ |acquia-product:add|\
.. _add: </dev-desktop>

